# Day 11–15: Integrated Thermal Reactor Simulator (Final Version)

import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# TIME SETUP
# -----------------------------
def generate_time():
    return np.linspace(0, 50, 1000)


# -----------------------------
# HEATING MODEL (Exponential)
# -----------------------------
def heating_model(time, power):
    T0 = 20  # ambient temperature
    Tmax = 20 + (60 * power)  # equilibrium temperature depends on power
    k = 0.1 * power  # response speed increases with power

    # Exponential rise toward equilibrium
    return T0 + (Tmax - T0) * (1 - np.exp(-k * time))


# -----------------------------
# SHUTDOWN + COOLING
# -----------------------------
def apply_shutdown_and_cooling(time, temperature, safety_limit):
    modified_temp = np.copy(temperature)

    if np.max(temperature) >= safety_limit:
        shutdown_index = np.where(temperature >= safety_limit)[0][0]
        shutdown_time = time[shutdown_index]

        # Clamp shutdown start exactly at safety limit
        shutdown_temp = safety_limit

        cooling_rate = 0.15
        cooling_time = time[shutdown_index:] - shutdown_time

        # Cooling toward ambient (physically realistic)
        cooling_temp = 20 + (shutdown_temp - 20) * np.exp(-cooling_rate * cooling_time)

        modified_temp[shutdown_index:] = cooling_temp

        return modified_temp, shutdown_time

    return modified_temp, None


# -----------------------------
# CLASSIFICATION
# -----------------------------
def classify_system(raw_temp, shutdown_time, warning_limit):
    if shutdown_time is not None:
        return "Shutdown Activated"
    elif np.max(raw_temp) >= warning_limit:
        return "Warning"
    else:
        return "Safe"


# -----------------------------
# MAIN SIMULATION
# -----------------------------
def run_simulation(power_levels, warning_limit, safety_limit):
    time = generate_time()

    plt.figure()
    first_shutdown = True

    for power in power_levels:

        # Step 1: Heating
        temperature = heating_model(time, power)

        # Step 2: Shutdown + Cooling
        modified_temp, shutdown_time = apply_shutdown_and_cooling(
            time, temperature, safety_limit
        )

        # Step 3: Classification
        status = classify_system(temperature, shutdown_time, warning_limit)

        # Peak comparison (engineering insight)
        raw_peak = np.max(temperature)
        controlled_peak = np.max(modified_temp)

        # Plot curve
        plt.plot(time, modified_temp, linewidth=2,
                 label=f"Power={power} ({status})")

        # Shutdown marker
        if shutdown_time is not None:
            if first_shutdown:
                plt.axvline(x=shutdown_time, linestyle=":", alpha=0.7,
                            label="Shutdown Time")
                first_shutdown = False
            else:
                plt.axvline(x=shutdown_time, linestyle=":", alpha=0.7)

            print(
                f"Power {power}: {status}, "
                f"Controlled Peak = {controlled_peak:.2f}°C, "
                f"Raw Peak = {raw_peak:.2f}°C, "
                f"Shutdown at {shutdown_time:.2f}s"
            )
        else:
            print(
                f"Power {power}: {status}, "
                f"Controlled Peak = {controlled_peak:.2f}°C, "
                f"Raw Peak = {raw_peak:.2f}°C"
            )

    # Safety zones
    plt.axhline(y=warning_limit, linestyle="--", color="orange",
                label=f"Warning Zone ({warning_limit}°C)")
    plt.axhline(y=safety_limit, linestyle="--", color="red",
                label=f"Safety Limit ({safety_limit}°C)")

    # Labels and styling
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Integrated Thermal Reactor Simulator (Days 11–15)")

    plt.grid()
    plt.legend(loc="lower right")

    # Final polish
    plt.tight_layout()
    plt.savefig("day11_15_simulation.png", dpi=300)

    plt.show()


# -----------------------------
# ENTRY POINT
# -----------------------------
def main():
    warning_limit = 80
    safety_limit = 100

    # Clear behavioral separation
    power_levels = [1, 2, 3]

    run_simulation(power_levels, warning_limit, safety_limit)


if __name__ == "__main__":
    main()