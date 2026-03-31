import numpy as np 
import matplotlib.pyplot as plt

# x = np.linspace(0, 2 * np.pi, 100)

# fig, axes = plt.subplots(1, 3, sharex=True,figsize = (15, 4))


# axes[0].plot(x, np.sin(x), "bo", label = "sinx")
# axes[0].set_title("sinx")
# axes[0].grid(True)



# axes[1].plot(x, np.tan(x), "r--", label = "tanx")
# axes[1].set_title("tanx")
# axes[1].set_ylim(-10, 10)
# axes[1].grid(True)

# axes[2].plot(x, np.cos(x), label = "cosx")
# axes[2].set_title("cosx")
# axes[2].grid(True)

# plt.tight_layout()
# plt.show()



# products = ["a", "b", 'c', 'd', 'e']

# sales = [100, 160 ,20 ,2500 ,150]
# profit = [10, 30, -50, 500, 20]

# x = np.arange(len(products))
# width = 0.35


# plt.bar(x-width/2, sales,  width, label = "sales")
# plt.bar(x+width/2, profit, width,  label = "profit" )


# plt.xticks(x, products)
# plt.ylim(-500, 2500)
# plt.xlabel("products")
# plt.ylabel("values")
# plt.title("sales v profit")
# plt.legend()
# plt.grid(True, axis = "y")

# plt.show()


items = ["uno", "Dos", "tres", "quatro", "five", "six", "seven", "eight"]

values = [10, 20, 30, 40, 50, 60, 70, 80]


order = np.argsort(values[::-1])
sorteditems = [items[i] for i in order]
sorted_values = [values[i] for i in order]
plt.barh(sorteditems, sorted_values)

plt.xlabel("value")
plt.title("itmms sorted by value(descneding)")
for i,v in enumerate(sorted_values):
    plt.text(v+1, i, str(v), va = "center")


plt.show(block=True)


# categories = ["A", "B", "C", "D"]
# part1 = [10, 15, 20, 12]
# part2 = [5, 8, 6, 9]
# part3 = [2, 3, 4, 5]

# x = np.arange(len(categories))

# plt.bar(x, part1, label="Part 1")
# plt.bar(x, part2, bottom=part1, label="Part 2")
# plt.bar(x, part3, bottom=np.array(part1)+np.array(part2), label="Part 3")

# plt.xticks(x, categories)
# plt.xlabel("Categories")
# plt.ylabel("Value")
# plt.title("Stacked Bar Chart")
# plt.legend()
# plt.grid(True, axis="y")

# plt.show()

# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [5, 3, 6, 2, 7]
# categories = ['A', 'B', 'C', 'D']
# values = [10, 15, 7, 12]
# scores = [55, 67, 70, 72, 78, 85, 90, 95, 60, 73]

# fig, axes = plt.subplots(2, 2, figsize = (10,8))
# axes[0,0].plot(x,y1,linestyle="--",marker="o",color="black",linewidth=2)
# axes[0,0].set_title("line plot1")


# axes[0,1].plot(x,y2,linestyle="-",marker="s", color="blue")
# axes[0,1].annotate("peak", xy=(3,6), xytext=(3.2,6.5),arrowprops=dict(arrowstyle="->"))
# axes[0, 1].set_title("Line Plot 2")


# axes[1, 0].bar(categories, values, color='green')
# axes[1, 0].set_title("Bar Chart")


# axes[1, 1].hist(scores, bins=5, color='purple', edgecolor='black')
# axes[1, 1].set_title("Score Distribution")

# plt.tight_layout()
# plt.show()


# labels = ["maths", "physics", "chem", "Biology"]
# sizes = [30, 25, 20, 25]


# plt.pie(sizes, labels=labels, autopct="%1.1f%%",startangle=90,explode=[0.1,0,0,0])
# plt.title("Subject distribution")
# plt.axis("equal")
# plt.show()


# x = [0, 1, 2, 3, 4, 5]
# y = [0, 1, 4, 9, 16, 25]


# plt.figure()

# plt.plot(
#     x, y,
#     linestyle=':',
#     color='green',
#     marker='^',
#     markerfacecolor='yellow',
#     markeredgecolor='black'
# )

# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.grid()

# plt.annotate("x=4", xy=(4,16), xytext=(4.2,18),
#              arrowprops=dict(arrowstyle="->"))

# plt.show()


# x=[1,2,3,4,5]
# y1=[2,4,6,8,10]
# y2=[5,3,6,2,7]
# categories=["A", "B", "C", "D"]
# values=[10,15,7,12]
# scores = [55, 67, 70, 72, 78, 85, 90, 95, 60, 73]


# fig, axes = plt.subplots(2,2,figsize=(10,8))

