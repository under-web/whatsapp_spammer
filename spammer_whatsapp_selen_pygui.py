from selenium import webdriver
import time
import pyautogui
import re

# ============================
# Прототип рассылки в вотсап #
# ============================
# TODO: допилить корректный преобразователь номеров телефонов?


driver = webdriver.Firefox()
driver.get(r'https://web.whatsapp.com/send?phone=79656115280')  # стартовая страница не важно какой номер здесь

# print(pyautogui.position())                                   # определение позиции курсора
input('Введите QR код и нажмите ENTER')                         # c этого момента мышь не трогать

lists = []

with open('Юла телефоны.txt', 'r') as file:                     # место с телефонами
    phones = file.readlines()
    # for i in phones:
    #     clear_phone = re.sub(r'\+', '', i)
    #     i.replace('(', '')
    #     i.replace(')', '')                                    # блок с форматированием номера телефона
    #
    #     result = '+7' + clear_phone[1:].strip()
    #     lists.append(result)
    set_phone = set(phones)

step = 1
all_phone = len(set_phone)

for phone in set_phone:
    print(phone, 'В списке №{} из {}'.format(step, all_phone))
    step += 1

    try:
        driver.execute_script("window.open('https://web.whatsapp.com/send?phone={}')".format(phone.strip()))
    except Exception as e:
        print('ошибка с урл', e)
        continue

    try:
        time.sleep(8)

        driver.switch_to.window(driver.window_handles[-1])

        # print(driver.window_handles)
        msg_box = driver.find_elements_by_class_name('_2_1wd')     # находим бокс куда вставлять сообщение
        msg_box[1].send_keys('Здравствуйте! Вы сувенирами занимаетесь? Можно посмотреть?')  # вставляем нужный текст
        time.sleep(3)

        button = driver.find_element_by_class_name('_1E0Oz')       # находим кнопку
        button.click()                                             # кликаем по ней
        print('Отправил')

        time.sleep(1)
        if len(driver.window_handles) >= 3:
            pyautogui.moveTo(207, 47, 1)
            pyautogui.click()
            time.sleep(2)

    except Exception as ero:
        print('Что то пошло не так', ero)
        pyautogui.moveTo(168, 242, 2)
        pyautogui.click()
        time.sleep(2)

