from selenium import webdriver
import time
import pyautogui
import random


# v.2.1
# ============================
# Прототип рассылки в вотсап #
# ============================


def get_phone():
    with open('Юла телефоны.txt', 'r') as file:                     # место с телефонами
        phones = file.readlines()
        set_phone = set(phones)
    return set_phone


def run_spammer(set_phone):
    driver = webdriver.Firefox()
    driver.get(r'https://web.whatsapp.com/send?phone=79656115280')  # стартовая страница не важно какой номер здесь
    time.sleep(6)
    print(pyautogui.position())                                     # определение позиции курсора
    input('Введите QR код и нажмите ENTER')                         # c этого момента мышь не трогать

    step = 1
    all_phone = len(set_phone)

    for phone in set_phone:
        print(phone, 'В списке №{} из {}'.format(step, all_phone))
        step += 1
        if step % 50 == 0:                                          # если делится без остатка на 50 пауза 15 мин
            time.sleep(900)
        else:
            try:
                driver.execute_script("window.open('https://web.whatsapp.com/send?phone={}')".format(phone.strip()))
            except Exception as e:
                print('ошибка с урл', e)
                continue

            try:
                time.sleep(random.randint(5, 10))
                with open('messages.txt', 'r') as files: # открываем файл с сообщениями
                    txt = files.readlines()              # считываем его в список
                driver.switch_to.window(driver.window_handles[-1])


                # print(driver.window_handles)
                msg_box = driver.find_elements_by_class_name('_2_1wd')  # находим бокс куда вставлять сообщение
                msg_box[1].send_keys(random.choice(txt))  # вставляем нужный текст выбрав рандомно из списка
                time.sleep(random.randint(3, 5))

                button = driver.find_element_by_class_name('_1E0Oz')  # находим кнопку
                time.sleep(1)
                button.click()  # кликаем по ней
                time.sleep(2)
                print('Отправил')

                time.sleep(random.randint(45, 80))
                if len(driver.window_handles) >= 2:
                    pyautogui.moveTo(206, 56, 1)
                    pyautogui.click()
                    time.sleep(2)

            except Exception as ero:
                print('Что то пошло не так', ero)
                pyautogui.moveTo(206, 56, 1)
                pyautogui.click()
                time.sleep(random.randint(45, 80))


def main():
    run_spammer(get_phone())


if __name__ == '__main__':
    main()
