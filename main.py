from jappalibs.interface import *
from time import sleep

cabecario()

while True:
    resp = menu(['Rotinas SSMA', 'Checklist', 'Treinamentos', 'Sair'])

    if resp == 1:
        opc = menu(['Ambientação', 'DDS', 'Permissão de Trabalho', 'Diário de Campo', '<- Voltar'], 'ROTINAS SSMA')

        if opc == 1:
            meu_menu = menu(['Nova ambientação', 'Ficha de EPI', 'Ordem de serviço', '<- Voltar'], 'AMBIENTAÇÃO')
        
        elif opc == 2:
            meu_menu = menu(['Informar tema', 'Inserir data manual', 'Equipes', '<- Voltar'], 'DIÁLOGO DE SEGURANÇA')
        
        elif opc == 3:
            meu_menu = menu(['Preencher PT', 'Consultar PT', '<- Voltar'], 'PERMISSÃO DE TRABALHO')
        
        elif opc == 4:
            titulo('DIÁRIO DE CAMPO')
        
        elif opc == -1:
            continue
    
    elif resp == 2:
        meu_menu = menu(['Forma de alumínio', 'Máquinas rotativas', 'Máquinas pesadas', 'Máquina de solda', '<- Voltar'], 'CHECKLIST')
    
    elif resp == 3:
        meu_menu = menu(['Lista de presença', 'Certificados', '<- Voltar'], 'TREINAMENTOS')
    
    elif resp == 4:
        print('Salvando as alterações...')
        sleep(2)
        print('Sistema finalizado!')
        break
    
    else:
            print('\033[mERRO: Opção inválida! Tente novamente.\033[m')
