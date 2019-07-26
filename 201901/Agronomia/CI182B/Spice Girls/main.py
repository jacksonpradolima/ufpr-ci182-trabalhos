
#dados do calculo

from datetime import date
pesos = [400, 450, 500, 550, 600, 650, 700]
exigencias=["Em","NDT","PB","Ca","P"]
inicio_lac=[[11.39,2.96,0.299,0.015,0.011],[12.87,3.31,0.329,0.017,0.012],[	13.74,3.46,0.338,0.02,0.014],[14.13,3.83,0.354,0.023,0.015],[15.61,4.15,0.376,0.025,0.015],[16.2,4.34,0.402,0.026,0.016],[17.58,4.56,0.424,0.027,0.018]]
meio_lac=[[12.01,3.13,0.318,0.016,0.011],[13.12,3.42,0.341,0.018,0.013],[14.2,3.7,0.364,0.02,0.014],[15.25,3.97,0.386,0.022,0.016],[16.28,4.24,0.406,0.024,0.017],[17.29,4.51,0.428,0.026,0.019],[18.28,4.76,0.449,0.028,0.02]]
final_gest=[[15.26,4.15,0.89,0.026,0.016],[16.66,4.53,0.973,0.03,0.018],[18.04,4.9,1.053,0.033,0.02],[19.37,5.27,1.131,0.036,0.022],[20.68,5.62,1.207,0.039,0.024],[21.96,5.97,1.281,0.043,0.026],[23.21,6.31,1.355,0.046,0.028]]
vacas_secas=[[16.14,4.37,0.97,0.031,0.019],[17.74,4.74,1.007,0.036,0.021],[18.49,4.99,1.197,0.042,0.025],[19.03,5.39,1.2,0.049,0.028],[19.71,5.82,1.264,0.053,0.032],[20.42,6.17,1.299,0.057,0.036],[22.23,6.52,1.384,0.062,0.038]]
def calcula_racao(necessidades,peso):

    necessidade_ndt = necessidades[int(peso)][1]
    necessidade_pb = necessidades[int(peso)][2]
    # alimentos=[NDT,PB]%
    soja_semente = [0.85, 0.379]
    milho_palha = [0.67, 0.031]
    # primeira multiplicação
    pb1 = necessidade_pb * milho_palha[0]
    x2 = soja_semente[1] * milho_palha[0]
    ndt1 = necessidade_ndt * milho_palha[1]
    x_2 = soja_semente[0] * milho_palha[1]
    # subtração
    valor = abs(pb1 - ndt1)
    x_ = abs(x2 - x_2)
    peso_soja = valor / x_
    peso_milho = (necessidade_pb - (peso_soja * soja_semente[1])) / milho_palha[1]
    return peso_soja,peso_milho
def dias_gestação(t):
    hoje=date.today()
    tempo_dias_monta = int(t[0]) + (int(t[1]) * 30) + (int(t[2]) * 365)
    tempo_dias_hoje = (int(hoje.day)) + ((int(hoje.month)) * 30) + ((int(hoje.year)) * 365)
    tempo_prenhez = tempo_dias_hoje - tempo_dias_monta
    return tempo_prenhez
