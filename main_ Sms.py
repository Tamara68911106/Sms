import smtplib
from email.message import EmailMessage
from tkinret import*


def send_email():
    sender_email = 'vika.gornakowa@ya.ru'
    recipient_mail = 'super.pin-0985@ya.ru'
    password = 'wwoimnuynuqgvkut'
    subject = 'Проверка связи'
    body = 'Привет из программы на Питоне'


    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email # от кого отправляем
    msg['To'] = recipient_mail # кому отправляем

    server = None

    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) # протокол - способ кодирования сообщения.
        # Порт - дверь, через них поступает инфо в комп
        server.login(sender_email,password)
        server.send_message(msg)
        print('Письмо отправлено!')
    except Exception as e:
        print(f'Ошибка: {e}')
    finally:  #при обработки исключений, пишем то, что будет в любом случае,
    # файнели всегда выполняется и закроет сервер
        if server:
            server.quit()

window=Tk()
window.title('Отправка Email')
window.geometry('500x300')


Label(text="Отправитель:").grid(row=0, columb=0, sticky=W)# sticky - растягивать  в бок
sender_email_entry=Entry()
sender_email_entry.grid(row=0, columb=0, sticky=W)

Label(text="Получатель:").grid(row=1, columb=0, sticky=W)# sticky - растягивать  в бок
recipient_mail_email_entry=Entry()
recipient_email_entry.grid(row=1, columb=1, sticky=W)

Label(text="Пароль приложения:").grid(row=2, columb=0, sticky=W)# sticky - растягивать  в бок
password_entry=Entry()
password_entry.grid(row=2, columb=1, sticky=W)

Label(text="Тема письма:").grid(row=3, columb=0, sticky=W)# sticky - растягивать  в бок
subject_entry=Entry()
subject_entry.grid(row=3, columb=1, sticky=W)

Label(text="Сообщение:").grid(row=4, columb=0, sticky=W)# sticky - растягивать  в бок
body_text= Text(width=45, height=10)
body_text.grid(row=4, columb=1, sticky=W)

Button(text="Отправить письмо", command =send_email).grid(row=5, columb=1, sticky=W)
result_label = Label(text='')
result_label.grid(row=6, columb=1, sticky=W)

window.mainloop()

