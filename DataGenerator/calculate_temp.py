import pandas as pd

def calculateTemp(operation):
    dictToReturn = {}
    arr = []
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/TEMP_0{index}.csv')
        df.rename(columns={" temp" : "temp"}, inplace=True)
        df['temp'] = pd.to_numeric(df['temp'], downcast="float")
        if operation == "min":
            arr.append('{0:.2f}'.format(df["temp"].min()))
        if operation == "max":
            arr.append('{0:.2f}'.format(df["temp"].max()))
        if operation == "Q1G":
            arr.append(float('{0:.2f}'.format(df["temp"].quantile(0.25))))
        if operation == "Q3G":
            arr.append(float('{0:.2f}'.format(df["temp"].quantile(0.75))))
        if operation == "std":
            arr.append('{0:.2f}'.format(df["temp"].std()))
        if operation == "mean":
            arr.append('{0:.2f}'.format(df["temp"].mean()))
    dictToReturn["temp_" + operation] = arr
    return dictToReturn

if __name__ == '__main__':
    #small test
    dict = calculateTemp("mean")
    print(dict)