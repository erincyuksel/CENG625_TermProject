import pandas as pd

def calculateHR(operation):
    dictToReturn = {}
    arr = []
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/HR_0{index}.csv')
        df["datetime"] = pd.to_datetime(df["datetime"])
        df.index = pd.DatetimeIndex(df["datetime"])
        df = df.sort_index()
        df.rename(columns={" hr" : "hr"}, inplace=True)
        df['hr'] = pd.to_numeric(df['hr'], downcast="float")
        if operation == "min":
            arr.append(float('{0:.2f}'.format(df["hr"].min())))
        if operation == "max":
            arr.append(float('{0:.2f}'.format(df["hr"].max())))
        if operation == "Q1G":
            arr.append(float('{0:.2f}'.format(df["hr"].quantile(0.25))))
        if operation == "Q3G":
            arr.append(float('{0:.2f}'.format(df["hr"].quantile(0.75))))
        if operation == "std":
            arr.append(float('{0:.2f}'.format(df["hr"].std())))
        if operation == "mean":
            arr.append(float('{0:.2f}'.format(df["hr"].mean())))
    dictToReturn["hr_" + operation] = arr
    return dictToReturn

if __name__ == '__main__':
    #small test
    dicts = calculateHR("mean")
    print(dicts)