'''
script para alterar data e hora do computador
* by Eduardo Araújo - diaseduardo139@gmail.com
* Execute em um terminal como administrador
'''

import requests
from datetime import datetime
import os


class API():
    url = 'http://worldtimeapi.org/api/timezone/America/Sao_Paulo'
    time = ''
    date = ''
    def __init__(self):
        try:
            response = requests.get(self.url)

            if response.status_code == 200:
                dados = response.json()
                data_hora = dados['datetime']
                self.time = data_hora[11:16]
                self.date = data_hora[:10]

            else:
                print('Não foi possível obter o horário da internet.')
                raise
        except Exception as erro:
            print('Erro, não foi possível conectar-se a internet.'+str(erro))
            raise


class Computer():
    dados = datetime.now()
    time = ''
    date = ''
    def __init__(self):
        data_hora= str(self.dados)
        self.time = data_hora[11:16]
        self.date = data_hora[:10]

computador = Computer()
internet = API()

# funções para sincronizar
def timesinc():
    dados = API()
    cmd = 'time '+dados.time
    os.system(cmd)
    print('horário ajustado...')
    return

def datesinc():
    internet_data = API()
    data_EUA = datetime.strptime(internet_data.date, "%Y-%m-%d")
    data_Br = data_EUA.strftime("%d/%m/%Y")
    os.system('date '+ str(data_Br))
    print('Data ajustada...')
    loop_time()

def loop_time():
    while True:

        if internet.time != computador.time:
            print(f'Hora da internet: {internet.time}.\nHora do sistema: {computador.time}.')
            option_time = input('O horário precisa ser ajustado, deseja fazer isso agora?\tS/sim, N/não.')

            if option_time.upper() == 'N':
                print('Saindo sem ajustar a hora...')
                break

            elif option_time.upper() == 'S':
                timesinc()
                break

        else:
            print('A hora não precisa ser ajustada, fique tranquilo!')
            break

def loop_date():
    while True:

        if internet.date != computador.date:
            print(f'Data do sistema: {computador.date}.\nData da internet: {internet.date}.')
            option_date = input('A data precisa ser ajustada, deseja fazer isso agora?\tS/sim, N/não.')

            if option_date.upper() == 'N':
                print('Saindo sem ajustar a data...')
                loop_time()
                break

            elif option_date.upper() == 'S':
                datesinc()
                break

        else:
            print('A data não precisa ser ajustada, fique tranquilo!')
            loop_time()
            break

def main():
    loop_date()

main()
