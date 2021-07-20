import time
import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# TODO: вместо повторения функции close_book написать цикл с закрытием лишних вкладок если их больше чем нужно

def close_book(need_book=3): # Количество вкладок в вирт браузере не более (N)
    """
    Функция закрывает первую вкладку если выполняется условие
    :param book:
    :return:
    """
    all_books = len(driver.window_handles)
    if all_books >= need_book:
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        time.sleep(5)
    else:
        print(f'Сейчас {all_books} вкладок')


def get_phone_lists(rand=True):
    """
    Собирает телефоны из файла и рандомизирует их
    :return: random list
    """
    with open(r'T:\Desktop\tg700.txt', 'r', encoding='utf-8') as file:
        norm_phones = file.readlines()
        if rand:
            rand_all_phones = random.sample(norm_phones, len(norm_phones))
            return rand_all_phones
        else:
            return norm_phones

def get_message():
    """
    Берет случайную строчку из файла и подставляет ее в сообщение
    :return: txt
    """
    with open('messages.txt', 'r', encoding='utf-8') as files:  # открываем файл с сообщениями
        txt = files.readlines()  # считываем его в список
        return txt


def send_message(txt, any_phones):
    driver.get(r'https://web.whatsapp.com/send?phone=79656115280')  # стартовая страница не важно какой номер здесь

    input('Введите QR код и нажмите ENTER')
    time.sleep(6)
    print(f'Всего телефонов {len(any_phones)}')
    for phone in any_phones:
        try:
            driver.switch_to.window(driver.window_handles[-1])
            driver.execute_script("window.open('https://web.whatsapp.com/send?phone={}')".format(phone.strip()))
        except Exception as e:
            print('ошибка с урл', e)
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            continue

        time.sleep(random.randint(5, 10))
        driver.switch_to.window(driver.window_handles[-1])

        try:
            wait = WebDriverWait(driver, 10)
            msg_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div')))
            time.sleep(3)
            msg_box.send_keys(random.choice(txt).strip())  # вставляем нужный текст выбрав рандомно из списка
            print('Отправил текст в msg_box')

        except Exception as e:
            print('Не нашел msg_box')
            close_book()
            continue

        time.sleep(random.randint(3, 5))
        try:
            button = driver.find_element_by_class_name('_4sWnG')  # находим кнопку
            time.sleep(1)
            button.click()  # кликаем по ней
            close_book()
        except Exception as r:
            print('Нет стрелочки')
            close_book()
            time.sleep(random.randint(15, 30))


def main():
    send_message(get_message(), get_phone_lists())


if __name__ == '__main__':
    main()
