import random
import matplotlib.pyplot as plt
import seaborn as sns

s = random.randrange(6)
k= s * 3
lim = k*10000000

k_values = []
true_probabilities = []
false_probabilities = []

while k < lim:
    l = [0, 7, 8, 9]
    nl = []
    for i in range(k):
        n = random.randrange(10)
        while n in l:
            n = random.randrange(10)
        nl.append(n)

    i = 0
    nnl = []

    while i < k - 2:
        s = nl[i] + nl[i + 1] + nl[i + 2]
        nnl.append(s >= 10)
        i += 3

    n1 = nnl.count(True)
    n2 = nnl.count(False)

    true_prob = n1 / (n1 + n2)
    false_prob = n2 / (n1 + n2)

    k_values.append(k)
    true_probabilities.append(true_prob)
    false_probabilities.append(false_prob)

    k *= 10

plt.figure(figsize=(12, 6))
sns.lineplot(x=k_values, y=true_probabilities, marker='o', label='win Probability')
sns.lineplot(x=k_values, y=false_probabilities, marker='o', label='lose Probability')
plt.xscale('log')
plt.xlabel('k values')
plt.ylabel('Probability')
plt.title('Probability of True and False Outcomes as k Increases')
plt.legend()
plt.grid(True)
plt.show()
