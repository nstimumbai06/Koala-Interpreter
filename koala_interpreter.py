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

execute_koala_file('index.koala')