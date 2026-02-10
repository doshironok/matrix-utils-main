from utils.diagonal_sum import diagonal_sums
from utils.determinant import determinant
from utils.min_element import find_min

def input_matrix():
    n = int(input("Введите N (строки): "))
    m = int(input("Введите M (столбцы): "))
    print("Введите матрицу построчно (через пробел):")
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        if len(row) != m:
            raise ValueError("Неверное количество элементов в строке")
        matrix.append(row)
    return matrix

def main():
    print("Выберите задачу:")
    print("1. Сумма диагоналей")
    print("2. Определитель")
    print("3. Минимальный элемент")
    choice = input("Ваш выбор: ")
    matrix = input_matrix()

    try:
        if choice == "1":
            main_sum, anti_sum = diagonal_sums(matrix)
            print(f"Главная диагональ: {main_sum}, Побочная: {anti_sum}")
        elif choice == "2":
            det = determinant(matrix)
            print(f"Определитель: {det}")
        elif choice == "3":
            val, i, j = find_min(matrix)
            print(f"Минимум: {val} на позиции [{i}][{j}]")
        else:
            print("Неверный выбор")
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()