import numpy as np
import matplotlib.pyplot as plt

# Time axis
time = np.linspace(0, 20, 100)

# Reactor-like temperature model
temperature = 20 + 40 * (1 - np.exp(-0.3 * time))

# Plot main curve
plt.plot(time, temperature, label="Reactor Temperature", linewidth=2)

# Steady-state reference
plt.axhline(y=60, linestyle="--", color="red", label="Steady State")

# 95% response time marker
plt.axvline(x=10, linestyle=":", color="green", label="95% Response Time")

# Labels and styling
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Reactor Temperature Rise and Transient Response")

plt.grid()
plt.legend(loc="lower right")  # improved legend placement

plt.show()