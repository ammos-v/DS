# *** Списки (lists) *** 

# создание пустого списка

my_list = []
my_list_2 = list()

# метод append

my_list.append(100)
my_list.append(200)
my_list.append("hello")
my_list.append([1,2,3])

# создание заполненного списка

my_list = [10, 20, 30, 40, "A", 3.14, True]

s = "Привет, Мир!"
list_1 = list(s)

# *** функция range() ***

numbers = list(range(10) ) # создается набор чисел от 0 до 10 не включительно
numbers = list(range(2, 10) ) # создается набор чисел от 2 до 10 не включительно
numbers = list(range(2, 10, 2) ) # создается набор чисел от 2 до 10 не включительно с шагом 2
numbers = list(range(10, 1, -1) ) # создается набор чисел от 10 до 1 не включительно с шагом -1(в обратном направлнии)

# *** методы списков ***

a = [10,20,30,40,50]

# обьект.метод()

# добавление элемента по индексу

a.insert(0, "A")

# удаление элемента по значению
# a.remove(30)

# очистка списка

# print(a)
# a.clear()

# сортировка списка
b = [8,4,1,6,8,34,2,5,2,35]
# b.sort() в сторону возраствния
b.sort(reverse=True) # в сторону убыванию

# обращение к элементам 

c = [1,2,3,4,5]


# print(c[0]) # извлечение элемента(чтение) значение элемент

# del c[1] #  удаление элемента по индексу

# c[3] =10 # замена значения
# c[-1] =10 # замена значения элемента через обратный индекс

# *** срезы (slice)***

c = c + [6,7,8,9,10,11]

c_slice = c[0:3] # срез с 0 индекса по 3 индекс не включительно
c_slice = c[:3] # срез с 0 индекса по 3 индекс не включительно
c_slice = c[1:4] # срез с 1 индекса по 4 индекс не включительно
c_slice = c[1:8:2] # срез с 1 индекса по 8 индекс не включительно с шагом 2
c_slice = c[::2] # срез всего списка с шагом 2
c_slice = c[::-1] # поворот списка
c_slice = c[-1:-4:-1] # срез в обратном направлении


print(c_slice)