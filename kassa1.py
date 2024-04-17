products = {"молоко": 20, "хлеб": 15, "сыр": 10, "картошка": 5,"огурцы": 8,"помидоры": 30,"драники": 35,"сок": 40,"газировка": 15}
coins = [15, 10, 7, 5, 1]

def calculate_change(product_name, payment):
    price = products[product_name]
    change = payment - price


    result = []
    while change > 0:
        max_coin = max([coin for coin in coins if coin <= change])
        result.append(max_coin)
        change -= max_coin

    return result


product_name = "хлеб" 
payment = 50

change = calculate_change(product_name, payment)
print(f"Сдача составляет: {sum(change)} р.")
print(f"Минимальное количество монет для сдачи: {len(change)}")
print(f"Монеты для сдачи: {change}")