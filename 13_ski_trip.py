days = int(input())
accommodation = input()
evaluation = input()
nights = days - 1
price = 0
if accommodation == "room for one person":
    price = 18.00
elif accommodation == "apartment":
    price = 25.00
    if nights < 10:
        price *= 0.7
    elif 10 <= nights <= 15:
        price *= 0.65
    elif nights > 15:
        price *= 0.5
elif accommodation == "president apartment":
    price = 35.00
    if nights < 10:
        price *= 0.9
    elif 10 <= nights <= 15:
        price *= 0.85
    elif nights > 15:
        price *= 0.8
if evaluation == "positive":
    price *= 1.25
else:
    price *= 0.9
price_holiday = price * nights
print(f"{price_holiday:.2f}")
