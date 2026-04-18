# Day 4: Temperature Analysis System

temps = []

# Step 1: Take inputs
for i in range(5):
    t = float(input(f"Enter temperature {i+1}: "))
    temps.append(t)

print("\nAll temperatures:", temps)

# Step 2: Initialize counters
very_hot = 0
warm = 0
cool = 0
cold = 0

# Step 3: Classify each temperature
for temp in temps:
    if temp >= 35:
        print(temp, "→ very hot")
        very_hot += 1
    elif temp >= 25:
        print(temp, "→ warm")
        warm += 1
    elif temp >= 15:
        print(temp, "→ cool")
        cool += 1
    else:
        print(temp, "→ cold")
        cold += 1

# Step 4: Calculate average
average = sum(temps) / len(temps)

# Step 5: Final summary
print("\n--- Summary ---")
print("Total readings:", len(temps))
print("Very hot:", very_hot)
print("Warm:", warm)
print("Cool:", cool)
print("Cold:", cold)
print("Average temperature:", round(average, 2))
