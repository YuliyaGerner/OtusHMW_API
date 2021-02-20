import requests, pytest


#url произвольного изображения породы собаки
random_image_url = "https://dog.ceo/api/breeds/image/random"
#url породы собаки
concrete_breed_url = "https://dog.ceo/api/breed/"
#url базы пивоварен
openbrewery = "https://api.openbrewerydb.org/"
#url списка постов
jsonplaceholder = "https://jsonplaceholder.typicode.com/posts/"

@pytest.fixture()
def response_status_random_dog_image():
    """Фикстура возвращает статус ответа
    получения произвольного изображения собаки"""
    response = requests.get(random_image_url).json().get("status")
    return response

@pytest.fixture()
def random_dog_status():
    """Фикстура возвращает код ответа
    получения произвольного изображения собаки"""
    response = requests.get(random_image_url).status_code
    return response

@pytest.fixture(params=["labrador", "bulldog", "affenpinscher"])
def dog_breed(request):
    """Фикстура возвращает статус ответа
    получения потомка породы собаки"""
    response = requests.get(concrete_breed_url + f'{request.param}/list').json()['status']
    print(response)
    return response

@pytest.fixture(params=["hound", "labrador", "affenpinscher"])
def dog_random_breed_image(request):
    """Фикстура возвращает результат
    запроса получения произвольного изображения породы собаки"""
    response = requests.get(concrete_breed_url + f'{request.param}/images/random').json()
    return response

@pytest.fixture(params=["houn", "labr", "afenpinscher"])
def incorrect_dog_breed_image(request):
    """Фикстура возвращает результат
    запроса получения изображения некорректной породы собаки"""
    response = requests.get(concrete_breed_url + f'{request.param}/images/random').json()
    return response

@pytest.fixture()
def response_brewery_list():
    """Фикстура возвращает результат
    запроса получения списка пивоварен"""
    response = requests.get(openbrewery + f'breweries').json()
    return response

@pytest.fixture()
def response_brewery_status():
    """Фикстура возвращает результат
    запроса получения статуса ответа списка пивоварен """
    response = requests.get(openbrewery + f'breweries').status_code
    return response

@pytest.fixture(params=[{"by_state":"new_york"}])
def response_brewery_by_state(request):
    """Фикстура возвращает результат
    запроса получения списка пивоварен, выбранных по региону"""
    response = requests.get(openbrewery + f'breweries', params=request.param).json()
    return response

@pytest.fixture(params=[{"by_name":"Yellowhammer Brewery"}])
def response_brewery_by_name(request):
    """Фикстура возвращает результат
    запроса получения списка пивоварен, выбранных по названию пивоварни"""
    response = requests.get(openbrewery + f'breweries', params=request.param).json()
    return response

@pytest.fixture(params=[{"by_type":"brewpub"}])
def response_brewery_by_type(request):
    """Фикстура возвращает результат
    запроса получения списка пивоварен, выбранных по типу"""
    response = requests.get(openbrewery + f'breweries', params=request.param).json()
    return response

@pytest.fixture()
def response_post_list():
    """Фикстура возвращает результат
    запроса получения списка постов"""
    response = requests.get(jsonplaceholder).json()
    return response

@pytest.fixture()
def response_post_status():
    """Фикстура возвращает результат
    запроса получения статуса ответа списка постов"""
    response = requests.get(jsonplaceholder).status_code
    return response

@pytest.fixture(params=[1, 2, 3])
def response_post_by_id(request):
    """Фикстура возвращает результат
    запроса получения поста, выбранного по id"""
    response = requests.get(jsonplaceholder + f'{request.param}').json()
    return response

@pytest.fixture(params=[1, 2, 3])
def response_post_comments_by_id(request):
    """Фикстура возвращает результат
    запроса получения комментария поста, выбранного по id"""
    response = requests.get(jsonplaceholder + f'{request.param}/comments').json()
    return response

@pytest.fixture(params=[1, 2, 3])
def response_albums_photos_by_id(request):
    """Фикстура возвращает результат
    запроса получения фотографии, выбранной по id"""
    response = requests.get(jsonplaceholder + f'/albums/{request.param}/photos').json()
    return response

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url",
        required=False
    )

@pytest.fixture()
def url_param(request):
    """Фикстура возвращает результат запроса аргумента командной строки"""
    return request.config.getoption("--url")