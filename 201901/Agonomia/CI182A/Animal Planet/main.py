import telebot
#baixa-se o telebot pelo pip do python no prompt de comando: pip install pyTelegramBotAPI
TOKEN = '785570680:AAEEdjvCFWLAbJtfYxiX4rsU_xyRYRcqpsc'
#o código que identifica meu bot no telegram
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'ajuda'])
def send_welcome(message):
    """"Essa função serve para dar boas vindas ao usuário :param messagem: Mensagem enviada pelo usuário: início ou ajuda :return: retorna uma resposta ao usuário"""
    bot.reply_to(message,
                 "Bem vindo(a) a Hamburgueria Animal Planet! Aqui você encontrará diversos tipos de hambúrgueres.Para finalizar o processo, digite 'Sair'")
    bot.reply_to(message, ("""Basta escolher as opções que oferecemos em nosso cardapio:
                            01-X-SALADA  | PREÇO: R$ 12,99 |(PÃO, DOIS HAMBÚRGUER, TOMATE, CEBOLA, MOSTARDA, MAIONESE E MOLHO BRANCO)
                            02-X-CROQUI  | PREÇO: R$ 13,99 |(PÃO, DOIS HAMBÚRGUER, TOMATE, CEBOLA FRITA CROCANTE, MOSTARDA E MAIONESE)
                            03-X-MÉXICO  | PREÇO: R$ 14,99 |(PÃO, DOIS HAMBÚRGUER, DUPLO COMBO DE PIMENTA, CEBOLA, ALFACE E MOLHO DE PIMENTA)
                            04-X-RATIOU  | PREÇO: R$ 15,99 |(PÃO, DOIS HAMBÚRGUER, TOMATE, ISCAS DE FRANGO AO MOLHO BRANCO)
                            05-X-PIG     | PREÇO: R$ 16,99 |(PÃO, DOIS HAMBÚRGUER, BACON CROCANTE, TOMATE, ALECRIM E PIMENTA)
                            06-X-CHICKEN | PREÇO: R$ 17,99 |(PÃO, DOIS HAMBÚRGUER, TOMATE, PIMENTA, OREGANO E  FRANGO DESFIADO)
                            07-X-VINA    | PREÇO: R$ 18,99 |(PÃO, DOIS HAMBÚRGUER, TOMATE, DUAS VINAS E MAIONESE VERDE)
                            08-X-KING    | PREÇO: R$ 19,99 |(PÃO, DOIS HAMBÚRGUER, TOMATE, BACON, CEBOLA, MAIONESE E VINA)
                            09-X-4QUEIJOS| PREÇO: R$ 20,99 |(PÃO, DOIS HAMBÚRGUER, TOMATE, BACON, DUPLO QUEIJO AO MOLHO BRANCO DERRETIRO E OREGANO)
                            10-X-CASA    | PREÇO: R$ 21,99 |(PÃO, TRÊS HAMBÚRGUER, DUPLO BACON, VINA, PIMENTA, MOLHO BRANCO E FRANGO DESFIADO)
                            11-SUCO DE LARANJA(500ML)     | PREÇO: R$ 6, 99
                            12 - SUCO DE LIMÃO(500ML)     | PREÇO: R$ 6, 99
                            13 - SUCO DE TAMARINDO(500ML) | PREÇO: R$ 6, 99
                            14 - FANTA UVA(350ML)         | PREÇO: R$ 4, 50
                            15 - FANTA JESUS(350ML)       | PREÇO: R$ 4, 50 
                            16 - COCA COLA(2L)            | PREÇO: R$ 8, 00
                            17-MOUSSE DE LIMÃO            |PREÇO: R$ 4,00
                            18-TORTA DE LIMÃO             |PREÇO: R$ 3,50
                            19-PAMONHA                    |PREÇO: R$ 4,99
                            20-COCADA COM DOCE DE LEITE   |PREÇO: R$ 4,99
                            21-BRIGADEIRO DE POTE         |PREÇO: R$ 6,99
                            Caso queira finalizar seu pedido digite 'Sair'""")) #cardápio

@bot.message_handler(func=lambda message: True)
def echo_all(message): #se o cliente digitar o numero correspondente, o restaurante armazena o pedido .
    if message.text.lower() == '01':
        bot.reply_to(message, "Um X-SALADA saindo!")
    elif message.text.lower() == '02':
        bot.reply_to(message, "Um X-CROQUI saindo!")
    elif message.text.lower() == '03':
        bot.reply_to(message, "Um X-MÉXICO saindo!")
    elif message.text.lower() == '04':
        bot.reply_to(message, "Um X-RATIOU saindo!")
    elif message.text.lower() == '05':
        bot.reply_to(message, "Um X-PIG saindo!")
    elif message.text.lower() == '06':
        bot.reply_to(message, "Um X-CHICKEN saindo!")
    elif message.text.lower() == '07':
        bot.reply_to(message, "Um X-VINA saindo!")
    elif message.text.lower() == '08':
        bot.reply_to(message, "Um X-KING saindo!")
    elif message.text.lower() == '09':
        bot.reply_to(message, "Um X-4QUEIJOS saindo!")
    elif message.text.lower() == '10':
        bot.reply_to(message, "Um X-CASA  saindo!")
    elif message.text.lower() == '11':
        bot.reply_to(message, "Seu SUCO DE LARANJA foi anotada!")
    elif message.text.lower() == '12':
        bot.reply_to(message, "Seu SUCO DE LIMÃO foi anotada")
    elif message.text.lower() == '13':
        bot.reply_to(message, "Seu SUCO DE TAMARINDO foi anotada")
    elif message.text.lower() == '14':
        bot.reply_to(message, "Sua FANTA UVA foi anotada")
    elif message.text.lower() == '15':
        bot.reply_to(message, "Sua FANTA JESUS foi anotada")
    elif message.text.lower() == '16':
        bot.reply_to(message, "Sua COCA COLA foi anotada")
    elif message.text.lower() == '17':
        bot.reply_to(message, "Ótima escolha! Um MOUSSE DE LIMÃO para adoçar seu dia! ")
    elif message.text.lower() == '18':
        bot.reply_to(message, "Ótima escolha! Um TORTA DE LIMÃO para adoçar seu dia! ")
    elif message.text.lower() == '19':
        bot.reply_to(message, "Ótima escolha! Um PAMONHA  para adoçar seu dia! ")
    elif message.text.lower() == '20':
        bot.reply_to(message, "Ótima escolha! Um COCADA COM DOCE DE LEITE para adoçar seu dia! ")
    elif message.text.lower() == '21':
        bot.reply_to(message, "Ótima escolha! Um BRIGADEIRO DE POTE para adoçar seu dia! ")
    elif message.text.lower() == 'SAIR' or message.text.lower() == 'Sair' or message.text.lower() == 'sair':
        bot.reply_to(message, "Obrigada por escolher o nosso restaurante, esperamos que voce goste, sua comida ja está a caminho!")
    else:
        bot.reply_to(message, ('Opção inválida! Tente novamente...')) #mensagem para caso o usuário digite algo fora do comum

bot.polling() #finaliza o programa (obrigatório)