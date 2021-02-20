"""Тесты методов api сайта https://api.openbrewerydb.org/"""


class TestBreweryDb:
    """Класс для тестирования методов api сайта https://api.openbrewerydb.org/"""

    def test_check_brewery_list(self, response_brewery_list):
        """Проверка наличия списка пивоварен"""
        assert response_brewery_list != []
        print(response_brewery_list)

    def test_check_brewery_response_status(self, response_brewery_status):
        """Проверка кода успешности ответа при получении списка пиоварен """
        assert response_brewery_status == 200
        print(response_brewery_status)

    def test_check_brewery_by_state(self, response_brewery_by_state):
        """Проверка наличия пивоварен по выбранному штату"""
        assert response_brewery_by_state != []
        assert response_brewery_by_state[0]['state'] == "New York"
        print(response_brewery_by_state)

    def test_check_brewery_by_name(self, response_brewery_by_name):
        """Проверка по выбранному имени"""
        assert response_brewery_by_name != []
        assert response_brewery_by_name[0]['name'] == "Yellowhammer Brewery"
        print(response_brewery_by_name)

    def test_check_brewery_by_type(self, response_brewery_by_type):
        """Проверка по выбранному типу"""
        assert response_brewery_by_type != []
        assert response_brewery_by_type[0]['by_type'] == "planning"
        print(response_brewery_by_type)
