from colorama import init, Fore, Back, Style
preguntas=("hola como estan","","","","","","","","","")
elecciones=("A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal","A) bien    B) mal  C)regular   D) normal")
respuestas=("1","2","3","4","5","6","7","8","9","10")
primero=""
segundo=""
tercero=""
n_pregunta=1

init()

#PRESENTACION
print("\n")
print(Fore.GREEN + "*"*140+"\n"  + '''                                            '''+Back.GREEN + Style.BRIGHT+ Fore.WHITE+'''BIENVENIDOS AL CUESTIONARIO SOSTENIBLE\n'''+ Style.RESET_ALL + Fore.GREEN +"*"*140+Style.RESET_ALL)
input("")
#IMPERSION DE PREGUNTAS

i=1
j=0
while i<= 10:
  
    input('''\n                                               '''+Back.LIGHTWHITE_EX+ Style.BRIGHT + Fore.BLACK+f'''Pregunta {i} --> {preguntas[j]}'''+Style.RESET_ALL+'''
          
                                              '''+Back.BLACK+ Style.BRIGHT + Fore.WHITE+f'''{elecciones[j]}'''+Style.RESET_ALL)
    i+=1
    j+=1
    
#IMPRESION DE RESPUESTAS
print('''\n'''+'''                                                 '''+Style.BRIGHT+Fore.LIGHTCYAN_EX+'''¡¡¡TEST FINALIZADO!!!'''+Style.RESET_ALL+'''
      
      ''')
print("                    "+Back.GREEN+Style.BRIGHT+Fore.WHITE+f"LAS RESPUESTAS SON --> {respuestas}"+Style.RESET_ALL + "\n")

#OBTENER GANADORES

primero=input('''                       '''+Back.YELLOW+ Style.BRIGHT + Fore.BLACK+'''Introduce al ganador: '''+Style.RESET_ALL)
segundo=input('''                       '''+Back.BLACK+ Style.BRIGHT + Fore.BLACK+'''Introduce al segundo: '''+Style.RESET_ALL)
tercero=input('''                       '''+Back.MAGENTA+ Style.BRIGHT + Fore.BLACK+'''Introduce al tercero: '''+Style.RESET_ALL)
print('\n')

#DIBUJITO FINAL

print(f'''                              '''+Back.YELLOW+f'''{primero}'''+Style.RESET_ALL+'''           '''+Back.BLACK+f'''{segundo}'''+Style.RESET_ALL+'''                 '''+Back.MAGENTA+f'''{tercero}'''+Style.RESET_ALL+'''
      
                               * * * *      * * * * * *         * * * * * * 
                             * * * * *      * * * * * * *       * * * * * * *
                           * * * * * *            * * *                 * * *
                               * * * *           * * *          * * * * * * *
                                 * * *         * * *            * * * * * * *
                                 * * *        * * *                     * * *
                                 * * *      * * * * * * *       * * * * * * *
                                 * * *      * * * * * * *       * * * * * *  ''')
