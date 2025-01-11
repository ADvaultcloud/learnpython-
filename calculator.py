print("Calculator")

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

def mod(n1,n2):
    return n1 % n2

operations={
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "%": mod,
}


# print(operations["*"](2,3))
def calculator():
    should_accumulate=True
    num1=float(input("Give the first number to be calculated:"))
    while should_accumulate:
        for symbols in operations:
            print(symbols)
        choose_operation = input("Choose an operation to be executed:")
        #print(operations[choose_operation](num1,num2))n
        num2=float(input("Give the second number to be calculated:"))
        answer=operations[choose_operation](num1,num2)
        print(f"{num1} {choose_operation} {num2} = {answer}")

        choice = input("Type 'y' to continue calculating with {answer}, or Type 'n' to start a new calculation:")
        if choice == "y":
            num1=answer
        else:
            should_accumulate = False
            # print("\n" * 20)    
            calculator()

calculator()
