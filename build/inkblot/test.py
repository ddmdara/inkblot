import unittest
import io
import sys
from inkblot import main  # Импортируем функцию, где реализован ваш код Inkblot на Python

class TestInkblot(unittest.TestCase):
    def test_output_matches_expected(self):
        # Перенаправляем stdout в буфер для захвата вывода программы
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Запускаем функцию Inkblot
        main()

        # Возвращаем стандартный stdout
        sys.stdout = sys.__stdout__

        # Получаем результат программы
        output = captured_output.getvalue()

        # Загружаем эталонный лог
        with open("expected_log.txt", "r") as file:
            expected_output = file.read()

        # Сравниваем вывод программы с эталонным
        self.assertEqual(output.strip(), expected_output.strip())

if __name__ == "__main__":
    unittest.main()
