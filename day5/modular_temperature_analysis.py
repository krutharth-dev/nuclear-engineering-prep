# Day 5: Modular Temperature Analysis System

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


def print_summary(temperatures, analysis):
    print("\n--- Temperature Analysis Report ---")
    print(f"Temperatures: {temperatures}")
    print(f"Average: {analysis['average']:.2f}")
    print("\nCategory counts:")
    for category, count in analysis["counts"].items():
        print(f"{category.title()}: {count}")


def get_sample_data():
    return [12, 18, 27, 36, 22, 40, 14]


def main():
    temperatures = get_sample_data()

    analysis = analyze_temperatures(temperatures)

    print_summary(temperatures, analysis)


if __name__ == "__main__":
    main()