###persona project 

##task1

#1.importing data file and reviewing general information
import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv("persona.csv")
df.head()
df.tail()
df.shape
df.info()
df.describe().T

#2.Unique prices and their frequencies 
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

#3.Number of unique prices
df["PRICE"].nunique()

#4.Number of sales on each unnique prices
df["PRICE"].value_counts()

#5.Number of sales in each country 
df["COUNTRY"].value_counts()

#6.Earnings from sales in each country 
total_sales = df.groupby("COUNTRY")["PRICE"].sum()

#7.Number of sales accourding to source 
sales_per_source = df["SOURCE"].value_counts()

#8.Average prices by countries
av_price_country = pd.DataFrame({"AV_PRICE": df.groupby("COUNTRY")["PRICE"].mean()})

#9.Average prices by the type of sources
av_price_source = pd.DataFrame({"AV_PRICE": df.groupby("SOURCE")["PRICE"].mean()})

#10.Average prices by country and source
pd.DataFrame({"AV_PRICE": df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean()})

###task2: Total earnings by country, source, sex, age
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "sum"})

###task3: Sorting the previous output by price in descending order
agg_df = agg_df.sort_values("PRICE", ascending = False)

###task4: Converting the index to variable names 
agg_df = agg_df.reset_index()
agg_df.head()

###task5: Converting the age variable to categorical variable and add to the agg_df
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins = [0, 18, 24, 35, 46, 61],
                           labels=["0_18", "19_23", "25_34", "35_46", "47_61"])

###task6: Defining persona(level based customers)
agg_df["customers_level_based"] = [agg_df["COUNTRY"][i].upper() + "_" + agg_df["SOURCE"][i].upper() + "_" +\
                                   agg_df["SEX"][i].upper() + "_" + str(agg_df["AGE_CAT"][i]) for i in range(len(agg_df))]

agg_df = pd.DataFrame({"customers_level_based": agg_df["customers_level_based"],
                        "PRICE": agg_df["PRICE"]})

agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

###task7: Segmentation of persona
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



