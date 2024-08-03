import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound = 0, cat="Integer")
fruit_juice = pulp.LpVariable('FruiteJuice', lowBound = 0, cat="Integer")

model += lemonade + fruit_juice, 'Total_products'

model += 2* lemonade + 1 * fruit_juice <= 100, "Water_Limit"
model += 1* lemonade <= 50, "Sugar_Limit"
model += 1 * lemonade <= 30, "LemonJuice_Limit"
model += 2 * fruit_juice <= 40, "FruitePuree_Limit"

model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade to produce: {lemonade.varValue}")
print(f"Fruit Juice to produce: {fruit_juice.varValue}")
print(f"Total products: {pulp.value(model.objective)}")
