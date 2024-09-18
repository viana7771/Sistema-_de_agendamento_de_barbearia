print('Fiu da Navalha!\n')
print('1 - Agendar horário')
print('2 - Mostrar clientes agendados')
print('3 - Excluir clientes agendados')
print('4 - Finalizar programa\n')

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Valor incoreto, por favor digite uma das opções.')
        match opcao:
            case 1: agendar_horarios
            case 2: mostrar_clientes_agendados
            case 3: excluir_clientes_agendados
            case 4:
                print('Finalizar programa.') 
            case _:
                print('Opçao invalida, digite o numero da opção que deseja escolher: ') 

escolher_opcao()

def agendar_horarios():
    pass

def mostrar_clientes_agendados():
    pass

def excluir_clientes_agendados():
    pass