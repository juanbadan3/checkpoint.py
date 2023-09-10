# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def numeroBinario(numero):
    '''
    Esta función recibe como argumento un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    #Tu código aca:
def NumeroBinario(numero):
    if isinstance(numero, int) and numero >= 0:
        binario_str = format(numero, 'b')  # Convierte a binario como cadena de texto
        binario_int = int(binario_str)  # Convierte la cadena binaria en entero
        return binario_int
    else:
        return None
    
resultado1 = NumeroBinario(12)
resultado2 = NumeroBinario(2)
resultado3 = NumeroBinario(14)

print(resultado1)  
print(resultado2)  
print(resultado3)


def dividirMultiplicar(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar una lista con los siguientes parámetros:
   1.Los números que sean positivos y pares se deben dividir por 2, y el resultado expresado como entero (sin decimales, no redondeando, debe tomar sólo la parte entera de la división por 2).
   2.Los números negativos multiplicados por 2.
   3.Los que no cumplan los criterios anteriores deben quedar igual al valor original.
   4.Ordernar los números de mayor a menor.
   Ej: dividirMultiplicar([2,4,1,-3]): debe retornar: [2, 1, 1, -6]
   '''   
   #Tu código acá
def dividirMultiplicar(lista):
    resultado = []
    for numero in lista:
        if numero > 0 and numero % 2 == 0:          
            resultado.append(numero // 2)
        elif numero < 0:            
            resultado.append(numero * 2)
        else:            
            resultado.append(numero)
    
    resultado.sort(reverse=True)

    return resultado
entrada = [2, 4, 1, -3]
resultado = dividirMultiplicar(entrada)
print(resultado)
   

def crearDiccionario(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar un diccionario con tres claves, "multiplos3", 'cuadrados", "menores_promedio".
   Para la clave "multiplos3", el valor debe ser una lista con los múltiplos de 3 de la lista original.
   Para la clave "cuadrados", el valor debe ser una lista con los valores de la lista original elevados al cuadrado.
   Para la clave "menores_promedio", el valor debe ser una lista con los valores menores al promedio de la lista original.
   EJ: crearDiccionario([3,6,7,12]): debe retornar: {'multiplos3': [3, 6, 12], 'cuadrados': [9, 36, 49, 144], 'menores_promedio': [3, 6]}
   '''
   #Tu código acá
def crearDiccionario(lista):
    if not lista:
        return None
    promedio = sum(lista) / len(lista)
    multiplos3 = [num for num in lista if num % 3 == 0]
    cuadrados = [num ** 2 for num in lista]
    menores_promedio = [num for num in lista if num < promedio]
    diccionario = {
        "multiplos3": multiplos3,
        "cuadrados": cuadrados,
        "menores_promedio": menores_promedio
    }
    return diccionario
entrada = [3, 6, 7, 12]
resultado = crearDiccionario(entrada)
print(resultado)


def trianguloRectangulo(a,b,c):
   '''
   La función debe recibir como argumentos el valor en cm de los lados de un triángulo (a y b son los catetos), y dado estos valores, retornar True si en efecto corresponden a un triángulo rectángulo, o False en caso contrario. Sólo se debe poder pasar valores enteros como argumentos de la función, caso contrario debe retornar nulo.
   EJ: trianguloRectangulo(3.5,3.5,2.4), debe retornar nulo
   EJ: trianguloRectangulo(3,3,3), debe retornar False
   EJ: trianguloRectangulo(3,4,5), debe retornar True
   '''
   #Tu código acá
def es_entero(numero):
    return isinstance(numero, int)

def trianguloRectangulo(a, b, c):
    if es_entero(a) and es_entero(b) and es_entero(c):
        
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
        else:
            return False
    else:
        return None
resultado1 = trianguloRectangulo(3.5, 3.5, 2.4)
resultado2 = trianguloRectangulo(3, 3, 3)
resultado3 = trianguloRectangulo(3, 4, 5)

print(resultado1)  
print(resultado2)  
print(resultado3) 
   

def ciudadesPoblacion(diccionario):
   '''
   Dado el siguiente diccionario ciudades, la función debe retornar una lista de listas, donde cada elemento de la lista sea una lista con el par ['ciudad', población], pero sólo de las ciudades que comiencen con la letra 'B', y como último elemento de la lista el par ['promedio', promedio de población] con el promedio de población de las ciudades seleccionadas.
   Ej: Si se pidiera ciudades que comiencen con la letra 'S', debe devolver: [['São Paulo', 21048514], ['Santiago de Chile', 7112808],['promedio', 14080661.0]]

   ciudades = {
      'São Paulo': 21048514,
      'Buenos Aires': 14975587,
      'Río de Janeiro': 11902701,
      'Bogotá': 10777931,
      'Lima': 10479899,
      'Santiago de Chile': 7112808,
      'Belo Horizonte': 6006091,
      'Caracas': 5622798,
      'Brasília': 4291577
      }
      Pista: investigar método de string startswith()
   '''
   #Tu código acá
def ciudadesConLetra(ciudades, letra):
    ciudades_seleccionadas = []
    total_poblacion = 0
    contador = 0

    for ciudad, poblacion in ciudades.items():
        if ciudad.startswith(letra):
            ciudades_seleccionadas.append([ciudad, poblacion])
            total_poblacion += poblacion
            contador += 1

    if contador > 0:
        promedio_poblacion = total_poblacion / contador
    else:
        promedio_poblacion = 0

    ciudades_seleccionadas.append(['promedio', promedio_poblacion])

    return ciudades_seleccionadas


ciudades = {
    'São Paulo': 21048514,
    'Buenos Aires': 14975587,
    'Río de Janeiro': 11902701,
    'Bogotá': 10777931,
    'Lima': 10479899,
    'Santiago de Chile': 7112808,
    'Belo Horizonte': 6006091,
    'Caracas': 5622798,
    'Brasília': 4291577
}


resultado = list(ciudadesConLetra(ciudades, 'B'))
print(resultado)




def ordenarPalabras(palabras):
   '''
   La función recibe como argumento una secuencia de palabras unidas por guiones, y debe retornar las mismas palabras, unidas por guiones, pero en orden alfabético. Si el argumento que se le pasa no es un string o no contiene guiones, debe retornar nulo.
   EJ: ordenarPalabras('saco-libro-casa') debe retornar 'casa-libro-saco'
   EJ: ordenarPalabras('Hola') debe retornar nulo
   Pista: investigar métodos de string
   '''
   #Tu código acá
def ordenarPalabras(cadena):
    if isinstance(cadena, str) and '-' in cadena:
        palabras = cadena.split('-')  
        palabras.sort()  
        return '-'.join(palabras) 
    else:
        return None
cadena1 = 'saco-libro-casa'
cadena2 = 'Hola como estas'
resultado1 = ordenarPalabras(cadena1)
resultado2 = ordenarPalabras(cadena2)
print(resultado1)  
print(resultado2)






def stringEspejo(texto):
    '''
    La función recibe como argumento una cadena de texto y retorna la cadena invertida, pero sólo si tiene más de tres caracteres, sino debe retornar nulo.
    EJ: stringEspejo('Hola Mundo') debe retornar 'odnuM aloH'
    EJ: stringEspejo('Hoy') debe retornar nulo
    '''
    #Tu código acá
def stringEspejo(cadena):
    if len(cadena) > 3:
        return cadena[::-1]
    else:
        return None
cadena1 = 'Hola Mundo'
cadena2 = 'Hoy'
resultado1 = stringEspejo(cadena1)
resultado2 = stringEspejo(cadena2)
print(resultado1) 
print(resultado2)   


         

    
