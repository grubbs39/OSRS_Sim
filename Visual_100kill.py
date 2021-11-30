import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

with open('Data_100kill.json') as project_file:    
    data = json.load(project_file)  

df = pd.json_normalize(data)

#Zulrah

df = pd.DataFrame(data["Zulrah"])

print(df)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.bar(df["Item"], df["Quantity"], color = ["b", "g"] )

plt.ylabel("Quantity of drops")
plt.xlabel("Drops")
plt.title("Graph of Drops and How They Statistically Compare After 100 Kills")

plt.show()

#TzTok-Jad

df = pd.DataFrame(data["TzTok-Jad"])

print(df)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.bar(df["Item"], df["Quantity"], color = ["b", "g"] )

plt.ylabel("Quantity of drops")
plt.xlabel("Drops")
plt.title("Graph of Drops and How They Statistically Compare After 100 Kills")

plt.show()

#TzKal-Zuk

df = pd.DataFrame(data["TzKal-Zuk"])

print(df)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.bar(df["Item"], df["Quantity"], color = ["b", "g"] )

plt.ylabel("Quantity of drops")
plt.xlabel("Drops")
plt.title("Graph of Drops and How They Statistically Compare After 100 Kills")

plt.show()