from sklearn.datasets import fetch_california_housing


def main():
    data = fetch_california_housing(as_frame=True)
    print(data)


if __name__ == "__main__":
    main()
