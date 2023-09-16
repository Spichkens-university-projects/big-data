from sklearn.datasets import fetch_california_housing
import pandas as pd


def main():
    data = fetch_california_housing(as_frame=True)
    df = data.frame

    print(df.isna().sum())


if __name__ == "__main__":
    main()
