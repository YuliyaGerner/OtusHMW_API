"""Тесты методов api сайта https://dog.ceo/api"""

class TestDogAPI:
    """Класс для тестирования методов api сайта https://dog.ceo/api"""

    def test_check_answer_text(self, response_status_random_dog_image):
        """Проверка статуса успешности ответа сервера
        для запроса произвольно выбранного изображения собаки"""
        assert response_status_random_dog_image == 'success'
        print(response_status_random_dog_image)

    def test_check_status_code(self, random_dog_status):
        """Проверка кода успешности ответа сервера
        для запроса произвольно выбранного изображения собаки"""
        assert random_dog_status == 200
        print(random_dog_status)

    def test_dog_list_sub_breeds_status(self, dog_breed):
        """Проверка текста успешности ответа сервера
        для запроса наличия потомков породы собаки"""
        assert dog_breed == "success"
        print(dog_breed)

    def test_dog_breeds_images(self, dog_random_breed_image):
        """Проверка наличия произвольного изображения,
         выбранной породы собаки"""
        assert dog_random_breed_image['message'] is not None
        print(dog_random_breed_image)

    def test_incorrect_dog_breeds_images(self, incorrect_dog_breed_image):
        """Проверка отсутствия какого-либо изображения,
         неккоретно выбранной породы собаки"""
        assert incorrect_dog_breed_image['message'] == "Breed is not found (master breed does not exist)"
        print(incorrect_dog_breed_image)