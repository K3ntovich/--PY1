salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

def life(salary,spend,months,increase):
    need_money = 0;
    for i in range(months):
        need_money += spend - salary;
        spend *= 1 + increase;
    return need_money;
need_money = life(salary,spend,months,increase);

print(round(need_money))
