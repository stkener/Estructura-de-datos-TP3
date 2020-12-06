###################################################################
#################### TP 3 LISTAS Y ARBOLES ########################
###################################################################

##################### KENER SEBASTIAN ############################


from TDA_Lista import*

###################################################################
################ TDA NODO ARBOL DE CANCIONES ######################
###################################################################
class NodoArbolDeCanciones:

  '''__init__(self, interprete, listaDeCanciones): Constructor de la clase NodoArbolDeCanciones'''

  def __init__(self, interprete, listaDeCanciones):
    self.interprete = interprete
    self.canciones = listaDeCanciones
    self.izquierdo = None
    self.derecho = None

  '''tieneIzquierdo(self): Devuelve true o False, si tiene o no nodo izquierdo'''  

  def tieneIzquierdo(self):
    return self.izquierdo != None

  '''tieneDerecho(self):Devuelve true o False, si tiene o no nodo derecho'''

  def tieneDerecho(self):
    return self.derecho != None

  '''insertarCanciones(self, listaNueva): Recibe una lista con canciones 
  y si no esta en la lista del nodo actual la agrega'''

  def insertarCanciones(self, listaNueva):
    for aux in range (0, listaNueva.len()):
      if not self.canciones.estaLaCancion(listaNueva.get(aux)):
        self.canciones.append(listaNueva.get(aux))
      else:
        print("La cancion ya esta en la lista")

  '''insertarInterprete(self, nuevoNodo): Recibe un nodo y verifica si el interprete esta o no,
  si no esta lo agrega, y si esta agrega las canciones a la lista'''  
  
  def insertarInterprete(self, nuevoNodo):
    if nuevoNodo.interprete < self.interprete:
      if not self.tieneIzquierdo():
        self.izquierdo = nuevoNodo
      else:
        self.izquierdo.insertarInterprete(nuevoNodo)
    elif nuevoNodo.interprete > self.interprete:
      if not self.tieneDerecho():
        self.derecho = nuevoNodo
      else:
        self.derecho.insertarInterprete(nuevoNodo)
    elif nuevoNodo.interprete == self.interprete:
       self.insertarCanciones(nuevoNodo.canciones)     

  '''interpretesDeCanciones(self, unaCancion): recibe una cancion, 
  revisa todas las listas de canciones del arbol y devuelve una lista 
  de interpretes en la que se encuentra la cancion ''' 

  def interpretesDeCanciones(self, unaCancion):
    listaInterpretes = Lista()
    if self.canciones.estaLaCancion(unaCancion):
      listaInterpretes.append(self.interprete)
    if self.tieneIzquierdo():
      self.izquierdo.interpretesDeCanciones(unaCancion)
    if self.tieneDerecho():
      self.derecho.interpretesDeCanciones(unaCancion)      
    return listaInterpretes

  
  '''buscarInterprete(self, interprete): Recibe un interprete y devuelve el nodo en el que esta'''  

  def buscarInterprete(self, interprete):
    nodoDato = None
    #print(nodoDato)
    if self.interprete == interprete:
      nodoDato = self
    elif self.tieneIzquierdo():
        nodoDato = self.izquierdo.buscarInterprete(interprete)
    elif self.tieneDerecho():
        nodoDato = self.derecho.buscarInterprete(interprete)
    return nodoDato

  '''buscarCanciones(self, listaInterpretes): recibe una lista de interpretes, tiene que ser mas de uno, 
  y devuelve una lista con las canciones que comparten entre si'''

  def buscarCanciones(self, listaInterpretes):
    pos = 0
    cantDeInterpretesEnLista = listaInterpretes.len()
    listaDeCanciones = Lista()
    cantidadCanciones = 0
    posicionCanciones = 0
    nodoUno = None
    nodoDos = None
    if cantDeInterpretesEnLista > 1:
      while pos < cantDeInterpretesEnLista:
        interpretePosMasUno = listaInterpretes.get(pos+1)
        if interpretePosMasUno != None:
          nodoUno = self.buscarInterprete(listaInterpretes.get(pos))
          nodoDos = self.buscarInterprete(listaInterpretes.get(pos+1))
          if nodoUno != None and nodoDos != None:
            cantidadCanciones = nodoUno.canciones.len()
            while posicionCanciones < cantidadCanciones:
              
              if nodoDos.canciones.estaLaCancion(nodoUno.canciones.pop(posicionCanciones)):
                listaDeCanciones.append(nodoUno.canciones.pop(posicionCanciones))
              else:
                posicionCanciones+=1
        else:
          print("Al menos un interprete no esta en el arbol")    
        pos = pos + 1
        
    else:
      return listaDeCanciones

  '''OTRA VERSION DE BUSCAR CANCIONES COMPARTIDAS, DONDE DEVUELVE LA CANTIDAD DE CANCIONES COMPARTIDAS'''

  '''buscarCanciones: recibe un interprete y una lista de canciones, devuelve una lista de canciones '''

  '''def buscarCanciones(self, interprete, unaLista):
        for cancion in range(0, interprete.canciones.len()):
          if self.canciones.estaLaCancion(interprete.canciones.get(cancion)):
            unaLista.append(interprete.canciones.get(cancion))
        if self.tieneIzquierdo():
          self.izquierdo.buscarCanciones(interprete, unaLista)
        if self.tieneDerecho():
          self.derecho.buscarCanciones(interprete, unaLista)
        return unaLista'''

  '''buscaPadre(self, dato): Recibe un interprete(dato), y devuelve el padre 
  de este nodo y a que lado esta'''

  def buscaPadre(self, dato): 
    nodoHijo = None
    nodoPadre = None
    lado = None
    if dato < self.interprete:
      if self.tieneIzquierdo():
        if self.izquierdo.interprete == dato:
          nodoHijo = self.izquierdo
          nodoPadre = self
          lado = "izq"
        else:
          nodoHijo, nodoPadre, lado = self.izquierdo.buscaPadre(dato)
    else:
      if self.tieneDerecho():
        if self.derecho.interprete == dato:
          nodoHijo = self.derecho
          nodoPadre = self
          lado = "der"
        else:
          nodoHijo, nodoPadre, lado = self.derecho.buscaPadre(dato)
    return nodoHijo, nodoPadre, lado
 
  '''eliminarInterprete(self, nombreInterprete): Recibe el nombre de un interprete y 
  elimina el nodo en el que se encuentra el interprete'''

  def eliminarInterprete(self, nombreInterprete):
    nodoEliminar, nodoPadre, lado = self.buscaPadre(nombreInterprete)  ##lado = "izq" / "der"
    if nodoEliminar != None:
      if nodoEliminar.grado() == 2:
        nodoPred = nodoEliminar.predecesor()
        self.eliminar(nodoPred.nombreInterprete)
        nodoPred.izquierdo = nodoEliminar.izquierdo
        nodoPred.derecho = nodoEliminar.derecho
        if lado == "izq":
          nodoPadre.izquierdo = nodoPred
        else:
          nodoPadre.derecho = nodoPred
      elif nodoEliminar.tieneIzquierdo():
        if lado == "izq":
          nodoPadre.izquierdo = nodoEliminar.izquierdo
        else:
          nodoPadre.derecho = nodoEliminar.izquierdo
      elif nodoEliminar.tieneDerecho():
        if lado == "izq":
          nodoPadre.izquierdo = nodoEliminar.derecho
        else:
          nodoPadre.derecho = nodoEliminar.derecho
      else:
        if lado == "izq":
          nodoPadre.izquierdo = None
        else:
          nodoPadre.derecho = None

  #RAIZ BALANCEADA
  '''altura(self): Indica la altura del arbol que se encuentra el nodo actual'''

  def altura(self):
    alt=0                     
    if self.grado()==2:          
      alt=1+max(self.izquierdo.altura(),self.derecho.altura())
    elif self.grado()==1:   
      if self.tieneIzquierdo():
        alt=1+(self.izquierdo.altura())
      else:
        alt=1+(self.derecho.altura())
    return alt 
     
  '''diferenciaDeAltura(self): Devuelve la diferencia de altura entre el nodo 
  izquierdo y el derecho del nodo actual'''

  def diferenciaDeAltura(self):
    return abs(self.izquierdo.altura() - self.derecho.altura())  
          
  '''grado(self): Devuelve el grado del nodo actual'''

  def grado(self):
      grado=0
      if self.tieneDerecho():
        grado+=1
      if self.tieneIzquierdo():
        grado+=1
      return grado

  '''esHoja(self): Devuelve True o False, revisa si el nodo actual 
  es hoja(el ultimo de la rama del arbol) o no'''

  def esHoja(self):
      return not self.tieneDerecho() and not self.tieneIzquierdo()   

  '''cancionesEnNivel(self,lista,nivel,nivelActual): Recibe una lista, un nivel y el nivel 
  del nodo actual. Guarda las canciones del nivel ingresado en la lista'''

  def cancionesEnNivel(self,lista,nivel,nivelActual):
        if nivelActual==nivel:
            self.guardarListaEnLista(lista)   
        if self.tieneIzquierdo():    
            self.izquierdo.cancionesEnNivel(lista, nivel,nivelActual+1)
        if self.tieneDerecho():
            self.derecho.cancionesEnNivel(lista, nivel,nivelActual+1) 
            
  '''guardarListaEnLista(self,lista): Recibe una lista y guarda las canciones del nodo actual en ella'''

  def guardarListaEnLista(self,lista):
      largoDeLista=self.canciones.len() 
      elementoNuevo=None
      pos=0
      while pos<largoDeLista:
         elementoNuevo=self.canciones.get(pos)
         #print(elementoNuevo)
         if lista.estaVacia():
            lista.append(elementoNuevo)
         elif not lista.estaLaCancion(elementoNuevo):
                 lista.append(elementoNuevo)
         pos+=1    
 
  '''interpretesConMasCanciones(self,cantidadCancionesMinima,lista): Recibe un numero (cantidadCancionesMinima)
  y una lista, si la cantidad de canciones del nodo actual es mayor o igual al numero ingresado, 
  se agrega el interprete a la lista'''

  def interpretesConMasCanciones(self,cantidadCancionesMinima,lista):
            if self.canciones.len()>=cantidadCancionesMinima:
                 lista.append(self.interprete)
            if self.tieneIzquierdo() :
                   self.izquierdo.interpretesConMasCanciones(cantidadCancionesMinima,lista)          
            if self.tieneDerecho() :
                   self.derecho.interpretesConMasCanciones(cantidadCancionesMinima,lista)

  '''internosAlfabetico(self,lista): Recibe una lista de interpretes y los ordena alfabeticamente'''

  def internosAlfabetico(self,lista):
            if self.tieneIzquierdo():
                self.izquierdo.internosAlfabetico(lista)
            if self.canciones.primero.dato[0].isupper() and not self.esHoja():
               lista.append(self.canciones.primero.dato)                          
            if self.tieneDerecho() :
               self.derecho.internosAlfabetico(lista)

  '''eliminaCancion(self,nombreCancion): Recibe el nombre de una cancion y la elimina de la lista'''

  def eliminaCancion(self,nombreCancion):
       posicion=None
       if self.canciones.estaLaCancion(nombreCancion):
               posicion = self.canciones.buscarCancionYRetornarPosicion(nombreCancion)
               self.canciones.pop(posicion)
                  
       else:    
            if self.tieneIzquierdo() :
                      self.izquierdo.eliminaCancion(nombreCancion)
                  
            if self.tieneDerecho() :
                      self.derecho.eliminaCancion(nombreCancion)

  '''estaPalabraEnInterprete(self, palabra): Se ingresa una palabra y revisa 
  si esta en el nombre del interprete actual. Devuelve un booleano'''

  def estaPalabraEnInterprete(self, palabra):
    resultado = self.interprete.find(palabra)
    booleano = resultado >= 0 
    return booleano

  '''cantidadTotalInterpretes(self, Palabra, lista): Recibe una palabra y una lista. Revisa 
  los interpretes y pone en la lista los que tienen en su nombre la palabra ingresada'''

  def cantidadTotalInterpretes(self, Palabra, lista):
      if self.estaPalabraEnInterprete(Palabra):
        print(self.interprete)
        lista.append(self.interprete)  
      if self.tieneIzquierdo():
          self.izquierdo.cantidadTotalInterpretes(Palabra, lista)
      if self.tieneDerecho():
          self.derecho.cantidadTotalInterpretes(Palabra, lista)
            
      return  lista
