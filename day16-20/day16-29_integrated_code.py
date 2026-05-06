import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# CONSTANTS
# -----------------------------
AMBIENT_TEMP = 25
TIME_END = 100
DT = 1

K_COOLING = 0.05

SHUTDOWN_TEMP = 120
RESTART_TEMP = 90


# -----------------------------
# POWER FUNCTION
# -----------------------------
def get_power(time):
    if time < 30:
        return 80
    elif time < 60:
        return 120
    else:
        return 60


# -----------------------------
# COOLING FUNCTION
# -----------------------------
def calculate_cooling(temp):
    return K_COOLING * (temp - AMBIENT_TEMP)


# -----------------------------
# SAFETY SYSTEM (FINAL)
# -----------------------------
def safety_system(temp, shutdown, time, event_log):
    if temp > SHUTDOWN_TEMP and not shutdown:
        shutdown = True
        print(f"⚠️ Reactor Shutdown Triggered at t = {time}s")
        event_log.append(("shutdown", time))

    elif temp < RESTART_TEMP and shutdown:
        shutdown = False
        print(f"✅ Reactor Restarted at t = {time}s")
        event_log.append(("restart", time))

    return shutdown


# -----------------------------
# SIMULATION
# -----------------------------
def run_simulation():
    time_values = np.arange(0, TIME_END, DT)

    temp = AMBIENT_TEMP
    shutdown = False

    temperature = []
    power_list = []
    cooling_list = []
    status_list = []   # 1 = ON, 0 = OFF
    event_log = []

    for t in time_values:
        power = get_power(t)

        if shutdown:
            power = 0

        cooling = calculate_cooling(temp)

        # 🔥 Tuned heating for visible dynamics
        temp = temp + power * 0.08 - cooling

        shutdown = safety_system(temp, shutdown, t, event_log)

        # Store values
        temperature.append(temp)
        power_list.append(power)
        cooling_list.append(cooling)
        status_list.append(0 if shutdown else 1)

    return time_values, temperature, power_list, cooling_list, status_list, event_log


# -----------------------------
# PLOTTING
# -----------------------------
def plot_results(time, temp, power, cooling, status):
    plt.figure(figsize=(12, 7))

    plt.plot(time, temp, label="Temperature")
    plt.plot(time, power, label="Power Input")
    plt.plot(time, cooling, label="Cooling Effect")

    # Safety thresholds
    plt.axhline(y=SHUTDOWN_TEMP, linestyle='--', label="Shutdown Limit")
    plt.axhline(y=RESTART_TEMP, linestyle='--', label="Restart Limit")

    # Highlight shutdown periods
    for i in range(len(time)):
        if status[i] == 0:
            plt.axvspan(time[i], time[i] + DT, alpha=0.1)

    plt.xlabel("Time (s)")
    plt.ylabel("Values")
    plt.title("Smart Reactor Simulation (Final V3)")

    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig("smart_reactor_simulation_v3.png", dpi=300)
    plt.show()


# -----------------------------
# MAIN
# -----------------------------
def main():
    time, temp, power, cooling, status, events = run_simulation()

    print("\n--- EVENT LOG ---")
    for event in events:
        print(f"{event[0].upper()} at t = {event[1]}s")

    plot_results(time, temp, power, cooling, status)


if __name__ == "__main__":
    main()