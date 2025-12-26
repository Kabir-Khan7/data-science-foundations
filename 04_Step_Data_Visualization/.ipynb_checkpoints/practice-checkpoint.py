import matplotlib.pyplot as plt

plt.style.use("ggplot")

labels = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs = [18426, 8273, 7490, 6172]
colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF"]
explode = [0.1, 0, 0, 0]

plt.title("Career Runs of Indian Batsmen")
plt.pie(
    runs,
    labels=labels,
    colors=colors,
    wedgeprops={"edgecolor": "black", "linewidth": 1, "linestyle": "solid"},
    autopct="%1.1f%%",
    explode=explode,
    )
plt.show()