import telebot
import requests
from weatherAPI.secrets import api_tkey
from weatherAPI.secrets import  API_KEY
from weatherAPI.secrets import  BASE_URL


bot = telebot.TeleBot(api_tkey)

@bot.message_handler(commands=["aqui"])
def opcao1(msg):
    bot.send_message(msg.chat.id, "Digite a cidade a qual deseja obter informações. ")
    global msg2
    msg2 = msg.text
    return  msg2


@bot.message_handler(content_types=['text'])
def command_text_hi(msg):
    city = msg.text

    request_url = f"{BASE_URL}?appid={API_KEY}&lang=pt&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        # coletando a tempo
        weather = data['weather'][0]['description']
        # coventer para celsius e arredondar o valor
        temperature = round(data['main']['temp'] - 273.15)
        #temperaturas max/min
        temp_max = round(data['main']['temp_max'] - 273.15)
        temp_min = round(data['main']['temp_min'] - 273.15)
        #humidade
        humidade = data['main']['humidity']
        int(temp_max)
        int(temp_min)
        int(temperature)


        bot.send_message(msg.chat.id, f"""
    No momento, a temperatura em {city} é de {temperature}°C
    \n-{weather.capitalize()}.
    \nTemperatura minima de {temp_min}°C
    \nTemperatura máxima de {temp_max}°C
    \nHumidade do ar: {humidade}%
    
    """ )
        bot.send_message(msg.chat.id, "Digite o nome de outra cidade para continuar. ")

def verify(msg):
    return True

@bot.message_handler(func=verify)
def resposta(msg):
    texto = "Eu sou o bot que informa as condições climáticas em tempo real! \n \n Clique /aqui para começar. "
    bot.reply_to(msg, texto)



bot.polling()

