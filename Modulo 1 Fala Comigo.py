
def memory_user(email, options):
   """
   Guarda o email do usuário e seu histórico de navegação no bot em um dicionário.
 KArgs:
   param email: input email as string
   param options: list of strings


 Returns:
   dict_user
   """
   dict_user = {email: list_options}
   print("Obrigado")
   print(dict_user)  #remover prints depois
   return dict_user




def memory_chat(list_options, option):
   """
   Guarda as opções selecionadas pelo usuário em uma lista.
 Args:
   param email: input email as string
   param options: list of strings


 Returns:
   none
   """
   list_options.append(option)
   
  


def parse(value):
   """
   Valida o input como um número inteiro de 0 a 4.
 Args:
   param value: input number as string


 Returns:
   value int
   """
   try:
    
       value = int(value)  #exceção de converter int() cai no except
       if value in list(range(0,5)):
           return value
       else:
           raise ValueError  #forçou que qualquer valor no else (fora da lista) vire uma exceção e caia no except
           #OBS: É POSSÍVEL FAZER COM APENAS IF E ELSE, FIZ COM RAISE SÓ PRA TREINAR


   except:  #só vai entrar no except quando for exceção, diferentemente do else
       value = input("Valor inválido. Digite um número inteiro viável: ")
       parse(value)


list_options = []


print("\n","-" * 40, "\nBem vindo a Bendito Tour\nSua empresa de viagens que é a glória.\n","-" * 40,"\n")


op = 4
  
