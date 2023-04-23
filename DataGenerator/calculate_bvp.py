import pandas as pd

def calculateBVP(operation):
    dictToReturn = {}
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/BVP_0{index}.csv')
        df.rename(columns={" bvp" : "bvp"}, inplace=True)
        df['bvp'] = pd.to_numeric(df['bvp'], downcast="float")
        if operation == "min":
            dictToReturn[i] = df["bvp"].min()
        if operation == "max":
            dictToReturn[i] = df["bvp"].max()
        if operation == "Q1G":
            dictToReturn[i] = '{0:.2f}'.format(df["bvp"].quantile(0.25))
        if operation == "Q3G":
            dictToReturn[i] = '{0:.2f}'.format(df["bvp"].quantile(0.75))
        if operation == "std":
            dictToReturn[i] = '{0:.2f}'.format(df["bvp"].std())
        if operation == "mean":
            dictToReturn[i] = '{0:.2f}'.format(df["bvp"].mean())
    return dictToReturn

if __name__ == '__main__':
    #small test
    dict = calculateBVP("mean")
    print(dict)