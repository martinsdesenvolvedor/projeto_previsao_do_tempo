from django.shortcuts import render
from django.http import HttpResponse
from dotenv import load_dotenv
import os
import requests

# Create your views here.
load_dotenv()
def tempo(request):
    if request.method == 'GET':
            return render(request, 'home.html')
    elif request.method == 'POST':
        API_KEY = os.getenv('API_KEY')
        cidade = request.POST.get('cidade').title()
        link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},BR&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link)
       
        if requisicao.status_code == 200:
            requisicao_dic = requisicao.json() # aqui traz as informaçoes em json
            
            icone = requisicao_dic['weather'][0]['icon']
            icone_img = f'http://openweathermap.org/img/wn/{icone}.png'

            descricao = requisicao_dic['weather'][0]['description'].title()
            temperatura = int(requisicao_dic['main']['temp'] - 273.15)
            pressao = requisicao_dic['main']['pressure'] 
            umidade = requisicao_dic['main']['humidity'] 
           
            temperatura_minima = int(requisicao_dic['main']['temp_min'] - 273.15)
            temperatura_maxima = int(requisicao_dic['main']['temp_max'] - 273.15)
       
         

            print(temperatura, temperatura_minima, temperatura_maxima, pressao, umidade, descricao)
            return render(request, 'previsao.html', {'cidade': cidade, 'temperatura': temperatura, 'descricao': descricao, 'temperatura_minima': temperatura_minima, 'temperatura_maxima': temperatura_maxima, 'pressao': pressao, 'umidade': umidade, 'icone_img': icone_img})

        else:
             return HttpResponse(f'Erro na requisição: {requisicao.status_code}')
         
        


