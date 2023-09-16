def main():
    A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']

    dct = {}
    for i in range(len(B)):
        dct[B[i]] = sum(A[j] for j in range(len(A)) if B[j] == B[i])

    print(dct)


if __name__ == "__main__":
    main()