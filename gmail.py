import smtplib


def send_mail(*email):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("binancenewsmonitor@gmail.com","ujbenluypopgyqge")


    server.sendmail(' binancenewsmonitor@gmail.com ', email,
    "Subject: BINANCE NEWS.")
    server.quit()
            
