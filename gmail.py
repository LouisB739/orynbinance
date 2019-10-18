import smtplib


def send_mail(adresse):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("binancenewsmonitor@gmail.com","ujbenluypopgyqge")


    server.sendmail(' binancenewsmonitor@gmail.com ', adresse,
    "Subject: BINANCE NEWS.")
    smtpObj.quit()
            


