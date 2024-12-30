[Setup]
AppName=Koala Programming Language
AppVersion=1.0
DefaultDirName={pf}\Koala
DefaultGroupName=Koala
OutputDir=Output
OutputBaseFilename=KoalaInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\koala.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Koala"; Filename: "{app}\koala.exe"
Name: "{group}\Uninstall Koala"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\koala.exe"; Description: "Launch Koala"; Flags: nowait postinstall skipifsilent

[Code]
procedure AddToPath(PathToAdd: string);
var
  OldPath: string;
  NewPath: string;
begin
  if not RegQueryStringValue(HKCU, 'Environment', 'Path', OldPath) then
    OldPath := '';

  if Pos(PathToAdd, OldPath) = 0 then
  begin
    if OldPath <> '' then
      NewPath := OldPath + ';' + PathToAdd
    else
      NewPath := PathToAdd;

    RegWriteStringValue(HKCU, 'Environment', 'Path', NewPath);
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    AddToPath(ExpandConstant('{app}'));
  end;
end;
