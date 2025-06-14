types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

values = list(tickets.values()) #создаем список со значениями словаря tickets
types = list(types.values()) #создаем список со значениями словаря types

def delete_duplicates(values):              
    saved_items = [] #здесь сохраняем все элементы вложенных списков
    
    for i in range(len(values)): #проходим по каждому вложенному списку
        list_without_duplicates = [] #создаём временный список для хранения уникальных элементов текущего вложенного списка
        for item in values[i]: 
            if item not in saved_items: #если элемент не находится в saved_items
                list_without_duplicates.append(item) #добавляем его во временный текущий список
                saved_items.append(item) #добавляем его в общий список
        values[i] = list_without_duplicates #заменяем исходный вложенный список на очищенный от дубликатов
    return values

tickets_without_duplicates = delete_duplicates(values) #сохраняем результат в переменную запущенной функции на удаление дубликатов

def compare_dict(types, new_dict):
    dict_macth = {} #создаем пустой словарь
    for i in range(len(types)): #проходимся по элементам списков
        dict_macth[types[i]] = new_dict[i] #сопоставляем значения
    return dict_macth

tickets_by_type = compare_dict(types, tickets_without_duplicates) #сохраняем результат в переменную запущенной функции
print(tickets_by_type)