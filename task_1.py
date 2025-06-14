time_intervals = '1h 45m,360s,25m,30m 120s,2h 60s' 
total_time = 0 #здесь будем сохранять минуты

time_intervals = time_intervals.replace(' ', ',') #меняем пробелы на запятые, чтобы было удобнее разделить строку
time_intervals_list = time_intervals.split(',') #разделяем строку на части и работаем со списком единиц времени

for time_unit in time_intervals_list:
    if 'h' in time_unit:
        total_time += int(time_unit.replace('h', '')) * 60 #избавляемся от h и считаем минуты, умножив часы на 60
    elif 'm' in time_unit:
        total_time += int(time_unit.replace('m', '')) * 1 #избавляемся от m и считаем минуты, умножив минуты на 1
    elif 's' in time_unit:
        total_time += int(time_unit.replace('s', '')) // 60 #избавляемся от s и считаем минуты, разделив секунды на 60

print(total_time)




    
