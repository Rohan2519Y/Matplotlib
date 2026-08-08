import matplotlib.pyplot as plt
import numpy as np

X = ['A', 'B', 'C', 'D', 'E']
Y = [100, 200, 300, 400, 500]
Z = [200, 300, 400, 500, 600]
# plt.bar(X, Y, color='red')
# plt.bar(X, Y, color=['pink', 'green', 'blue', 'red', 'yellow'], width=0.5, align='center', edgecolor='black', linewidth=2, linestyle="-.", alpha=0.8)

# plt.bar(X, Z, color='green', label='Z')
# plt.bar(X, Y, color='red', label='Y')

# plt.xlabel("X", fontsize=20)
# plt.ylabel("Y")
# plt.title("X annnnnd Y")
# plt.pie( Y)

# width = 0.3
# p = np.arange(len(X))
# p1 = [i + width for i in p]

# plt.bar(p, Z, width=width, color='green', label='Z')
# plt.bar(p1, Y, width=width, color='red', label='Y')
# plt.xticks(p + width/2.0, X)
# plt.legend()

# plt.scatter(X, Y, c=[10, 20, 30, 40, 50], s=50, marker='*', cmap='viridis')

# plt.pie(Y, labels=X, autopct='%.2f%%', explode=[0.4, 0.4, 0, 0, 0], shadow=False, radius=1, startangle=30, wedgeprops={"edgecolor":'black'})
# plt.pie(Y, labels=X, autopct='%.2f%%',shadow=False, radius=1, startangle=30, wedgeprops={"edgecolor":'black'})
# plt.pie([1], colors = 'w', radius=0.7)
# plt.legend(loc = 'upper right', bbox_to_anchor = (0.7, 0, 0.5, 1))


# plt.stem(X, Y, linefmt=":", markerfmt="ro", bottom=1, basefmt='g', label='Data', orientation='horizontal')
# plt.legend()


# plt.boxplot(Y, notch=False, vert=True, widths=0.2, patch_artist=True, whis=2, showmeans=True, boxprops=dict(color='r'), capprops=dict(color='r'), whiskerprops=dict(color='r'))

# plt.stackplot(X, Y, Z)
# plt.grid()


# plt.text(150, 0.5, 'X', fontsize=15)
# plt.annotate('python', xy=(100, 200))
# plt.plot(Y)
# plt.plot(Z)


plt.plot(Z, Y)
# plt.xticks(Z)
# plt.xticks(Y)
# plt.xlim(0, 200)
plt.show()