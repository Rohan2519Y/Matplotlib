import matplotlib.pyplot as plt

X = ['A', 'B', 'C', 'D', 'E']
Y = [100, 200, 300, 400, 500]
Z = [200, 300, 400, 500, 600]
# plt.bar(X, Y, color='red')
# plt.bar(X, Y, color=['pink', 'green', 'blue', 'red', 'yellow'], width=0.5, align='center', edgecolor='black', linewidth=2, linestyle="-.", alpha=0.8)

plt.bar(X, Z, color='green')
plt.bar(X, Y, color='red')

plt.xlabel("X", fontsize=20)
plt.ylabel("Y")
plt.title("X annnnnd Y")
# plt.pie( Y)
plt.show()