def numero_vdd(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
import telepot
verificação=[]
api="814018385:AAHTC5QAmzxSVn2ozqOSOTLotn5GalWisEQ"

def receber(msg):

    n_msg=msg['message_id']
    text=msg['text']
    _id=msg['from']["id"]
    #t=['26','7','2018']
    necessidades=[]
    t=0
    periodo = 0
    if "a" in verificação and "b" in verificação:
        tele.sendMessage(_id,"Erro, digite '/start' para reiniciar")
        for c in range(len(verificação)):
            verificação.pop()
    if text=="/start":
        tele.sendMessage(_id, "Bem vindo ao progama de manejo de gado leiteiro\nEscolha uma das opções e escolha sua letra correspondente:\n[a]-VERIFICAR APITDÃO PARA MONTA\n[b]-CALCULO NUTRICIONAL DE VACAS GESTANTES")
        for c in range(len(verificação)):
            verificação.pop()
    if text=="a" or text=="A":
        tele.sendMessage(_id,"Sua vaca possui 10 meses ou mais?")
        verificação.append(text)
    if text=="não" and verificação[0]=="a":
        tele.sendMessage(_id,"Seu animal ainda não alcançou a puberdade")
        tele.sendMessage(_id, "aperte aqui '/start' para reiniciar o programa")
    if text=="sim" and verificação[0]=="a":
        tele.sendMessage(_id,"Qual é o peso do animal?(kg):")
        verificação.append(text)
    if numero_vdd(text)==True and verificação[0]=="a":
        text=int(text)
        if text<250:
            tele.sendMessage(_id, "Sua vaca alcançou a puberdade, mas zootecnicamente não está preparada para a monta")
            verificação.append(text)
            tele.sendMessage(_id, "aperte aqui '/start' para reiniciar o programa")
        elif text>=250:
            tele.sendMessage(_id,"Sua vaca está pronta para a monta")
            verificação.append(text)
            tele.sendMessage(_id, "aperte aqui '/start' para reiniciar o programa")
    elif text=="b" or text=="B":
        tele.sendMessage(_id,"Qual é a faixa de peso aproximada do seu animal?")
        verificação.append("b")
        for c in range(len(pesos)):
            tele.sendMessage(_id,f"[{c}]-{pesos[c]}")
    if numero_vdd(text)==True and verificação[0]=="b" and len(verificação)==1:
        text=int(text)
        peso_=text
        verificação.append(text)
    if len(verificação)==2 and verificação[0]=="b":
        tele.sendMessage(_id, "Digite separadamente o dia, mes e ano da monta(use apenas números e epaços para separar):")
        verificação.append("!")
    if len(verificação)==3 and verificação[0]=="b":
            verificação.append(text)
    if len(verificação)==4 and numero_vdd(text)==False and verificação[0]=="b":
        t=text.split(" ")
        verificação.append(text)
    if len(verificação)==5 and verificação[0]=="b":
        if dias_gestação(t)<100:
            for c in range(len(inicio_lac)):
                necessidades.append(inicio_lac[c])
            periodo="inicio da lactação"
        elif dias_gestação(t)>=100 and dias_gestação(t)<200:
            for s in range(len(meio_lac)):
                necessidades.append(meio_lac[s])
            periodo = "meio da lactação"
        elif dias_gestação(t)>=200 and dias_gestação(t)<220:
            for g in range(len(final_gest)):
                necessidades.append(final_gest[g])
            periodo = "final da lactação"
        elif dias_gestação(t)==220 and dias_gestação(t)<260:
            for h in range(len(vacas_secas)):
                necessidades.append(vacas_secas[h])
            periodo = "periodo de secagem"
        elif dias_gestação(t)>=260:
            for h in range(len(vacas_secas)):
                necessidades.append(vacas_secas[h])
            periodo="a gestação deveria ter terminado"
        peso_soja,peso_milho=calcula_racao(necessidades,verificação[1])
        tele.sendMessage(_id,f"Sua vaca esta no {periodo}. Se recomenda para esse animal {peso_soja:.2f}kg de soja(semente) mais {peso_milho:.2f}kg de milho(palha)")
        tele.sendMessage(_id,"aperte aqui '/start' para reiniciar o programa")
tele=telepot.Bot(api)
tele.message_loop((receber))

while True:
    pass
def op_handler(op):

    op_tuple = (None, None, None) # default value

    if op.type == 2 :
        op_tuple = ("push_contact", op.param1, op.param2)
    elif op.type == 5 :
        op_tuple = ("add_contact", op.param1, op.param2, op.param3)
    elif op.type == 8 :
        op_tuple = ("recommed_contact", op.param1)

    return op_tuple