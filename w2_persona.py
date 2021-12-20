###persona
##task1
##q1
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv("persona.csv")
df.head()
df.tail()
df.shape
df.info()
df.describe().T
##q2
df["SOURCE"].nunique()
df["SOURCE"].value_counts()
##q3
df["PRICE"].nunique()
##q4
df["PRICE"].value_counts()
#q5
df["COUNTRY"].value_counts()
##q6
total_sales = df.groupby("COUNTRY")["PRICE"].sum()
##q7
sales_per_source = df["SOURCE"].value_counts()
##q8
av_price_country = pd.DataFrame({"AV_PRICE": df.groupby("COUNTRY")["PRICE"].mean()})
##q9
av_price_source = pd.DataFrame({"AV_PRICE": df.groupby("SOURCE")["PRICE"].mean()})
##q10
pd.DataFrame({"AV_PRICE": df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean()})

###task2
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "sum"})

###task3
agg_df = agg_df.sort_values("PRICE", ascending = False)

###task4
agg_df = agg_df.reset_index()
agg_df.head()

###task5
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins = [0, 18, 24, 35, 46, 61],
                           labels=["0_18", "19_23", "25_34", "35_46", "47_61"])

###task6
agg_df["customers_level_based"] = [agg_df["COUNTRY"][i].upper() + "_" + agg_df["SOURCE"][i].upper() + "_" +\
                                   agg_df["SEX"][i].upper() + "_" + str(agg_df["AGE_CAT"][i]) for i in range(len(agg_df))]

agg_df = pd.DataFrame({"customers_level_based": agg_df["customers_level_based"],
                        "PRICE": agg_df["PRICE"]})

agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

###task7
agg_df = pd.DataFrame({"customers_level_based": agg_df["customers_level_based"],
                       "PRICE": agg_df["PRICE"],
                       "SEGMENT": pd.qcut(agg_df["PRICE"], 4, ["D", "C", "B", "A"])})

##description of segments
agg_df.groupby("SEGMENT").agg(["mean", "max", "min", "sum"])

##analysis of price segment C
SEGMENT_C = agg_df[agg_df["SEGMENT"] == "C"]
SEGMENT_C["PRICE"].agg(["mean", "max", "min", "sum"])

##average return on 33 years old Android user Turkish female
new_user1 = "TUR_ANDROID_FEMALE_25_34"
agg_df[agg_df["customers_level_based"]==new_user1].agg({"SEGMENT": "max", "PRICE": "mean"})
##average return on 35 years old IOS user French female
new_user2 = "FRA_IOS_FEMALE_35_46"
agg_df[agg_df["customers_level_based"]==new_user2].agg({"SEGMENT": "max", "PRICE": "mean"})













###task6
#dilara kod
agg_df["customers_level_based"]=[(i[0]+""+i[1]+""+i[2]+"_"+i[5]).upper() for i in agg_df.values]
#hamit kod
[f"{agg_df['COUNTRY'][i].upper()}{agg_df['SOURCE'][i].upper()}\
{agg_df['SEX'][i].upper()}_{agg_df['AGE_CAT'][i].upper()}" for i in range(len(agg_df))]
#sevval
col_names = ["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]
agg_df[col_names]
agg_df["customers_level_based"] = ["_".join(row).upper() for row in agg_df[col_names].values]
agg_df
#tugrul kod
new_df = pd.DataFrame([agg_df["COUNTRY"][i].upper() + "" + agg_df["SOURCE"][i].upper() + "" + agg_df["SEX"][
    i].upper() + "_" + str(agg_df["AGE_CAT"][i]) for i in range(len(agg_df))])
#mehmet
pd.DataFrame(["_".join(col).upper() for col in agg_df[col_names].values])
#hamit2
A=[]
[A.append(f"{agg_df['COUNTRY'][i].upper()}{agg_df['SOURCE'][i].upper()}\
{agg_df['SEX'][i].upper()}_{agg_df['AGE_CAT'][i].upper()}") for i in range(len(agg_df))]
######hata: can only concatenate str (not "float") to str

###

df = pd.read_csv('titanic.csv')
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def cat_summary(dataframe, col_name, title=False, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    if plot:
        if title:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.title(col_name)
            plt.show()
        else:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show()



cat_summary(df, col_name="Embarked", title=False, plot=True)
