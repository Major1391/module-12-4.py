import logging
import unittest
from rt_with_exeptions import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            v_test = Runner('Djo', speed=-100)
            for i in range(10):
                v_test.walk()
            self.assertEqual(v_test.distance, 50)
            logging.info('Тест "test_walk" выполнен успешно')
        except ValueError:
            logging.warning(msg='Неверная скорость для Runner',exc_info=True)

    def test_run(self):
        try:
            v_test = Runner(333)
            for i in range(10):
                v_test.run()
            self.assertEqual(v_test.distance, 100)
            logging.info('Тест "test_run" выполнен успешно')
        except TypeError:
            logging.warning(msg="Неверный тип данных для обьекта Runner", exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
    unittest.main()
