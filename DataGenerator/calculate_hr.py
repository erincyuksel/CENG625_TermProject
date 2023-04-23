import pandas as pd

def calculateHR(operation):
    dictToReturn = {}
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/HR_0{index}.csv')
        df.rename(columns={" hr" : "hr"}, inplace=True)
        df['hr'] = pd.to_numeric(df['hr'], downcast="float")
        if operation == "min":
            dictToReturn[i] = df["hr"].min()
        if operation == "max":
            dictToReturn[i] = df["hr"].max()
        if operation == "Q1G":
            dictToReturn[i] = '{0:.2f}'.format(df["hr"].quantile(0.25))
        if operation == "Q3G":
            dictToReturn[i] = '{0:.2f}'.format(df["hr"].quantile(0.75))
        if operation == "std":
            dictToReturn[i] = '{0:.2f}'.format(df["hr"].std())
        if operation == "mean":
            dictToReturn[i] = '{0:.2f}'.format(df["hr"].mean())
    return dictToReturn

if __name__ == '__main__':
    #small test
    dict = calculateHR("mean")
    print(dict)