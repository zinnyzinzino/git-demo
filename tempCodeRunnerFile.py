total = df.shape[0]
survived = df[df["Survived"] == 1].shape[0]
surviveddf = df["Survived"] == 1
died = total - survived


figs, axes = plt.subplots(1, 2, figsize = (12,5))
axes[0].pie([survived, died,], labels = ["Survived", "Not survived"], autopct = "%1.1f%%", startangle = 90, shadow = True, 
explode = (0.05, 0))
axes[0].set_title("lucky vs unlucky folks")



pclass1 = df[(surviveddf) & (df["Pclass"] == 1)].shape[0]
pclass2 = df[(surviveddf) & (df["Pclass"] == 2)].shape[0]
pclass3 = df[(surviveddf) & (df["Pclass"] == 3)].shape[0]
values = [pclass1, pclass2, pclass3]
print(values)

survivedbypclass=df[df["Survived"] == 1]["Pclass"].value_counts().sort_index()
print(survivedbypclass)


bars = axes[1].bar(survivedbypclass.index.astype(str), survivedbypclass.values, color = ["red","blue","black"], label = ["1st", "2nd", "3rd"])
for bar in bars:
    height = bar.get_height()
    x = bar.get_x()+bar.get_width()/2
    axes[1].text(x, height, str(int(height)), ha = "center", va = "bottom")
axes[1].set_title("survivors by class")
axes[1].set_xlabel("pclass")
axes[1].set_ylabel("survivors")
axes[1].set_ylim(0, max(survivedbypclass.values) * 1.15)

# plt.grid(True, axis="y")
axes[1].legend()
plt.tight_layout()
plt.show()