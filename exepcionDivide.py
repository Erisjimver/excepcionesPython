def divide():

	try:

		op1=(float(input("intoduce un numero: ")))
		op2=(float(input("introduce el segundo numero: ")))

		print("La division es: "+str(op1/op2))
	except ValueError:
		print("Valor introducido erroneo...")
	except ZeroDivisionError:
		print("No se puede dividir entre 0...")
	finally:
		print("finalizado..")
		
divide()