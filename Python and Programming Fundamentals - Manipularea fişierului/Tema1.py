import calculator

def reverse(text):
    rev = ''
    for i in range(len(text), 0, -1):
        rev += text[i-1]
    return rev

with open(r"C:\Users\andre\OneDrive\Desktop\Temaaa1\expresii1", "r") as f:
    with open(r"C:\Users\andre\OneDrive\Desktop\Temaaa1\iesire1", "w") as f2:
        content = f.read()
        lines = content.splitlines()
        b = ''
        c = ''
        d = ''
        result = []
        for i in lines:
            b = ''
            for j in i:
                if j.isnumeric():
                    b = b + j
                if j == '+' or j == '-' or j == '/' or j == '*':
                    c = c + b
            b = ''
            reverse_i = reversed(i)
            for k in reverse_i:
                if k.isnumeric():
                    b = b + k
                if k == '+' or k == '-' or k == '/' or k == '*':
                    d = d + reverse(b)
                    if k == '+':
                        result.append(calculator.sum(int(c), int(d)))
                    if k == '-':
                        result.append(calculator.sub(int(c), int(d)))
                    if k == '/':
                        result.append(calculator.div(int(c), int(d)))
                    if k == '*':
                        result.append(calculator.mul(int(c), int(d)))
            c = ''
            d = ''
        for index in range(len(lines)):
            f2.write(str(lines[index]) + " = " + str(result[index]) + "\n")
    print("Operations: ", lines)
    print("Results for operations: ", result)

with open(r"C:\Users\andre\OneDrive\Desktop\Temaaa1\iesire1", "r") as f3:
    print(f3.read())
    print(f3.name)