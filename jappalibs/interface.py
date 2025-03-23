def linha(caracter='-', tamanho=60):
    print(caracter * tamanho)


def cabecario():
    linha()
    print("""
   _____           _                 _____ _____ _______ 
  / ____|         | |               / ____/ ____|__   __|
 | |  __  ___  ___| |_ __ _  ___   | (___| (___    | |   
 | | |_ |/ _ \/ __| __/ _` |/ _ \   \___ \\___ \    | |   
 | |__| |  __/\__ \ || (_| | (_) |  ____) |___) |  | |   
  \_____|\___||___/\__\__,_|\___/  |_____/_____/   |_|   
""")
    print('Sistem de Gestão em Saúde e Segurança do Trabalho'.center(56))
    linha()
    print()
cabecario()