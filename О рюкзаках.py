def get_area_and_value(stuffdict):
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]        
    return area, value

def get_memtable(stuffdict, A=8):
      area, value = get_area_and_value(stuffdict)
      n = len(value) # найдем размеры таблицы
      
      # создадим из нулевых значений таблицу
      V = [[0 for a in range(A+1)] for i in range(n+1)]

      for i in range(n+1):
            for a in range(A+1):
                  # базовый случай
                  if i == 0 or a == 0:
                        V[i][a] = 0

                  # если площадь предмета меньше площади столбца,
                  # максимизируем значение суммарной ценности
                  elif area[i-1] <= a:
                        V[i][a] = max(value[i-1] + V[i-1][a-area[i-1]], V[i-1][a])

                  # если площадь предмета больше площади столбца,
                  # забираем значение ячейки из предыдущей строки
                  else:
                        V[i][a] = V[i-1][a]       
      return V, area, value

def get_selected_items_list(stuffdict, A=8):
      V, area, value = get_memtable(stuffdict)
      n = len(value)
      res = V[n][A]      # начинаем с последнего элемента таблицы
      a = A              # начальная площадь - максимальная
      items_list = []    # список площадей и ценностей
    
      for i in range(n, 0, -1):  # идём в обратном порядке
            if res <= 0:  # условие прерывания - собрали "рюкзак" 
                  break
            if res == V[i-1][a]:  # ничего не делаем, двигаемся дальше
                  continue
            else:
                  # "забираем" предмет
                  items_list.append((area[i-1], value[i-1]))
                  res -= value[i-1]   # отнимаем значение ценности от общей
                  a -= area[i-1]  # отнимаем площадь от общей
      
      return items_list

points = 20
one=[15,25,15,10]
two=[15,15,20,20,20]
three=[25,20]
name1=['н','о','ф','д']
name2=['п','б','а','к','р']
name3=['в','т']
stuffdict = {'н': (1,15),'o':(1,25),'ф':(1,15),'д':(1,10),'п':(2,15),'б':(2,15),'а':(2,20),'к':(2,20),'р':(2,20),'в':(3,25),'т':(3,20)}
area = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3]
value = [15, 25, 15, 10, 15, 15, 20, 20, 20, 25, 20]
endval = [15.0, 25.0, 15.0, 10.0, 7.5, 7.5, 10.0, 10.0, 10.0, 8.333333333333334, 6.666666666666667]
stuffdict2 = {}
sorteddict = sorted(stuffdict)
print(sorteddict)
area, value = get_area_and_value(stuffdict)

end = get_selected_items_list(stuffdict)
for i in value:
    points -= i
for i in range(len(end)):
    points += end[i][1]*2

for search in end:
    for key, value in stuffdict.items():
        if value == search:
            print(key)
            stuffdict.pop(key)
            break
print(end)
print(points)
