def main():
    print("enter two numbers")
    a = int(input())
    b = int(input())
    while (b != 0):
        c = b
        b = a%b
        a = c
    hcf = a
    print("The HCF is %d"%hcf )

if __name__ == '__main__':
    main()
