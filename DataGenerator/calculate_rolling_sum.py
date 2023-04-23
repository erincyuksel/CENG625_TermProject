import pandas as pd
def giveRollingSum(timeInterval, category):
    dictToReturn = {}
    for i in range(16):
        index = str(i+1).zfill(2)
        df = pd.read_csv(f'../Participants/Participant_{i+1}/Food_Log_0{index}.csv')
        df["time_begin"] = pd.to_datetime(df["time_begin"])
        df.index = pd.DatetimeIndex(df["time_begin"])
        df = df.sort_index()
        result = df.rolling(timeInterval, on="time_begin")[category].sum()
        dictToReturn[i] = result.sum()
    return dictToReturn

if __name__ == '__main__':
    #small test
    result = giveRollingSum("2h", "total_carb")
    print(result)
    # create DataFrame
    # df = pd.DataFrame({'date': pd.date_range(start='1/1/2020', freq='min', periods=12),
    #                    'sales': [6, 8, 9, 11, 13, 8, 8, 15, 22, 9, 8, 4],
    #                    'returns': [0, 3, 2, 2, 1, 3, 2, 4, 1, 5, 3, 2]})
    # print(df)
    # # set 'date' column as index
    # df = df.set_index('date')
    # result = df.resample('5min').sum()
    # print(result)