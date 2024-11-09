ВЕРСИЯ v1.01 от 09-NOV-2024 (патч)

================== О ПРОГРАММЕ ==================

Open-Source программа для изучения языков

Написано на 100% python3

Функционал: добавление элементов в отдельные словари в формате значение1=значение2

Имеет не самый современный, но дружелюбный пользовательский интерфейс с обилием иконок

Платформы: Linux (Ubuntu, Fedora) и Windows
(порт на OS X не планируется)

Требует библиотеку tkinter которая может не быть включена нативно (см. инструкцию как их установить)

================== ИНСТРУКЦИЯ ==================

Установка:

Распакуйте программу на рабочий стол чтобы путь до нее выглядел так:
.../Desktop/TkLearn/TkLearn/Main.pyw

Windows:
* Установите последнюю версию python из Microsoft Store
* Кликните дважды по файлу "Main.pyw"
Если не сработало:
* Откройте терминал и введите "python3 C:\Users\Пользователь\Desktop\TkLearn\TkLearn\Main.pyw"
Если программа не запускается попробуйте открыть Main.pyw в IDLE python и нажать F5.

Linux:
Установите python и библиотеки:

Ubuntu/Debian:
* Введите в терминал "$ sudo apt install python3 python3-tk"

RedHat/Fedora:
* Введите в терминал "$ sudo dnf install python3 python3-tkinter"

Arch:
Поддержка не введена в связи с отстутсвием соответствующих библиотек! 

Поместите папку на рабочий стол чтобы путь до программы выглядел так:

~/Desktop/TkLearn/TkLearn/Main.pyw

Если вы используете дистру без десктопа то просто создайте такую папку 

Чтобы запустить программу введите в терминал 
"$ cd ~/Desktop/TkLearn/TkLearn/ && python3 Main.pyw"
Скрипт можно автоматизировать
(!) Программа запускается только через консоль!

================== РЕШЕНИЕ ПРОБЛЕМ ==================

Если вы столкнулись с багом/вылетом и т.д. напишите об этом в обсуждении

Убедитесь что вы правильно установили все библиотеки
Убедитесь что вашей проблемы нет в списке известных проблем
Неконструктивные и глупые вопросы вроде "Не работает", "Вирусы есть?" не рассматриваются

* Укажите какие действия вызвали ошибку
* Опишите ошибку
* Укажите информацию о вашей системе

Буду рад выслушать предложения, исправления, и конструктивную критику 

================== ИЗВЕСТНЫЕ ПРОБЛЕМЫ ==================

* Если список элементов был пуст, то при добавлении элемента или создании нового словаря может появиться элемент с пустым названием. Просто удалите его, я работаю над этим багом
* При попытке перенести словари с Windows на Linux и наооборот могут возникнуть вылеты и искаженные символы из-за того что, не смотря на все усилия, интерпретатор Windows использует другую кодировку. Из коробки все работает корректно.

На этом все. Пользуйтесь с удовольствием