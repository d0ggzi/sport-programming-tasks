n = int(input())
cities = dict()
people = dict()
max_cities = dict()
for i in range(n):
    name, city, money = input().split()
    money = int(money)
    people[name] = [city, money]
    cities[city] = cities.get(city, 0) + money
                            
m, k = map(int, input().split())
prev_day = 0
for i in range(k):
    day, name, city_move = input().split()
    day = int(day)
    human = people.get(name)
    if day != prev_day:
        max_sum = 0
        for city, value in cities.items():
            if value == max_sum:
                flag = False
            elif value > max_sum:
                max_sum = value
                max_city = city
                flag = True
        if flag: max_cities[max_city] = max_cities.get(max_city, 0) + (day-prev_day)

    cities[human[0]] -= human[1]
    if cities[human[0]] == 0:
        del cities[human[0]]
    human[0] = city_move
    cities[city_move] = cities.get(city_move, 0) + human[1]
    
    prev_day = day

max_sum = 0
for city, value in cities.items():
    if value == max_sum:
        flag = False
    elif value > max_sum:
        max_sum = value
        max_city = city
        flag = True
if flag: max_cities[max_city] = max_cities.get(max_city, 0) + (m-prev_day)

for city in sorted(max_cities.keys()):
    print(city, max_cities[city])