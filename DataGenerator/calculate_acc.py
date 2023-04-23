import pandas as pd
import numpy as np
def calculateACC(operation):
    dictToReturn = {}
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/ACC_0{index}.csv')
        df.rename(columns={" acc_x" : "acc_x"}, inplace=True)
        df.rename(columns={" acc_y" : "acc_y"}, inplace=True)
        df.rename(columns={" acc_z" : "acc_z"}, inplace=True)
        df['acc_x'] = pd.to_numeric(df['acc_x'], downcast="float")
        df['acc_y'] = pd.to_numeric(df['acc_y'], downcast="float")
        df['acc_z'] = pd.to_numeric(df['acc_z'], downcast="float")
        #get vector magnitude of the three axes
        df["vec_mag"] = np.sqrt(np.power(df["acc_x"], 2) + np.power(df["acc_y"], 2) + np.power(df["acc_z"], 2))
        if operation == "mean":
            dictToReturn[i] = df["vec_mag"].mean()
        if operation == "std":
            dictToReturn[i] = df["vec_mag"].std()
    return dictToReturn

if __name__ == '__main__':
    #small test
    dict = calculateACC("mean")
    print(dict[0])