world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина' #добавили новый элемент

for keys, values in world_champions.items():
        print(str(keys) + ' - ' + values)#вывели всех чемпионов в формате год - страна

country = 'Италия'

if  country in world_champions.keys() or country in world_champions.values(): #ищем, выигрывала ли когда-то Италия
        print('Италия становилась чемпионом мира по футболу в 21 веке!')
else:
        print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
