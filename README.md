# whatsapp_spammer
Спаммер на библиотеке селениум для рассылки по whatsapp .
Запускам spammer_whatsapp_selen_pygui.py  после сканирования QR кода с телефона жмем ENTER в консоли. И сразу переключаемся на браузер.




Если не запускается драйвер скачиваем gecodriver для firefox и перемещаем его 
mv gecodriver usr/local/bin

Для виндовс и Google Chrome достаточно указать путь к драйверу
driver = webdriver.Chrome('path to driver')
