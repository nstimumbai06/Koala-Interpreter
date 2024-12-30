import sys
import os
import re

class ThodaIdharAye:
    def log(self, message):
        print(message)

thoda_idhar_aye = ThodaIdharAye()

def execute_koala_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if match := re.match(r'thoda_idhar_aye\.log\(\"(.*?)\"\)', line):
                message = match.group(1)
                thoda_idhar_aye.log(message)
            else:
                print(f"Syntax error: {line}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: koala <path_to_koala_file>")
        sys.exit(1)

    koala_file = sys.argv[1]

    if not os.path.exists(koala_file):
        print(f"File not found: {koala_file}")
        sys.exit(1)

    execute_koala_file(koala_file)
