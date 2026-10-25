Feature: Калькулятор
  Как пользователь
  Я хочу использовать калькулятор
  Чтобы выполнять арифметические операции

  Background:
    Given у меня есть калькулятор

  Scenario: Сложение
    When я складываю 2 и 3
    Then результат равен 5

  Scenario: Деление на ноль
    When я делю 10 на 0
    Then результат равен "Ошибка: деление на ноль"

  Scenario Outline: Проверка разных операций
    When я выполняю "<operation>" над <a> и <b>
    Then результат равен <expected>

    Examples:
      | operation | a  | b | expected |
      | add       | 2  | 3 | 5        |
      | sub       | 10 | 4 | 6        |
      | mul       | 3  | 4 | 12       |
      | div       | 10 | 2 | 5        |