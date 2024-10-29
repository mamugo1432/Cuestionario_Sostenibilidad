preguntas=("hola como estan","","","","","","","","","")
elecciones=("A) bien    B) mal  C)regular   D) normal","","","","","","","","","")
respuestas=("1","2","3","4","5","6","7","8","9","10")
primero=""
segundo=""
tercero=""
n_pregunta=1

#PRESENTACION
print("\n")
print("*"*140+"\n" + '''                                            BIENVENIDOS AL CUESTIONARIO SOSTENIBLE\n''' + "*"*140)
            
#IMPERSION DE PREGUNTAS

i=1
j=0
while i<= 10:
    input(f'''\n                                               Pregunta {i} --> {preguntas[j]}
          
                                              {elecciones[j]}\n''')
    i+=1
    j+=1
    
#IMPRESION DE RESPUESTAS
print('''                                             ¡¡¡TEST FINALIZADO!!!
      
      ''')
print(f"          LAS RESPUESTAS SON --> {respuestas}\n")

#OBTENER GANADORES

primero=input('''                       Introduce al ganador: ''')
segundo=input('''                       Introduce al segundo: ''')
tercero=input('''                       Introduce al tercero: ''')
print('\n')

#DIBUJITO FINAL

print(f'''                              {primero}           {segundo}                 {tercero}
      
                               * * * *      * * * * * *         * * * * * * 
                             * * * * *      * * * * * * *       * * * * * * *
                           * * * * * *            * * *                 * * *
                             *   * * *           * * *          * * * * * * *
                                 * * *         * * *            * * * * * * *
                                 * * *        * * *                     * * *
                                 * * *      * * * * * * *       * * * * * * * 
                                 * * *      * * * * * * *       * * * * * *  ''')
