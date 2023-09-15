def main(N):
    res = ""
    for i in range(0, N):
        res += (str(i) + " ") * i

    print("".join(res.split(" ")[:N]))


if __name__ == "__main__":
    N = int(input("N >> "))
    main(N)