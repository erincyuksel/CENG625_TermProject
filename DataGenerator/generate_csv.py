import pandas as pd
import calculate_acc as acc
import calculate_bvp as bvp
import calculate_eda as eda
import calculate_glucose as glucose
import calculate_hr as hr
import calculate_ibi as ibi
import calculate_temp as temp
import calculate_rolling_sum as food

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

    # bvp_min = pd.DataFrame(bvp.calculateBVP("min"))
    # bvp_max = pd.DataFrame(bvp.calculateBVP("max"))
    # bvp_mean = pd.DataFrame(bvp.calculateBVP("mean"))
    # bvp_std = pd.DataFrame(bvp.calculateBVP("std"))
    # bvp_Q1G = pd.DataFrame(bvp.calculateBVP("Q1G"))
    # bvp_Q3G = pd.DataFrame(bvp.calculateBVP("Q3G"))
    # df2 = pd.concat([bvp_min, bvp_max, bvp_mean, bvp_std, bvp_Q1G, bvp_Q3G], axis=1)
    # df2.to_csv("./bvp.csv")


    # Start building the initial CSV file for our machine learning process
    df = pd.read_csv("./data.csv")
    # 0 is male, 1 is female
    # 0 is normal, 1 is prediabetic
    demographics = {"gender": [1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,0],
                    "HbA1c": [5.5, 5.6, 5.9, 6.4, 5.7, 5.8, 5.3, 5.6, 6.1, 6.0, 6.0, 5.6, 5.7, 5.5, 5.5, 5.5],
                    "class": [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0]}

    demographics = pd.DataFrame(demographics)

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
    hr_std = pd.DataFrame(hr.calculateHR("std"))
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

    eda_min = pd.DataFrame(eda.calculateEDA("min"))
    eda_max = pd.DataFrame(eda.calculateEDA("max"))
    eda_mean = pd.DataFrame(eda.calculateEDA("mean"))
    eda_std = pd.DataFrame(eda.calculateEDA("std"))
    eda_Q1G = pd.DataFrame(eda.calculateEDA("Q1G"))
    eda_Q3G = pd.DataFrame(eda.calculateEDA("Q3G"))

    df = pd.concat([calorie2hr, calorie8hr, calorie24hr, protein2hr, protein24hr, protein24hr,
               sugar2hr, sugar8hr, sugar24hr, hr_min, hr_max, hr_mean, hr_std, hr_Q1G, hr_Q3G,
               ibi_nn50, ibi_pnn50, ibi_sdnn, ibi_rmssd, temp_min, temp_max, temp_mean, temp_std, temp_Q1G, temp_Q3G,
               eda_min, eda_max, eda_mean, eda_std,
               eda_Q1G, eda_Q3G, demographics], axis=1)
    df.to_csv("./data.csv")
