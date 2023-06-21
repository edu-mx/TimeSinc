'''
Programa simples para sincronizar o horário do Windows com o horário da Internet, útil nos casos em que seu computador não pode fazer isso automaticamente.
* by Eduardo Araújo - diaseduardo139@gmail.com
* Execute em um terminal como administrador
'''

import requests
from datetime import datetime
import os

# Dados da internet
class API():
    url = 'http://worldtimeapi.org/api/timezone/America/Sao_Paulo'
    def time(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                dados = response.json()
                hora = dados['datetime']
                return hora[11:16]

            else:
                print('Não foi possível obter o horário da internet.')
                exit()
        except Exception as erro:
            print('Erro, não foi possível conectar-se a internet.'+str(erro))
            exit()

    def date(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                dados = response.json()
                data = dados['datetime']
                return data[:10]

            else:
                print('Erro, Não foi possível obter a data da internet.')
                exit()
        except Exception as erro:
            print('Erro, não foi possível conectar-se a internet.'+str(erro))
            exit()

# dados do computador
class computer():
    dados = datetime.now()
    def time(self):
        hora= str(self.dados)
        return hora[11:16]

    def date(self):
        data = str(self.dados)
        return data[:10]

computador = computer()
internet = API()

# funções para sincronizar
def timesinc():
    nova_hora = API()
    cmd = 'time '+nova_hora.time()
    os.system(cmd)
    print('Horário alterado com sucesso!')
    exit()

def datesinc():
    dados = API()
    date_split = dados.date().split('-')
    new_date = '{}/{}/{}'.format(date_split[2], date_split[1], date_split[0])
    os.system('date '+new_date)
    print('Data alterada com sucesso!'+new_date)
    step_time()

loop = True
def step_time():
    loop = False
    while True:
        if internet.time() != computador.time():
            print(f'Hora da internet: {internet.time()}.\nHora do sistema: {computador.time()}.')
            option_time = input('O horário precisa ser ajustado, deseja fazer isso agora?\tS/sim, N/não.')
            if option_time.upper() == 'N':
                print('Saindo sem ajustar a hora...')
                break
            elif option_time.upper() == 'S':
                timesinc()
                break

        else:
            print('A hora não precisa ser ajustada, fique tranquilo!')
            exit()

def step_date():
    while loop!=False:
        if internet.date() != computador.date():
            print(f'Data do sistema: {computador.date()}.\nData da internet: {internet.date()}.')
            option_date = input('A data precisa ser ajustada, deseja fazer isso agora?\tS/sim, N/não.')
            if option_date.upper() == 'N':
                print('Saindo sem ajustar a data...')
                step_time()
            elif option_date.upper() == 'S':
                datesinc()

        else:
            print('A data não precisa ser ajustada, fique tranquilo!')
            step_time()

def main():
    step_date()
main()