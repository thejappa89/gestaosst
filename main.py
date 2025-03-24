from jappalibs.interface import *
from time import sleep

cabecario()

while True:
    resp = menu(['Rotinas SSMA', 'Checklist', 'Treinamentos', 'Sair'])

    if resp == 1:
        opc = menu(['Ambientação', 'DDS', 'Permissão de Trabalho', 'Diário de Campo', '<- Voltar'], 'ROTINAS SSMA')

        if opc == 1:
            titulo('AMBIENTAÇÃO')
        
        elif opc == 2:
            titulo('DDS')
        
        elif opc == 3:
            titulo('PERMISSÃO DE TRABALHO')
        
        elif opc == 4:
            titulo('DIÁRIO DE CAMPO')
        
        elif opc == -1:
            continue
    
    elif resp == 2:
        titulo('CHECKLIST')
    
    elif resp == 3:
        titulo('TREINAMENTOS')
    
    elif resp == 4:
        print('Salvando as alterações...')
        sleep(2)
        print('Sistema finalizado!')
        break
    
    else:
            print('\033[mERRO: Opção inválida! Tente novamente.\033[m')
