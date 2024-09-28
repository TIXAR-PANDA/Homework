# Домашняя работа по уроку "Способы вызова функции"

def send_email(message: str, recipient: str, *, sender='university.help@gmail.com'):
    if not all(['@' in recipient,
                '@' in sender,
                recipient.endswith('.net') or
                recipient.endswith('.com') or
                recipient.endswith('.ru'),
                sender.endswith('.net') or
                sender.endswith('.com') or
                sender.endswith('.ru')]):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>")
    elif recipient == sender:
        print(f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>')

# Пример выполняемого кода (тест):
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
