import numpy as np

n = 20
k = 5

# 1. Generate data
data = []
for i in range(n):
    amt = np.random.randint(100, 10001)
    time = np.random.randint(1, 121)
    fail = np.random.randint(0, 11)
    data.append([amt, time, fail])
data = np.array(data)

# 2. Get min and max for normalization
mn = data.min(axis=0)
mx = data.max(axis=0)

# 3. Loop through data and append to risk
risk = []
for i in range(len(data)):
    # Normalize each feature for the current user (i)
    norm_amt = (data[i][0] - mn[0]) / (mx[0] - mn[0])
    norm_time = (data[i][1] - mn[1]) / (mx[1] - mn[1])
    norm_fail = (data[i][2] - mn[2]) / (mx[2] - mn[2])
    
    # Formula
    score = norm_amt * 0.6 + norm_time * 0.3 + norm_fail * 0.1
    risk.append(score)

# Convert risk to numpy array just to use argsort easily
risk = np.array(risk)
top = np.argsort(risk)[::-1][:k]

print("Generated Data")
print(data)

print("\nTop Risky Users")
for i in range(k):
    idx = top[i]
    print(i + 1, "User", idx, data[idx], "Score =", round(risk[idx], 4))