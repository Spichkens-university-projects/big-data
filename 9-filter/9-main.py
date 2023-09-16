from sklearn.datasets import fetch_california_housing
import pandas as pd


def main():
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    filtered = df.loc[((df['HouseAge'] > 50.0) & (df['Population'] > 2500.0))]
    print(filtered)
    

if __name__ == "__main__":
    main()
