import time
from googletrans import Translator, constants
from selenium.webdriver.common.by import By


def change_using(driver, element_name, ):
    """
    Метод перехода по ссылкам
    :param element_name: имя селектора
    :param driver:
    :return:
    """

    find_elements = driver.find_elements(By.CSS_SELECTOR, element_name)

    return find_elements


def next_page(items_elemts: list, find_element: str, deleted_text: str):
    """
    Функция перехода на следущую страницу и поиска необоходимых элементов в ней
    :param items_elemts:  элементы на страницк
    :param find_element:  какой элемент ищем
    :param deleted_text:  что нужно убрать их текста
    :return:
    """
    read_files = []
    for item in items_elemts:
        for items2 in item.find_elements(By.CSS_SELECTOR, find_element):
            if len(items2.text) <= 0 or items2.text == deleted_text:
                read_files.append("")
            else:
                read_files.append(items2.text)
    return read_files


def test(url, driver, type_list):
    """
    Функция тестирования  парсера и дальнейщего запуска
    :param drivers:
    :return:
    """
    translator = Translator()
    read_files = []
    json_dictionary = {}
    key = []
    value = []
    all_dictonary = []
    other_list = []
    page_number = 0
    time.sleep(5)
    button = driver.execute_script(" return document.querySelector('#MainContent_ucComfirmButton_btnSure')")
    button.click()
    time.sleep(10)
    while page_number < 1:
        list_data = change_using(driver, "#MainContent_ucAlertList_rptAlert_lbtnMore_0")
        list_data[0].click()
        time.sleep(5)
        data_key = driver.find_elements(By.CSS_SELECTOR, ".register p label")
        print("len key", len(data_key))
        data_value = driver.find_elements(By.CSS_SELECTOR, ".register p font")
        print("len value", len(data_value))

        for i in range(len(data_key)):
            translators_key = translator.translate(data_key[i].text, dest="ru")
            translators_value = translator.translate(data_value[i].text, dest="ru")
            key.append(translators_key.text)
            if translators_value:
                if i == 4:
                    other_list.append(translators_value.text.split(":"))
                    for other in range(len(other_list)):
                        print(other_list[other][2].split("\n"))

                value.append(translators_value.text)

            else:
                value.append("null")

        count = 0
        print(len(key))
        print(len(value))
        # chek = len(key)
        #
        for s in range(len(key)):

            if count != len(key):
                count += 1
                json_dictionary[key[s]] = value[s]

                if count == len(key):
                    json_dictionary['type'] = type_list
                    json_dictionary['source'] = url
                    all_dictonary.append(json_dictionary)
                    json_dictionary = {}
                    count += 1

        page_number += 1
        # print("Page number", page_number)
        # print(url + "page/" + str(page_number))
        # time.sleep(3)
        # driver.get(url + "page/" + str(page_number))

    return all_dictonary
