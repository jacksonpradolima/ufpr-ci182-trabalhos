# Codigo: Controle de temperatura para cultivo utilizando Raspberry Pi
# Grupo: Frozen

# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as gpio
import time

# Define o tipo de sensor, no nosso caso DHT11
sensor = Adafruit_DHT.DHT11

# Define o modo de numeracao e identificacao dos pinos da gpio
gpio.setmode(gpio.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor=3

# Define a GPIO conectada ao pino de comando (output) do rele
gpio.setup(7,gpio.OUT)

cultura=0

# Pede para o usuario selecionar o tipo da cultura
while cultura!=1 and cultura!=2 and cultura!=3:
   print("Por favor, selecione o numero da cultura:")
   print("1 - Morango")
   print("2 - Jaboticaba")
   print("3 - Banana")
   cultura=int(input(">"))
   if cultura!=1 and cultura!=2 and cultura!=3:
      print("Numero invalido")

time.sleep(2)

if cultura==1:
   tempmin=18
   tempmax=20
   print(" ")
   print("Cultura selecionada: Morango")
   print("Temperatura maxima: ",tempmax)
   print("Temperatura minima: ",tempmin)
elif cultura==2:
   tempmin=20
   tempmax=22
   print(" ")
   print("Cultura selecionada: Jaboticaba")
   print("Temperatura maxima: ",tempmax)
   print("Temperatura minima: ",tempmin)
elif cultura==3:
   tempmin=22
   tempmax=24
   print(" ")
   print("Cultura selecionada: Banana")
   print("Temperatura maxima: ",tempmax)
   print("Temperatura minima: ",tempmin)

time.sleep(5)

# Informacoes iniciais
print(" ")
print ("Lendo os valores de temperatura e umidade");
time.sleep(5)

while(1):
   # Efetua a leitura do sensor
   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
   # Caso leitura esteja ok, mostra os valores na tela
   if umid is not None and temp is not None:
     print(" ") 
     print ("Temperatura: ",temp," Umidade: ",umid);
     # Se a temperatura lida for maior que a temperatura maxima ideal, aciona o rele para ligar a refrigeracao) 
     if temp>tempmax:
        print("Temperatura acima do recomendavel, sistema de refrigeracao ligado")
        gpio.output(7,0) #fecha o contato do rele na porta NF
     # Se a temperatura lida for menor que a temperatura minima ideal, aciona o rele para desligar a refrigeracao)   
     elif temp<tempmin:
        print("Temperatura abaixo do recomendavel, sistema de refrigeracao desligado")
        gpio.output(7,1) #abre o contato do rele na porta NF
     elif temp>=tempmin and temp<=tempmax:
        print("Temperatura dentro dos parametros recomendados")
     print ("Aguarda 5 segundos para efetuar nova leitura...");
     time.sleep(5)
   else:
     # Mensagem de erro de comunicacao com o sensor
     print("Falha ao ler dados do DHT11 !!!")
