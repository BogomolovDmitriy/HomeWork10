# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
#  (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) 
#  для всех значений предикат.

my_list = [1, 2, 3]

if not (my_list[0] or my_list[1] or my_list[2]) == \
    ((not my_list[0]) and (not my_list[1]) and (not my_list[2])):
    print(True)
else:
    print(False)
