with open("expresii1", "r") as f_in:
    with open("iesire", "w") as f_out:
        lines = f_in.readlines()
        operators = ['+','-', '*', '/']

        for lineFromFile in lines:
            for op in operators:
                 parts = lineFromFile.split(op)
                 if len(parts) == 2:
                      expression = parts[0] + op + parts[1].rstrip()
                      f_out.write(expression + " = ")
                      f_out.write(str(float(eval(expression))))
                      f_out.write("\n")
                      break

with open(r"iesire", "r") as f_in:
    print(f_in.read())
