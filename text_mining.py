file = open('aliceinwonderland.txt', 'r', encoding='utf-8')
text1 = file.read()
##print(text1)

##Contar cuantas veces aparece cada letra (no es el proposito del codigo
# pero puede llagar a ser ùtil)
def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  for letter in text:
   
    # Check if the letter needs to be counted or not
    if letter.isalpha() :
      # Add or increment the value in the dictionary
      count = text.count(letter)
      result[letter] = count
  return result

##Metodo para Contar palabras
def count_words(text):
  
##Eliminar aquellas palabras comunes que no agragan valor al analisis
  palabras_comunes = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
  "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
  "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
  "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
  "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
  "on", "in", "for", "", "i’m", "it’s"] 
  ##Modificar el texto a analizar de tal forma que todo este en minusculas y separado como lista
  texto = text.lower().split()
  ##Eliminar las palabras comunes del texto a analizar
  palabras = [x for x in texto if x not in palabras_comunes]
  
  ##Algunos signos de puntuaciòn comunes para eliminar entre los caracteres
  puntuaciones = '''!()-[]{};:'"\,<>./?@#$%^&*_~“'''
  
  conteo_palabras={}
  for palabra_cruda in palabras:
    palabra = palabra_cruda.strip(puntuaciones)
    if palabra not in conteo_palabras:
      conteo_palabras[palabra] = 0
    conteo_palabras[palabra] += 1
  return conteo_palabras

def generar_reporte(diccionario):
  for (llave, valor) in sorted(diccionario.items(), key=lambda x: x[1], reverse=True):
    if valor > 30:
      print("{}: {}".format(llave, valor))

if __name__ == "__main__":
    ##print(count_letters(text1))
    ##print(count_words(text1))
    print(generar_reporte(count_words(text1)))