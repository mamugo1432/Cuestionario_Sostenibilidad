from colorama import init, Fore, Back, Style
preguntas=("¿En qué consiste el concepto de sostenibilidad?","¿Dónde aparece por primera vez el concepto de SOSTENIBILIDAD?","Cuántos objetivos conforman los Objetivos de Desarrollo del Milenio?","¿Qué evento marcó la creación de la ONU?","El fin del Pacto de las naciones unidas es...","El año objetivo del Pacto verde Europeo es...","Cuál de los siguientes no es un objetivo del Pacto Verde Europeo","¿Cuáles de estos países tienen problemas con el Pacto Verde Europeo?")
elecciones=('''A) Satisfacer nuestras necesidades compromentiendo generaciones futuras    B) Apoyar al medioambiente  
C) Satisfacer nuestras necesidades sin comprometer generaciones futuras   D) Hacer el mundo más sostenible''',
'''A) Informe Butland    B) Informe Brutland
C) Informe Dudand  D) Informe putland''',
'''A) 8    B) 17
C) 15   D) 7''',
'''A) La primera guerra mundial    B) La llegada de Franco al poder
C) La segunda guerra mundial   D) La muerte de Napoleón''',
'''A) potenciar un sector público responsable y sostenible    B) potenciar el sector agrícola de manera sostenible  
C) potenciar el sector privado de manera sostenible y responsable   D) potenciar el turismo de manera sostenible y responsable''',
'''A) 2025    B) 2050
C)2040   D) 2030''',
'''A) Avanzar hacia una economía limpia y circular    B) Reducir la contaminación  
C) Garantizar una transición justa y equilibrada   D) Fomentar la creación de zonas verdes en las capitales de los países afiliados a la UE''',
'''A) Irlanda y Chequía    B) Irlanda y República Checa
C)Irlanda y Escocia   D) Reino Unido y Croacia''')
respuestas=("A","B","A","C","C","B","D","B")
primero=""
segundo=""
tercero=""
n_pregunta=1

init() #INICIALIZACION DE COLORAMA

#PRESENTACION
print("\n")
print(Fore.GREEN + "*"*140+"\n"  + '''                                            '''+Back.GREEN + Style.BRIGHT+ Fore.WHITE+'''BIENVENIDOS AL CUESTIONARIO SOSTENIBLE\n'''+ Style.RESET_ALL + Fore.GREEN +"*"*140+Style.RESET_ALL)
input("")

#IMPERSION DE PREGUNTAS

i=1
j=0
while i<= 8:
  
    input('''\n                                               '''+Back.LIGHTWHITE_EX+ Style.BRIGHT + Fore.BLACK+f'''Pregunta {i} --> {preguntas[j]}'''+Style.RESET_ALL+"\n"+Back.BLACK+ Style.BRIGHT + Fore.WHITE+f'''{elecciones[j]}'''+Style.RESET_ALL)
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

print(f'''                              '''+Back.YELLOW+f'''{primero}'''+Style.RESET_ALL+'''           '''+Back.BLACK+f'''{segundo}'''+Style.RESET_ALL+'''                 '''+Back.MAGENTA+f'''{tercero}'''+Style.RESET_ALL+Fore.LIGHTGREEN_EX+Style.BRIGHT+'''
      
                               * * * *      * * * * * *         * * * * * * 
                             * * * * *      * * * * * * *       * * * * * * *
                           * * * * * *            * * *                 * * *
                               * * * *           * * *          * * * * * * *
                                 * * *         * * *            * * * * * * *
                                 * * *        * * *                     * * *
                                 * * *      * * * * * * *       * * * * * * *
                                 * * *      * * * * * * *       * * * * * *  ''')
