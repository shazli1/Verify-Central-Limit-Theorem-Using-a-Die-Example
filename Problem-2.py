# Simulation of Die Throwing
import random
import matplotlib.pyplot as plt
import statistics
import numpy as np

###################################################
# Function to simulate throwing a die for "n" times
###################################################
def generate_random(times):
    data = []
    for i in range(times):
        result = random.randint(1, 6)
        data.append(result)
    return data

# Simulate the outcome of throwing a die 1000 times
first_die = generate_random(1000)

# Plot the histogram (100 bins)
plt.figure()
plt.hist(first_die, bins=100)
plt.show()

#####################################################
# Simulate the outcome of throwing TWO dice 1000 times
die_a = generate_random(1000)
die_b = generate_random(1000)

# Calculate the average of the resulting values of the two dice in each time
avg1 = []
for i in range(1000):
    temp1 = (die_a[i] + die_b[i]) / 2
    avg1.append(temp1)

print("=========================== Throwing TWO Dice 1000 Times =========================")
print("Outcome of Throwing Two Dice 1000 Times:")
print(avg1)
print("Length of Data: " + str(len(avg1)))

# Plot the histogram of the average "avg1" (100 bins)
plt.figure()
plt.hist(avg1, bins=100)
plt.show()

# Calculate mean & variance of the average "avg1"
print('Mean of Throwing Two Dice = %f' %np.mean(np.array(avg1)))
print('Variance of Throwing Two Dice = %f' %np.var(np.array(avg1)))

#######################################################
# Simulate the outcome of throwing TEN dice 1000 times
die_0 = generate_random(1000)
die_1 = generate_random(1000)
die_2 = generate_random(1000)
die_3 = generate_random(1000)
die_4 = generate_random(1000)
die_5 = generate_random(1000)
die_6 = generate_random(1000)
die_7 = generate_random(1000)
die_8 = generate_random(1000)
die_9 = generate_random(1000)

# Calculate the average of the resulting values of the Ten dice in each time
avg2 = []
for j in range(1000):
    temp2 = (die_0[j] + die_1[j] + die_2[j] + die_3[j] + die_4[j] + die_5[j] + die_6[j] + die_7[j] + die_8[j] + die_9[j]) / 10
    avg2.append(temp2)

print("=========================== Throwing TEN Dice 1000 Times =========================")
print("Outcome of Throwing Ten Dice 1000 Times:")
print(avg2)
print("Length of Data:" + str(len(avg2)))

# Plot the histogram of the average "avg2" (100 bins)
plt.figure()
plt.hist(avg2, bins=100)
plt.show()

# Calculate mean & variance of the average "avg2"
print('Mean of Throwing Ten Dice = %f' %np.mean(np.array(avg2)))
print('Variance of Throwing Ten Dice = %f' %np.var(np.array(avg2)))

# Copy means & variances into output text file
results = []
labels = np.array(['Mean of 2 Dice', 'Variance of 2 Dice', 'Mean of 10 Dice', 'Variance of 10 Dice'])
results.append(np.mean(np.array(avg1)))
results.append(np.var(np.array(avg1)))
results.append(np.mean(np.array(avg2)))
results.append(np.var(np.array(avg2)))

DAT =  np.column_stack((labels, np.array(results)))

np.savetxt(r'C:\Users\chtv2985\Desktop\Assig-2\Codes\Output-Prob2.txt', DAT, delimiter=" = ", fmt="%s")