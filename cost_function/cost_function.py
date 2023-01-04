import beans_dateset
import matplotlib.pyplot as plt
import numpy as np

xs, ys = beans_dateset.get_beans(120)

# image config
plt.title("Bean Size-Toxicity Function", fontsize=10)
plt.xlabel("Bean Size")
plt.ylabel("Bean Toxicity")

# print scatter
plt.scatter(xs, ys)
plt.show()

ws = np.arange(0, 3, 0.1)
# 针对每个w值平方误差数组
es = []
for w in ws:
    y_pre = w * xs
    e = (1 / 120) * np.sum((ys - y_pre) ** 2)
    es.append(e)
    print("w:" + str(w) + " e:" + str(e))

# image config
plt.title("Cost function", fontsize=10)
plt.xlabel("w")
plt.ylabel("e")

# print scatter
plt.plot(ws, es)
plt.show()

# w_min公式 = sum(x*y) / sum(x*x)
w_min = np.sum(xs*ys)/np.sum(xs*xs)

y_pre = w_min * xs
plt.title("Bean Size-Toxicity Function", fontsize=10)
plt.xlabel("Bean Size")
plt.ylabel("Bean Toxicity")

# 带入w_min重新计算 print scatter
plt.scatter(xs, ys)

plt.plot(xs, y_pre)

plt.show()
