def add(a, b):
  return a + b


def sub(a, b):
  return a - b


def mul(a, b):
  return a * b


def div(a, b):
  return a / b


def calc():
  result = float(input("Введите число: "))

  while True:
    op = input("Оператор (+, -, *, /), '=' (выход) или ')' (конец скобок): ")

    if op in ("=", ")"):
      return result

    val_input = input("Введите число или '(' для вложенных скобок: ")
    if val_input == "(":
      num = calc()
    else:
      num = float(val_input)

    if op == "+":
      result = add(result, num)
    elif op == "-":
      result = sub(result, num)
    elif op == "*":
      result = mul(result, num)
    elif op == "/":
      result = div(result, num)
    else:
      print("Неверный оператор!")
      continue

    print(f"= {result}")


print(f"Итоговый результат: {calc()}")