import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stars_with_gravity.csv")
Mass = df["Mass"].to_list()
Radius = df["Radius"].to_list()
Gravity = df["Gravity"].to_list()
Distance = df["Distance"].to_list()

Mass.sort()
Radius.sort()
Gravity.sort()
Distance.sort()

plt.plot(Radius,Mass)
plt.title("Radius & Mass of the star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.plot(Mass,Gravity)
plt.title("Mass & Gravity of the star")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()


plt.scatter(Radius,Mass)
plt.title("Radius & Mass of the star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()

plt.scatter(Mass,Gravity)
plt.title("Mass & Gravity of the star")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()