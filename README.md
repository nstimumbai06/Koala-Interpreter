# Koala Interpreter

## How to Build the Koala Interpreter

1. Install **PyInstaller** using pip:
   ```bash
   pip install pyinstaller
   ```

2. Build the **Koala Interpreter** as a standalone executable:
   ```bash
   pyinstaller --onefile koala_interpreter.py
   ```

## How to Build the GUI Path Installer

1. Open **Inno Setup Compiler**.
2. Import the `installer_script.iss` into Inno Setup Compiler.
3. Compile the script to create the GUI installer for Koala.

## How to Run Koala Files

1. To run a `.koala` file, use the following command:
   ```bash
   koala file.koala
   ```