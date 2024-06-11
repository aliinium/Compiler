import re

class PascalInterpreter:
    def __init__(self, filename):
        self.filename = filename
        self.code = self.read_file()
        self.variables = {}

    def read_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def parse_code(self):
        self.code = re.sub(r'\s+', ' ', self.code)
        self.code = self.code.strip()

    def execute(self):
        self.parse_code()
        if not self.code.startswith("var") or "begin" not in self.code or "end." not in self.code:
            raise ValueError("Invalid Pascal code")

        var_section = self.code[self.code.find("var") + 3:self.code.find("begin")].strip()
        begin_section = self.code[self.code.find("begin") + 5:self.code.find("end.")].strip()

        self.declare_variables(var_section)
        self.execute_statements(begin_section)

    def declare_variables(self, var_section):
        var_section = var_section.strip()
        declarations = var_section.split(';')
        for decl in declarations:
            if decl:
                var_name, var_type = decl.split(':')
                var_name = var_name.strip()
                var_type = var_type.strip()
                if var_type == "integer":
                    self.variables[var_name] = 0

    def execute_statements(self, begin_section):
        statements = self.split_statements(begin_section)
        for statement in statements:
            if statement:
                self.execute_statement(statement.strip())

    def split_statements(self, code):
        statements = []
        nested_level = 0
        current_statement = ""
        for char in code:
            if char == ';' and nested_level == 0:
                statements.append(current_statement.strip())
                current_statement = ""
            else:
                if char == 'b' and code[code.index(char):].startswith("begin"):
                    nested_level += 1
                if char == 'e' and code[code.index(char):].startswith("end"):
                    nested_level -= 1
                current_statement += char
        if current_statement:
            statements.append(current_statement.strip())
        return statements

    def execute_statement(self, statement):
        if ":=" in statement:
            var_name, value = statement.split(":=")
            var_name = var_name.strip()
            value = self.evaluate_expression(value.strip())
            if var_name in self.variables:
                self.variables[var_name] = value
            else:
                raise ValueError(f"Variable {var_name} not declared")
        elif statement.startswith("writeln"):
            content = re.findall(r'\((.*?)\)', statement)[0].strip()
            if content.startswith("'") and content.endswith("'"):
                print(content[1:-1])
            else:
                if content in self.variables:
                    print(self.variables[content])
                else:
                    raise ValueError(f"Variable {content} not declared")
        elif statement.startswith("if"):
            condition_match = re.match(r'if\s*\((.*?)\)\s*then\s*(.*)', statement)
            if condition_match:
                condition_expr = condition_match.group(1).strip()
                then_clause = condition_match.group(2).strip()
                if self.evaluate_condition(condition_expr):
                    if then_clause.startswith("begin"):
                        nested_statements = then_clause[5:then_clause.rfind("end")].strip()
                        self.execute_statements(nested_statements)
                    else:
                        self.execute_statement(then_clause)
        else:
            raise ValueError(f"Unknown statement {statement}")

    def evaluate_expression(self, expr):
        expr = expr.strip()
        try:
            return eval(expr, {}, self.variables)
        except:
            raise ValueError(f"Invalid expression {expr}")

    def evaluate_condition(self, condition):
        tokens = re.split(r'(\W+)', condition)
        left = self.evaluate_expression(tokens[0].strip())
        operator = tokens[1].strip()
        right = self.evaluate_expression(tokens[2].strip())

        if operator == ">=":
            return left >= right
        elif operator == "<=":
            return left <= right
        elif operator == ">":
            return left > right
        elif operator == "<":
            return left < right
        elif operator == "==":
            return left == right
        elif operator == "!=":
            return left != right
        else:
            raise ValueError(f"Unknown operator {operator}")

interpreter = PascalInterpreter('2.pas')
interpreter.execute()
