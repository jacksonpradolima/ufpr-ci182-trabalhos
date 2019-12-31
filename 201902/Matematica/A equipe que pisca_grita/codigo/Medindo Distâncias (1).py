#Leitura de distância em Arduinos

#Função responsável por configurar as saídas de luzes dos LED's
#E definir o emissor/captor de sinais no arduino.
def pinMode(parametro):
    if parametro == "LED":
        status = "Todos configurados como Output"
    else:
        status = "É Output/Input, Pino_echo é Entrada e Pino_trigger é Saída"
    return status

#Função responsável por analisar a distância do objeto ao sensor
# Acender os LED's e aumentar/diminuir a intensidade do som do Buzzer.
def digital_write(dist):
    print("Sensor sempre é 1")  #Esta sempre ligado.

    #Para cada distância informada pelo usuário, uma ação será realizada.
    #Distância sempre informada em cm.
    if dist > 200:
        status_LED  = "Nenhum LED Ligado"
        status_Buzzer = "Buzzer Desativado"

    elif dist > 150 and dist <= 200:
        status_LED  = "LED Azul Ligado"
        status_Buzzer = "Buzzer com 1/2 segundo"

    elif dist <= 150 and dist > 120:
        status_LED = "LED Verde Ligado"
        status_Buzzer = "Buzzer com 1/3 segundo"

    elif dist <= 120 and dist > 80:
        status_LED  = "LED Verde Ligado"
        status_Buzzer = "Buzzer com 1/4 segundo"

    elif dist <= 80 and dist > 50:
        status_LED  = "LED Amarelo Ligado"
        status_Buzzer = "Buzzer com 1/5 segundo"

    elif dist <= 50 and dist > 30:
        status_LED = "LED Amarelo Ligado"
        status_Buzzer = "Buzzer com 1/6 segundo"

    elif dist <= 30 and dist > 15:
        status_LED  = "LED Vermelho Ligado"
        status_Buzzer = "Buzzer com 1/7 segundo"

    elif dist <= 15 and dist > 8:
        status_LED  = "LED Vermelho Ligado"
        status_Buzzer = "Buzzer com 1/10 segundo"

    elif dist <= 8 and dist > 0:
        status_LED = ["LED Azul Ligado", "LED Verde Ligado","LED Amarelo Ligado","LED Vermelho Ligado"]
        status_Buzzer = "Buzzer com 1/20 Segundo"

    # Retorna o LED que será aceso e a intensidade de som do Buzzer.
    return status_LED, status_Buzzer


#INÍCIO DO CÓDIGO PARA O USUÁRIO

#Usuário informa se deseja ligar, ou não o sensor.
ard = input("(L)iga ou (D)eslige o Sensor:").upper()

#Enquanto o usuário informar "D", o sensor permanecerá desligado.
while ard != "L":
    print("Sensor Desligado, ligue o Sensor.")
    ard = input("Liga ou Desliga o Sensor:").upper()

#Quando o usuário informar que deseja Ligar o sensor, o mesmo irá ligar.
if ard == "L":
    print("Sensor ligado")
    #Configure os LED's ou o sensor apenas uma vez
    parametro = input("Deseja configurar LED ou Sensor?").upper()
    while parametro != "LED" and parametro != "SENSOR":
        #Caso algo diferente de LED e SENSOR seja digitado
        print("Parametro Inexistente")
        parametro = input("Deseja configurar LED ou Sensor?").upper()
    #O while acima impossibilita que o parâmetro seja diferente de "LED" e "SENSOR".
    #Se o parâmetro for "LED" o programa pedirá a próxima configuração, que só poderá ser SERSOR

    #Caso contrário, o programa pedirá novamente o parâmetro.
    if parametro == "LED":
        print(pinMode(parametro))
        parametro = input("Deseja configurar LED ou Sensor?").upper()
        while parametro != "SENSOR":
            if parametro == "LED":
                print("LED já configurado!")
            else:
                print("Parametro Inexistente")
            parametro = input("Deseja configurar LED ou Sensor?").upper()
        print(pinMode(parametro))
    #Se o parâmetro for "SENSOR" o programa pedirá a próxima configuração, que só poderá ser LED
    #Caso contrário, o programa pedirá novamente o parâmetro.
    else:
        print(pinMode(parametro))
        parametro = input("Deseja configurar LED ou Sensor?").upper()
        while parametro != "LED":
            if parametro == "SENSOR":
                print("SENSOR já configurado!")
            else:
                print("Parametro Inexistente")
            parametro = input("Deseja configurar LED ou Sensor?").upper()
        print(pinMode(parametro))

    #Estando os LED's e o SENSOR configurados, o usuário informará a distância
    distancia = int(input("Digite sua distância em Cm do Sensor:"))

    #Se a distancia for maior que 0, o programa fara os comandos enviados a função digital_write().
    while distancia > 0:
        status_LED, status_Buzzer = digital_write(distancia)
        if distancia <= 8 and distancia > 0:
            for i in range(len(status_LED)):
                print(status_LED[i])
        else:
            print(status_LED)
        print(status_Buzzer)

        distancia = int(input("Digite sua distância em Cm do Sensor:"))

    #Caso a distância seja menor ou igual a 0.
    #O programa entende que o usuário bateu no sensor, e automaticamente encerra.
    if distancia <= 0:
        print("Você Bateu, a gente avisou!!!")
        #PROGRAMA ENCERRADO
