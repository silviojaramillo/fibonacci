###################################################
# Crear un programa que calcule 16 términos de la #
# sucesión de Fibonacci.                          #
# sucesión = 0,1,1,2,3,5,8,13,21,34...            #
###################################################

#Creando una lista para los valores de la sucesión
fibonacci = [0,1]
#Agregando los valores correspondientes a cada 
#posición de acuerdo a la secuencia
for i in range(1,15):
    valor = fibonacci[i-1] + fibonacci[i]
    fibonacci.append(valor)
#Mostrando los valores en la consola
salida = '0'
for j in range(1,len(fibonacci)):
  salida = salida + ',' + str(fibonacci[j])
print(salida)
