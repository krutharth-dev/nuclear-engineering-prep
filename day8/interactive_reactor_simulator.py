# Day 8: Interactive Reactor Temperature Simulation

import numpy as np
import matplotlib.pyplot as plt


def get_power_input():
    while True:
        try:
            power = float(input("Enter reactor power level (1-5): "))
            if 1 <= power <= 5:
                return power
            else:
                print("Please enter a value between 1 and 5.")
        except ValueError:
            print("Invalid input. Enter a number.")


def generate_time():
    return np.linspace(0, 20, 100)


def reactor_temperature(time, power):
    return 20 + (10 * power) * (1 - np.exp(-0.3 * time))


def plot_graph(time, temperature, power):
    plt.figure()

    # Main curve
    plt.plot(time, temperature, label=f"Reactor Temp (Power={power})", linewidth=2)

    # Dynamic steady-state line
    steady_state = 20 + 10 * power
    plt.axhline(y=steady_state, linestyle="--", color="red", label="Steady State")

    # Labels
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Interactive Reactor Temperature Simulation")

    # Styling
    plt.grid()
    plt.legend(loc="lower right")

    # Save image
    plt.savefig("day8_reactor_simulation.png", dpi=300)

    plt.show()


def main():
    power = get_power_input()
    time = generate_time()
    temperature = reactor_temperature(time, power)

    plot_graph(time, temperature, power)


if __name__ == "__main__":
    main()