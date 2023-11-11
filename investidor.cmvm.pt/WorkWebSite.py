import re
import time
from googletrans import Translator, constants
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


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
    json_dictionary = {}
    key = []
    value = []
    all_dictonary = []
    page_number = 0
    time.sleep(10)
    button = driver.execute_script(" return document.querySelector('.welcome-panel-close')")
    button.click()
    number_pagedown = 0
    body = driver.find_element(By.TAG_NAME, "body")

    while number_pagedown < 1:
        print("push_end", number_pagedown)
        body.send_keys(Keys.END)
        number_pagedown += 1
        time.sleep(3)

    while page_number < 17:
        time.sleep(5)
        list_link = driver.execute_script("return document.querySelectorAll('.gc-see-more')")
        list_link[page_number+1].click()
        time.sleep(5)
        name = driver.find_elements(By.CSS_SELECTOR, ".template-dynamic-title")

        key.append("name")
        value.append(name[0].text)

        text_url = driver.find_elements(By.CSS_SELECTOR, ".cke_contents_ltr")
        pattern = r"(?:https?:\/\/|ftps?:\/\/|www\.)(?:(?![.,?!;:()]*(?:\s|$))[^\s]){2,}"
        url_2 = re.findall(pattern, text_url[0].text)

        key.append("social_networks")
        value.append(url_2[0])
        list_link_2 = driver.execute_script("return document.querySelectorAll('#b5-Links > div > a')")
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_UP)
        time.sleep(3)
        list_link_2[3].click()




        count = 0
        # print(len(key))
        # print(len(value))

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
        url = "https://investidor.cmvm.pt/PInvestidor/Content?Input" \
              "=2261423276FE736012E5188493A75BA7DF245F268FA18A136059316E2C3550AE "
        time.sleep(3)
        driver.get(url)

    return all_dictonary
