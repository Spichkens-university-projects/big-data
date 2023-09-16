from sklearn.datasets import fetch_california_housing
from statistics import mean


def avg(x):
    return mean(x)


def main():
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    print(df.apply(avg))


if __name__ == "__main__":
    main()
