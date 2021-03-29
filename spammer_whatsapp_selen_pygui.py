from selenium import webdriver
import time
import pyautogui
import random



# ============================
# Прототип рассылки в вотсап #
# ============================


def get_phone():
    with open('Юла телефоны.txt', 'r') as file:  # место с телефонами
        phones = file.readlines()
        set_phone = set(phones)
    return set_phone


def run_spammer(set_phone):
    driver = webdriver.Firefox()
    driver.get(r'https://web.whatsapp.com/send?phone=79656115280')  # стартовая страница не важно какой номер здесь
    time.sleep(6)
    print(pyautogui.position())  # определение позиции курсора
    input('Введите QR код и нажмите ENTER')  # c этого момента мышь не трогать

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
            time.sleep(random.randint(5, 10))

            driver.switch_to.window(driver.window_handles[-1])
            txt = "Доброго времени суток! 🔥Горячая тема в 21 году: Видео-магнит, как доход для частника и крупного бизнеса, НЕ ФРАНШИЗА, " \
                  "Для собственников, Отелей, Сувенирных лавок, Музеев и Театров, Так же для, Музыкантов, Блогеров, " \
                  "Пиарщиков,Magic-Magnet.ru, Вы можете хорошо заработать! Присоединяйтесь."

            # print(driver.window_handles)
            msg_box = driver.find_elements_by_class_name('_2_1wd')  # находим бокс куда вставлять сообщение
            msg_box[1].send_keys(txt)  # вставляем нужный текст
            time.sleep(random.randint(3, 5))

            button = driver.find_element_by_class_name('_1E0Oz')  # находим кнопку
            button.click()  # кликаем по ней
            print('Отправил')

            time.sleep(random.randint(30, 60))
            if len(driver.window_handles) >= 2:
                pyautogui.moveTo(206, 56, 1)
                pyautogui.click()
                time.sleep(2)

        except Exception as ero:
            print('Что то пошло не так', ero)
            pyautogui.moveTo(206, 56, 1)
            pyautogui.click()
            time.sleep(random.randint(30, 60))


def main():
    run_spammer(get_phone())


if __name__ == '__main__':
    main()
