from pylab import mpl
import matplotlib.pyplot as plt
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14,)
ax.set_ylabel("值的平方", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()