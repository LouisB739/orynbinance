
import telegram
#token that can be generated talking with @BotFather on telegram
my_token = '"927884908:AAEOF5CVBsjdVSNLT8--t09MUYdc88xtyDk"'


def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

test = telegram_bot_sendtext("Testing Telegram bot")
print(test)


send("SALUT",+33684086800)

