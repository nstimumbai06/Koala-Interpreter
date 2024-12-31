import sys
import os
import re

class ThodaIdharAye:
    def log(self, message):
        print(message)

thoda_idhar_aye = ThodaIdharAye()

def execute_koala_file(file_path):
    variables = {}

    def evaluate_expression(operator, operands):
        if operator == '+':
            return sum(operands)
        elif operator == '-':
            return operands[0] - operands[1]
        elif operator == '*':
            return operands[0] * operands[1]
        elif operator == '/':
            try:
                return operands[0] / operands[1]
            except ZeroDivisionError:
                return "Error: Division by zero"

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("//") or not line:
                continue

            if match := re.match(r'thoda_idhar_aye\.log\((.*?)\)', line):
                message = match.group(1).strip()
                if message in variables:
                    message = variables[message]
                thoda_idhar_aye.log(message)
            
            elif match := re.match(r'(\w+)?\s*=?\s*ek_kaam_kro:\s*(\w+),\s*(\+|\-|\*|\/),\s*(.*)', line):
                var_name = match.group(1)
                func_name = match.group(2)
                operator = match.group(3)
                operands = match.group(4).split(',')
                operands = [int(operand.strip()) if operand.strip().isdigit() else variables.get(operand.strip()) for operand in operands]

                if None in operands:
                    thoda_idhar_aye.log("aayein: Undefined variable used in operation.")
                    continue

                result = evaluate_expression(operator, operands)

                if var_name:
                    variables[var_name] = result
            
            elif match := re.match(r'reason_mat_do:\s*throw\((.*?)\)', line):
                error_type = match.group(1).strip()
                try:
                    if error_type == 'zerodivisionerror':
                        raise ZeroDivisionError("Custom ZeroDivisionError")
                    elif error_type == 'ioerror':
                        raise IOError("Custom IOError")
                    elif error_type == 'attributeerror':
                        raise AttributeError("Custom AttributeError")
                    elif error_type == 'datatypeerror':
                        raise TypeError("Custom TypeError")
                    elif error_type == 'importerror':
                        raise ImportError("Custom ImportError")
                    elif error_type == 'typeerror':
                        raise TypeError("Custom TypeError")
                except Exception as e:
                    thoda_idhar_aye.log(f"aayein: Caught error: {e}")
            
            else:
                thoda_idhar_aye.log(f"aayein: Syntax error: {line}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: koala <path_to_koala_file>")
        sys.exit(1)

    koala_file = sys.argv[1]

    if not os.path.exists(koala_file):
        print(f"aayein: File not found: {koala_file}")
        sys.exit(1)

    execute_koala_file(koala_file)
