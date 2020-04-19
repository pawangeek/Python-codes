# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
# It's quit straightforward to use a hashmap to save meals that each table has

from collections import Counter,defaultdict
orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]

desk = defaultdict(Counter)
meal = set()

for _, table, food in orders:
    meal.add(food)
    desk[table][food] += 1

foods = sorted(meal)
result = [['Table'] + [food for food in foods]]

for table in sorted(desk, key=int):
    result.append([table] + [str(desk[table][food]) for food in foods])

print (result)