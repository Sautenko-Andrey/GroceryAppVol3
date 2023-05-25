prices_list = [
    ("ATB",15.00),
    ("EKO",32.56),
    ("Varus",15.00),
    ("Metro",15.000)
]


prices_only=[]
for item in prices_list:
    prices_only.append(item[1])
print(prices_only)

best_price = min(prices_only)
print(best_price)

final_respond=[]
for item in prices_list:
    if item[1]==best_price:
        final_respond.append((item[0],item[1]))
print(final_respond)









