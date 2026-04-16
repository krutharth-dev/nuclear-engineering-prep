name=input("Enter your name: ")
temp=float(input("Enter temperature: "))

if temp>=40:
    result="Very Hot"
elif temp>=35:
    result="Hot"
elif temp>=25:
    result="Warm"
elif temp>=15:
    result="Cool"
else:
    result="Cold"

print(f"Hello {name},it is {result}")