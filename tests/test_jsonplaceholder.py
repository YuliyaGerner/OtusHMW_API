"""Тесты методов api сайта https://jsonplaceholder.typicode.com"""

class TestJsonPlaceHolder:
    """Класс для тестирования методов api сайта https://jsonplaceholder.typicode.com"""

    def test_check_post_list(self, response_post_list):
        """Проверка наличия списка постов"""
        assert response_post_list != []
        print(response_post_list)

    def test_check_post_status(self, response_post_status):
        """Проверка кода успешности ответа от полуения списка постов"""
        assert response_post_status == 200
        print(response_post_status)

    def test_check_post_by_id(self, response_post_by_id):
        """Проверка наличия поста по выбранному id"""
        assert response_post_by_id != []
        print(response_post_by_id)

    def test_check_post_comments_by_id(self, response_post_comments_by_id):
        """Проверка наличия комментария поста по выбранному id"""
        assert response_post_comments_by_id != []
        print(response_post_comments_by_id)

    def test_check_albums_photos_by_id(self, response_albums_photos_by_id):
        """Проверка наличия фотографий поста по выбранному id"""
        assert response_albums_photos_by_id != []
        print(response_albums_photos_by_id)