products = {"молоко": 20, "хлеб": 15, "сыр": 10, "картошка": 5,"огурцы": 8,"помидоры": 30,"драники": 35,"сок": 40,"газировка": 15}
coins = [15, 10, 7, 5, 1]
coins_in_cash = {15: 2, 10: 0, 7: 0, 5: 4, 1: 0}

def calculate_change(product_name, payment):
    price = products[product_name]
    change = payment - price

    result = []
    while change > 0:
        max_coin = max([coin for coin in coins if coin <= change and coins_in_cash[coin] > 0])
        result.append(max_coin)
        coins_in_cash[max_coin] -= 1
        change -= max_coin

    return result

product_name = "молоко"
payment = 40


change = calculate_change(product_name, payment)
print(f"Сдача составляет: {sum(change)} р.")
print(f"Минимальное количество монет для сдачи: {len(change)}")
print(f"Монеты для сдачи: {change}")