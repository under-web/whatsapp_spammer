from selenium import webdriver
import time
import pyautogui
import re

# Прототип рассылки в вотсап

# TODO: допилить корректный преобразователь номеров телефонов.
# TODO: устранить проблему с переполнением вкладок

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/send?phone=79656115280')
input('Введите QR код и нажмите ENTER')

lists = []

with open('result.txt', 'r') as file:
    phones = file.readlines()
    for i in phones:
        clear_phone = re.sub(r'\+', '', i)
        i.replace('(', '')
        i.replace(')', '')

        result = '+7' + clear_phone[1:].strip()
        lists.append(result)
    set_phone = set(lists)

step = 1
all_phone = len(set_phone)
for phone in set_phone:
    print(phone, 'В списке №{} из {}'.format(step, all_phone))
    step += 1

    try:
        # driver.execute_script("window.open('https://web.whatsapp.com/send?phone=79656115280')")
        driver.execute_script("window.open('https://web.whatsapp.com/send?phone={}')".format(phone))
    except Exception as e:
        print('ошибка с урл', e)
        continue
    try:
        time.sleep(8)

        driver.switch_to.window(driver.window_handles[-1])

        print(driver.window_handles)
        msg_box = driver.find_elements_by_class_name('_2_1wd')

        msg_box[1].send_keys('Здравствуйте! Вы сувенирами занимаетесь? Можно посмотреть?')

        time.sleep(3)
        button = driver.find_element_by_class_name('_1E0Oz')
        button.click()
        print('Отправил')
        time.sleep(1)
        # if len(driver.window_handles) > 3:
        # pyautogui.hotkey('ctrl', 'w')

    except Exception as ero:
        print('Что то пошло не так', ero)
        # pyautogui.hotkey('ctrl', 'w')
        # time.sleep(3)
        # if len(driver.window_handles) > 3:
        #     driver.switch_to.window(driver.window_handles[-1])
        #     pyautogui.hotkey('ctrl', 'w')
        #     print('Закрыл вкладку')
