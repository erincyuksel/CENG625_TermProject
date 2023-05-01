import pandas as pd

def calculateBVP(operation):
    dictToReturn = {}
    arr = []
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/BVP_0{index}.csv')
        df.rename(columns={" bvp" : "bvp"}, inplace=True)
        df['bvp'] = pd.to_numeric(df['bvp'], downcast="float")
        if operation == "min":
            arr.append('{0:.2f}'.format(df["bvp"].min()))
        if operation == "max":
            arr.append('{0:.2f}'.format(df["bvp"].max()))
        if operation == "Q1G":
            arr.append(float('{0:.2f}'.format(df["bvp"].quantile(0.25))))
        if operation == "Q3G":
            arr.append(float('{0:.2f}'.format(df["bvp"].quantile(0.75))))
        if operation == "std":
            arr.append(float('{0:.2f}'.format(df["bvp"].std())))
        if operation == "mean":
            arr.append(float('{0:.2f}'.format(df["bvp"].mean())))
    return dictToReturn

if __name__ == '__main__':
    #small test
    dict = calculateBVP("mean")
    print(dict)