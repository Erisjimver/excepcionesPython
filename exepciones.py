def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1, num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "operacion erronea..."

op1=(int(input("Introduce el primer numero: ")))
op2=(int(input("Introduce el segundo numero: ")))

operacion=input("Introduce la operacion deseada (suma,resta,multiplica,divide): ")
#print(str(operacion))


if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print("error: no se reconoce operacion solicitada...")

print("funciona la exepcion..")