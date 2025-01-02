import sys
import os
import re

class Console:
    @staticmethod
    def log(message):
        print(message)

console = Console()

def execute_ts_file(file_path):
    variables = {}

    def evaluate_expression(expression):
        try:
            for var in variables:
                expression = re.sub(rf'\b{var}\b', str(variables[var]), expression)
            return eval(expression, {"__builtins__": {}})
        except Exception as e:
            raise ValueError(f"Invalid expression: {expression}. Error: {e}")

    def parse_condition(condition):
        try:
            condition = re.sub(r'\b(\w+)\b', lambda m: str(variables.get(m.group(1), m.group(1))), condition)
            return eval(condition, {"__builtins__": {}})
        except Exception as e:
            console.log(f"Invalid condition: {condition}. Error: {e}")
            return False

    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if line.startswith("//") or not line:
                i += 1
                continue

            if match := re.match(r'console\.log\((.*?)\);', line):
                message = match.group(1).strip()
                try:
                    message = evaluate_expression(message) if '"' not in message else message.strip('"')
                except ValueError as e:
                    console.log(f"Error in console.log: {e}")
                else:
                    console.log(message)

            elif match := re.match(r'(let|const)\s+(\w+)\s*:\s*(number|string)\s*=\s*(.+);', line):
                var_type, var_name, var_kind, expression = match.groups()

                try:
                    value = evaluate_expression(expression) if var_kind == "number" else expression.strip('"')
                except ValueError as e:
                    console.log(f"Error: Invalid value for {var_name}. {e}")
                    i += 1
                    continue

                if var_kind == "number" and not isinstance(value, (int, float)):
                    console.log(f"Type Error: Expected a number for variable '{var_name}'")
                elif var_kind == "string" and not isinstance(value, str):
                    console.log(f"Type Error: Expected a string for variable '{var_name}'")
                else:
                    variables[var_name] = value

            elif match := re.match(r'if\s*\((.*?)\)\s*{', line):
                condition = match.group(1).strip()
                if not parse_condition(condition):
                    depth = 1
                    while depth > 0 and i + 1 < len(lines):
                        i += 1
                        if '{' in lines[i]:
                            depth += 1
                        if '}' in lines[i]:
                            depth -= 1

            elif match := re.match(r'throw\((.*?)\);', line):
                error_message = match.group(1).strip()
                raise Exception(error_message)

            elif line == '}':
                i += 1
                continue

            else:
                console.log(f"Syntax Error: {line}")

            i += 1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ts <path_to_ts_file>")
        sys.exit(1)

    ts_file = sys.argv[1]

    if not os.path.exists(ts_file):
        print(f"Error: File not found: {ts_file}")
        sys.exit(1)

    try:
        execute_ts_file(ts_file)
    except Exception as e:
        print(f"Unhandled Exception: {e}")
