# A function is a reusable chunk of code that is used to accomplish a single, related action. 
# Functions are an important aspect of the Python programming language, and there are many built-in functions.
# Nevertheless, as Python programmers, we frequently need to develop custom methods to address difficulties.

# How to write a function (Syntax)?
'''def function_name():
    {
        # some code here
    }
'''
#basic function of adding two number
def add_number(num1, num2):
    return num1 + num2
#calling a function
print(add_number(20,5))

#lets test something out
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  FAIL '
    print((f' {prefix} got: {got} expected: {expected}'))

#checking print the function of test
test('f', 'fo')
test('w', 'w')
