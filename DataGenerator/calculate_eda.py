import pandas as pd

def calculateEDA(operation):
    dictToReturn = {}
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/EDA_0{index}.csv')
        df.rename(columns={" eda" : "eda"}, inplace=True)
        df['eda'] = pd.to_numeric(df['eda'], downcast="float")
        if operation == "min":
            dictToReturn[i] = df["bvp"].min()
        if operation == "max":
            dictToReturn[i] = df["bvp"].max()
        if operation == "Q1G":
            dictToReturn[i] = '{0:.2f}'.format(df["eda"].quantile(0.25))
        if operation == "Q3G":
            dictToReturn[i] = '{0:.2f}'.format(df["eda"].quantile(0.75))
        if operation == "std":
            dictToReturn[i] = '{0:.2f}'.format(df["eda"].std())
        if operation == "mean":
            dictToReturn[i] = '{0:.2f}'.format(df["eda"].mean())
    return dictToReturn

if __name__ == '__main__':
    #small test
    dict = calculateEDA("mean")
    print(dict)