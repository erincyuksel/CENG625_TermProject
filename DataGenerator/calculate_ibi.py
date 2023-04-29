import math

import pandas as pd
def calculateIBI(operation):
    dictToReturn = {}
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/IBI_0{index}.csv')
        df.rename(columns={" ibi" : "ibi"}, inplace=True)
        df['ibi'] = pd.to_numeric(df['ibi'], downcast="float")
        if operation == "NN50":
            dictToReturn[i] = sum(abs(df["ibi"] - df["ibi"].shift(1)) >= 0.05)
        if operation == "pNN50":
            NN50 = abs(df["ibi"] - df["ibi"].shift(1)) >= 0.05
            num_true = sum(NN50)
            dictToReturn[i] = num_true / len(NN50)
        if operation == "SDNN":
            dictToReturn[i] = df["ibi"].std()
        if operation == "RMSSD":
            ibiDifferences = df["ibi"].diff().fillna(0).pow(2).sum()
            dictToReturn[i] = math.sqrt(ibiDifferences) / len(df)
    return dictToReturn

if __name__ == '__main__':
    #small test
    dict = calculateIBI("RMSSD")
    print(dict)