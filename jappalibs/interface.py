def linha(caracter='-', tamanho=42):
    print(caracter * tamanho)


def cabecario():
    linha()
    print(""" _____  _____  _____  _____   ____  _____ 
/  ___|/  ___||_   _||____ | / ___||  _  |
\ `--. \ `--.   | |      / // /___ | |/' |
 `--. \ `--. \  | |      \ \| ___ \|  /| |
/\__/ //\__/ /  | |  .___/ /| \_/ |\ |_/ /
\____/ \____/   \_/  \____/ \_____/ \___/ 
                                          """)
    print('Sistem de Gestão em Saúde e Segurança do Trabalho'.center(42))
    linha()
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
