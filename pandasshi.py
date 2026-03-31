import pandas as pd 

# path = r"C:\Users\User\Downloads\titanic.csv"

# df = pd.read_csv(path, index_col=0, na_values = r"\N")
# print(df.head())
# print(df.tail(2))
# print(df.shape)
# print(df.info())
# df2 = df.copy()
# fare_col=df.columns.get_loc("Fare")
# df2.iloc[0, df.columns.get_loc("Fare")] = 0
# df.iloc[0] ["Fare"], df2.iloc[0]["Fare"]
# print(df.iloc[0, fare_col], df2.iloc[0, fare_col])

# df2 = df.copy()
# df2.loc[1, "Fare"] = 0
# print(df2.loc[1, "Fare"])
# print(df.loc[1, "Fare"])
# print(df["Fare"].mean())
# print(df["Survived"].value_counts())    
# females = df[df["Sex"] == "female"]
# print(females.shape[0])

# print(df.columns)

# print(df)
# a = df["Embarked"] == "S"
# print(a)
# b = df[(df["Embarked"] == "S") & (df["Sex"] == "female")]
# print(b)

# df_small = df[["Name", "Sex", "Age"]]
# df_small.shape

# print(df_small)

# c = df[["Embarked", "Age", "Cabin"]].isna().sum()
# print(c)
# c = df[df[["Embarked", "Age", "Cabin"]].isna().any(axis=1)]
# c.reset_index(inplace = True)
# print(c)


# print(df["Age"].mean())


# df2 = df.copy() 

# df2["FamilySize"] = df2["SibSp"] + df2["Parch"] + 1
# df2max = df2["FamilySize"].max()

# print(df2)
# print(df2max)



# d= df[(df["Survived"] == 1) & (df["Sex"] == "male")]
# print(d)

# e = df[df["Sex"] == "male"].shape[0]
# print(e)


# temp = pd.concat([df, d])
# temp.shape
# print(temp)
# print(temp.shape)
# temp2 = temp.drop_duplicates(inplace=True)
# print(temp2)
# print(temp)
# print(df["Survived"].mean())



# path = r"C:\Users\User\Downloads\titanic.csv"

# df = pd.read_csv(path, index_col=0, na_values = r"\N")

# print(df.shape)
# print(df.head(7))
# print(df.info())


# print(df["Cabin"].isna().sum())

# df2 = df.copy()
# first_id = df.index[0]

# before = df.loc[first_id, "Fare"]
# df2.loc[first_id, "Fare"] = 0

# print("PassengerId:", first_id, "| df Fare:", before, "| df2 Fare:", df2.loc[first_id, "Fare"])


# df2 = df.copy()

# farecol= df.columns.get_loc("Fare")

# df.iloc[0, farecol]


# print(df.iloc[0,farecol])






# df3 = pd.concat([df,df2], ignore_index=True)

# print(df3.shape)

# df3_clean = df3.drop_duplicates()

# print(df3_clean.shape)

# df3_none = df3.drop_duplicates(keep=False)
# print(df3)
# print(df3_none.shape)
# print(df3_none.head())



# df4 = df.copy()

# df4["FamilySize"] = df4["SibSp"] + df4["Parch"] + 1
# print(df4)

# realquick = df4[(df4["FamilySize"] >= 5) & (df4["Survived"] == 1)]
# realquick2 = df4[(df4["FamilySize"] >= 5) & (df4["Survived"] == 0)]

# print(realquick)
# print(realquick2)


# realquick3 = df4[df4["FamilySize"] > 5]

# checkingmean = realquick3["Survived"].mean()


# # print(realquick3)
# # print(checkingmean)
# # print(realquick3.shape)






# # df2 = df[(df["Embarked"] == "S") & (df["Sex"] == "female") & (df["Fare"] >30)]

# # print(df2.shape[0])
# # print(df2.head())
# # print(df2["Fare"].mean())


# # missing_rows = df[df[["Embarked", "Age", "Cabin"]].isna().any(axis=1)]

# # print(missing_rows.head())

# # better= missing_rows.reset_index()
# # print(missing_rows.reset_index())

# # better.to_csv("missing_rows.csv", index = False)



# path = r"C:\Users\User\Downloads\flights-1m.csv"
# df = pd.read_csv(path, index_col = 0,)
# print(df.head())
# df.info()
# print(df.shape[0])
# df= pd.concat([df,df])
# df.info()
# print(df.shape)


# df1 =df.copy()
# print(df1.head())
# df1.info()
# print(df.columns)
# print(df)
# a = df["DISTANCE"].value_counts()
# print(a)
# print(df.describe())

# df["fulldelay"] = df["DEP_DELAY"] + df["ARR_DELAY"]
# print(df)
# a = df.sort_values(by="AIR_TIME")
# print(a)
# a= df.groupby("AIR_TIME")["DISTANCE"].max()
# print(a)



df = pd.DataFrame({"Name ": ["alo", "mahad", "rahad"], "Age" : [13,14, 15]})
df2 = pd.DataFrame({"City": ["kutaisi", "tbilisi"], "Address": ["here", "there"] })
print(df)
print(df2)
df3 = df.copy()
print(df3)
# df = pd.concat([df,df3])
# print(df)
# df = df.reset_index()
# print(df)
# print(df.head(2))
# print(df.tail(2))
# df.drop_duplicates(inplace=True, keep="last")
# print(df)

df4 = pd.concat([df,df2], axis=1)
print(df4)
df4 = df4.reset_index()
print(df4)
df4 = df["Age"].mean()
df4 = df[df["Age"] >13 ]
print(df4)
print(df4.shape)
df.info()


