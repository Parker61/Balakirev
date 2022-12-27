########  3.6 Списки и операции над нимиПодвиг9.Вводятсяоценкистудента(числаот2о5) воднустрокучерезпробел.Необходимо
# определитьколичестводвоекивывестиэтозначениенаэкран.SampleInput:23524225SampleOutpu:4
print(sum(char == '2' for char in
          input().split()))  # здесь char == '2' расценивается как True=1 и дальше единички суммируются

###########  Срезы 3.7
# Необходимо с помощью срезов выбрать элементы с 3-го по 7-й (включительно) и вывести их на экран в обратном порядке.
m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
print(m[2:7][::-1])
# m[2:7][::-1]
# [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4][2:7][::-1]
# 0  1  2  3 4  5  6  7 8 9 10 11 <- индексы
# | ^              ^ |                     <- срез [2:7] индекс 7 не берется
# [5, 5, 2, 2, 3]                     <- срез предыдущего списка
# [5, 5, 2, 2, 3][::-1] срез в обратном порядке


########  4.1 Условный оператор if. Конструкция if-else
# Подвиг 1. Вводятся два вещественных числа в одну строку через пробел. Вывести на экран наибольшее из чисел. Задачу
# решить с помощью условного оператора.
s1, s2 = map(float, (input()).split())
print(s1 if s1 > s2 else s2)

print(max(map(float, (input()).split())))

# Подвиг 2. Вводится слово. Необходимо определить, является ли это слово палиндромом (одинаково читается вперед и
# назад, например, АННА). Регистр букв не учитывать. Если введенное слово палиндром, на экран вывести ДА, иначе - НЕТ.
w = input().upper()
print('да' if w == w[::-1] else 'нет')

w = list(input().upper())
w1 = list(reversed(w))
print('да' if w == w[::-1] else 'нет')

a = input().lower()
b = a[::-1]
print(a.count(b))
if a.count(b) == 1:  # кол вхождений в строки b в строку a
    print("ДА")
else:
    print("НЕТ")

a = input().lower()
print(('ДА', 'НЕТ')[a != a[::-1]])  # - используем индекс(True =1, False=0)
# или так
print('ДА' * (a == a[::-1]) or 'НЕТ')  # - разворачиваем логическое выражение, компактный аналог if
(lambda x: print('ДА' if x == x[::-1] else 'НЕТ'))(input().lower())

