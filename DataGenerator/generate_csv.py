import pandas as pd
import calculate_acc as acc
import calculate_bvp as bvp
import calculate_eda as eda
import calculate_glucose as glucose
import calculate_hr as hr
import calculate_ibi as ibi
import calculate_temp as temp
import calculate_rolling_sum as food
from os import path

if __name__ == '__main__':
    # Below lines take too long to work, therefore we ran them once
    # to create the initial csv, then worked our way from there

    # acc_mean = acc.calculateACC("mean")
    # acc_std = acc.calculateACC("std")
    # acc_min = acc.calculateACC("min")
    # acc_max = acc.calculateACC("max")
    # acc_q1g = acc.calculateACC("Q1G")
    # acc_q3g = acc.calculateACC("Q3G")
    # df = pd.DataFrame([acc_mean, acc_std, acc_min, acc_max, acc_q1g, acc_q3g])
    # df.to_csv("./data.csv")

    df = pd.read_csv("./data.csv")

    calorie2hr = pd.DataFrame(food.giveRollingSum("2h", "total_carb"))
    calorie8hr = pd.DataFrame(food.giveRollingSum("8h", "total_carb"))
    calorie24hr = pd.DataFrame(food.giveRollingSum("24h", "total_carb"))

    protein2hr = pd.DataFrame(food.giveRollingSum("2h", "protein"))
    protein8hr = pd.DataFrame(food.giveRollingSum("8h", "protein"))
    protein24hr = pd.DataFrame(food.giveRollingSum("24h", "protein"))

    sugar2hr = pd.DataFrame(food.giveRollingSum("2h", "sugar"))
    sugar8hr = pd.DataFrame(food.giveRollingSum("8h", "sugar"))
    sugar24hr = pd.DataFrame(food.giveRollingSum("24h", "sugar"))

    hr_min = pd.DataFrame(hr.calculateHR("min"))
    hr_max = pd.DataFrame(hr.calculateHR("max"))
    hr_mean = pd.DataFrame(hr.calculateHR("mean"))
    hr_Q1G = pd.DataFrame(hr.calculateHR("Q1G"))
    hr_Q3G = pd.DataFrame(hr.calculateHR("Q3G"))

    ibi_nn50 = pd.DataFrame(ibi.calculateIBI("NN50"))
    ibi_pnn50 = pd.DataFrame(ibi.calculateIBI("pNN50"))
    ibi_sdnn = pd.DataFrame(ibi.calculateIBI("SDNN"))
    ibi_rmssd = pd.DataFrame(ibi.calculateIBI("RMSSD"))

    temp_min = pd.DataFrame(temp.calculateTemp("min"))
    temp_max = pd.DataFrame(temp.calculateTemp("max"))
    temp_mean = pd.DataFrame(temp.calculateTemp("mean"))
    temp_std = pd.DataFrame(temp.calculateTemp("std"))
    temp_Q1G = pd.DataFrame(temp.calculateTemp("Q1G"))
    temp_Q3G = pd.DataFrame(temp.calculateTemp("Q3G"))



    print(ibi_nn50)
