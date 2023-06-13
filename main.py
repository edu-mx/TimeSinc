'''
Programa simples para sincronizar o horário do Windows com o horário da Internet, útil nos casos em que seu computador não pode fazer isso automaticamente.
* by Eduardo Araújo - diaseduardo139@gmail.com
* Execute em um terminal como administrador
'''

import requests
from datetime import datetime
import os

def time_API():
    url = 'http://worldtimeapi.org/api/timezone/America/Sao_Paulo'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        hora = data['datetime']
        return hora[11:16]
    else:
        print('Não foi possível obter o horário da internet.')
        exit()

def time_system():
    hora = str(datetime.now())
    return hora[11:16]

def time_sinc():
    cmd = 'time ' +time_API()
    os.system(cmd)
    print('Horário definido para ', time_API())

hora_internet = time_API()
hora_system = time_system()
while True:
    if hora_system != hora_internet:
        print(f'Hora atual do sistema: {hora_system}\nHora atual da internet: {hora_internet}.')
        print('A hora do seu computador não está correta. quer corrigir?')
        question = input('S/sim, N/não')
        if question.upper() == 'S':
            time_sinc()
            break
        elif question.upper() == 'N':
            print('Saindo...')
            break
    else:
        print('A hora do seu sistema está sincronizada com a internet, você não precisa fazer nada')
        break
