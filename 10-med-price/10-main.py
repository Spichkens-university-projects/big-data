from sklearn.datasets import fetch_california_housing


def main():
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    print("Max: " + str(df["MedHouseVal"].max()))
    print("Min: " + str(df["MedHouseVal"].min()))


if __name__ == "__main__":
    main()
