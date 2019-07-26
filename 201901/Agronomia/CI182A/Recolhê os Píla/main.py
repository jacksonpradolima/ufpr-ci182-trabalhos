import telebot

#Código do BotTelegram, criado pelo BotFather @chadavovobot
TOKEN = '835146510:AAHomtAKyhkEIjKsQYPl8JozxkVtHAbIKVw'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'ajuda'])
def send_welcome(message):
    """
    Essa função serve para dar as boas vindas ao usuário
    :param message: Mensagem enviada pelo usuário: início ou ajuda
    :return: retorna uma resposta ao usuário
    """
    bot.reply_to(message, """Olá, seja bem-vindo(a) ao cházinho da Vovó!
    Como posso te ajudar? Tenho algumas receitinhas especiais aqui...""")
    bot.reply_to(message, """É só escolher uma das opções abaixo:
    01 - Afecções do fígado
    02 - Ajuda a acelerar o metabolismo
    03 - Ameniza irritação na faringe 
    04 - Anemia
    05 - Antiescorbútico, abre apetite
    06 - Aumenta leite
    07 - Azia
    08 - Cálculo renal
    09 - Calmante
    10 - Cicatrizante
    11 - Colesterol
    12 - Cólica
    13 - Cólica menstrual
    14 - Contusões (pancada)
    15 - Corrimento vaginal
    16 - Desobstruir vias respiratórias
    17 - Digestivo
    18 - Diurético
    19 - Dor de dente 
    20 - Dores abdominais
    21 - Dores nos rins
    22 - Expectorante
    23 - Faringite
    24 - Febre
    25 - Feridas
    26 - Fortalecer cabelo (queda)
    27 - Garganta irritada
    28 - Gases intestinais
    29 - Gastrite
    30 - Gripe
    31 - Hemorroidas
    32 - Hipertensão
    33 - Inflamações
    34 - Insônia
    35 - Má digestão
    36 - Mau hálito
    37 - Menstruação irregular
    38 - Problemas digestivos em geral
    39 - Problemas respiratórios
    40 - Queda de cabelo
    41 - Reumatismo
    42 - Rouquidão
    43 - Tosse, bronquite, rouquidão
    44 - Úlcera no estômago e intestino
    45 - Verme
    
    Para finalizar o processo, digite "SAIR"
    """)

