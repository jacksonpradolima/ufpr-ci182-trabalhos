import random
import telebot  # Vamos então importar a API que instalamos (pyTelegramBotApi)

TOKEN = "876604242:AAHnRGizrurcSZ-3Z7sNFKAKZ4BtoseOfDg"  # Gerado pelo fatherbot

# criamos a variável bot chamando ela pelo token que geramos acima, com a função ‘Telebot’
bot = telebot.TeleBot(TOKEN)


def d4():
    dado = random.randrange(1, 5)
    return dado


def d6():
    dado = random.randrange(1, 7)
    return dado


def d8():
    dado = random.randrange(1, 9)
    return dado


def d10():
    dado = random.randrange(1, 11)
    return dado


def d12():
    dado = random.randrange(1, 13)
    return dado


def d16():
    dado = random.randrange(1, 17)
    return dado


def d20():
    dado = random.randrange(1, 21)
    return dado


def d30():
    dado = random.randrange(1, 31)
    return dado


def d100():
    dado = random.randrange(1, 101)
    return dado


# codigo gerado pelo FatherBot, serve como uma id do bot
#TOKEN = "876604242:AAHnRGizrurcSZ-3Z7sNFKAKZ4BtoseOfDg"
# criamos a variável bot chamando ela pelo token que geramos no começo do projeto com a função ‘Telebot’
#bot = telebot.TeleBot(TOKEN)


# o método @bot.message_handler  “escuta” as mensagens que chegam no nosso bot
@bot.message_handler(commands=["ajuda"])
def send_welcome(message):
    bot.reply_to(message,
                 "Selecione o Dado desejado: (4- D4) (6- D6) (8- D8) (10- D10) (12- D12) (16- D16) (20-D20) (30- D30) (100- D100) ")


# O parâmetro func=lambda m: true é para escutar qualquer mensagem que chegar no bot                    )
@bot.message_handler(func=lambda message: True)
# A função echo_all é responsável pelas mensagens que o método @bot.message_handle ‘escutou’.
def echo_all(message):
    if message.text.lower() == "4":
        d = d4()
        bot.reply_to(message, "D4:"+str(d))

    elif message.text.lower() == "6":
        d = d6()
        bot.reply_to(message, "D6:"+str(d))

    elif message.text.lower() == "8":
        d = d8()
        bot.reply_to(message, "D8:"+str(d))

    elif message.text.lower() == "10":
        d = d10()
        bot.reply_to(message, "D10:"+str(d))

    elif message.text.lower() == "12":
        d = d12()
        bot.reply_to(message, "D12:"+str(d))

    elif message.text.lower() == "16":
        d = d16()
        bot.reply_to(message, "D16:"+str(d))

    elif message.text.lower() == "20":
        d = d20()
        bot.reply_to(message, "D20:"+str(d))

    elif message.text.lower() == "30":
        d = d30()
        bot.reply_to(message, "D30:"+str(d))

    elif message.text.lower() == "100":
        d = d100()
        bot.reply_to(message, "D100:"+str(d))

    elif message.text.lower() == "SAIR" or message.text.lower() == "sair" or message.text.lower() == "Sair":
        bot.reply_to(message, "Adios muchacho")
    else:
        bot.reply_to(message, "Invalid Option")


bot.polling()
