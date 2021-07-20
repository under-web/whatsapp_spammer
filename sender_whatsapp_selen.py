from selenium import webdriver
import time
import random

# TODO: сделать скрытой отправку сообщений
def send_message():
    driver = webdriver.Chrome()
    driver.get(r'https://web.whatsapp.com/send?phone=79656115280')  # стартовая страница не важно какой номер здесь

    input('Введите QR код и нажмите ENTER')
    print('Жду')
    time.sleep(6)
    print('go')
    step = 1
    with open(r'T:\Desktop\tg700.txt', 'r', encoding='utf-8') as file_phone:
        for phone in file_phone.readlines():
            print(phone, f'Отправляю сообщение на {step} из')
            try:
                driver.execute_script("window.open('https://web.whatsapp.com/send?phone={}')".format(phone.strip()))
            except Exception as e:
                print('ошибка с урл', e)
                continue

            try:
                time.sleep(random.randint(5, 10))

                with open('messages.txt', 'r') as files:  # открываем файл с сообщениями
                    txt = files.readlines()  # считываем его в список
                try:
                    driver.switch_to.window(driver.window_handles[-1])
                except Exception as r:
                    print(r)
                msg_box = driver.find_element_by_class_name('_1SEvr')  # находим бокс куда вставлять сообщение
                print('нашел msg_box')
                time.sleep(2)
                try:
                    msg_box.send_keys(random.choice(txt))  # вставляем нужный текст выбрав рандомно из списка
                    print('отправил на msg_box')
                except Exception as ms:
                    print('Не смог вставить текст', ms)
                    time.sleep(5)

                time.sleep(random.randint(3, 5))

                button = driver.find_element_by_class_name('_1E0Oz')  # находим кнопку
                time.sleep(1)
                button.click()  # кликаем по ней
                time.sleep(2)
                print('Отправил')

                time.sleep(random.randint(45, 80))

            except Exception as ero:
                print('Что то пошло не так', ero)



def main():
    send_message()


if __name__ == '__main__':
    main()
