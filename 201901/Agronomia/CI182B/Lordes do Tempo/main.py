import telebot
import telepot
from telebot import types
from funcoes import *


bot_token = "626239086:AAGtqcMKcV-DRd6jBfh_lGoXU_Q_zVut2j8"

bot = telebot.TeleBot(bot_token)

opcoes = ["ClimatempoAPI", "OpenWeatherAPI"]
selecionarOpcao = types.ReplyKeyboardMarkup()
selecionarOpcao.add(*opcoes)

cancelar = types.ReplyKeyboardMarkup()
cancelar.add("Cancelar")

esconderTeclado = types.ReplyKeyboardRemove()

all_messages = []


@bot.message_handler(commands=['start'])
def boas_vindas(message):
    usu_id = message.chat.id
    nome_usu = message.chat.first_name
    bot.send_message(
        usu_id, "Bem-vindo(a) {0} ao AccuWeatherBot".format(nome_usu))
    bot.send_message(
        usu_id, "Este bot fornece os dados meteorológicos momentâneos do local escolhido")
    bot.send_message(usu_id, "Escolha qual API você deseja ",
                     reply_markup=selecionarOpcao)
    all_messages.append(message.text)


@bot.message_handler(func=lambda message: message.text == opcoes[0] or message.text == opcoes[1])
def local1(message):
    usu_id = message.chat.id
    bot.send_message(
        usu_id, "Digite o nome do estado, por favor em siglas (ex: PR)", reply_markup=cancelar)
    all_messages.append(message.text)


@bot.message_handler(func=lambda message: message.text == "Cancelar")
def correcao(message):
    usu_id = message.chat.id
    bot.send_message(usu_id, "Escolha outra opção",
                     reply_markup=selecionarOpcao)
    all_messages.append(message.text)


@bot.message_handler(func=lambda message: message.text.isupper())
def continuacao(message):
    usu_id = message.chat.id
    bot.send_message(usu_id, "Estado escolhido", reply_markup=esconderTeclado)
    bot.send_message(usu_id, "Digite o nome da cidade, (ex: curitiba)")
    all_messages.append(message.text)


@bot.message_handler(func=lambda message: message.text.islower())
def final(message):
    usu_id = message.chat.id
    all_messages.append(message.text)
    if all_messages[-3] == "OpenWeatherAPI":
        cid_info = all_messages[-1]
        cid, country, humidity, pressure, temp_min, temp_max, temp, wind_speed, condition = dados_momento_info_open(
            cid_info)
        bot.send_message(usu_id, ("Seu país: {0}".format(country)))
        bot.send_message(usu_id, ("Sua cidade: {0}".format(cid)))
        bot.send_message(
            usu_id, ("Temperatura momentânea: {0:.2f}°C".format(temp-273.15)))
        bot.send_message(
            usu_id, ("Temperatura Máxima: {0:.2f}°C".format(temp_max-273.15)))
        bot.send_message(
            usu_id, ("Temperatura Mínima: {0:.2f}°C".format(temp_min-273.15)))
        bot.send_message(usu_id, ("Condição: {0}".format(condition)))
        bot.send_message(usu_id, ("Pressão: {0} hPa".format(pressure)))
        bot.send_message(
            usu_id, ("Velocidade do vento: {0} km/h".format(wind_speed*3.6)))
        bot.send_message(usu_id, ("Umidade relativa(%): {0}".format(humidity)))
    elif all_messages[-3] == "ClimatempoAPI":
        cid = all_messages[-1]
        state = all_messages[-2]
        temp, wind_velocity, wind_direction, humidity, condition, pressure, sensation, date, name_cid, name_state, id_cid, name_country = dados_momento_info_clima(
            cid, state)
        bot.send_message(usu_id, ("Seu país: {0}".format(name_country)))
        bot.send_message(usu_id, ("Seu estado: {0}".format(name_state)))
        bot.send_message(usu_id, ("Sua cidade: {0}".format(name_cid)))
        bot.send_message(usu_id, ("Data e horário: {0}".format(date)))
        bot.send_message(usu_id, ("Temperatura de hoje: {0}°C".format(temp)))
        bot.send_message(usu_id, ("Sensação térmica: {0}°C".format(sensation)))
        bot.send_message(usu_id, ("Condição: {0}".format(condition)))
        bot.send_message(usu_id, ("Pressão: {0} hPa".format(pressure)))
        bot.send_message(
            usu_id, ("Velocidade do vento: {0} km/h".format(wind_velocity)))
        bot.send_message(
            usu_id, ("Direção do vento: {0}".format(wind_direction)))
        bot.send_message(usu_id, ("Umidade relativa(%): {0}".format(humidity)))


bot.polling()
