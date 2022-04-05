import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Авторизациящ на сайте http://petfriends1.herokuapp.com/login и выход на главную страницу
def test_log_in_and_show_all_pets():
#Вводим данные для авторизации
    pytest.driver.find_element_by_id('email').send_keys('testling@test.test')
    pytest.driver.find_element_by_id('pass').send_keys('123123')
#Выполняем вход нажатием кнопки
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
#Проверяем, что попали на главную страницу
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
#Переходим в раздел "Мои питомцы"
    pytest.driver.find_element_by_css_selector('.nav-link[href="/my_pets"]').click()
#Проверяем, что перешли к списку питомцев на странице пользователя
    assert pytest.driver.find_element_by_tag_name('h2').text == "Testling"

#Проверка карточек питомцев "my pets". (ЗАДАНИЕ 1) Неявные ожидания всех элементов (фото, имя питомца, его возраст).
def test_data_of_my_pets():
    pytest.driver.find_element_by_id('email').send_keys('testling@test.test')
    pytest.driver.find_element_by_id('pass').send_keys('123123')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    pytest.driver.find_element_by_css_selector('.nav-link[href="/my_pets"]').click()
#Добавляем неявное ожидание
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

#Проверка таблицы питомцев "my pets". (ЗАДАНИЕ 2) Добавить явные ожидания элементов страницы.
def test_all_pets_are_present():
    pytest.driver.find_element_by_id('email').send_keys('testling@test.test')
    pytest.driver.find_element_by_id('pass').send_keys('123123')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    pytest.driver.find_element_by_css_selector('.nav-link[href="/my_pets"]').click()
#Добавляем явное ожидание появления элементов списка питомцев
    pytest.driver.element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ('//tbody/tr'))))
    my_pets = len(pytest.driver.find_elements_by_xpath('//tbody/tr'))
    # количество питомцев в статистике
    my_pets_are_all_present = pytest.driver.find_element_by_xpath('//*[h2][1]').text.split()
    assert my_pets_are_all_present[2] == str(my_pets)

