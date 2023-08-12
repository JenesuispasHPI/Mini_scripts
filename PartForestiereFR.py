
import matplotlib.pyplot as plt

# Années sur l'axe des x
annees = range(1920, 2021)

# Surface forestière en hectares sur l'axe des y
surface_forestiere = [12000000, 11000000, 10500000, 10000000, 9500000, 9000000, 8500000, 8000000,
                       7500000, 7000000, 6500000, 6000000, 5500000, 5000000, 4500000, 4000000,
                       3500000, 3000000, 2500000, 2000000, 1500000, 1000000, 500000]

plt.figure(figsize=(10, 6))
plt.plot(annees, surface_forestiere, marker='o')
plt.title("Diminution de la Forêt en France sur 100 ans")
plt.xlabel("Années")
plt.ylabel("Surface Forestière (hectares)")
plt.grid(True)
plt.show()
