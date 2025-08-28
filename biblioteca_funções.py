#1
def volume(raio:float)->float:
	PI=3.14
	v=((4 * PI* raio) / 3)
	return v
#2
def calculo_media(n1:float,n2:float,n3:float,letra:str)->float:
	if letra=='A':
		aritmetica= n1+n2+n3/3
		return aritmetica
	if letra=='P':
		ponderada=(n1*5)+(n2*3)+(n3*2)/3
		return ponderada
	if letra=='H':
		harmonica = 3/(1/n1 + 1/n2 + 1/n3)
		return harmonica
#3	
def primo(a:int)->str:
	if a>=1:
		if a%1==0 and a%a==0:
			return True
		elif a%1!=0 and a%a!=0:
			return False
#4
def bhaskara(a:int,b:int,c:int)->float:
	delta= (b**2)-(4*a*c)
	raiz_delta= delta**0,5
	valor_x1= (-(b)+ raiz_delta)//(2*a)
	valor_x2= (-(b)- raiz_delta)//(2*a)
	return valor_x1,valor_x2
#5
def tempo(segundos:int)->int:
	minutos= segundos//60
	horas= segundos//3600
	return segundos, minutos, horas
#6	
def idade(anos:int, meses:int, dias:int)->int:
	a= anos*360
	m= meses*30
	d= dias*1
	idade_em_dias= a+m+d
	return(idade_em_dias)
#7
def num_perfeito(num:int)->str:
	divisores=[]
	for x in (1,num-1):
		if num%x ==0:
			divisores=divisores.append(x)
	soma= sum(divisores)
	if soma==num:
		return True
	else:
		return False
#8
def categoria_nadador(idade:int)->str:
	if idade>=5 and idade<=7:
		return('Infantil A')
	if idade>=8 and idade<=10:
		return('Infantil B')
	if idade>=11 and idade<=13:
		return('Juvenil A')
	if idade>=14 and idade<=17:
		return('Juvenil B')
	if idade>=18:
		return('Adulto')
#9
def par_impar(num:int)->str:
	return('Impar : False / Par : True')
	if num%2==0:
		return True
	else: 
		return False
#10
def media_conceito(media:float)->str:
	if media>=0.0 and media<=4.9:
		return('D')
	if media>=5.0 and media<=6.9:
		return('C')
	if media>=7.0 and media<=8.9:
		return('B')
	if media>=9.0 and media<=10.0:
		return('A')
#11
def peso_ideal(altura:float,sexo:str)->float:
	try:
		if sexo=='F' or sexo=='M':
			if sexo=='F':
				peso_ideal_fem= (62.1*altura)-44.7
				return peso_ideal_fem
			if sexo=='M':
				peso_ideal_masc= (72.7*altura)-58
				return peso_ideal_masc
	except ValueError:
		print('Erro: Você deve digitar o parâmetro "sexo" como "F" se feminino e "M" se masculino')
#12	
def ordene(a:int,b:int,c:int)->int:
	lista=[a,b,c]
	lista.sort()
	for x in len(lista):
		return(x,end==' ')

#13
#14
#15
def triangulos(x,y,z):
	if x<(y+z) and y<(x+z) and z<(y+x):
		if x==y and x==z:
			return('Triângulo Equilátero')
        if x!=y and x!=z:
            return("Triângulo Escaleno")
        else:
            return('Triângulo Isósceles')
    else:
		return('Não é um triângulo')

#16
def cidade():
	salarios=[]
	pessoas=0
	filhos=[]
	pessoas_salario_limite=0

	flag=True
	while flag==True:
		try:
			a=float(input())
			if a<0:
				raise ValueError
			else:
				salarios.append(a)
			if a<1350:
				pessoas_salario_limite+=1
			b=int(input())
			if b<0:
				raise ValueError
			else:
				filhos.append(b)
			pessoas+=1
		except:
			print (ValueError)

	print(f'Média Salarial:{sum(salarios)//pessoas}')
	print(f'Média Filhos:{sum(filhos)//pessoas}')
	print(f'Maior Salário:{max(salarios)}')
	print(f'Percentual pessoas com salário<= $1350:{(pessoas_salario_limite//pessoas)*100:.2f}')
        
#17
def media ():
	lista=[]
	while True:
		try:
			a=int(input())
			if a<0:
				raise ValueError
			else:
				lista.append(a)
		except:
			print(ValueError)
	media_=sum(lista)//len(lista)
	return media_

#18
def fatorial(num):
	try:
		if num<0:
			raise ValueError
		a=int(num)
		if num==0:
			return 0
		if num==1:
			return 1
		if num==2:
			return 2
		if num>2:				
			r=2
		for x in range(3,num):
				r=x*r
		return r
	except:
		print(ValueError)

#19
def valores_50():
	contador=0
	lista=[]
	while contador<=50:
		entrada=int(input())
		lista.append(entrada)
	return max(lista), min(lista)

#20

#21
def dividores(num):
	divisores=0
	for x in range(0,num):
		if num%x==0:
			divisores+=1
	return divisores

#22
def somatorio(num):
	divisores=[]
	for x in range(0,num):
		if num%x==0:
			divisores.append(x)
	return sum(divisores)

#23
def formula_1(num):
	from fracions import Fraction
	try:
		num=int(num)
		if num<0:
			raise ValueError
		s= 1+ 0.5 + fraction(1,3) +0.25+0.20+fraction(1,num)
		return s
	except:
		print(ValueError)

#24
def formula_2(num):
	from fracions import Fraction
	try:
		num=int(num)
		if num<0:
			raise ValueError
		if num==0:
			fatorial=0
		if num==1:
			fatorial= 1
		if num==2:
			fatorial=2
		if num>2:				
			r=2
		for x in range(3,num):
				r=x*r
		fatorial=r
		s= 1+ 1+0.5 + fracion(1,6) +(1,fatorial)
		return s
	except:
		print(ValueError)
#25
def potencia(x,z):
	passagem=0
	r=x*x
	while passagem<z:
		r=x*r
	return r
#26
def fatorial_recursivo(num):
	if num==1:
		return 1 
	return n*fatorial_recursivo(num-1)

#27
def somatorio_recursivo(num):
    if num == 1:
        return 1
    else:
        return num + somatorio_recursivo(num - 1)
	
#28
def soma_vetor_recursiva(vetor, indice=0):
    if indice == len(vetor):
        return 0
    else:
        return vetor[indice] + soma_vetor_recursiva(vetor, indice + 1)

#29
def inverter_string_recursiva(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + inverter_string_recursiva(s[:-1])

#30