usuario = input ('Digite seu usuário: ')
senha = int( input ('Digite a sua senha: '))
cont = 2

while usuario != 'admin' or senha != 123:
	print ('Usuário ou senha inválidos. Tente novamente.')
	usuario = input ('Digite seu usuário: ')
	senha = int(input ('Digite sua senha: '))
	cont = cont - 1
	if cont == 0:
		break
	else:
		print ('Acesso liberado.')