while (op >= 4):
  
   if op == 4:
       print("Olá! Eu sou Benedito. Seu atendente virtual.\nEstou aqui especialmente para atender você.\nEm que posso ajudar?\nDigite a opção desejada: ")
       print("1 - Reservas\n2 - Comercial\n3 - Financeiro\n0 - Sair\n")
  
       op = parse(input())


       if op == 1:
           op = ("RESERVAS")
           memory_chat(list_options, op)
          
           print("\nRESERVAS\n\nQue legal! Quer saber sobre nossas reservas.\nEscolha uma opção que eu te ajudarei.\nDigite a opção desejada: ")
           print("1 - Hospedagens disponíveis\n2 - Como fazer sua reserva\n3 - Como cancelar sua reserva\n4 - Voltar\n")


           op = int(input())
      
           if op == 1:
               op = ("HOSPEDAGENS DISPONÍVEIS")
               memory_chat(list_options, op)


               print("\nHOSPEDAGENS DISPONÍVEIS\n\nVai conhecer agora os lugares mais bonitos do Brasil.\nDigite a opção desejada: ")
               print("1 - Rio de Janeiro\n2 - Porto Seguro\n3 - Natal\n4 - Voltar\n")


               op = int(input())


               if op == 1:
                   op = ("Gamboa Rio Hotel")
                   memory_chat(list_options, op)
                   print("\nGamboa Rio Hotel\nDiária a partir de R$ 100,00\n4 - Voltar\n")
              
                   op = int(input())
              
               elif op == 2:
                   op = ("Hotel Fenix")
                   memory_chat(list_options, op)
                   print("\nHotel Fenix\nDiária a partir de R$ 145,00\n4 - Voltar\n")
              
                   op = int(input())
              
               elif op == 3:
                   op = ("Yak Beach Hotel")
                   memory_chat(list_options, op)
                   print("\nYak Beach Hotel\nDiária a partir de R$ 192,00\n4 - Voltar\n")
              
                   op = int(input())
              
              
           elif op == 2:
               op = ("COMO FAZER SUA RESERVA")
               memory_chat(list_options, op)


               print("\nCOMO FAZER SUA RESERVA\n\nNão tem nenhum mistério. Veja como é fácil:\nDigite a opção desejada:")
               print("Ligue para o telefone (XX)XXX-XXXXX e faça já sua reserva\n4 - Voltar\n")
          
               op = int(input())
          
           elif op == 3:
               op = ("COMO CANCELAR SUA RESERVA")
               memory_chat(list_options, op)


               print("\nCOMO CANCELAR SUA RESERVA\n\nNão vai poder viajar agora? Que pena.\nMas estaremos de braços abertos para próxima oportunidade.")
               print("Ligue para o telefone (XX) XXX-XXXXX e faça o cancelamento de sua reserva.\n4 - Voltar\n")
          
               op = int(input())
                  
       elif op == 2:
           op = ("COMERCIAL")
           memory_chat(list_options, op)


           print("\nCOMERCIAL\n\nMuito bem. Agora me indique o que precisa saber.\nDigite a opção desejada:")
           print("1 - Formas de pagamento\n2 - Pacotes promocionais\n4 - Voltar\n")
  
           op = int(input())
  
           if op == 1:
               op = ("FORMAS DE PAGAMENTO")
               memory_chat(list_options, op)


               print("\nFORMAS DE PAGAMENTO\n\nCom essa molezinha, seu sonho de viagem fica mais real.\nDigite a opção desejada:")
               print("1 - À vista\n2 - PIX\n3 - Cartão de crédito\n4 - Voltar\n")
      
               op = int(input())
      
               if op == 1:
                   op = ("À vista")
                   memory_chat(list_options, op)
                   print("\nCom desconto de 10%\n4 - voltar\n")
          
                   op = int(input())
          
               elif op == 2:
                   op = ("PIX" )
                   memory_chat(list_options, op)
                   print("\nCom desconto de 10%\n4 - Voltar\n")
          
                   op = int(input())
          
               elif op == 3:
                   op = ("Cartão de crédito")
                   memory_chat(list_options, op)
                   print("\nParcelado em até 05 vezes\n4 - Voltar\n")
          
                   op = int(input())
          
           elif op == 2:
               op = ("PACOTES PROMOCIONAIS")
               memory_chat(list_options, op)


               print("\nPACOTES PROMOCIONAIS\n\nOs melhores preços estão aqui.\nDigite a opção desejada:")
               print("1 - Rio de Janeiro\n2 - Buenos Aires\n3 - Outras Ofertas\n4 - Voltar\n")
      
               op = int(input())
      
               if op == 1:
                   op = ("Promoção Rio de Janeiro")
                   memory_chat(list_options, op)
                   print("\nVoo para o Rio de Janeiro ida e volta a partir de R$ 640,00 (Consulte condições)\n4 - Voltar\n")
          
                   op = int(input())
          
               elif op == 2:
                   op = ("Promoção Buenos Aires")
                   memory_chat(list_options, op)
                   print("\nVoo para Buenos Aires ida e volta a partir de R$ 1.740,00 (Consulte condiçoes)\n4 - Voltar\n")
          
                   op = int(input())
          
               elif op == 3:
                   op = ("Outras ofertas")
                   memory_chat(list_options, op)
                   print()
                   print("Ofertas de passagens a partir de R$ 299,00 (Consulte condiçoes")
                   print("4 - Voltar")
          
                   op = int(input())
  
       elif op == 3:
           op = ("FINANCEIRO")
           memory_chat(list_options, op)


           print("\nFINANCEIRO\n\nBem vindo ao setor financeiro.\nDigite a opção desejada:")
           print("1 - Código de barras\n2 - Faturas vencidas\n4 - Voltar\n")
      
           op = int(input())


           if op == 1:
               op = ("Código de barras")
               memory_chat(list_options, op)
               print("Para gerar seu boleto acesse: https://bit.ly/boletoxxxxx\n4 - Voltar\n")
          
               op = int(input())
          
           elif op == 2:
               op = ("Faturas vencidas")
               memory_chat(list_options, op)
               print("Para conhecer faturas vencidas acesse: https://bit.ly/faturayyyyy\n4 - Voltar\n")
          
               op = int(input())


       elif (op == 0):
           email = input("Para encerrar experiência, digite seu email: ")
           memory_user(email, list_options)
           print ("Agradecemos sua visita, volte sempre.")
      
           break


