def linha(caracter='-', tamanho=42):
    print(caracter * tamanho)


def cabecario():
    linha(tamanho=68)
    print("""
   _____           _                 _____ _____ _______ 
  / ____|         | |               / ____/ ____|__   __|
 | |  __  ___  ___| |_ __ _  ___   | (___| (___    | |   
 | | |_ |/ _ \/ __| __/ _` |/ _ \   \___ \\___ \    | |   
 | |__| |  __/\__ \ || (_| | (_) |  ____) |___) |  | |   
  \_____|\___||___/\__\__,_|\___/  |_____/_____/   |_|   
""")
    print('Sistem de Gestão em Saúde e Segurança do Trabalho'.center(56))
    linha(tamanho=68)
    print()


def leiaint(msg):
    while True:
        try:
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido!\33[m]]')
        except KeyboardInterrupt:
            print('\033[31m\nEntrada de lib interrompida pelo usuário\033[m')
            return 0
        else:
            return numero

def titulo(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista, msg='MENU PRINCIPAL'):
    titulo(msg)

    for e, item in enumerate(lista):
        print(f'[{e + 1}] {item}')
    linha()

    opc = leiaint('Sua opção: ')
    return opc
