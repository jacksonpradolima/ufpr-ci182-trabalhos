import tweepy
import random

# DADOS DA CONTA DO BOT NO TWITTER
CONSUMER_KEY = 'AhpIWmebOsOtBCZsjgSSuZxVA'
CONSUMER_SECRET = '97D9jpoR6M4bhwkYecAh6mlwVda0LbwU7AJaGeSyBe3508nuOk'
ACCESS_KEY = '1138937981409083392-Uvp3UNxBMVIGEfT1XRuAemCC1qpDby'
ACCESS_SECRET = 'ouaPIkgMXcgkIw3WZVlPz6P1YxynoVS5IzUtUzsvTxAe4'

# INSERIR AS INFORMAÇÔES DA CONTA DO TWITTER NO PROGRAMA
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

arquivo = 'armazenamento_de_id.txt'


def armazenar_id(id_repetido, arquivo):
    escrever_id = open(arquivo, 'a+')
    escrever_id.write(str(id_repetido)+";")
    escrever_id.close()
    return


def devolver_id(arquivo):
    ler_id = open(arquivo, 'r')
    id_repetido = ler_id.read().strip()
    ler_id.close()
    return id_repetido


charadas = ['O que é um ponto verde na parede?' + 60*' ' + 'Uma ervilha caindo de paraquedas',
            'O que é uma minhoca com sono?' + 55*' ' + 'Uma dorminhoca',
            'O que o pato disse pra pata durante o jogo?' + 50*' ' + 'Estamos empatados',
            'Qual o vinho que não tem álcool?' + 50*' ' + 'O-vinho de codorna',
            'Qual a comida que liga e desliga?' + 60*' ' + 'Strog(on)off']

musicas = ['Portal - Still alive https://www.youtube.com/watch?v=Y6ljFaKRTrI&t=28s',
           'Portal 2 - Want you gone https://www.youtube.com/watch?v=dVVZaZ8yO6o',
           'Poppy - Computer boy https://www.youtube.com/watch?v=5Ao5mg11xIk',
           'hello world https://www.youtube.com/watch?v=Yw6u6YkTgQ4',
           'Computer error song https://www.youtube.com/watch?v=mKkLjJHwRec',
           'Elektronik supersonik https://www.youtube.com/watch?v=MNyG-xu-7SQ']

ultimo_id = devolver_id(arquivo)
mentions = api.mentions_timeline(ultimo_id)

for mention in mentions:

    print(str(mention.id) + ' - ' + mention.text)
    id_repetido = mention.id

    armazenar_id(id_repetido, arquivo)

    if 'piada' in mention.text.lower():
        print("Contando uma piada!")
        api.update_status('@' + mention.user.screen_name +
                          ' ' + random.choice(charadas), mention.id)

    elif 'amo esse bot' in mention.text.lower():
        print(":o")
        api.retweet(mention.id)

    elif 'musica' in mention.text.lower():
        print("Vou cantar uma música pra você.")
        api.update_status('@' + mention.user.screen_name +
                          ' ' + random.choice(musicas), mention.id)

    elif 'testando' in mention.text.lower():
        print("Opa!")
        api.update_status('@' + mention.user.screen_name +
                          ' ' + 'Olá!', mention.id)
