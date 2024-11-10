import smtplib
from email.message import EmailMessage

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
