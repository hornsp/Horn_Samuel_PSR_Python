def fizzBuzz(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    n = 16

    fizzBuzz(n)

if __name__ == "__main__":
    main()