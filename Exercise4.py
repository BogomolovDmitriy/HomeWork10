# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

list_dotA = []
list_dotB = []
list_dotA.append(int(input("Введите координату X первой точки: ")))
list_dotA.append(int(input("Введите координату Y первой точки: ")))
list_dotB.append(int(input("Введите координату X второй точки: ")))
list_dotB.append(int(input("Введите координату Y второй точки: ")))

distance = round((((list_dotB[0] - list_dotA[0]) ** 2 + (list_dotB[1] - list_dotA[1]) **2) ** (0.5)), 3)

print(f"Расстояние  между заданными точками = {distance}")