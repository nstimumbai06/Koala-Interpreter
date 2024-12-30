# Koala Interpreter

## Table of Contents

1. [How to Build the Koala Interpreter](#how-to-build-the-koala-interpreter)
2. [How to Build the GUI Path Installer](#how-to-build-the-gui-path-installer)
3. [How to Run Koala Files](#how-to-run-koala-files)
4. [TODO List](#todo-list)

---

```
📦 
├─ .gitignore
├─ README.md
├─ index.koala
├─ installer_script.iss
└─ koala_interpreter.py
```


## How to Build the Koala Interpreter

1. Install **PyInstaller** using pip:
   ```bash
   pip install pyinstaller
   ```

2. Build the **Koala Interpreter** as a standalone executable:
   ```bash
   pyinstaller --onefile --name koala koala_interpreter.py
   ```

---

## How to Build the GUI Path Installer

1. Open **Inno Setup Compiler**.
2. Import the `installer_script.iss` into Inno Setup Compiler.
3. Compile the script to create the GUI installer for Koala.

---

## How to Run Koala Files

1. To run a `.koala` file, use the following command:
   ```bash
   koala file.koala
   ```

---

## TODO List

1. **Arithmetic Operators**:
   - Implement basic arithmetic operations: addition, subtraction, multiplication, division.
   - Add error handling for division by zero.
   
2. **List**:
   - Implement list creation and manipulation.
   - Support basic list operations: index access, appending, removing items, etc.

3. **Dictionary**:
   - Implement dictionary creation and key-value pair handling.
   - Add functionality for adding, updating, and deleting dictionary items.

4. **Testing**:
   - Write test cases for arithmetic operators, lists, and dictionaries.
   - Ensure correct error handling and edge cases are covered.

5. **Documentation**:
   - Expand documentation to include examples for the new features (arithmetic operators, lists, dictionaries).
   - Add a section for advanced features and troubleshooting.

6. **Optimization**:
   - Profile and optimize the performance of the Koala Interpreter for larger files.
   - Address memory consumption during extensive list and dictionary operations.