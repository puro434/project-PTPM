from behave import given, when, then

# Простой класс калькулятора
class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b):
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b

@given("у меня есть калькулятор")
def step_impl(context):
    context.calc = Calculator()

@when("я складываю {a:d} и {b:d}")
def step_impl(context, a, b):
    context.result = context.calc.add(a, b)

@when("я делю {a:d} на {b:d}")
def step_impl(context, a, b):
    context.result = context.calc.div(a, b)

@when('я выполняю "{operation}" над {a:d} и {b:d}')
def step_impl(context, operation, a, b):
    # Вызываем нужный метод в зависимости от operation (add, sub, mul, div)
    method = getattr(context.calc, operation)
    context.result = method(a, b)

@then("результат равен {expected:d}")
def step_impl(context, expected):
    assert context.result == expected

@then('результат равен "{expected}"')
def step_impl(context, expected):
    assert context.result == expected