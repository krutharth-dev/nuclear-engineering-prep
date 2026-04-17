temps = []

for i in range(3):
    t = float(input("Enter temperature: "))
    temps.append(t)

avg=sum(temps) / len(temps)
print("Temperatures:", temps)
print("Average:", avg)