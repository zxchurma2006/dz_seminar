def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi
def interpret_bmi(bmi):
    if bmi < 16.0:
        return "Тяжелое недоедание"
    elif 16.0 <= bmi < 17.0:
        return "Умеренное недоедание"
    elif 17.0 <= bmi < 18.5:
        return "Легкое недоедание"
    elif 18.5 <= bmi < 26.0:
        return "Нормальное положение (вес в норме)"
    elif 26.0 <= bmi < 31.0:
        return "Избыточная масса тела"
    elif 31.0 <= bmi < 43.0:
        return "Ожирение (I степень)"
    elif 43.0 <= bmi < 54.0:
        return "Ожирение (II степень)"
    else:
        return "Ожирение (III степень)"
def main():
    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(input("Введите ваш рост в метрах: "))

    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)

    print(f"Ваш ИМТ: {bmi:.2f}")
    print(f"Интерпретация: {interpretation}")


if __name__ == "__main__":
    main()
