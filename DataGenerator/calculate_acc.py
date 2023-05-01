import math

import pandas as pd
import numpy as np
def calculateACC(operation):
    dictToReturn = {}
    arr = []
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/ACC_0{index}.csv')
        df["datetime"] = pd.to_datetime(df["datetime"])
        df.index = pd.DatetimeIndex(df["datetime"])
        df = df.sort_index()
        df.rename(columns={" acc_x" : "acc_x"}, inplace=True)
        df.rename(columns={" acc_y" : "acc_y"}, inplace=True)
        df.rename(columns={" acc_z" : "acc_z"}, inplace=True)
        df['acc_x'] = pd.to_numeric(df['acc_x'], downcast="float")
        df['acc_y'] = pd.to_numeric(df['acc_y'], downcast="float")
        df['acc_z'] = pd.to_numeric(df['acc_z'], downcast="float")
        df['acc_x'] = df["acc_x"] ** 2
        df['acc_y'] = df["acc_y"] ** 2
        df['acc_z'] = df["acc_z"] ** 2
        #get vector magnitude of the three axes
        df["vec_mag"] = np.sqrt(df["acc_x"] + df["acc_y"] + df["acc_z"])
        if operation == "mean":
            arr.append(df["vec_mag"].mean())
        if operation == "std":
            arr.append(df["vec_mag"].std())
        if operation == "min":
            arr.append(df["vec_mag"].min())
        if operation == "max":
            arr.append(df["vec_mag"].max())
        if operation == "Q1G":
            arr.append('{0:.2f}'.format(df["vec_mag"].quantile(0.25)))
        if operation == "Q3G":
            arr.append('{0:.2f}'.format(df["vec_mag"].quantile(0.75)))
    dictToReturn["acc_" + operation] = arr
    return dictToReturn

if __name__ == '__main__':
    #small test
    dicts = calculateACC("mean")
    print(dicts)