# axes[0,0].plot(x,y1,linestyle = "--", color = "red", marker = "o", markerfacecolor="black", linewidth=2 )
# axes[0,0].set_title("first plot")

# axes[0,1].plot(x,y2, linestyle = "-", color ="blue", marker = "s",)
# axes[0,1].annotate("peak", xy=(3,6), xytext=(3.1,6.1))
# axes[0,1].set_title("second")

# axes[1,0].bar(categories, values, color="green", edgecolor= "Black")
# axes[1,0].set_title("bar chart")

# axes[1,1].hist(scores, bins=5, color = "purple", edgecolor = "Black")
# axes[1,1].set_title("score")






# labels = ['Math', 'Physics', 'Chemistry', 'Biology']
# sizes = [30, 25, 20, 25]

# plt.figure()

# plt.pie(
#     sizes,
#     labels=labels,
#     autopct='%1.1f%%',
#     startangle=90,
#     explode=[0.1, 0, 0, 0])
# plt.title("distribution")
# plt.axis('equal')
# plt.show()

# x = [0, 1, 2, 3, 4, 5]
# y = [0, 1, 4, 9, 16, 25]

# plt.figure()

# plt.plot(x,y, linestyle = "dotted", marker = "^", markerfacecolor= "yellow", markeredgecolor="black" )

# plt.xlabel("x values")
# plt.ylabel("y values")
# plt.grid(True)
# plt.annotate("x=4", xy=(4,16))

# plt.show()



# x = [1, 2, 3, 4, 5]
# y1 = [2, 3, 5, 7, 11]
# y2 = [1, 4, 6, 8, 9]


# plt.plot(x,y1,linestyle= "-", marker = "o", color = "red", label = "y1" )

# plt.plot(x, y2, linestyle = "--", marker="s", label = "y2" ,color = "blue")
# plt.title("two at the same time yessirski")
# plt.legend()
# plt.grid(True)

# plt.show()



# data1 = [12, 15, 14, 16, 18, 20, 22, 19]
# data2 = [10, 13, 15, 17, 19, 21, 23, 25]



# plt.hist(data1, bins=5, alpha=0.6, label='Data 1')
# plt.hist(data2, bins=5, alpha=0.6, label='Data 2')

# plt.title("woopwoop")
# plt.legend()

# plt.show()




# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [25, 16, 9, 4, 1]

# max_x= max(x)
# max_y1=y1[x.index(max_x)]
# fig, axs = plt.subplots(2, 1, sharex=True)

# axs[0].plot(x, y1, color='blue')
# axs[0].set_title("y1 Plot")
# axs[0].annotate("peak", xy=(max_x,max_y1), xytext =(max_x,max_y1 + 10), arrowprops=dict(arrowstyle="->"))

# axs[1].plot(x, y2, color='red')
# axs[1].set_title("y2 Plot")

# plt.tight_layout()
# plt.show()


# x = [5, 7, 8, 10, 12, 15]
# y = [50, 55, 60, 65, 70, 80]
# sizes = [50, 80, 100, 120, 150, 200]



# plt.figure()

# plt.scatter(
#     x, y,
#     s=sizes,
#     color='red',
#     edgecolors='black',
#     alpha=0.7
# )

# plt.title("Scatter Plot")
# plt.xlabel("X values")
# plt.ylabel("Y values")

# plt.show()



# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# sales = [120, 150, 170, 160, 180]
# expenses = [100, 110, 130, 120, 140]
# market_share = [40, 30, 20, 10]
# regions = ['North', 'South', 'East', 'West']
# temps = [22, 24, 19, 23, 25, 26, 21, 20]



# figs, axes = plt.subplots(2,2, figsize=(10,8))
# max_sales=max(sales)
# max_index=sales.index(max_sales)
# prime_month=months[max_index]
# axes[0,0].plot(months, sales, linestyle="-", color = "blue", marker = "o", markerfacecolor="red", label = "hi")
# axes[0,0].annotate("Peak", xy=(prime_month, max_sales), xytext=(prime_month, max_sales + 10) , arrowprops = dict(arrowstyle="->"))
# axes[0,0].set_title("monthly sales")

# max_expenses=max(expenses)
# peak_index=expenses.index(max_expenses)
# peak_month=months[peak_index]
# axes[0,1].plot(months, expenses, linestyle="--", color="red", marker = "s", markerfacecolor="blue", label = "hello")
# axes[0,1].annotate("Most expenses", xy=(peak_month, max_expenses), xytext=(peak_month, max_expenses + 10), arrowprops = dict(arrowstyle="->"))
# axes[0,1].set_title("monthly expenses")


# bars =axes[1,0].bar(regions, market_share, color="green", edgecolor="white", label = "yipyiphooray")
# for bar in bars:
#     height = bar.get_height()
#     axes[1,0].text(bar.get_x()+bar.get_width()/2, height, height, ha="center", va="bottom")
# axes[1,0].set_title("ioin even know")


