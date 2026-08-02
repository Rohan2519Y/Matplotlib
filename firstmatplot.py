import matplotlib.pyplot as plt

X = ['A', 'B', 'C', 'D', 'E']
Y = [100, 200, 300, 400, 500]
# plt.bar(X, Y, color='red')
plt.bar(X, Y, color=['pink', 'green', 'blue', 'red', 'yellow'])
plt.xlabel("X", fontsize=20)
plt.ylabel("Y")
plt.title("X annnnnd Y")
# plt.pie( Y)
plt.show()