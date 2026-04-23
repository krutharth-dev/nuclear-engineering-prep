# Mini Reactor Temperature Simulator (Days 8–10 Integrated)

import numpy as np
import matplotlib.pyplot as plt


def generate_time():
    return np.linspace(0, 40, 2000)


def calculate_temperature(power, time):
    k = 0.1 * power
    return 20 + (10 * power) * (1 - np.exp(-k * time))


def apply_shutdown(temperature, time, safety_limit):
    modified_temp = np.copy(temperature)

    if np.max(temperature) > safety_limit:
        shutdown_index = np.where(temperature >= safety_limit)[0][0]
        shutdown_time = time[shutdown_index]
        shutdown_temp = temperature[shutdown_index]

        cooling_rate = 0.15
        cooling_time = time[shutdown_index:] - shutdown_time

        # Cooling toward ambient (20°C)
        cooling_temp = 20 + (shutdown_temp - 20) * np.exp(-cooling_rate * cooling_time)

        modified_temp[shutdown_index:] = cooling_temp
        return modified_temp, shutdown_time

    return modified_temp, None


def classify_system(original_temp, shutdown_time, warning_limit, safety_limit):
    if shutdown_time is not None:
        return "Shutdown Activated"
    elif np.max(original_temp) >= warning_limit:
        return "Warning"
    else:
        return "Safe"


def plot_simulation(time, power_levels, warning_limit, safety_limit):
    plt.figure()

    first_shutdown = True

    for power in power_levels:
        temperature = calculate_temperature(power, time)
        modified_temp, shutdown_time = apply_shutdown(temperature, time, safety_limit)

        status = classify_system(temperature, shutdown_time, warning_limit, safety_limit)

        # 🔥 Raw vs Controlled peaks
        raw_peak_temp = np.max(temperature)
        controlled_peak_temp = np.max(modified_temp)

        label = f"Power={power} ({status})"
        plt.plot(time, modified_temp, linewidth=2, label=label)

        if shutdown_time is not None:
            if first_shutdown:
                plt.axvline(x=shutdown_time, linestyle=":", alpha=0.7, label="Shutdown Time")
                first_shutdown = False
            else:
                plt.axvline(x=shutdown_time, linestyle=":", alpha=0.7)

            print(
                f"Power {power}: {status}, "
                f"Controlled Peak = {controlled_peak_temp:.2f}°C, "
                f"Raw Peak = {raw_peak_temp:.2f}°C, "
                f"Shutdown at {shutdown_time:.2f}s"
            )
        else:
            print(
                f"Power {power}: {status}, "
                f"Controlled Peak = {controlled_peak_temp:.2f}°C, "
                f"Raw Peak = {raw_peak_temp:.2f}°C"
            )

    # 🔥 Clearer zone labels
    plt.axhline(
        y=warning_limit,
        linestyle="--",
        color="orange",
        label=f"Warning Zone ({warning_limit}°C)"
    )
    plt.axhline(
        y=safety_limit,
        linestyle="--",
        color="red",
        label=f"Safety Limit ({safety_limit}°C)"
    )

    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.title("Mini Reactor Temperature Simulator")

    plt.grid()
    plt.legend(loc="lower right")

    plt.savefig("mini_reactor_simulation.png", dpi=300)
    plt.show()


def main():
    time = generate_time()

    warning_limit = 55
    safety_limit = 65

    # Clean demonstration set
    power_levels = [2, 4, 6]

    plot_simulation(time, power_levels, warning_limit, safety_limit)


if __name__ == "__main__":
    main()