def main():
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    area = length * width
    perimeter = 2 *(length + width)
    print("The area of your rectangle is " + str(area))
    print("The perimeter of your rectangle is " + str(perimeter))


if __name__ == '__main__':
    main()