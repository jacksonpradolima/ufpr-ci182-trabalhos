import requests
import json

def localizacao(cid,state):
	cidade = cid
	estado = state
	requisição = requests.get("http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+cidade+"&state="+estado+"&token=cb687205e4827654ae34805feff813e1")
	loc=json.loads(requisição.text)
	lista_loc=list(loc)
	id_cid=str(lista_loc[0]['id'])
	name_cid=lista_loc[0]['name']
	name_state=lista_loc[0]['state']
	name_country=lista_loc[0]['country']
	return name_cid,name_state,id_cid,name_country

def dados_momento_info_clima(cid,state):
	name_cid,name_state,id_cid,name_country = localizacao(cid,state)
	id_cid= id_cid
	requisição = requests.get("http://apiadvisor.climatempo.com.br/api/v1/weather/locale/"+id_cid+"/current?token=cb687205e4827654ae34805feff813e1")
	lista_prev=json.loads(requisição.text)
	temp=lista_prev['data']['temperature']
	wind_direction=lista_prev['data']['wind_direction']
	wind_velocity=lista_prev['data']['wind_velocity']
	humidity=lista_prev['data']['humidity']
	condition=lista_prev['data']['condition']
	pressure=lista_prev['data']['pressure']
	sensation=lista_prev['data']['sensation']
	date=lista_prev['data']['date']
	return temp,wind_velocity,wind_direction,humidity,condition,pressure,sensation,date,name_cid,name_state,id_cid,name_country

def dados_momento_info_open(cid_info):
	cid_info = cid_info
	requisição = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+cid_info+'&appid=032724f464f443a20fa48ca83b587ecd')
	lista_prev=json.loads(requisição.text)
	condition = lista_prev['weather'][0]['description']
	temp = lista_prev['main']['temp']
	temp_max = lista_prev['main']['temp_max']
	temp_min = lista_prev['main']['temp_min']
	pressure = lista_prev['main']['pressure']
	humidity = lista_prev['main']['humidity']
	wind_speed = lista_prev['wind']['speed']
	country = lista_prev['sys']['country']
	cid = lista_prev['name']
	return cid, country, humidity, pressure, temp_min, temp_max, temp, wind_speed, condition