# counts, bins, patches = axes[1,1].hist(temps, bins=4, color ="orange", edgecolor="black", width = 0.5, label =" yippie woohoo")

# for count, patch in zip(counts, patches):
#     x= patch.get_x() + patch.get_width()/2
#     y=patch.get_height()
#     axes[1,1].text(x,y,int(count), ha = "center", va="bottom")
# axes[1,1].set_title("temp distribution")
# axes[1,1].grid(True)
# axes[1,1].set_ylim(0, 4.00 )


# axes[0,0].legend()
# axes[0,1].legend()
# figs.legend()

# plt.tight_layout()
# plt.show()



# x = [1, 2, 3, 4, 5]
# y = [3, 7, 2, 9, 4]


# max_x=max(x)
# peak_index = x.index(max(x))
# max_y=y[peak_index]
# plt.plot(x,y, linestyle = "-", color = "purple", marker = "d")
# plt.annotate("Max", xy=(max_x, max_y), xytext=(max_x, max_y + 5), arrowprops=dict(arrowstyle="->"))

# plt.title("xy")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()



# years = ['2021', '2022', '2023']
# product_A = [30, 40, 50]
# product_B = [20, 25, 30]

# x = np.arange(len(years)) * 1.5

# bars1 = plt.bar(x, product_A, color="blue", label="A", width=0.5)
# for bar in bars1:
#     height = bar.get_height()
#     plt.text(
#         bar.get_x() + bar.get_width(),
#         height / 2,
#         str(height),
#         ha="left",
#         va="center"
#     )

# bars2 = plt.bar(x, product_B, bottom=product_A, color="red", label="B", width=0.5)
# for bar, bottom in zip(bars2, product_A):
#     height = bar.get_height()
#     plt.text(
#         bar.get_x() + bar.get_width(),
#         bottom + height / 2,
#         str(height),
#         ha="left",
#         va="center"
#     )

# plt.xticks(x, years)
# plt.legend()
# plt.tight_layout()
# plt.show()


# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [25, 16, 9, 4, 1]

# figs, axes = plt.subplots(2,1, figsize=(10,8), sharex=True)
# axes[0].plot(x,y1,color = "red", marker = "d")
# axes[0].set_title("hi")
# max_x=max(x)
# max_index=x.index(max_x)
# maxy1= y1[max_index]
# axes[0].annotate("hi", xy=[max_x,maxy1], arrowprops=dict(arrowstyle = "->"))

# axes[1].plot(x,y1,color="blue", marker="o")
# axes[1].set_title("hi")

# plt.tight_layout()
# plt.show()




# x = [5, 7, 8, 10, 12, 15]
# y = [50, 55, 60, 65, 70, 80]
# sizes = [50, 80, 100, 120, 150, 200]


# plt.scatter(x,y, sizes,label = 'idk', marker="*", color="red",edgecolors = "black", alpha = 1)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("scatter")
# plt.legend()
# plt.show()




# x = np.linspace(-5, 5, 400)


# y1 = x**2
# y2 = x**3


# plt.plot(x, y1, label="y = x^2", color="blue")
# plt.plot(x, y2, label="y = x^2", color="red")

# plt.axhline(0, color="black",)
# plt.axvline(0, color="black", )


# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("yippiehoohoo")


# plt.legend()
# plt.grid(True)

# plt.show()



# import matplotlib.pyplot as plt

# # Example data
# labels = ["A", "B", "C", "D"]
# sizes  = [30, 25, 20, 25]

# fig, ax = plt.subplots(figsize=(6, 6))

# # 1) Normal pie chart
# ax.pie(
#     sizes,
#     labels=labels,
#     autopct="%1.1f%%",
#     startangle=90
# )

# # 2) White circle in the middle (this makes it a donut)
# center_circle = plt.Circle((0, 0), 0.65, fc="white")  # radius controls hole size
# ax.add_artist(center_circle)

# # 3) Keep it perfectly circular
# ax.axis("equal")

# ax.set_title("Donut Chart")
# plt.show()





# x = np.linspace(-5,5,100)


# y1 = x**2
# y2=x**3



# plt.plot(x,y1, color = "blue", marker = "o")
# plt.plot(x,y2,  color = "red", marker = "d")
# plt.axhline(0,linewidth=1)
# plt.axvline(0, linewidth=1)
# plt.grid(True)
# plt.tight_layout()
# plt.show()



figs, axes = plt.subplots(2,2, figsize=[10,8])
x=np.linspace(0,2*np.pi, 100)
sinx = np.sin(x)
cosx=np.cos(x)
axes[0,0].plot(x,)
