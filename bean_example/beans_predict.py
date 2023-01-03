import beans_dateset
from matplotlib import pyplot as plt

xs, ys = beans_dateset.get_beans(200)
print(xs)
print(ys)

# image config
plt.title("Bean Size-Toxicity Function", fontsize=10)
plt.xlabel("Bean Size")
plt.ylabel("Bean Toxicity")

# print scatter
plt.scatter(xs, ys)
# y = w * x
w = 0.5
alpha = 0.05  # learning rate
for j in range(500):
    for i in range(200):
        y_pre = w * xs[i]
        e = ys[i] - y_pre
        w = w + e * xs[i] * alpha
        print("No.", j, "-", i, "w: ", w, "e: ", e, "y_pre: ", y_pre)
y_pre = w * xs
print("final w is", w)
# print fitted curve
plt.plot(xs, y_pre)
plt.show()
