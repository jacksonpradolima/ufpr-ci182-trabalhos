import telebot
import serial
from serial.tools import list_ports

bot = telebot.TeleBot("859832840:AAGCqrBMfri4iC9_4prenY6Q3jML4BUfL-w")

# Salva todas as leituras de umidade/temperatura
lista = []

def le_porta():
    #Primeiramente precisamos determinar as portas seriais disponiveis na maquina
    # para isso, obtemos a lista de portas seriais e escolhemos manualmente
    # aquela com index 0.

    selectedPortIndex = 0
    selectedDevice = ""

    ports = list_ports.comports()
    #print("Avaiable ports:\n%s"%"\n".join(["\t%d: %s"%
    #(portIndex,str(ports[portIndex])) for portIndex in range(len(ports))]))

    selectedDevice = ports[selectedPortIndex].device
    #print(f"Selected device: {selectedDevice}")

    ser = serial.Serial(selectedDevice, 57600)

    # Cada execução lê uma linha da porta serial
    # e separa os dois valores (umidade e temperatura)

    try:
        for line in ser:
            try:
                entry = line.decode("utf-8").split("\t")
                humidity = float(entry[0])
                temperature = float(entry[1])
                #print(f"T: {temperature} - H: {humidity}")
                lista.append([humidity,temperature])
                return humidity, temperature
            except ValueError as e:
                print(f"E: {line}")
                return -1, 0
            except IndexError as e:
                print(f"E: {line}")
                return -1, 0
    except KeyboardInterrupt:
        # Ao abortar a execução do programa esta exception é chamada
        # deve-se então fechar a porta serial para novas comunicações
        ser.close()
        return -1, 0
    except:
        #Caso seja um erro não especificado é importante fechar a porta
        # serial para permitir comunicação futura
        ser.close()
        return -1, 0
    
# mensagem de Início ao comando /start do Bot
@bot.message_handler(commands=['start', 'help']) 
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou um Bot criado com a finalidade de captar as informações transmitidas pelo Sensor DHT22 integrado com um Arduíno Mega 2560, e te enviar! Você pode solicitar a umidade ou temperatura atuais.")

# Bot informa a umidade captada pelo sensor do arduíno (ultima info passada pelo sensor) e passa para o usuário
@bot.message_handler(commands=['umidade']) 
def analisa_umidade(message):
    umidade, temperatura = le_porta()
    
    if umidade == -1:
        bot.reply_to(message, "Erro ao obter informações")
    else:
        bot.reply_to(message,"Umidade atual: {0}".format(umidade))

# Bot informa a Temperatura captada pelo sensor do arduíno (ultima info passada pelo sensor) e passa para o usuário
@bot.message_handler(commands=['temperatura']) 
def analisa_temperatura(message):
    umidade, temperatura = le_porta()
    
    if umidade == -1:
        bot.reply_to(message, "Erro ao obter informações")
    else:
        bot.reply_to(message,"Temperatura atual: {0}".format(temperatura))

bot.polling()
