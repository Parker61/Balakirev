lst_in = ['Номер;Имя;Оценка;Зачет', '1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет",
          '5;Балакирев;1;Нет']
# таблица на выводе должна быть такой:
# (('Имя', 'Зачет', 'Оценка', 'Номер'), ('Портос', 'Да', 5, 1), ('Арамис', 'Да', 3, 2), ('Атос', 'Да', 4, 3),
# ("д'Артаньян", 'Нет', 2, 4), ('Балакирев', 'Нет', 1, 5))

# example=  Имя;Зачет;Оценка;Номер
# t = tuple(tuple(int(st) if st.isdigit() else st for st in row.split(";")) for row in lst_in)
t = tuple(tuple(int(j) if j.isdigit() else j for j in i.split(';')) for i in lst_in)
print(t)
order = "Имя;Зачет;Оценка;Номер"
# t_sorted = tuple(zip(*sorted(list(zip(*t)), key=lambda x: order.find(x[0]))))
t_sorted = tuple(zip(*sorted(zip(*t), key=lambda x: order.find(x[0]))))
print(t_sorted)
