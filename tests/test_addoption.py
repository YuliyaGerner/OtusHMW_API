import requests

def test_answer_status_code(url_param):
    """Проверка на корректность ответа по заданному аргументу командной строки"""
    response = requests.get(url_param).status_code
    assert response == 200
    print(response)