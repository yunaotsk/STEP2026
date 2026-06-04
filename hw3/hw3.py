#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_multiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1



def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isspace():
            index += 1
        elif line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_multiply(line, index)
        elif line[index] == '/':    
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            token = {'type': 'LPAREN'}
            index += 1
        elif line[index] == ')':
            token = {'type': 'RPAREN'}
            index += 1
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    def evaluate_arithmetic(tokens):
        answer = 0
        tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
        index = 1
        index1 = 1
        while index < len(tokens):
            if tokens[index]['type'] == 'MULTIPLY':
                tokens[index - 1]['number'] *= tokens[index + 1]['number']
                del tokens[index:index + 2]
            elif tokens[index]['type'] == 'DIVIDE':
                tokens[index - 1]['number'] /= tokens[index + 1]['number']
                del tokens[index:index + 2]
            else:
                index += 1
        while index1 < len(tokens):
            if tokens[index1]['type'] == 'NUMBER':
                if tokens[index1 - 1]['type'] == 'PLUS':
                    answer += tokens[index1]['number']
                elif tokens[index1 - 1]['type'] == 'MINUS':
                    answer -= tokens[index1]['number']
                else:
                    print('Invalid syntax')
                    exit(1)
            index1 += 1
        return answer
    index0 = 1
    start_index = []
    while index0 < len(tokens):
        if tokens[index0]['type'] == 'LPAREN':
            start_index.append(index0)
        if tokens[index0]['type'] == 'RPAREN':
            end_index = index0
            sub_answer = evaluate_arithmetic(tokens[start_index[-1] + 1:end_index])
            tokens[start_index[-1]] = {'type': 'NUMBER', 'number': sub_answer}
            del tokens[start_index[-1] + 1:end_index + 1]
            index0 = start_index[-1]
            start_index.pop()
        index0 += 1
    return evaluate_arithmetic(tokens)


def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1")
    test("1.0+2.1-3")
    test("1.0+2")
    test("1.0+2.0")
    test("10-3")
    test("1.0*0")
    test("1.0*2.0")
    test("1*2*3")
    test("8/2/2")
    test("2*4/2")
    test("2+3*4")
    test("2/3*4")
    test("2*(3+4)")
    test("2*(3+4*5)")
    test("2/(4*5)+6")
    test("0*(2/3)")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