# Подвиг 3. Вводятся два целых положительных числа m и n в одну строку через пробел. Если число m делится нацело на
# число n, то вывести на экран частное от деления (результат деления) в виде целого числа. В противном случае вывести
# сообщение «m на n нацело не делится» (без кавычек) и вместо m и n подставить соответствующие числа, например: «13 на
# 2 нацело не делится».
m, n = map(int, input().split())
print(m // n if m % n == 0 else f'{m} на {n} нацело не делится')

print((lambda a, b: a // b if not a % b else f"{a} на {b} нацело не делится")(*map(int, input().split())))
print(not 8 % 4)

m, n = map(int, input().split())
if not m % n:  # not 0 ---> True
    print(m // n)
else:
    print(f"{m} на {n} нацело не делится")

m, n = map(int, input().split())
if m % n:  # результат операции  % или 0 или не 0, зачем продолжать  ==0 ?
    print(f"{m} на {n} нацело не делится")
else:
    print(int(m / n))

# Подвиг 4. Вводятся три целых положительных числа в одну строку через пробел. Убедиться, что первые два числа - это
# катеты прямоугольного треугольника, а третье - его гипотенуза. (Подсказка: проверка делается по теореме Пифагора ).
# Если проверка проходит (истинна), то вывести на экран ДА, иначе - НЕТ.
a, b, c = map(int, input().split())
print(['НЕТ', 'ДА'][c ** 2 == a ** 2 + b ** 2])

(lambda a, b, c: print('ДА' if pow(a, 2) + pow(b, 2) == pow(c, 2) else 'НЕТ')) \
    (*map(int, input().split()))

# Подвиг 5. Вводится четырехзначное число. Проверить, что оно оканчивается на цифру 7. Вывести на экран ДА, если это
# так и НЕТ - в противном случае.
print('НДЕАТ'[input()[-1] == '7'::2])
print(('НЕТ', 'ДА')[input()[-1] == '7'])

x = list(input()).pop()
print('ДА' if x == '7' else 'НЕТ')

# Подвиг 5. Вводится четырехзначное число. Проверить, что оно оканчивается на цифру 7. Вывести на экран ДА, если это
# так и НЕТ - в противном случае.
s1 = input()
print('ДА' if all(['t' in s1, 'h' in s1, 'o' in s1]) else 'НЕТ')

s0 = input()
print(['НЕТ', 'ДА']['t' in s0 and 'h' in s0 and 'o' in s0])

print(('НЕТ', 'ДА')[{*'hot'}.issubset(
    input())])  # прописывать * чтобы распаковать строку :), иначе получится множество из одногой строки {'hot'}.
# Можно было конечно написать set('hot')
# set1.issubset(set2) возвращает True если множество set1 является подмножеством множества set2 и False в иных случаях.
print(['НЕТ', 'ДА'][{'t', 'h', 'o'}.issubset(input().lower())])
print(('НЕТ', 'ДА')[set('tho').issubset(set(input().lower()))])
print('ДА' if {'t', 'h', 'o'} <= set(list(input())) else 'НЕТ')

s = input()
if s.count("t") and s.count("h") and s.count("o"):
    print("ДА")
else:
    print("НЕТ")

# Подвиг 7. Вводится список городов в одну строку через пробел. Если в этом списке присутствует город Москва, то
# удалить его. Вывести на экран результирующий список в виде строки с городами через пробел.
s = input().split()
if 'Москва' in s:
    s.remove('Москва')  # Если Москва будет в списке хотя бы 2 раза уже не сработает.
print(*s)

print(*input().replace("Москва", "").split())
print(*[i for i in input().split() if i != 'Москва'])  # print(всего кроме "Москва")
print(input().replace('Москва ', ''))

# Подвиг 8. Вводятся четыре целых числа a, b, c, d в одну строку через пробел. Определить, войдет ли в конверт с
# внутренними размерами a и b мм прямоугольная открытка с размерами с и d мм. Для размещения открытки в конверте
# необходим зазор в 1 мм с каждой стороны. Открытку можно поворачивать на 90 градусов. Вывести ДА, если входит и НЕТ
# - если не входит.
# Sample Input:#12 5 7 2
a, b, c, d = map(int, input().split())
if (a - 1 > c and b - 1 > d) or (a - 2 >= d and b - 1 > c):
    print('ДА')
else:
    print('НЕТ')

a, b, c, d = map(int, input().split())
print('ДА' if (a - 2 >= c and b - 2 >= d) or (a - 2 >= d and b - 2 >= c) else 'НЕТ')

a, b, c, d = map(int, input().split())
print(("НЕТ", "ДА")[(a - c >= 2 and b - d >= 2) or (a - d >= 2 and b - c >= 2)])

s = tuple(map(int, input().split()))
a, b = sorted(s[:2])
c, d = sorted(s[2:])
print(('НЕТ', 'ДА')[a >= c + 2 and b >= d + 2])

# a[:3] - это срез из 0, 1 и 2 элемента списка а

sum(a[:3]) - этосуммавсехэлементовсреза

sum(a[:3]) == sum(a[3:]) - этосравнениедвухсумм, возвращаетTrueилиFalse

('НЕТ', 'ДА') - этокортежиздвухэлементов, здесьдалееидетвыбор: НЕТэто0 - войиндекскортежа, тоестькогдасравнениебудет
False, ДАполучаемеслииндексполучили1, т.е.
True.
x = list(map(int, (input())))
print(sum(x), sum(x[:3]), sum(x[3:]))
print(['НЕТ', 'ДА'][sum(x[:3]) == sum(x[3:])])

lst = [int(n) for n in input()]
print(('ДА', 'НЕТ')[sum(lst[:3]) != sum(lst[3:])])

##Подвиг 8. Вводятся четыре целых числа a, b, c, d в одну строку через пробел. Определить, войдет ли в конверт с
# внутренними размерами a и b мм прямоугольная открытка с размерами с и d мм. Для размещения открытки в конверте
# необходим зазор в 1 мм с каждой стороны. Открытку можно поворачивать на 90 градусов. Вывести ДА, если входит и НЕТ -
# если не входит.
# Sample Input:811235

# используются два оператора % и //. Первый (%) возвращает остаток от деления, второй (//) возвращает результат
# целочисленного деления. Возьмем для примера число 9874. 9874 % 10 дает 4 (те 1-ая цифра справа), а 9874 // 10 дает
# 987. Здесь их применяют последовательно: 9874 % 100 получаем 74, дальше 74 // 10 получаем 7 (те 2-ая цифра справа).
# Дальше 9874 % 1000 дает 874 и 874 //100 дает 8 (3-ая цифра справа). И так далее... Цифры складываем. Результат
# сравниваем.
x = int(input())
x1 = x // 100000
x2 = x // 10000 % 10
x3 = x // 1000 % 10
x4 = x // 100 % 10
x5 = x // 10 % 10
x6 = x % 10
if x1 + x2 + x3 == x4 + x5 + x6:
    print('ДА')
else:
    print('НЕТ')

print((lambda s=input(): "НДЕАТ"[sum(map(int, s[:3])) == sum(map(int, s[3:]))::2])())

# Подвиг 10. Работа светофора для пешеходов запрограммирована следующим образом: в начале каждого часа в течение
# трех минут горит зеленый сигнал, затем в течение двух минут – красный, в течение трех минут – опять зеленый и т. д.
# Дано вещественное число t, означающее время в минутах, прошедшее с начала очередного часа. Определить, сигнал какого
# цвета горит для пешеходов в этот момент. На экран вывести сообщение (без кавычек) "green" - для зеленого и "red" -
# для красного.
a = [int(i) for i in input()]
if sum(a[:3]) == sum(a[-3:]):
    print('ДА')
else:
    print('НЕТ')

a = list(map(int, input()))
b = 'НЕТ'
if sum(a[:3]) == sum(a[3:]):
    b = 'ДА'
print(b)

print('green' if float(input()) % 5 <= 3 else 'red')

#############  4.2 Вложенные условия и множественный выбор ############
# В программе вводится целое число от 1 до 6.
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
m = (m.split('\n'))
n = int(input())
if n == int(m[n - 1][0]):
    print(m[n - 1])

m = (m.split('\n'))
n = int(input())
print(m[n - 1])

m = (m.split('\n'))
print(m[int(input()) - 1])

print(m.split('\n')[int(input()) - 1])

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''.split('\n')
print(m[int(input()) - 1])

print(m.split('\n')[int(input()) - 1])

lst = m.split('\n')
n = int(input())
print(lst[n - 1])

a = input()
a_1 = int(a)
print(m[m.index(a)])
if a_1 < 6:
    b = a_1 + 1
    c = str(b)
    print(m[m.index(a):m.index(c)])
elif a_1 == 6:
    print(m[m.index(a):])

x = int(input())
m = m.split('\n')
if len(m) >= x:
    print(m[x - 1])

m = m.split('\n')
menu_item = int(input())

if 1 <= menu_item <= 6:
    print(m[menu_item - 1])

m = [0] + m.split('\n')  # ноль вперед подставил, чтобы цифры совпадали
n = int(input())
if n == 1:
    print(m[1])
elif n == 2:
    print(m[2])
elif n == 3:
    print(m[3])
elif n == 4:
    print(m[4])
elif n == 5:
    print(m[5])
elif n == 6:
    print(m[6])

a = int(input())
print(m[m.find(str(a)):m.find(str(a + 1))] if a < 6 else m[m.find(str(a)):])

menu_items = {
    1: '1. Введение в Python',
    2: '2. Строки и списки',
    3: '3. Условные операторы',
    4: '4. Циклы',
    5: '5. Словари, кортежи и множества',
    6: '6. Выход'
}
print(menu_items[int(input())])

paragraph = input()
if paragraph in m and str(int(paragraph) + 1) in m:
    print(m[m.index(paragraph):m.index(str(int(paragraph) + 1))])
elif paragraph in m and str(int(paragraph) + 1) not in m:
    print(m[m.index(paragraph):])

list_m = m.split('\n')  # Преобразование в словарик.
dict_m = dict()
for i in list_m:
    list_i = i.split('.')
    dict_m[list_i[0]] = dict_m.setdefault(int(list_i[0]), list_i[1])

index = int(input())
print(f'{str(index)}.{dict_m[index]}')

print({1: '1. Введение в Python', 2: '2. Строки и списки', 3: '3. Условные операторы', 4.: '4. Циклы',
       5: '5. Словари, кортежи и множества', 6: '6. Выход'}[int(input())])

n = int(input())
a = []
b = []
m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''.strip().split('\n')
x = ' '.join(m)
s = x.split('. ')
for i, j in enumerate(m, 1):
    a.append(i)
    b.append(j[3:])
v = dict(zip(a, b))
print(f'{n}. {v[n]}')

m = m.split("\n")
num_m = input()
for i in m:
    if num_m in i:
        print(i)
        break

flag = False
n = input()
for i in m:
    if n == i:
        s = m.index(i)
    if str(int(n) + 1) == i:
        f = m.index(i)
        flag = True
        break
if flag:
    print(m[s:f])
else:
    print(m[s:])

####Подвиг 2. Вводятся три целых числа в одну строку через пробел.
# Необходимо определить наименьшее среди них и вывести его на экран.
a, b, c = map(int, input().split())
if a <= b and a < c:
    print(a)
elif b <= a and b < c:
    print(b)
else:
    print(c)

a, b, c = map(int, input().split())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
print(a)

a, b, c = map(int, input().split())
if a > b:
    a = b
if a > c:
    a = c
print(a)

print(sorted(map(int, input().split()))[0])

a, b, c = map(int, input().split())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)

# Подвиг 3. Вводится вес боксера-любителя (в кг, в виде вещественного числа). Известно, что вес таков, что боксер может
# быть отнесен к одной из весовых категорий:
# 1) легкий вес – до 60 кг (включительно);
# 2) первый полусредний вес – до 64 кг (включительно);
# 3) полусредний вес – до 69 кг (включительно);
# 4) остальные - более 69 кг.
# Например, (60 <= weight) может вернуть False или True.

Допустим, чтовозвращаетсяTrue, тогдапризаписиprint((60 <= weight))
получимвконсолеTrue(Лишниескобкиможноубрать, вданном
примере)Ноеслизаписатьprint(1 + (60 <= weight)), тоTrueавтоматическизаменитсяна1, чтодастрезультат2weight = \
    float(input())

print(1 + (60 <= weight) + (64 <= weight) + (69 <= weight))

w = float(input())
print((3 * (w > 69) or 2 * (w > 64) or (w > 60) or 0) + 1)

Вводитсяпорядковыйномерднянедели(1, 2, ..., 7).Вывестинаэкранегоназвание(понедельник, вторник, среда, четверг, пятница,
                                                                         суббота, воскресенье).Программу
s = 'понедельник, вторник, среда, четверг, пятница, суббота, воскресенье'.split(',')
print(s[int(input()) - 1])

# Вводится порядковый номер месяца (1, 2, ..., 12). Вывести на экран количество дней в этом месяце. Принять, что год
# не является високосным. Реализовать через условный оператор, в котором следует использовать не более трех ветвей
# (блоков).# P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

x = int(input())
if x == 2:
    print('28')
elif x in (1, 3, 5, 7, 8, 10, 12):
    print('31')
else:
    print('30')

year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = int(input())
if 1 <= num <= 12:
    print(year[num - 1])
else:
    print('Введите число от 1 до 12')

d1 = int(input())
print([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][d1 - 1])

print([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][int(input())])

# monthrange возвращает кортеж, нам нужен элемент с индексом 1
print(__import__('calendar').monthrange(2021, int(input()))[1])

a = int(input())
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 0 < a <= 12:
    print(d[a - 1])

x = input()
print(((31, 30)[x in ('4', '6', '9', '11')], 28)[x == '2'])

month = int(input()) - 1
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 0 <= month < 13:
    print(days[month])
else:
    print('?')

year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
print(year[int(input())])

m = int(input())
day = ['Укажите месяц от 1 до 12', 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 0 < m < 13:
    print(day[m])
else:
    print(day[0])

# Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
# По введенным m и n (в одну строку через пробел) определить:
а) датупредыдущегодня(принять, нехарактеризуют1января);
б) датуследующегодня(принять, чтоmиnне
характеризуют31декабря).
m, n = map(int, (input()).split())
print(f'{m:02}')
if n == 31 and m in (1, 3, 5, 7, 8, 10, 12):
    print(f'{m:02}.{n - 1} {m + 1:02}.', end='')
n = 1
print(f'{n:02}')
# print(f'{str(m).rjust(2,"0")}.{n-1} {str(m+1).rjust(2,"0")}.01')
elif n == 30 and m in (2, 4, 6, 9, 11):
print(f'{m:02}.{n - 1} {m + 1:02}.01')
# print(f'{str(m).rjust(2,"0")}.{n-1} {str(m+1).rjust(2,"0")}.01')
elif n == 28 and m == 2:
print(f'{m:02}.{n - 1} {m + 1:02}.01')
# print(f'{str(m).rjust(2,"0")}.{n-1} {str(m+1).rjust(2,"0")}.01')
else:
print(f'{m:02}.{n - 1} {m:02}.{n + 1}')
# print(f'{str(m).rjust(2,"0")}.{n-1} {str(m).rjust(2,"0")}.{n+1}')

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, n = map(int, input().split())
if n == 1:
    pday = days[m]
pmh = m
fday = 2
fmh = m + 1
elif n == days[m]:
pday = n - 1
pmh = m
fday = 1
fmh = m + 1
else:
pday = n - 1
pmh = m
fday = n + 1
fmh = m
print(f'0{pmh}.'[-3:], end='')
print(f'0{pday}'[-2:], end=' ')
print(f'0{fmh}.'[-3:], end='')
print(f'0{fday}'[-2:], end='')

m, n = map(int, input().split())
lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if n == 1:
    print(f'{m - 1:02}.{lst[m - 2]} {m:02}.{n + 1:02}')
elif n == lst[m - 1]:
    print(f'{m:02}.{n - 1:02} {m + 1:02}.01')
else:
    print(f'{m:02}.{n - 1:02} {m:02}.{n + 1:02}')

# {value: x > n}
# x - чт одобавляем (число, символ без кавычек)> - добавляем до value
# < - добавляем после value
# n - общее число символов, которое должно получиться встроке вместе с value
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, d = map(int, input().split())
next_d = d + 1 if d < days[m - 1] else 1
next_m = m + 1 if next_d == 1 else m
prev_d = d - 1 if d > 1 else days[m - 2]
prev_m = m if d > prev_d else m - 1
print(f'{prev_m:0>2}.{prev_d:0>2} {next_m:0>2}.{next_d:0>2}')

# Все объекты datetime.date(), datetime.datetime() и datetime.time() поддерживают метод .strftime(format) для создания
# троки, представляющей время под контролем явной строки формата.
# И наоборот, метод класса datetime.datetime.strptime() создает объект datetime.datetime() из строки, представляющей
# дату и время в строке, соответствующей формату.
import datetime as dt

d = dt.datetime.strptime(input(), '%m %d')
print(dt.timedelta(1))
print((d - dt.timedelta(1)).strftime('%m.%d'), (d + dt.timedelta(days=1)).strftime('%m.%d'))

import datetime

date = datetime.datetime(2021, *map(int, input().split()))
print(date)
print(str(date - datetime.timedelta(days=1))[5:10].replace('-', '.'),
      str(date + datetime.timedelta(days=1))[5:10].replace('-', '.'))

# Вводится целое число k (1 <= k <= 365).
# Определить, каким днем недели (понедельник, вторник, среда, четверг, пятница, суббота или воскресенье)
# является k-й день не високосного года, в котором 1 января является понедельником.
import datetime as dt, calendar, locale

d = dt.datetime(2018, 1, 1)
k = int(input())
delta = dt.timedelta(days=k - 1)
fd = (d + delta)

print(fd.weekday())  # где пН =1
print(fd.strftime('%A'))

f_weekday = calendar.weekday(fd.year, fd.month, fd.day)
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
f_name = calendar.day_name[f_weekday]
print(f'{f_name.lower()}')

import datetime

days = {1: 'понедельник', 2: 'вторник', 3: 'среда', 4: 'четверг', 5: 'пятница', 6: 'суббота', 0: 'воскресенье'}
k = int(input())
need = datetime.date(2006, 12, 31) + datetime.timedelta(days=k)
print(days[need.isoweekday()])

days = {1: 'понедельник', 2: 'вторник', 3: 'среда', 4: 'четверг', 5: 'пятница', 6: 'суббота', 0: 'воскресенье'}
k = int(input())
print(days[k % 7])

days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
n = int(input())
print(days[n % 7 - 1])

#########  4.3 ########
# 1. Вводится два вещественных числа, каждое с новой строки.
# Необходимо с помощью тернарного условного оператора наибольшее значение
# присвоить переменной d и вывести ее на экран.
print(max(input(), input()))

(lambda x, y: print(x if x > y else y))(float(input()), float(input()))
(lambda a, b: print(b if a <= b else a))(*[float(input()) for _ in 'ab'])
print(*[d1 if d1 > d2 else d2 for d1, d2 in [[float(input()) for _ in 'ab']]])

x, y = [float(input()) for _ in range(2)]  # "2 в скобках" - это количество переменных
d = x if x > y else y
print(d)

d = [float(input()) for i in range(2)]
print(d[0] if d[0] > d[1] else d[1])

# Подвиг 2. Вводится целое число. Необходимо переменной msg присвоить строку "кратно 3",
# если введенное число кратно 3, а иначе присвоить строку "не кратно 3".
# Реализовать программу с использованием тернарного оператора. Переменную msg отобразить на экране.

x = int(input())
msg = "кратно 3" if x % 3 == 0 else "не кратно 3"
print(msg)

print('не кратно 3' if int(input()) % 3 else 'кратно 3')

print(['не ', ''][int(input()) % 3 == 0] + 'кратно 3')

msg = 'не ' * (int(input()) % 3 != 0) + 'кратно 3'
print(msg)

print(f"{('не ', '')[not int(input()) % 3]}кратно 3")  # 0 если input%3==0 и not 0 = 1 (True)
print(not 0)

print(('кратно 3', 'не кратно 3', 'не кратно 3')[int(input()) % 3])

# Вводится слово. Переменной msg присвоить строку "палиндром",
# если введенное слово является палиндромом (одинаково читается и вперед и назад),
# а иначе присвоить строку "не палиндром". Проверку проводить без учета регистра.
# Программу реализовать с помощью тернарного условного оператора.
# Значение переменной msg отобразить на экране.
w = input().lower()
msg = 'палиндром'
print(msg if w == w[::-1] else "не палиндром")

a = input().lower()
print(f"{('не ', '')[a == a[::-1]]}палиндром")

msg = 'палиндром'
print((lambda w: msg if w == w[::-1] else "не" + msg)(input().lower()))

s = input().lower()
print(['не палиндром', 'палиндром'][s == s[::-1]])

# Вводится целое число 0 или 1. Необходимо преобразовать их в строки: 0 - в "False",
# 1 - в "True". Реализовать это с помощью тернарного условного оператора.
x = int(input())
print('False' if x == 0 else 'True')

print((lambda x: 'False' if x == 0 else 'True')(int(input())))

n = int(input())
print(bool(n))

print(True if int(input()) else False)  # любое число или символ - это то, что можно так
# сказать "пощупать", а значит правда, т.е. True. А вот ноль или '' - это пустое место,
# "ничего", т.е обратное от True, а значит ложь, т.е False. Или можно еще так объяснить:
# машинный язык понимает только единицы и нули. Они образуют булевые значения, True и False

print(input() == '1')

print(bool(int(input())))

print(["False", "True"][int(input())])

# Подвиг 5. Вводится текущее время (секунды) в диапазоне [0; 59]. Если значение равно 59,
# то следующее должно быть 0. И так по кругу.
# Необходимо  вычислить следующее значение с проверкой граничного значения 59.
x = int(input())
print(0 if x == 59 else x + 1)

x = int(input())
print((x + 1, 0)[x == 59])

n = int(input())
print((n + 1) % 60)

seconds = int(input())
a = (seconds % 60 + 1) % 60
print(a)

a = int(input())
d = (a + 1) * (a != 59)
print(d)

res = (time + 1) % 60

a = int(input())
v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
     10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
     20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
     30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
     40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
     50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
print(v[a - 59])

sec = int(input())
min = 59
t = sec % min - sec // min + 1
print(t)

n = int(input())
if n in range(0, 60):
    print((n + 1) % 60)

# Подвиг 6. Имеется список базовых нот:
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел.
# Необходимо отобразить указанные ноты в виде строки через пробел, но перед нотами до и фа
# дополнительно ставить символ диеза '#'.
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
x, y, z = map(int, input().split())
print('#' + m[x - 1] if m[x - 1] == 'до' or m[x - 1] == 'фа' else m[x - 1], end=' ')
print('#' + m[y - 1] if y == 1 or y == 4 else m[y - 1], end=' ')
print('#' + m[z - 1] if z == 1 or z == 4 else m[z - 1])

d1, d2, d3 = map(int, input().split())
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

print('#' + m[d1 - 1] if m[d1 - 1] in ['до', 'фа'] else m[d1 - 1],
      '#' + m[d2 - 1] if m[d2 - 1] in ['до', 'фа'] else m[d2 - 1],
      '#' + m[d3 - 1] if m[d3 - 1] in ['до', 'фа'] else m[d3 - 1])

m = ['#', 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
print(*['#' + m[i] if i in (1, 4) else m[i] for i in map(int, input().split())])

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())
nota_a = "#до" if a == 1 else ("#фа" if a == 4 else m[a - 1])
nota_b = "#до" if b == 1 else ("#фа" if b == 4 else m[b - 1])
nota_c = "#до" if c == 1 else ("#фа" if c == 4 else m[c - 1])
print(nota_a, nota_b, nota_c)

print(*(['#до', 'ре', 'ми', '#фа', 'соль', 'ля', 'си'][i - 1] for i in map(int, input().split())))

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a = list(map(int, input().split()))
print(*[('#' if m[a[i] - 1] == 'до' or m[a[i] - 1] == 'фа' else '') + m[a[i] - 1] for i in range(3)])

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

lst = map(int, input().split())
lst2 = []
for i in lst:
    lst2.append('#' + m[i - 1]) if m[i - 1] == 'до' or m[i - 1] == 'фа' else lst2.append(m[i - 1])
print(*lst2)

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a = map(int, input().split())
for i in a:
    print('#' + m[i - 1] if i in (1, 4) else m[i - 1], end=' ')

# генератор + ветвление
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
musical_notes = list(map(int, input().split()))
print(*['#' + m[musical_notes[i] - 1]
if m[musical_notes[i] - 1] in ['до', 'фа']
else m[musical_notes[i]-1]
for i in range(len(musical_notes))]
)

m =['#до', 'ре', 'ми', '#фа', 'соль', 'ля', 'си']
print( *[m[i-1] for i in list(map(int, input().split()))] )


########### 5.1 Оператор цикла while  ######
# Подвиг 2. Вводятся два целых положительных числа n и m, причем, n < m.
# Вывести в строку через пробел квадраты целых чисел в диапазоне [n; m].
n, m=map(int, input().split())
while n <= m:
    print(n ** 2, end=' ')
    n += 1

n, m = map(int, input().split())
l = []
while n <= m:
    l.append(n ** 2)
    n = n + 1
print(*l)

a, b = (int(_) for _ in input().split())
print(*[i ** 2 for i in range(a, b + 1)])
print(*(x ** 2 for x in range(*(lambda x, y: (x, y + 1))(*map(int, input().split())))))

# Подвиг 3. Вводится стоимость одной книги x рублей (вещественное число). Необходимо
# вывести на экран в строчку через пробел стоимости 2, 3, ... 10
# таких книг с точностью до десятых.
import numpy

x = float(input())
l = []
i = 2
while i <= 10:
    l.append(i * x)
    print(format(l[i - 2], '.3f'), end=' ')
    i += 1
print()
# Позволяет округлить до n-ого знака все элементы
# списка или numpy массива List. Требует импорта модуля numpy.
print(*(numpy.around(l, decimals=1)))

x = float(input())
l = []
i = 2
while i <= 10:
    l.append(round(i * x, 1))
    i += 1
print(*l)

x = float(input())
i = 2
while i <= 10:  # while i in range(1,11):
    print(round(i * x, 1), end=' ')
    i += 1

x, i = float(input()), 2
while i <= 10:
    print(f'{i * x:1}', end=' ')
    i += 1

# Подвиг 4. Вводится целое положительное число n. Вычислить и вывести на экран
# сумму: 1 + 1/2 + 1/3 + ... + 1/n с точностью до тысячных (три знака после запятой)
n = int(input())
i = 1
sum = 0
while i <= n:
    sum += 1 / i
    i += 1
print(f'{sum:.3f}')

from decimal import *

getcontext().prec = 11  # устанавливаем количество знаков после запятой
iter_number = 9  # сколько нужно человек, при заданной точности, чтобы бармен сказал "дурачье! и налил 2 пива"
counter = 2
sum = Decimal(1)
i = Decimal(2)
time = 1
while counter < iter_number:
    sum += 1 / i
    i = i * 2
    counter += 1
    print('time' + str(time) + ' = ' + str(sum))
    time += 1
print(sum)

n = int(input())
res = 0
while n > 0:
    res += 1 / n
    n -= 1
print(round(res, 3))

n = int(input())
sum = i = 1
while i < n:
    i += 1
    sum += 1 / i
print(round(sum, 3))

n, sm = int(input()), 0
while n:
    sm += 1 / n
    n -= 1
print(round(sm, 3))

# Подвиг 5. На каждой итерации цикла пользователь вводит целое число. Цикл продолжается,
# пока не встретится число 0.
# Необходимо вычислить сумму введенных в цикле чисел
sm, n = 0, int(input())  # sm=n=int(input())
while n != 0:
    sm += n
    n = int(input())
print(sm)

sm, n = 0, 1
while n != 0:  # while n:
    n = int(input())
    sm += n
print(sm)

sm = 0
while True:
    n = int(input())
    if n:
        sm += n
    else:
        break
print(sm)

print(sum(int(i) for i in iter(input, '0')))
print(sum(map(int, iter(input, '0'))))

# Подвиг 6. Вводится строка (слаг). Замените в этой строке все подряд идущие
# дефисы (--, ---, ---- и т.д.) на одинарные (-).
print(input().replace('--', '-').replace('---', '-'))

s = input()
while '--' in s:
    s = s.replace('--', '-')  # Просто str.replace('--','-') не изменяет исходную строку
    # str = str.replace - вот правильный подход
# Функция replace() в Python используется для создания строки путем замены некоторых
# частей другой строки. Исходная строка остается неизменной. Новая строка – это
# копия исходной строки, в которой все вхождения старой подстроки заменены на новую.
# Тут новое присваивание есть.# Результат исполнения replace записывается в ту же переменную.
print(s)

s = input()
while s.count('--') != 0:
    s = s.replace('--', '-')
print(s)

s = input()
while s.count('--'):  # Посчитывает количество вхождений символа/подстроки в строку. при -- =0 False
    s = s.replace('--', '-')
print(s)

s = input().replace('-', ' ').split()
print('-'.join(s))

print('-'.join(input().replace('-', ' ').split()))  # join Создает строку из списка строк. str.join(iterable)
# str - строка-разделитель,

s = input()
while '--' in s:
    s = '-'.join(s.split('--'))
print(s)

s, i = input(), 0
while i < len(s) - 1:
    if s[i] != '-' or s[i + 1] != '-':
        print(s[i], end='')
    i += 1
print(s[-1])

s = input()
i, ln = 0, len(s) - 1
while i < ln:
    i += 1
    if s[i] + s[i - 1] != '--':
        print(s[i], end='')

string = ''
for i in input():
    if i.isalpha():
        string += i
    else:
        string += " "
print('-'.join([i.strip() for i in string.split()]))

s = ''
for i in input():
    if i.isalpha():
        s += i
    else:
        s += ' '
print('-'.join(i.strip() for i in s.split()))

s = input()
i = 0
news = ''
while i <= len(s) - 1:
    news += ' ' if s[i] == '-' else s[i]
    i += 1
print(*news.split(), sep='-')

s = input()
while s.find('--') != -1:  # Метод возвращает -1, если символ или подстрока sub не найдены.
    s = s.replace('--', '-')
print(s)

s = input()
st = pre = ''
i = 0
while i < len(s):
    if s[i] != '-' or pre != '-':
        st += s[i]
        pre = s[i]
    i += 1
print(st)

# Подвиг 7. Вводится натуральное (то есть, целое положительное) число
# (от трехзначного и более). Найти произведение всех его цифр
n = int(input())
ss = 1
while n % i != 0:
    ost = n % 10
    ss *= ost
    n = n // 10
print(ss)

n = int(input())
ss = 1
while n:
    ss *= n % 10
    n //= 10
print(ss)

n, s = list(map(int, input())), 1
while n:
    s *= n.pop()
print(s)

# Подвиг 8. Последовательность Фибоначчи образуется так: первые два числа
# равны 1 и 1, а каждое последующее равно сумме двух предыдущих. Имеем
# такую последовательность чисел: 1, 1, 2, 3, 5, 8, 13, ...
# Постройте последовательность Фибоначчи длиной n (n вводится с клавиатуры)
n = int(input())
s1, s2 = 1, 1
print(s1, s2, end=' ')
while n > 2:
    s1, s2 = s2, s1 + s2
    print(s2, end=' ')
    n -= 1

n = int(input())
lst = [1, 1]
while len(lst) < n:
    lst.append(lst[-2] + lst[-1])
print(*lst[:n])

num = int(input())  # сколько цифр в масиве
fib = [1, 1]  # начало массива с числоми фибоначи
while len(fib) < num:  # пока количество чисел в массиве меньше введенного числа{num} цикл выполняется
    fib.append(sum(fib[-2:]))  # добавляем в конец массива  число равное сумме двух последних цифр массива
print(*fib)  # ответ) выводим все значения масcива через пробел без квадратных скобок и запятых

n = int(input())
a = b = count = 1
while count <= n:
    print(a)
    a, b = b, a + b
    count += 1

n, a, b = int(input()), 1, 1
while n:
    print(a, end=' ')
    a, b, n = b, a + b, n - 1

# Подвиг 9. Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить,
# сколько клеток будет через n часов (n - целое положительное число, вводимое с
# клавиатуры). Считать, что изначально была одна амеба. Результат вывести на экран.
n = int(input())
a = 1
h = 3
while h <= n:
    a *= 2
    h += 3
print(a)

n = int(input())
print(2 ** (n // 3))

# Подвиг 10. Гражданин 1 января открыл счет в банке, вложив 1000 руб.
# Каждый год размер вклада увеличивается на 5% от имеющейся суммы.
# Определить сумму вклада через n лет
n = int(input())
m = 1000
i = 0
while i != n:
    i += 1
    m += 0.05 * m
# print(format(m,'.2f'))
# print(f'{m:.2f}')
print(round(m, 2))  # раунд отбрасывает незначащие нули, формат - нет

n, m = int(input()), 1000
while n:
    m += 0.05 * m
    n -= 1
print(round(m, 2))

print(round(1000 * pow(1.05, int(input())), 2))

# Подвиг 11. Вводятся два натуральных четных числа n и m в одну строчку
# через пробел, причем n < m. Напечатать все нечетные числа из интервала [n, m].
n, m = map(int, input().split())
n += 1
while n < m:
    print(n, end=' ')
    n += 2

n, m = map(int, input().split())
while n < m:
    print(n + 1, end=' ')
    n += 2

n, m = map(int, input().split())
while n < m:
    while n % 2 != 0:
        print(n, end=' ')
        n += 1
    n += 1

n, m = map(int, input().split())
i = n | 1
while i < m:
    print(i, end=' ')
    i += 2

n, m = map(int, input().split())
lst = []
while n < m:
    n += 1
    lst.append(n)
print(*lst[::2])

# Подвиг 12. Составить программу поиска всех трехзначных чисел, которые при делении на
# 47 дают в остатке 43 и кратны 3. Вывести найденные числа в строчку через пробел
n = 100
while n // 100 < 10:
    if n % 47 == 43 and n % 3 == 0:
        print(n, end=' ')
    n += 1

i = 100
l = []
while i in range(100, 1000):
    if i % 47 == 43 and i % 3 == 0:
        l.append(i)
    i += 1
print(*l)

# 5.2 Операторы break, continue и else
# Подвиг 2. Имеется одномерный список длиной 10 элементов, состоящий из нулей:
# p = [0] * 10
# На каждой итерации цикла пользователь вводит целое число - индекс элемента списка p,
# по которому записывается значение 1, если ее там еще нет. Если же 1 уже проставлена,
# то список не менять и снова запросить у пользователя очередное число. Необходимо
# расставить так пять единиц в список
p = [0] * 10
s = 0
while sum(p) != 5:
    i = int(input())
    if p[i] == 0:
        p[i] = 1
        s += 1
    else:
        continue
print(*p)

p = [0] * 10
s = 0
while True:
    i = int(input())
    if p[i] == 0:
        p[i] = 1
        s += 1
    if s == 5:
        break
print(*p)

p = [0] * 10
while p.count(1) != 5:
    n = int(input())
    if p[n]:
        continue
    p[n] = 1
print(*p)

p = [0] * 10
while sum(p) != 5:
    p[int(input())] = 1
print(*p)

# Подвиг 3. На каждой итерации цикла вводится целое число. Необходимо подсчитать
# произведение только положительных чисел, до тех пор, пока не будет введено значение 0.
n = 1
s = 1
while n != 0:
    n = int(input())
    if n < 0:
        continue
    if n == 0:
        break
    s *= n
print(s)

n = 1
s = 1
while n:
    n = int(input())
    if n <= 0:
        continue
    s *= n
print(s)

# Подвиг 4. Вводится список названий городов в одну строчку через пробел. Определить
# , что в этом списке все города имеют длину более 5 символов. Реализовать
# программу с использованием цикла while и оператора break. Вывести ДА, если условие
# выполняется и НЕТ - в противном случае.
s = (input().split())
i = 0
while i < len(s):
    if len(s[i]) > 5:
        i += 1
    else:
        print('НЕТ')
        break
else:
    print('ДА')

s = (input().split())
if all(len(i) > 5 for i in s):
    print('ДА')
else:
    "НЕТ"

print(['ДА', 'НЕТ'][len(min((input()))) > 5])

print(['НЕТ', 'ДА'][all(map(lambda n: len(n) > 5, input().split()))])

s = (input().split())
while s:
    if len(s.pop()) < 5:
        print('нет')
        break
else:
    print('ДА')

# Подвиг 5. Вводится список имен студентов в одну строчку через пробел. Определить, что хотя
# бы одно имя в этом списке начинается и заканчивается на ту же самую букву
# (без учета регистра). Вывести ДА, если условие выполняется и НЕТ - в противном случае.
w = input().lower().split()
i = 0
while i < len(w):
    if w[i][0] == w[i][-1]:
        print('ДА')
        break
    i += 1
else:
    print('НЕТ')

w = [i.lower() for i in input().split()]
while w:
    w.pop()
    if w[0] == w[-1]:
        print('ДА')
        break
else:
    print('НЕТ')

print(['НЕТ', 'ДА'][any(map(lambda i: i[0] == i[-1], input().lower().split()))])

# Подвиг 6. Вводится натуральное число n (то есть, целое положительное). В цикле
# перебрать все целые числа в интервале [1; n] и сформировать список из чисел, кратных
# 3 и 5 одновременно. Вывести полученную последовательность чисел в виде строки через
# пробел, если значение n меньше 100. Иначе вывести на экран сообщение "слишком большое
# значение n" (без кавычек).
n = int(input())
i = 1
w = ''
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        w += str(i) + ' '
    i += 1
    if n > 99:
        print('слишком большое значение n')
        break
else:
    print(w)

n = int(input())
i = 1
while i < 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
    i += 1
    if i == n:
        break
else:
    print('слишком большое значение n')

n = int(input())
if n < 100:
    print(*range(15, n + 1, 15))
else:
    print('слишком большое значение n')

n = int(input())
i = 1
l = []
while i <= n:
    if n > 99:
        print('слишком большое значение n')
        break
    if i % 15 == 0:
        l.append(i)
    i += 15
else:
    print(*l)

n = int(input())
print(*range(15, n + 1, 15) if n < 100 else ['слишком большое значение n'])

# Подвиг 7. Вводится натуральное число n. Вывести первое найденное натуральное
# число (то есть, перебирать числа, начиная с 1), квадрат которого больше
# значения n
n = int(input())
i = 1
while True:
    if i ** 2 > n:
        print(i)
        break
    i += 1

print(int(int(input()) ** .5) + 1)

# Подвиг 8. (На использование цикла while). Начав тренировки, лыжник в первый
# день пробежал 10 км. Каждый следующий день он увеличивал пробег на 10 % от
# пробега предыдущего дня. Определить в какой день он пробежит больше x км
x = int(input())
d = 10
i = 1
while d < x:
    d += 0.1 * d
    i += 1
print(i)

# Подвиг 9. (На использование цикла while). Вводятся названия книг (каждое с новой строки).
# Удалить из введенного списка все названия, состоящие из двух и более слов (слова в
# названиях разделяются пробелом). Результат вывести на экран в виде строки из оставшихся
# названий через пробел.P. S. Для считывания списка целиком в программе уже записаны начальные строчки
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
i = 0
while i < len(lst_in):
    if ' ' in str(lst_in[i]):
        lst_in.pop(i)
        continue
    i += 1
print(*lst_in)

import sys  # для PyCharm прерывать ввод текста комбинацией Ctrl + D

lst_in = list(map(str.strip, sys.stdin.readlines()))
i = len(lst_in)
while i:
    i -= 1
    if lst_in[i].count(' '):
        del lst_in[i]
print(*lst_in)

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
i = 0
while i < len(lst_in):
    if ' ' not in str(lst_in[i]):
        print(*lst_in[i], end=' ')
    i += 1

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
print(*[n for n in lst_in if len(n.split()) < 2])  # == 1

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
i = 0
lst = []
while i < len(lst_in):
    if len(lst_in[i].split()) == 1:
        lst.append(lst_in[i])
    i += 1
print(*lst)

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
print(*[i for i in lst_in if ' ' not in i])

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
l = []
i = 0
while i < len(lst_in):
    if lst_in[i].find(' ') != -1:
        pass
    else:
        l.append(lst_in[i])
    i += 1
print(*l)

################# 5.3 Оператор цикла for и функция range
# Подвиг 2. С помощью функции range() сформируйте следующую последовательность
# чисел: 10, 9, 8, ..., 0
print(*reversed(range(11)))

print(*(range(11)[::-1]))

# Подвиг 3. С помощью функции range() сформируйте следующую последовательность
# чисел:-10, -8, -6, -4, -2
print(*range(-10, -1, 2))

print(*(range(-10, -1)[::2]))

# Подвиг 5. Вводятся целые числа в одну строчку через пробел. Необходимо
# преобразовать эти данные в список целых чисел. Затем, перебрать этот
# список в цикле for и просуммировать все нечетные значения.
# Результат вывести на экран.Sample Input:8 11 -2 4 0 13 19 12 7
n = list(map(int, input().split()))
s = 0
for i in n:
    if i % 2 != 0:
        s += i
print(s)

# №№№№№№№№№№№№№№№№####5.5 Итератор и итерируемые объекты. Функции iter и next


# Подвиг 3.
# Вводится строка. Нужно создать итератор для перебора символов этой
# строки. Затем, перебрать через созданный итератор все символы до первого пробела.
# В процессе перебора символы выводить на экран в одну строчку друг за другом
# (без пробелов). Гарантируется, что во введенной строке имеется хотя бы один
# пробел.Возможно-это будет полезно

s = input()
it = iter(s)
r = ''
while r != ' ':
    r = next(it)
    print(r, end='')

# Подвиг 4. Вводится четырехзначное целое положительное число. Подумайте, как можно
# определить итератор для перебора его цифр. Выведите цифры этого введенного числа
# (с помощью итератора) в одну строчку через пробел.
n = '4387'
it = iter(n)
for i in iter(n):
    print(next(it), end=' ')

n = '4387'
print(*n)

n = '4387'
it = iter(n)
i = next(it, '.')  # Если передать в функцию next второй аргумент, то он вернётся
# вместо ошибки.
while i != '.':
    print(i, end=' ')
    i = next(it, '.')

n = '4387'
it = iter(n)
print(next(it), next(it), next(it))

n = '4387'
it = iter(n)
while not 0:
    try:
        i = next(it)
        print(i, end=' ')
    except StopIteration:
        break

n = int('4387')
# n = int(input())  # берем именно целое число
flag, lst = True, []  # создает флаг выхода их цикла, и пустой список, куда будем класть цифры
while flag:
    if n // 10 == 0:  # если результат целочисленного деления на 10 равен нулю, прерываем цикл
        flag = False
    lst.append(n % 10)  # пока выше не равно нулю мы добаляем крайнюю правую цифру в список
    n = n // 10  # инкремент - способ выхода их цикла, мы реально целочисленно делим на 10
it = iter(lst[::-1])  # создаем итератор из от списка с конца (т.к. последняя цифра стояла 1-ой)

for i, v in enumerate(lst):  # пробегаемся по списку (а вдруг там не четырехзначное число)
    print(next(it), end=" ")  # печатаем цифры в строчку

n = ('4387')
print(*iter(n))

# Подвиг 1. Вводится натуральное число N (то есть, положительное, целое). Требуется создать двумерный
# (вложенный) список размером N x N элементов, состоящий из всех единиц, а затем, в последний
# столбец записать пятерки. Вывести этот список на экран в виде таблицы чисел,
n = 4
lst = [[1] * n for __ in range(n)]

N = int(input())
# N=4
for i in range(N):
    for j in range(N):
        if j == N - 1:
            print('5')
            continue
        print('1', end=' ')

n = 4
lst = [[1] * n] * n  # копируется ссылка на один и тот же список на первую строчку.
lst[3][n - 1] = 5  # поэтому не важно  какая строка lst[0] или lst[n-1]
for i in lst:
    print(*i)
lst[3][n - 1] = 2  # т к ссылка скопирована на один и тот же элемент то везде замена 5 на 2.
print(lst)

lst2 = [[1] * n for i in range(n)]  # То создаются отдельные списки.
print(lst2)

import copy

n = 4
lst = [[1] * n] * n
lst_2 = copy.copy(lst)
lst_3 = copy.deepcopy(lst)
lst_4 = lst_2[::]  # тоже мелкое копирование
lst[3][n - 1] = 5  # изменения не коснуться оригинала но замена будет во всех строках на 5
print(lst, id(lst))  # id все разные
print(lst_2, id(lst_2))
print(lst_3, id(lst_3))
print(lst_4, id(lst_4))

# создание 2-го списка
lst_3 = []
for i in range(3):
    lst_3.append([])
    for j in range(3):
        lst_3[i].append([])
print(lst_3)
lst_3[0][0] = 1
print(lst_3)

lst_3 = []
for i in range(n):
    lst_3.append([1] * n)

lst = []  # 3-х мерный список
for i in range(3):
    lst.append([])
    for j in range(3):
        lst[i].append([])
        for z in range(3):
            lst[i][j].append([])
print(lst)
lst[0][0][0] = 0
print(lst)

n = 3
lst_3 = []
for i in range(n):
    lst_3.append([1] * n)
for i in range(len(lst_3)):
    lst_3[i][len(lst_3) - 1] = 5
print(lst_3)

n = 3
lst_3 = []
for i in range(n):
    lst_3.append([1] * n)
for i in range(n):
    lst_3[i][-1] = 3
print(lst_3)

n = 3
lst_3 = []
for i in range(n):
    lst_3.append([1] * n)
for i in range(n):
    lst_3[i][-1] = 5

for i in range(len(lst_3)):
    for j in range(len(lst_3)):
        if j == [-1]:
            print(lst_3[i][j])
        else:
            print(lst_3[i][j], end=' ')
    print()

n = 3
lst_3 = []
for i in range(n):
    lst_3.append([1] * n)
for i in range(n):
    lst_3[i][-1] = 5

for i in lst_3:
    for j in i:
        if j == i[-1]:
            print(j, end='\n')
        else:
            print(j, end=' ')

n = 4
for i in range(n):
    r = []
    for j in range(n - 1):
        r.append(1)
    r.append(5)
    print(*r)

n = 4
lst = [[1] * n for __ in range(n)]
for i in lst:
    i[-1] = 5
[print(*i) for _ in lst]

n = 4
lst = []
for i in range(n):
    lst.append([1] * n)
    lst[i][-1] = 5
    print(*lst[i])

n = 4
lst = [[1] * (n - 1) + [5] for _ in range(n)]
[print(*i) for i in lst]

n = 4
lst = [[1] * n for _ in range(n)]
for i in range(n):
    lst[i][-1] = 5
    print(*lst[i])

# Подвиг 2. Вводится список из URL-адресов (каждый с новой строки). Требуется в них заменить все пробелы на символ
# дефиса (-). Следует учесть, что может быть несколько подряд идущих пробелов. Результат преобразования вывести на
# экран в виде строк из URL-адресов.
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
for i in lst_in:
    print('-'.join(i.split()))

import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
for i in lst_in:
    while '  ' in i:
        i = i.replace('  ', ' ')
    i = i.replace(' ', '-')
    print(i)

import sys, re

s = re.sub(r' +', '-', lst_in)
print(s)

lst_in = list(map(str.strip, sys.stdin.readlines()))
[print('-'.join(i.split()) for i in lst_in)]

# Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть,
# в диапазоне [2; n). Результат вывести на экран в строчку через пробел.
n = 11
for i in range(2, n):
    count = 0
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
        if count > 1:
            break
    if count == 1:
        print(i, end=' ')

n = 11
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')

n = 11
for i in range(2, n):
    for j in range(2, 1 + i // 2):  # i // 2 значительно ускоряет процесс
        if not (i % j):
            break
    else:
        print(i, end=' ')

num = int(input())
for i in range(2, num):
    if (i == 2 or i == 3 or i == 5) or (i % 2 != 0 and i % 3 != 0 and i % 5 != 0):
        print(i, end=' ')

n = 11
sieve = [0, 0] + [1] * (n - 2)
for i in range(2, int(n ** 0.5) + 1):
    if sieve[i]:
        # print(i) #
        for j in range(i * i, n, i):
            sieve[j] = 0
print(*(i for i, e in enumerate(sieve) if e))

from sympy import *

n = 11
print(*(i for i in range(2, n) if isprime(i)))

# Подвиг 4. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из нулей и, в некоторых позициях,
# единиц (см. пример ввода ниже). Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали
# и диагонали. То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести ДА, иначе - НЕТ.
# import sys
# считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
flag = True
for i in range(len(lst_in) - 1):
    for j in range(len(lst_in[i]) - 1):
        if lst_in[i][j]:
            if lst_in[i + 1][j] or lst_in[i][j - 1] or lst_in[i + 1][j + 1] or lst_in[i - 1][j + 1]:
                flag = False
                break
    if not flag:
        break
print('ДА' if flag else 'НЕТ')

st_in = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
flag = True
for i in range(len(lst_in)):
    for j in range(1, len(lst_in[i])):
        if lst_in[i][j - 1] == 1 and lst_in[i][j] == lst_in[i][j - 1]:
            flag = False
        elif lst_in[i][j] == 1 and lst_in[i][j] == lst_in[i][j - 1]:
            flag = False
#########################по диагонали
for i in range(1, len(lst_in)):
    for j in range(1, len(lst_in[i])):
        if lst_in[i - 1][j - 1] == 1 and lst_in[i][j] == lst_in[i - 1][j - 1] or lst_in[i][j] == 1 and \
                lst_in[i - 1][j - 1] == lst_in[i][j]:
            flag = False
# по вертикали переворачиваем строки на столбцы
for i in range(len(lst_in)):
    for j in range(i + 1, len(lst_in)):
        lst_in[i][j], lst_in[j][i] = lst_in[j][i], lst_in[i][j]

for i in range(len(lst_in)):
    for j in range(1, len(lst_in[i])):
        if lst_in[i][j - 1] == 1 and lst_in[i][j] == lst_in[i][j - 1]:
            flag = False
        elif lst_in[i][j] == 1 and lst_in[i][j] == lst_in[i][j - 1]:
            flag = False
if flag:
    print('ДА')
else:
    print('НЕТ')

lst_in = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
for i in range(len(lst_in) - 1):
    for j in range(len(lst_in) - 1):
        if lst_in[i][j] + lst_in[i][j + 1] + lst_in[i + 1][j] + lst_in[i + 1][j + 1] > 1:
            flag = False
        else:
            flag = True
if flag:
    print('ДА')
else:
    print('НЕТ')

lst_in = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

# складываем поэлементно соседние строки матрицы и создаём список из получившихся сумм.
s = []
for i in range(len(lst_in) - 1):
    for j in range(len(lst_in)):
        s.append(lst_in[i][j] + lst_in[i + 1][j])

# создаём строку из получившегося списка - в правильном списке не должно встречаться "2" и строк типа "11"
# (спаренных единиц).
a = ''.join(map(str, s))

# выводим через принт, создав кортеж из "ДА" и "НЕТ" и используя булево значение в качестве индекса (0 или 1) к
# данному кортежу из двух элементов.
print(('ДА', 'НЕТ')['2' in a or '11' in a])

lst_in = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
for i in range(len(lst_in) - 1):
    for j in range(len(lst_in) - 1):
        if lst_in[i][j] + lst_in[i + 1][j] + lst_in[i + 1][j + 1] + lst_in[i][j + 1] > 1:
            print('НЕТ')
            break  # выход из внутреннего цикла
    else:  # если выхода из внутреннего цикла не было по break прорускаем итерации
        continue
    break  # выход из внешнего цикца,т к сработала строка if lst_in[i][j] +....
else:
    print('ДА')

import sys
from itertools import product

mtx = [tuple(map(int, x.strip().split())) for x in sys.stdin.readlines()]
for i, j in product(range(len(mtx) - 1), repeat=2):
    if sum(mtx[i][j] for i, j in product((i, i + 1), (j, j + 1))) > 1:
        print('НЕТ')
        break
else:
    print('ДА')

for i in range(4):
    if any(sum((lst_in[i][j], lst_in[i][j + 1], lst_in[i + 1][j], lst_in[i + 1][j + 1])) > 1 for j in range(4)):
        print('НЕТ')
        break
else:
    print('ДА')

flag = 'ДА'  # не совсем верный вариант
for i in range(len(lst_in) - 1):
    for j in range(len(lst_in) - 1):
        if lst_in[i][j] == 1 and any((lst_in[i + 1][j], lst_in[i][j + 1], lst_in[i + 1][j + 1])):
            flag = 'НЕТ'
print(flag)

for i in range(len(lst_in) - 1):
    for j in range(len(lst_in) - 1):
        if lst_in[i][j] + lst_in[i + 1][j] + lst_in[i][j + 1] + lst_in[i + 1][j + 1] > 1:
            # print('НЕТ')
            sys.exit(print('НЕТ'))  # быстрый выход
print('ДА')

# Подвиг 5. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из целых чисел (пример ввода см. ниже).
# Проверьте, является ли этот двумерный список симметричным относительно главной диагонали. Главная диагональ — та,
# которая идёт из левого верхнего угла двумерного массива в правый нижний. Выведите на экран ДА, если матрица
# симметрична и НЕТ - в противном случае. P.S. Для считывания списка целиком в программе уже записаны начальные
# 2 3 4 5 6
# 3 2 7 8 9
# 4 7 2 0 4
# 5 8 0 2 1
# 6 9 4 1 2

# lst_in = [[2, 3, 4, 5, 6], [3, 2, 7, 8, 9], [4, 7, 2, 0, 4], [5, 8, 0, 2, 1], [6, 9, 4, 1, 2]]
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
# здесь продолжайте программу (используйте список lst_in)
for i in range(len(lst_in)):
    for j in range(len(lst_in[i])):
        if lst_in[i][j] != lst_in[j][i]:
            print('НЕТ')
            break
    else:
        continue
    break
else:
    print('ДА')

# Версия №3. Обход нижнего левого треугольника
import sys

lst_in = [list(map(int, x.strip().split())) for x in sys.stdin]
print(('НЕТ', 'ДА')[all(lst_in[i][j] == lst_in[j][i] for i in range(len(lst_in)) for j in range(i))])

print(('ДА', 'НЕТ')[any(lst_in[i][j] != lst_in[j][i] for i in range(len(lst_in)) for j in range(i))])

# по сути, как только мы получили первую ошибку, нам больше нет смысла проверять таблицу дальше, поэтому мы выходим не
# только из внутреннего цикла, но и из внешнего) то есть если итерация внутри прошла без ошибок, то срабатывает
# необязательный для цикла else и запускает continue, тем самым мы пропускаем break для внешнего цикла. А если же мы
# словили ошибку во внутреннем цикле и он завершился по break, то при выполнении блок else для внешнего цикла
# пропускается и запускает break)

# для тех, кто не понял, что значит zip(*mtx) . * это просто распаковка вложенного списка. Допустим, есть вложенный
# список martix = [['a','b','c'], ['d', 'e', 'g'], ['n', 'x', 'y']] . звездочка передает его в zip  в таком виде
# zip(['a','b','c'], ['d', 'e', 'g'], ['n', 'x', 'y']), т.е. просто без внешних скобок. Потом zip берет и компонует
# столбцы матрицы в строки. Т.е. вот так (('a', 'd', 'n'), ('b', 'e', 'x'), ('c', 'g', 'y')). А дальше, как было
# сказано, в транспонированной матрице (где столбцы стоят на месте строк) значения не меняются, если матрица симметрична.

# Решение с помощью транспонирования матрицы. В случае симметричной матрици, транспонированная матрица совпадает с
# оригиналом. Для транспонирования используется магия zip. В результате транспонирования функция zip создает
# строки-кортежи вместо строк-список, поэтому чтобы симметричные матрицы при сравнении совпали, мы сразу преобразуем
# каждую строку оригинальной матрицы в кортеж.
import sys

s = sys.stdin.readlines()
lst_in = [tuple(map(int, x.strip().split())) for x in s]
# lst_in = [(2, 3, 4, 5, 6), (3, 2, 7, 8, 9), (4, 7, 2, 0, 4), (5, 8, 0, 2, 1), (6, 9, 4, 1, 2)]
print(('НЕТ', 'ДА')[lst_in == [*zip(*lst_in)]])

import random

print(random.choices(['НЕТ', 'ДА'], k=1))  # выбирает несколько случайных элементов

# Версия №2. Проверяем матрицу на симметричность прямо во время считывания и формирования двумерного списка.
# Главная диагональ делит матрицу на верхний правый и нижний левый треугольники. Можно обходить нижний треугольник
# и проверять симметричность соотвествующих элементов в вверхнем треугольнике. Можно это делать прямо во время
# считывания данных, потому что, для каждого элемента нижнего треугольника выполняется следующее свойство:
# На момент считывания элемента нижнего треугольника, симметричный ему элеменент верхнего треугольника уже считан.
import sys

mtx = []
for i, l in enumerate(sys.stdin):
    mtx += [l.split()]
    if any(mtx[i][j] != mtx[j][i] for j in range(i)):
        print('НЕТ')
        break
else:
    print('ДА')

# Большой подвиг 6. Вводится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку выбором
# по возрастанию (неубыванию)
# Сортировка выбором

lst = list(map(int, input().split()))
# lst=[8, 11, -53, 2, 10, 11]
print(*sorted(lst))

l = [8, 11, -53, 2, 10, 11]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):  # Сортировка выбором
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

n = len(l)
for i in range(n - 1):
    ind = l.index(min(l[i:]), i, n)  # первое вхождение будет искаться после индекса i и перед индексом j
    l[i], l[ind] = l[ind], l[i]
print(*l)

l = [int(i) for i in input().split()]
for i in range(len(l) - 1):
    ind = min(range(i, len(l)), key=l.sort())
    l[i], l[ind] = l[ind], l[i]
print(*l)

lst = [int(i) for i in input().split()]
n = len(lst)
for i in range(n - 1):
    min_digit_index = min(range(i, n), key=lst.__getitem__)
    lst[i], lst[min_digit_index] = lst[min_digit_index], lst[i]
print(*lst)

n = len(lst)
for i in range(n - 1):
    ind, nmin = min(enumerate(lst[i:], i), key=lambda j: j[1])  # в качестве специальной функции сортировки передавать
    # lambda-функцию lambda x: x[1] которая из получаемых на каждом этапе кортежей (ключ, значение) будет брать для
    # сортировки второй элемент кортежа.
    lst[i], lst[ind] = nmin, lst[i]
print(*lst)

n = len(lst)
for i in range(n - 1):
    nm, ind = min((lst[j], j) for j in range(i, n))
    lst[i], lst[ind] = lst[ind], lst[i]
print(*lst)

# Большой подвиг 7. Вводится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку по
# возрастанию (неубыванию) методом всплывающего пузырька
# lst=list(map(int,input().split()))
l = [4, 5, 2, 0, 6, 3, -56, 3, -1]
# l=[int(i) for i in input().split()]

# Сортировка пузырьком (метод всплывающего пузырька)
for i in range(len(l) - 1):
    if l[i] > l[i + 1]:
        l[i], l[i + 1] = l[i + 1], l[i]
    for j in range(len(l) - 1 - i):  # т.к. мы после каждой итерации (первый цикл по i) в конце массива получаем уже
        # отсортированные числа и по ним алгоритм прогонять уже не нужно
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
print(*l)

# Подвиг 8. В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64. Вводится натуральное
# число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму n? Вывести на экран список купюр для
# формирования суммы n (в одну строчку через пробел, начиная с наибольшей и заканчивая наименьшей). Предполагается, что
# имеется достаточно большое количество купюр всех достоинств.
l = [64, 32, 16, 8, 4, 2, 1]
n = 221
n = int(input())
for i in range(len(l)):
    num = n // l[i]
    if num:
        print(f'{l[i]} ' * num, end='')
    n = n % l[i]

l = [64, 32, 16, 8, 4, 2, 1]
for i in l:
    while n >= i:
        print(i, end=' ')
        n -= i

l = [64, 32, 16, 8, 4, 2, 1]
n = int(input())
while n != 0:
    for i in range(6, -1, -1):  # идём в цикле от 2 ** 6 степени (64) до 2 ** 0 (1)
        while n >= 2 ** i:  # Пока n больше n ** i не переступаем в следующей цифры
            n -= 2 ** i  # вычитаем 2 ** i
            print(2 ** i, end=' ')  # печатаем 2 ** I и так по кругу. Если n не больше 2 ** i, то переходим
            # к следующей цифре. Уже 2 ** 5

l = [64, 32, 16, 8, 4, 2, 1]
n = 221
for i in l:
    a, n = divmod(n, i)
    print(f'{i} ' * a, end='')  # Функция divmod() возвращает кортеж, содержащий частное и остаток

l = [64, 32, 16, 8, 4, 2, 1]
n = 221
for i in l:
    while n // i > 0:
        print(i, end=' ')
        n -= i

# Треугольник Паскаля
row = [1]
for i in range(10):
    print(row)
    row = [sum(i) for i in zip([0] + row, row + [0])]

# Он возвращает:
[1]
[0, 1][1, 0]  # [0]+row, row+[0]) - формирует два списка, один сдвинут на одну позицию нулем слева, другой справа
[(0, 1), (1, 0)]
[1, 1]
[0, 1, 1][1, 1, 0]  # пример со 2й итерации): [0, 1, 1] [1, 1, 0]
[(0, 1), (1, 1), (1, 0)]  # zip([0]+row, row+[0]) - эта функция формирует кортежи из элементов с одинаковым индексом:
[1, 2, 1]
[0, 1, 2, 1][1, 2, 1, 0]
[(0, 1), (1, 2), (2, 1), (1, 0)]
[1, 3, 3, 1]
[0, 1, 3, 3, 1][1, 3, 3, 1, 0]
[(0, 1), (1, 3), (3, 3), (3, 1), (1, 0)]
[1, 4, 6, 4, 1]
[0, 1, 4, 6, 4, 1][1, 4, 6, 4, 1, 0]
[(0, 1), (1, 4), (4, 6), (6, 4), (4, 1), (1, 0)]
Чтопроисходит: zip([0] + row, row + [0]) - этафункция
формирует
кортеж
и
из
элементов
содинаковым
индексом: [(0, 1), (1, 1), (1, 0)]
[sum(x) for x in zip([0] + row, row + [0])] - списочноевыражение(илигенераторсписков, дальшепотеме), вычисляет
суммуэлементовкаждогокортежаидобавляетеевсписок: [1, 2, 1]
Теперьrow = [1, 2, 1]

# 5.8 Генераторы списков (List comprehension)
lst = [abs(i) for i in map(float, input().split())]
print(lst)

lst = [abs(float(i) for i in input().split())]

print(list(map(abs, map(float, input().split()))))

print(list(map(int, input())))

# Подвиг 3. Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером
# N x N, состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали
# от верхнего левого угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы чисел как показано в
# примере ниже.

N = 4
lst = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    lst[i][i] = 1
for i in range(N):
    print(*lst[i])

N = 4
lst = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

for i in lst:
    print(*i)
print(lst)

[print(*i) for i in lst]

lst = [[int(i == j) for i in range(N)] for j in range(N)]  # i == j дает булевый рез,int переводит его в числа 0 или 1.

N = 4
[print(*[int(i == j) for i in range(N)]) for j in range(N)]

# Подвиг 4. Вводятся названия городов в строку через пробел. Необходимо сформировать список с помощью list comprehension,
# содержащий названия длиной более пяти символов. Результат вывести в строчку через пробел.
[print(*[i for i in input().split() if len(i) > 5])]

print(*[i for i in input().split() if len(i) > 5])

print(*filter(lambda x: len(x) > 5, input().split()))

# Подвиг 5. Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension, состоящий из
# делителей числа n (включая и само число n). Результат вывести на экран в одну строку через пробел.
n = int(input())
print(*[i for i in range(1, n + 1) if n % i == 0])

n = int(input())
print(*[i for i in range(1, n // 2 + 1) if n % i == 0], n)

# можно не только использовать списки которые позволяют быстро добавлять элементы с обоих сторон, но и просто по первой
# половине списка выстроить вторую.
x = int(input())
t = [i for i in range(1, int(x ** .5) + 1) if x % i == 0]
print(*t, *[x // i for i in t[::-1]][x ** .5 % 1 == 0:])
# вторые квадратные скобочки t[::-1]][x**.5%1==0:] предназначены для того, чтобы предотвратить повторение одного и того
# же элемента в случае, когда число x является точным квадратом. Например, для x = 36:t = [1, 2, 3, 4, 6]
# t[::-1] => [6, 4, 3, 2, 1] Если ничего не предпринять то соотвествующий список делителей x // i будет тоже содержать
# число 6: [6, 9, 12, 18, 36] Мы можем исключить первый элемент развернутого списка t[::-1] с помощью среза:
# [6, 4, 3, 2, 1][1:] => [4, 3, 2, 1] Логическое выражение x**.5%1==0 проверяет является ли число x точным квадратом,
# а именно есть ли у вещественного квадратного корня из числа x значащие разряды после запятой.
# понятнее было бы то же самое решение записать так
n = int(input())
a = [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
b = [n // j for j in reversed(a) if n // j not in a]
print(*(a + b))

# Подвиг 6. Вводится натуральное число N. Необходимо сгенерировать вложенный список с помощью list comprehension,
# размером N x N, где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки и так до N-й
# строки. Результат вывести в виде таблицы чисел как показано в примере ниже.
N = int(input())
[print(*([i] * N)) for i in range(N)]

N = 4
[print(*[j for i in range(N)]) for j in range(N)]

# Подвиг 7. Вводится список вещественных чисел. С помощью list comprehension сформировать список, состоящий из элементов
# введенного списка, имеющих четные индексы (то есть, выбрать все элементы с четными индексами). Результат вывести на
# экран в одну строку через пробел.
lst = list(map(float, input().split()))
[print(lst[i], end=' ') for i in range(len(lst)) if i % 2 == 0]

[print(*[lst[i] for i in range(len(lst)) if i % 2 == 0])]

print(*list(map(float, input().split()[::2])))

[print(*[float(i) for i in input().split()[::2]])]

[print(*[float(v) for i, v in enumerate(input().split()) if not i % 2])]

# Подвиг 8. Вводятся два списка целых чисел одинаковой длины каждый с новой строки. С помощью list comprehension
# сформировать третий список, состоящий из суммы соответствующих пар чисел введенных списков. Результат вывести на
# экран в одну строку через пробел.

# lst_1=[int(i) for i in input().split()]
# lst_2=list(map(int,input().split()))
lst_1 = [1, 2, 3, 4, 5]
lst_2 = [6, 7, 8, 9, 10]
[print(lst_1[i] + lst_2[i], end=' ') for i in range(len(lst_1))]

print(*[int(i) + int(j) for i, j in zip(lst_1, lst_2)])

print(*map(sum, zip(lst_2, lst_1)))

print(*[sum(z) for z in zip(lst_1, lst_2)])  # zip Возвращаемое значение:итератор кортежей. (1,6)(2,7)..

print(*map(sum, zip(*(map(int, input().split()) for i in '11'))))

# Подвиг 9. Вводится список в формате: <город 1> <численность населения 1> <город 2> <численность населения 2> ...
# <город N> <численность населения N> Необходимо с помощью list comprehension сформировать список lst, содержащий
# вложенные списки из пар: <город> <численность населения> Численность населения - целое число в тыс. человек.
# вывести результат на экран в виде списка командой:print(lst)
# Москва 15000 Уфа 1200 Самара 1090 Казань 1300
# s = 'Москва 15000 Уфа 1200 Самара 1090 Казань 1300'.split()
s = input().split()
lst = [[s[i], int(s[i + 1])] for i in range(0, len(s) - 1, 2)]
print(lst)

s = 'Москва 15000 Уфа 1200 Самара 1090 Казань 1300'
it = iter(s.split())
lst = []
for v in it:
    lst.append([v, int(next(it))])
print(lst)

s = 'Москва 15000 Уфа 1200 Самара 1090 Казань 1300'
it = iter(s.split())
lst = [[i, int(next(it))] for i in it]
print(lst)

lst = [[i, int(next(it))] for it in [iter(s.split())] for i in it]
print(lst)

s = 'Москва 15000 Уфа 1200 Самара 1090 Казань 1300'
[print([[j[i], int(j[i + 1])] for i in range(len(j)) if i % 2 == 0]) for j in [s.split()]]

s = 'Москва 15000 Уфа 1200 Самара 1090 Казань 1300'
lst = [[[j[i], int(j[i + 1])] for i in range(len(j)) if i % 2 == 0] for j in [s.split()]]
print(*lst)

s = 'Москва 15000 Уфа 1200 Самара 1090 Казань 1300'.split()
lst = [[s[i], int(s[i + 1])] for i in range(len(s)) if i % 2 == 0]
print(lst)

# Подвиг 1. Вводится двумерный список в виде таблицы целых чисел (см. пример ниже). С помощью list comprehension
# преобразовать двумерный список в одномерный так, чтобы значения элементов шли в обратном порядке. Результат
# отобразить в виде строки из чисел, записанных через пробел.
import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
# lst_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
print(*[j for i in lst_in[::-1] for j in i[::-1]])  # вложенный цикл в генераторе списков обход по циклам справа на лево
print(*[[j for j in i[::-1]] for i in lst_in[::-1]])  # вложенный генератор в генераторе списков обход по циклам слева
# на направо в нутрь
print(*[j for i in lst_in for j in i][::-1])
print(*[j for i in lst_in for j in i].__reversed__())

import sys

print(*list(map(int, sys.stdin.read().split()))[::-1])

lst_in = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
l = [j for i in lst_in for j in i]
l.reverse()
print(*l)

[print(*i[::-1], end=' ') for i in lst_in[::-1]]

# Подвиг 2. Вводится список целых чисел в строку через пробел. С помощью list comprehension сформировать из них
# двумерный список lst размером N x N (квадратную таблицу чисел). Гарантируется, что из набора введенных чисел можно
# сформировать квадратную матрицу (таблицу). Результат отобразить в виде списка командой:

lst = list(map(int, input().split()))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
N = int(len(lst) ** .5)  # Гарантируется, что из набора введенных чисел можно сформировать квадратную матрицу (таблицу
it = iter(lst)  # итератор
it = (i for i in lst)  # выражение генератор 2-й вариант генерации
lst = [[next(it) for j in range(N)] for i in range(N)]
print(lst)

lst = [lst[i:i + N] for i in range(0, len(lst), N)]

lst = [lst[i * N: i * N + N] for i in range(N)]

print([[lst[N * i + j] for j in range(N)] for i in range(N)])

lst = [[lst.pop(0) for i in range(n)] for j in range(n)]

print([[lst[j] for j in range(i, i + n)] for i in range(0, len(lst), n)])

# Необходимо преобразовать его в двумерный (вложенный) список lst, где каждая строка представляется списком из слов
# (слова разделяются пробелом), но сохранять слова только длиной более трех символов.
import sys

t = ["– Скажи-ка, дядя, ведь не даром",
     "Я Python выучил с каналом",
     "Балакирев что раздавал?",
     "Ведь были ж заданья боевые,",
     "Да, говорят, еще какие!",
     "Недаром помнит вся Россия",
     "Как мы рубили их тогда!"
     ]
l = sys.stdin.readlines()
lst = [[j for j in i.split() if len(j) > 3] for i in l]
print(lst)

import re

lst = [re.findall(r'\b[\w\!\,\?\-]{4,}', i) for i in t]
print(lst)

# Подвиг 4. Повторите задачу с транспонированием прямоугольной матрицы с помощью list comprehension, изложенной в
# видео-уроке к этой практике. На вход поступает таблица целых чисел, на выходе нужно отобразить эту же таблицу в
# транспонированном виде (строки заменяются на столбцы), используя команду:

# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]
A = [[lst_in[j][i] for j in range(len(lst_in))] for i in range(len(lst_in[0]))]
for row in A:
    print(*row)

A = [[j[i] for j in lst_in] for i in range(len(lst_in[0]))]

for i in zip(*lst_in):
    print(*i)

import numpy as np

lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]
A = np.array(lst_in).T
for row in A:
    print(*row)

################  https://habr.com/ru/post/320288/

# с тернарным оператором
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x ** 3 if x < 0 else x ** 2 for x in list_a if x % 2 == 0]
# вначале фильтр пропускает в выражение только четные значения
# после этого ветвление в выражении для отрицательных возводит в куб, а для остальных в квадрат
print(list_b)  # [-8, 0, 4, 16]

# Генерация строк
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
# используем генератор прямо в .join() одновременно приводя элементы к строковому типу
my_str = ' '.join(str(i) for i in list_a)
print(my_str)  # -2-1012345

# Периодичность и частичный перебор
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_e = [x for i, x in enumerate(list_a, 1) if i % 3 == 0]
print(list_e)  # [0, 3]

# частичный перебор
import itertools

first_ten = itertools.islice((i for i in range(10000000000) if i % 2 == 0), 10)  # 10-stop
first_ten = (i for i in range(100) if i % 2 == 0 and i < 5 * 2)  # аналогично но дольше тк обходит весь диапозон 100
print(*first_ten)

# генератор dict
# 7.1.1 Вложенные циклы for где циклы идут по независимым итераторам
# Общий синтаксис: [expression for x in iter1 for y in iter2]
rows = 1, 2, 3, -4, -5
cols = 'a', 'b', 'abc'
# Для наглядности разнесем на несколько строк
my_dict = {
    (col, row): 0  # каждый элемент состоит из ключа-кортежа и нулевого знаечния
    for row in rows if row > 0  # Только положительные значения
    for col in cols if len(col) == 1  # Только односимвольные
}
print(my_dict)  # {('a', 1): 0, ('b', 1): 0, ('a', 2): 0, ('b', 2): 0, ('a', 3): 0, ('b', 3): 0}

# Генератор итерирующийся по генератору
list_c = [x ** 2 for x in [x for x in range(-2, 4)]]
print(list_c)  # [4, 1, 0, 1, 4, 9]

# Последовательный проход по нескольким спискам
import itertools

l1 = [1, 2, 3]
l2 = [10, 20, 30]
result = [l * 2 for l in itertools.chain(l1, l2)]
print(result)  # [2, 4, 6, 20, 40, 60]

# Задача выбора только рабочих дней
# Формируем список дней от 1 до 31 с которым будем работать
days = [d for d in range(1, 32)]

# Делим список дней на недели
weeks = [days[i:i + 7] for i in range(0, len(days), 7)]
print(weeks)  # [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26,
# 27, 28], [29, 30, 31]]

# Выбираем в каждой неделе только первые 5 рабочих дней, отбрасывая остальные
work_weeks = [week[0:5] for week in weeks]
print(work_weeks)  # [[1, 2, 3, 4, 5], [8, 9, 10, 11, 12], [15, 16, 17, 18, 19], [22, 23, 24, 25, 26], [29, 30, 31]]

# Если нужно одним списком дней - можно объединить
wdays = [item for sublist in work_weeks for item in sublist]
print(wdays)  # [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 29, 30, 31]
print(len(wdays))

# 2-ой авриант
# Формируем список дней от 1 до 31 с которым будем работать
days = [d for d in range(1, 32)]
print(days)
wdays6 = [wd for (i, wd) in enumerate(days, 1) if i % 7 != 0]  # Удаляем каждый 7-й день
# Удаляем каждый 6 день в оставшихся после первого удаления:
wdays5 = [wd for (i, wd) in enumerate(wdays6, 1) if i % 6 != 0]
print(wdays5)
# [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 29, 30, 31]
# Обратите внимание, что просто объединить два условия в одном if не получится,
# как минимум потому, что 12-й день делится на 6, но не выпадает на последний 2 дня недели!
days = [d + 1 for d in range(31) if d % 7 < 5]
print(days)
