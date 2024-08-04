import pulp

model = pulp.LpProblem("Максимізація", pulp.LpMaximize)

lemonade = pulp.LpVariable("Лимонад", lowBound=0, cat='Continuous')
juice = pulp.LpVariable("Сік", lowBound=0, cat='Continuous')

model += lemonade + juice, "Total"

model += 2 * lemonade + 1 * juice <= 100, "Water"
model += 1 * lemonade <= 50, "Sugar"
model += 1 * lemonade <= 30, "Lemon_Juice"
model += 2 * juice <= 40, "Fruit_Puree"

model.solve()

print("Виробництво лимонадів:", pulp.value(lemonade))
print("Виробництво соку:", pulp.value(juice))
 
