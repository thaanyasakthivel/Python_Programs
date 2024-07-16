from lab import factorial

if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")
