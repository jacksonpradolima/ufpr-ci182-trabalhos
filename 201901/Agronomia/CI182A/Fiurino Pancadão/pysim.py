from importacoes import sg, os, sys
from layouts import layoutCalculo, layoutInicial, layoutResultados
from calcular import calcular


#                Definir o layout da janela principal
janela = sg.Window('Aplicativo', layoutInicial)


#                  Iniciar o procedimento de calculo
def novoCalculo():
    global janela
    janela.Hide()
    janela = sg.Window('Cálculo', layoutCalculo)

#
#             Exemplo de dictionary gerado no formulario
#
# {'culturaDes': 'Milho', 'culturaAnt': 'Gramínea',\
#  'produtividade': 'Menor que 8 ', 'interP': 'K trocável',\
#  'interK': 'Pastagem', 'phCaCl2': '0.00', 'phH2O': '0.00',\
#  'cmolAl': '0.000000', 'cmolH+': '0.000000', 'cmolCa2+': '0.000000',\
#  'cmolMg2+': '0.000000', 'cmolNa2+': '0.000000', 'cmolK': '0.000000',\
#  'fosforo': '0.0', 'argila': '0.00', 'matOrganica': '0.00',\
#  'carbOrganico': '0.00'}\
#


def viraFloat(dic):
    aux = 0
    dic['phCaCl2'] = float(dic['phCaCl2'])
    dic['phH2O'] = float(dic['phH2O'])
    dic['cmolAl'] = float(dic['cmolAl'])
    dic['cmolH+'] = float(dic['cmolH+'])
    dic['cmolCa2+'] = float(dic['cmolCa2+'])
    dic['cmolMg2+'] = float(dic['cmolMg2+'])
    dic['cmolNa+'] = float(dic['cmolNa+'])
    dic['cmolK'] = float(dic['cmolK'])
    dic['fosforo'] = float(dic['fosforo'])
    dic['argila'] = float(dic['argila'])
    dic['matOrganica'] = float(dic['matOrganica'])
    dic['carbOrganico'] = float(dic['carbOrganico'])


#                  Verifica se a variável é um número
def ehNumero(n):
    try:
        num = float(n)
    except ValueError:
        return False
    return True


#
#               #####  Função para verificar  ######
#               ##  se os valores do formulário  ###
#               #####  não podem ser usados  #######
#
def verificaValores(lista2):
    caiFora = {"culturaDes", "culturaAnt",
               "produtividade", "interP", "interK"}
    lista = {x: lista2[x] for x in lista2 if x not in caiFora}
    # inicialmente, verificar o pH
    phCaCl2 = lista['phCaCl2']
    phH2O = lista['phH2O']
    if not(ehNumero(phCaCl2) and ehNumero(phH2O)):
        # print(1)
        return False
    phCaCl2 = float(phCaCl2)
    phH2O = float(phH2O)
    if not ((0 <= phH2O <= 14) and (0 <= phCaCl2 <= 14)):
        # print(2)
        return False
    valores = [float(k) for k in lista.values()]
    if not all(ehNumero(x) for x in valores):
        # print(3)
        return False
    if not all(i >= 0 for i in valores):
        # print(4)
        return False
    return True


#
#               ####################################
#               ########  Função principal  ########
#               ####################################
#

while True:
    event, values = janela.Read()
    if event is None or event == 'Sair':
        break
    elif event == 'Sobre':
        sg.Popup(
            "", "Programa desenvolvido pela equipe ~Fiorino Pancadão~ como "
            "trabalho final da disciplina de Fundamentos de Programação "
            "de Computadores CI182-A).",
            "Professor: Jackson Antonio do Prado Lima",
            "Alunos: Nicolas Vieira Carneiro, Victor Hugo Farias Camargo, "
            "Yuri Cetnarski Mikos, Hugo Carlos Gouveia de Sá", "",
            no_titlebar=True)
    elif event == 'Novo cálculo':
        novoCalculo()
    elif event == 'Calcular':
        if not verificaValores(values):
            sg.Popup('Ocorreu um erro ao calcular!', 'Verifique se os dados'
                     ' foram inseridos de maneira correta.')
        else:
            textim = ''
            viraFloat(values)
            dicio = calcular(values)
            textim = '\n\n'.join("{!s} = {!r}".format(key,val) for (key,val) in dicio.items())
            sg.Popup(textim)

janela.Close()
