def main(sum):
    while sum != 0:
        print("sum = " + str(sum))
        sum += float(input(">> "))


if __name__ == "__main__":
    start = float(input(">> "))
    main(start)
