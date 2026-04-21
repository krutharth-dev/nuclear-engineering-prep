# Day 7: Reactor Temperature Model with Visualization + Export

import numpy as np
import matplotlib.pyplot as plt


def generate_time():
    return np.linspace(0, 20, 100)


def reactor_temperature(time):
    # Reactor-like exponential rise
    return 20 + 40 * (1 - np.exp(-0.3 * time))


def plot_graph(time, temperature):
    plt.figure()

    # Main curve
    plt.plot(time, temperature, label="Reactor Temperature", linewidth=2)

    # Steady-state line
    plt.axhline(y=60, linestyle="--", color="red", label="Steady State")

    # 95% response time line
    plt.axvline(x=10, linestyle=":", color="green", label="95% Response Time")

    # Labels and title
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.title("Reactor Temperature Rise and Transient Response")

    # Styling
    plt.grid()
    plt.legend(loc="lower right")

    # Save graph (same folder)
    plt.savefig("reactor_temperature_plot.png", dpi=300)

    # Show graph
    plt.show()


def main():
    time = generate_time()
    temperature = reactor_temperature(time)

    plot_graph(time, temperature)


if __name__ == "__main__":
    main()