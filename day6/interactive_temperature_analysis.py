# Day 6: Interactive Temperature Analysis System

def classify_temperature(temp):
    if temp >= 35:
        return "very hot"
    elif temp >= 25:
        return "warm"
    elif temp >= 15:
        return "cool"
    return "cold"


def calculate_average(temperatures):
    return sum(temperatures) / len(temperatures)


def count_categories(temperatures):
    counts = {
        "very hot": 0,
        "warm": 0,
        "cool": 0,
        "cold": 0
    }

    for temp in temperatures:
        counts[classify_temperature(temp)] += 1

    return counts


def analyze_temperatures(temperatures):
    return {
        "average": calculate_average(temperatures),
        "counts": count_categories(temperatures)
    }


def get_valid_temperatures():
    temperatures = []

    while True:
        user_input = input("Enter temperature (or 'done' to finish): ").strip().lower()

        if user_input == "done":
            break

        try:
            temp = float(user_input)

            if -100 <= temp <= 100:
                temperatures.append(temp)
            else:
                print("Temperature must be between -100 and 100.")
        except ValueError:
            print("Please enter a valid number or 'done'.")

    return temperatures


def print_summary(temperatures, analysis):
    print("\n--- Temperature Analysis Summary ---")
    print(f"Temperatures: {temperatures}")
    print(f"Average: {analysis['average']:.2f}")

    print("\nCategory counts:")
    for category, count in analysis["counts"].items():
        print(f"{category.title()}: {count}")


def main():
    temperatures = get_valid_temperatures()

    if not temperatures:
        print("No valid temperatures entered.")
        return

    analysis = analyze_temperatures(temperatures)

    print_summary(temperatures, analysis)


if __name__ == "__main__":
    main()