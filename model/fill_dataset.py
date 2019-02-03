import pandas as pd
from random import shuffle

# Columns: [money_left, property_cost, group_properties_needed, opponent_avg, go_dist, opponent_house_distance, max_price]

dataset = pd.read_csv('max_price.csv')
money_left = list(range(0, 2000, 200))  # 10
property_cost = [60, 60, 100, 100, 120, 140, 140, 160, 180, 180, 200, 220, 220, 240, 260, 260, 280, 300, 300, 320, 350, 400, 200, 200, 200, 200, 150, 150]  # 28
group_properties_needed = [1, 2] * 3 + [1, 2, 3] * 6 + [1, 2, 3, 4]  # 28
# group_properties_available_percent = [0, 50] * 3 + [0, 100/3, 200/3] * 6 + [0, 25, 50, 75]  # 28
opponent_avg = list(range(0, 2000, 200))  # 10
go_dist = list(range(1, 19)) + list(range(20, 39, 2))  # 28
opponent_house_distance = list(range(1, 19)) + list(range(20, 39, 2))  # 28

money_left = money_left * 28
property_cost = property_cost * 10
group_properties_needed = group_properties_needed * 10
# group_properties_available_percent = group_properties_available_percent * 10
opponent_avg = opponent_avg * 28
go_dist = go_dist * 10
opponent_house_distance = opponent_house_distance * 10

shuffle(money_left)
shuffle(property_cost)
shuffle(group_properties_needed)
# shuffle(group_properties_available_percent)
shuffle(opponent_avg)
shuffle(go_dist)
shuffle(opponent_house_distance)

dataset['money_left'] = money_left
dataset['property_cost'] = property_cost
dataset['group_properties_needed'] = group_properties_needed
# dataset['group_properties_available_percent'] = group_properties_available_percent
dataset['opponent_avg'] = opponent_avg
dataset['go_dist'] = go_dist
dataset['opponent_house_distance'] = opponent_house_distance

dataset.to_csv('max_price.csv')
