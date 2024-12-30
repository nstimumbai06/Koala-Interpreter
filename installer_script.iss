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
