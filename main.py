def calculate(first_number, operation, second_number):
    """Выполняет математическую операцию и возвращает результат."""
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            raise ZeroDivisionError("На ноль делить нельзя.")
        return first_number / second_number
    elif operation == "//":
        if second_number == 0:
            raise ZeroDivisionError("На ноль делить нельзя.")
        return first_number // second_number
    else:
        raise ValueError(
            "Неизвестная операция. Используйте +, -, *, / или //."
        )

def read_number(prompt):
    """Запрашивает число, повторяя ввод при ошибке."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Ошибка: введите корректное число.")


def ask_continue():
    """Спрашивает, нужно ли продолжить вычисления."""
    while True:
        answer = input("Хотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
        if answer in ("да", "д", "yes", "y"):
            return True
        if answer in ("нет", "н", "no", "n"):
            return False
        print("Пожалуйста, ответьте «да» или «нет».")


def main():
    print("Консольный калькулятор")
    print("Поддерживаемые операции: +, -, *, /")

    while True:
        first_number = read_number("Введите первое число: ")
        operation = input("Введите операцию (+, -, *, /): ").strip()
        second_number = read_number("Введите второе число: ")

        try:
            result = calculate(first_number, operation, second_number)
            print(f"Результат: {result:g}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"Ошибка: {error}")

        if not ask_continue():
            print("Работа программы завершена.")
            break
        print()


if __name__ == "__main__":
    main()