#Essa função, serve para responder a opção selecionada pelo usuário
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == '01':
        bot.reply_to(message, 'Um cházinho de GUACO vai super bem! A receita da Vovó é: 2 xícaras (cafezinho) de folhas picadas em 500ml d’água. Tome uma xícara 4 vezes ao dia.')
    elif message.text.lower() == '02':
        bot.reply_to(message, 'Um pouco de PIMENTA MALAGUETA vai super bem! A receita da Vovó é: Comê-la nas refeições normalmente.')
    elif message.text.lower() == '03':
        bot.reply_to(message, 'Um cházinho de PEIXINHO vai super bem! A receita da Vovó é: preparar um chá com uma xícara(cafezinho) de folhas em 500 ml d´água. Tome uma xícara 3 vezes ao dia e faça gargareijos.')
    elif message.text.lower() == '04':
        bot.reply_to(message, 'Um cházinho de CARQUEJA vai super bem! A receita da Vovó é: preparar um chá com uma xícara (cafezinho) de folhas picadas em 500 ml d´água. Tome de uma à duas xícaras de chá após cada refeição e também ao deitar.')
    elif message.text.lower() == '05':
        bot.reply_to(message, 'Um pouco de CAPUCHINHA vai super bem! A receita da Vovó é: consuma as flores em forma de salada à vontade,')
    elif message.text.lower() == '06':
        bot.reply_to(message, 'Um pouco de ERVA DOCE vai super bem! A receita da Vovó é: preparar o chá com uma xícara (cafezinho) com as sementes em 500 ml d´água. Tome uma xícara de quatro em quatro horas.')
    elif message.text.lower() == '07':
        bot.reply_to(message, 'Um pouco de ALECRIM vai super bem! A receita da Vovó é: preparar um chá com uma colher (café) de folhas picadas em uma xícara (cafezinho) de água. Tome uma xícara três vezes ao dia.')
    elif message.text.lower() == '08':
        bot.reply_to(message, 'Um pouco de MIL EM RAMAS vai super bem! A receita da Vovó é: preparar um chá com uma xícara (cafezinho) de inflorescência em 500 ml de água. Tome uma xícara de chá duas vezes ao dia.')
    elif message.text.lower() == '09':
        bot.reply_to(message, 'Um pouco de MELISSA vai super bem! A receita da Vovó é: preparar um chá com uma xícara (café) de folhas picadas em 500 ml de água. Tomar uma xícara quatro vezes ao dia.')
    elif message.text.lower() == '10':
        bot.reply_to(message, 'Um pouco de BABOSA vai super bem! A receita da Vovó é: cortar as folhas e retirar o líquido viscoso. Aplique no local.')
    elif message.text.lower() == '11':
        bot.reply_to(message, 'Um pouco de ABÓBORA vai super bem! A receita da Vovó é: deixar as sementes em molho na água de um dia para o outro, secar naturalmente, torrá-la e triturá-la no liquidificador. Consuma três colheres (sopa) ao longo do dia.')
    elif message.text.lower() == '12':
        bot.reply_to(message, 'Um pouco de HORTELÃ vai super bem! A receita da Vovó é: preparar um chá com uma xícara (cafezinho) de folhas picadas em 500 ml de água. Tomar uma xícara de chá seis vezes ao dia.')
    elif message.text.lower() == '13':
        bot.reply_to(message, 'Um pouco de MIL EM RAMAS vai super bem! A receita da Vovó é: preparar uma tintura com uma xícara (cafezinho) da planta picada para cada cinco xícaras (cafezinho) de álcool. Tomar dez gotas em meia xícara de água duas vezes ao dia.')
    elif message.text.lower() == '14':
        bot.reply_to(message, 'Um pouco de BABOSA vai super bem! A receita da Vovó é: preparar um alcoolatura com 50 gramas de pedaços da folha em meio litro de álcool e água. Aplicar no local afetado em forma de compressas.')
    elif message.text.lower() == '15':
        bot.reply_to(message, 'Um pouco de ALFAZEMA vai super bem! A receita da Vovó é: preparar uma maceração com duas colheres (sopa) de flores secas em uma garrafa de vinho branco por três dias. Para banho de assento, colocar dez colheres de sopa para cada litro de água. Para sarnas, aplicar no local com algodão.')
    elif message.text.lower() == '16':
        bot.reply_to(message, 'Um pouco de TOMILHO vai super bem! A receita da Vovó é: preparar um cházinho com uma xícara (café) de material picado em 500 ml de água. Tomar uma xícara (chá) de duas à três vezes ao dia.')
    elif message.text.lower() == '17':
        bot.reply_to(message, 'Um pouco de MANJERICÃO vai super bem! A receita da Vovó é: preparar um cházinho com uma xícara (café) de folhas picadas em 500 ml de água. Tomar uma xícara de três em três horas.')
    elif message.text.lower() == '18':
        bot.reply_to(message, 'Um pouco de VINAGREIRA vai super bem! A receita da Vovó é: adicionar uma xícara de folhas e as raízes picadas, e cozidas por 5 minutos, em 500ml de água. Tomar durante o dia.')
    elif message.text.lower() == '19':
        bot.reply_to(message, 'Um pouco de AGRIÃO DO NORTE vai super bem! A receita da Vovó é: mastigar sem engolir duas à três flores sobre o local dolorido. Repita a mastigação enquanto achar necessário.')
    elif message.text.lower() == '20':
        bot.reply_to(message, 'Um pouco de NIRÁ vai super bem! A receita da Vovó é: faça um suco batendo e coando 1 medida de nirá com 5 medidas de água. Tome duas xícaras (café) ao dia. Também pode ser utilizada ncomo tempero na alimentação.')
    elif message.text.lower() == '21':
        bot.reply_to(message, 'Um pouco de CANA DO BREJO vai super bem! A receita da Vovó é: prepare um cházinho com duas colheres de broto picado em 1 litro de água. Tomar uma xícara de chá de hora em hora.')
    elif message.text.lower() == '22':
        bot.reply_to(message, 'Um pouco de POEJO vai super bem! A receita da Vovó é: 1 xícara da planta fresca em 500ml de água fervente, deixar tampado por 5 à 10 minutos. Tomar de 1 à 2 xícaras por dia.')
    elif message.text.lower() == '23':
        bot.reply_to(message, 'Um pouco de AÇAFRÃO vai super bem! A receita da Vovó é: colocar uma colher (sopa) de mel e uma de açafrão em pó um copo de leite quente. Ingira à vontade.')
    elif message.text.lower() == '24':
        bot.reply_to(message, 'Um pouco de MANJERICÃO vai super bem! A receita da Vovó é: preparar um cházinho com uma xícara (café) de folhas picadas em 500ml de água. Tomar uma xícara de três em três horas. Pode ser adoçado com 1 colher de sobremesa de mel.')
    elif message.text.lower() == '25':
        bot.reply_to(message, 'Um pouco de SERRALHA vai super bem! A receita da Vovó é: pilar 3 colheres (sopa) de folhas frescas picadas, adicionar uma colher (sopa) de glicerina e misturar até formar uma pasta. Colocar em uma gaze e aplicar sobre o local infectado de duas à três vezes ao dia.')
    elif message.text.lower() == '26':
        bot.reply_to(message, 'Um pouco de TOMILHO vai super bem! A receita da Vovó é: preparar um chazinho com uma xícara (café) de material picado em 1 xícara (chá) de água. Aplicar sobre o couro cabeludo por 15 minutos.')
    elif message.text.lower() == '27':
        bot.reply_to(message, 'Um pouco de AÇAFRÃO vai super bem! A receita da Vovó é: preparar uma mistura com meia colher (sopa) de açafrão com meia colher (sopa) de sal em um copo de água morna. Fazer gargarejos.')
    elif message.text.lower() == '28':
        bot.reply_to(message, 'Um pouco de ALFAVACA vai super bem! A receita da Vovó é: preparar um cházinho com uma xícara (café) de folhas picadas de alfavaca em 500ml de água. Tomar uma xícara de chá antes das refeições.')
    elif message.text.lower() == '29':
        bot.reply_to(message, 'Um pouco de FOLHA DA FORTUNA vai super bem! A receita da Vovó é: triturar duas folhas em meio copo de água. Tomar 20ml até os sintomas desaparecerem.')
    elif message.text.lower() == '30':
        bot.reply_to(message, 'Um pouco de GENGIBRE vai super bem! A receita da Vovó é: mascar um pedaço sempre que necessário.')
    elif message.text.lower() == '31':
        bot.reply_to(message, 'Um pouco de BABOSA vai super bem! A receita da Vovó é: cortar um pedaço do miolo da folha e aplicar no local com o auxílio de uma seringa.')
    elif message.text.lower() == '32':
        bot.reply_to(message, 'Um pouco de ALECRIM vai super bem! A receita da Vovó é: triturar dez xícaras (cafezinho) de folhas em 500ml de água ardente, deixando descansar por 8 dias. Tomar uma colher (chá) três vezes ao dia em um copo de água.')
    elif message.text.lower() == '33':
        bot.reply_to(message, 'Um pouco de BERTALHA vai super bem! A receita da Vovó é: consumir as folhas frescas em refogados ou em sopas.')
    elif message.text.lower() == '34':
        bot.reply_to(message, 'Um pouco de MELISSA vai super bem! A receita da Vovó é: preparar um chá com uma xícara (cafeziho) de folhas picadas em um copo de leite. Tomar um copo do chá (quente) antes de dormir.')
    elif message.text.lower() == '35':
        bot.reply_to(message, 'Um pouco de CAMOMILA vai super bem! A receita da Vovó é: preparar um chá com uma xícara (cafezinhho) da flor em 500ml de água. Tomar uma xícara de chá 6 vezes ao dia.')
    elif message.text.lower() == '36':
        bot.reply_to(message, 'Um pouco de GENGIBRE vai super bem! A receita da Vovó é: preparar um chá com uma colher (chá) da raiz triturada em uma xícara de água. Tomar quatro xícaras de chá durante o dia.')
    elif message.text.lower() == '37':
        bot.reply_to(message, 'Um pouco de ARTEMISIA vai super bem! A receita da Vovó é: preparar um chá com uma xícara (cafezinho) da planta picada em 500ml de água. Tomar quatro xícaras ao dia.')
    elif message.text.lower() == '38':
        bot.reply_to(message, 'Um pouco de MANJERICÃO vai super bem! A receita da Vovó é: preparar um chá com uma xícara (cafezinho) de folhas picadas em 500ml de água. Tomar uma xícara (chá) de seis em seis horas.')
    elif message.text.lower() == '39':
        bot.reply_to(message, 'Um pouco de MANJERICÃO vai super bem! A receita da Vovó é: preparar o chá com uma xícara (cafezinho) de folhas picadas em meio litro de água. Tomar uma xícara (chá) de três em três horas. (adoçar cada xícara com 1 colher e sobremesa de mel.')
    elif message.text.lower() == '40':
        bot.reply_to(message, 'Um pouco de BELDROEGA vai super bem! A receita da Vovó é: usar 20g de raiz para 1 litro de água, de modo com que resulte em uma espécie de líquido. Lavar o couro cabeludo.')
    elif message.text.lower() == '41':
        bot.reply_to(message, 'Um pouco de GENGIBRE vai super bem! A receita da Vovó é: preparar um cataplasma com gengibre bem moído ou ralado num pano. Aplicar diretamente no local afetado.')
    elif message.text.lower() == '42':
        bot.reply_to(message, 'Um pouco de GENGIBRE vai super bem! A receita da Vovó é: mascar um pedaço da raiz sempr que houver necessidade.')
    elif message.text.lower() == '43':
        bot.reply_to(message, 'Um pouco de GUACO vai super bem! A receita da Vovó é: preparar meio litro de xarope e acrescentar quatro xícaras (cafezinho) de sumo. Tomar uma colher de sopa de quatro a seis vezes ao dia.')
    elif message.text.lower() == '44':
        bot.reply_to(message, 'Um pouco de BÁLSAMO DO JARDIM vai super bem! A receita da Vovó é: comer na forma de salada (sem tempero).')
    elif message.text.lower() == '45':
        bot.reply_to(message, 'Um pouco de ALHO vai super bem! A receita da Vovó é: Ferver por 1 minuto, em leite açucarado, alguns dentes de alhos amassados. Tomar 2 a 3 colheres ao dia.')
    #para finalizar o processo
    elif message.text.lower() == 'SAIR' or message.text.lower() == 'sair' or message.text.lower() == 'Sair':
        bot.reply_to(message, 'Espero ter te ajudado! Até a próxima... Com carinho, Vovó <3.')
    #mensagem de erro
    else:
        bot.reply_to(message, 'Puxa! Opção inválida, tente novamente um número válido!')

bot.polling()