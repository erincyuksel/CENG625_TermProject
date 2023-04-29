import pandas as pd

def calculateGlucose(operation):
    dictToReturn = {}
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/Dexcom_0{index}.csv')
        df['Glucose Value (mg/dL)'] = pd.to_numeric(df['Glucose Value (mg/dL)'], downcast="float")
        if operation == "min":
            dictToReturn[i] = df["Glucose Value (mg/dL)"].min()
        if operation == "max":
            dictToReturn[i] = df["Glucose Value (mg/dL)"].max()
        if operation == "Q1G":
            dictToReturn[i] = '{0:.2f}'.format(df["Glucose Value (mg/dL)"].quantile(0.25))
        if operation == "Q3G":
            dictToReturn[i] = '{0:.2f}'.format(df["Glucose Value (mg/dL)"].quantile(0.75))
        if operation == "std":
            dictToReturn[i] = '{0:.2f}'.format(df["Glucose Value (mg/dL)"].std())
        if operation == "mean":
            dictToReturn[i] = '{0:.2f}'.format(df["Glucose Value (mg/dL)"].mean())
    return dictToReturn

if __name__ == '__main__':
    #small test
    dict = calculateGlucose("max")
    print(dict)