import pandas as pd
import matplotlib.pyplot as plt

# path = r"C:\Users\User\Downloads\titanic.csv"
# df = pd.read_csv(path, index_col=0, na_values = "\\N")

# df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# total = df.shape[0]
# survived = df[df["Survived"] == 1].shape[0]
# surviveddf = df["Survived"] == 1
# died = total - survived


# figs, axes = plt.subplots(1, 2, figsize = (12,5))
# axes[0].pie([survived, died,], labels = ["Survived", "Not survived"], autopct = "%1.1f%%", startangle = 90, shadow = True, 
# explode = (0.05, 0))
# axes[0].set_title("lucky vs unlucky folks")



# pclass1 = df[(surviveddf) & (df["Pclass"] == 1)].shape[0]
# pclass2 = df[(surviveddf) & (df["Pclass"] == 2)].shape[0]
# pclass3 = df[(surviveddf) & (df["Pclass"] == 3)].shape[0]
# values = [pclass1, pclass2, pclass3]
# print(values)

# survivedbypclass=df[df["Survived"] == 1]["Pclass"].value_counts().sort_index()
# print(survivedbypclass)


# bars = axes[1].bar(survivedbypclass.index.astype(str), survivedbypclass.values, color = ["red","blue","black"], label = ["1st", "2nd", "3rd"])
# for bar in bars:
#     height = bar.get_height()
#     x = bar.get_x()+bar.get_width()/2
#     axes[1].text(x, height, str(int(height)), ha = "center", va = "bottom")
# axes[1].set_title("survivors by class")
# axes[1].set_xlabel("pclass")
# axes[1].set_ylabel("survivors")
# axes[1].set_ylim(0, max(survivedbypclass.values) * 1.15)

# # plt.grid(True, axis="y")
# axes[1].legend()
# plt.tight_layout()
# plt.show()


# bins =[0, 10, 20, 30, 40, 50, 60, 70, 80]
# labels = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80"]
# df["Agebin"] = pd.cut(df["Age"], bins=bins, labels=labels,include_lowest=True,right=False)

# surv_means = df[df["Survived"]==1].groupby("Agebin")["Fare"].mean()
# dead_means=df[df["Survived"]==0].groupby("Agebin")["Fare"].mean()

# surv_means =surv_means.reindex(labels)
# dead_means = dead_means.reindex(labels)
# print("survived", surv_means)
# print("died", dead_means)

# plt.figure(figsize=[10,5])

# surv_no_nan = surv_means.dropna()
# max_survivor = surv_no_nan.max()
# survivorindex = surv_means.dropna().idxmax()
# correlatedagebin= max_survivor

# x_pos = labels.index(survivorindex)

# plt.plot(labels, surv_means.values, linestyle = "--", marker = "o", color = "red", markerfacecolor = "blue", label = "survivors")
# plt.plot(labels, dead_means.values, linestyle = "-", marker = "s", color = "pink", markerfacecolor = "purple", label = "dead")
# plt.xlabel("age shualedi")
# plt.ylabel("fare means")
# plt.title("fuck this question")
# plt.legend()
# plt.annotate("highest mean", xy= (x_pos, correlatedagebin), xytext=(x_pos, correlatedagebin + 10), 
# arrowprops =dict(arrowstyle = "->")) 

# plt.show()


# surv_age = df.loc[df["Survived"]==1, "Age"].dropna()
# died_age = df.loc[df["Survived"]==0, "Age"].dropna()

# print(surv_age)

# bins = 20

# plt.hist(surv_age, bins = bins, alpha = 0.6, label ="Survived")
# plt.hist(died_age, bins = bins, alpha = 0.6, label = "Died")

# mean_surv = surv_age.mean()
# mean_dead = died_age.mean()

# plt.axhline(mean_surv, linestyle = "--", label = f"Survived mean: {mean_surv:.2f}")
# plt.axvline(mean_dead, linestyle = "--", label = f"Died mean: {mean_dead:.2f}")
# y_top = plt.ylim()[1]
# plt.text(mean_surv, y_top * 0.95, f"{mean_surv:.2f}", ha="center", va="top")
# plt.text(mean_dead, y_top * 0.90, f"{mean_dead:.2f}", ha="center", va="top")

# plt.title("dead age vs alive age")
# plt.legend()

# plt.show()




# survivors = df[df["Survived"]==1]

# dead = df[df["Survived"]==0]



# plt.scatter(survivors["Age"], survivors["Fare"], marker="^", alpha = 0.6, color = "Orange",label = "Survived")
# plt.scatter(dead["Age"], dead["Fare"], marker = "x", alpha= 0.8, label = "Died", color = "Blue" )

# max_row=df.dropna(subset = ["Age"]).loc[df["Fare"].idxmax()]
# max_age = max_row["Age"]
# max_fare = max_row["Fare"]

# plt.xlabel("age")
# plt.ylabel("fare")
# plt.title("yip")
# plt.legend()

# plt.annotate(
#     f"Max Fare: {max_fare:.0f}",
#     xy=(max_age, max_fare),
#     xytext=(max_age + 5, max_fare),
#     arrowprops=dict(arrowstyle="->"))
# plt.show()  




# df.info()
# print(df.shape)


# counts = df.groupby(["Embarked", "Survived"]).size().unstack()
# counts = counts.reindex(["C", "Q", "S"])

# dead = counts[0]
# alive = counts[1]


# plt.bar(counts.index, dead, label = "dead")
# plt.bar(counts.index, alive, bottom = dead, label = "alive")


# total = dead + alive

# for x, total in zip(counts.index, total):
#     plt.text(x, total, str(total), ha = "center", va = "bottom")
# plt.title("release")
# plt.xlabel("Embarked")
# plt.ylabel("Count")
# plt.legend()


# plt.tight_layout()
# plt.show()


