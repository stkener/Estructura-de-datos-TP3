###################################################################
#################### TP 3 LISTAS Y ARBOLES ########################
###################################################################

###################### KENER SEBASTIAN ############################


from TDA_NodoLista import*

###################################################################
##################### TDA LISTA ENLAZADA ##########################
###################################################################

class Lista:
  '''__init__(self, startList = None): Constructor de la clase Lista'''
  
  def __init__(self, startList = None):
    self.primero = None
    
  '''estaVacia(self): Indica si la lista se encuentra vacia, devuelve un booleano'''
  
  def estaVacia(self):
    return self.primero == None

  '''len(self): Nos devuelve la cantidad total de elementos que tiene la lista'''

  def len(self):
    cant = 0
    if not self.estaVacia():
      cant = self.primero.len()
    return cant

  '''append(self, dato): Agrega elemento al final, inserta nuevo nodo al final de la lista 
  con el elemento que recibe como parámetro.'''
  
  def append(self, dato):
    nodoNuevo = NodoLista(dato)
    if self.estaVacia():
      self.primero = nodoNuevo
    else:
      self.primero.append(nodoNuevo) 
  
  '''insert(self, dato, pos):Inserta un nuevo nodo, con el dato ingresado en la posicion dada'''

  def insert(self, dato, pos):
    if 0 <= pos:
      nodoNuevo = NodoLista(dato)
      if pos == 0:
        if self.estaVacia():
          self.primero = nodoNuevo
        else:
          nodoNuevo.siguiente = self.primero
          self.primero = nodoNuevo
      elif pos > self.len():
        self.primero.append(nodoNuevo)
      else:
        self.primero.insert(nodoNuevo, pos)
    else:
      raise Exception("Posicion incorrecta")

  '''pop(self, pos):De a cuerdo a una posicion ingresada, devuelve el dato de esa posicion, 
  y elimina el nodo que lo contenia. en otras palabras lo saca de la lista'''

  def pop(self, pos):
    if 0 <= pos < self.len()+1:
      print("self len lista",self.len())
      dato = None
      if pos == 0:
        dato = self.primero.dato  
        self.primero = self.primero.siguiente
      else:
        dato = self.primero.pop(pos)
      return dato
    else:
      raise Exception("Posicion incorrecta")
    
  '''clonar(self): Clona la lista actual'''

  def clonar(self):
    listaClon = Lista()
    if not self.estaVacia():
      self.primero.clonar(listaClon)
    return listaClon

  '''__repr__(self): Imprime por pantalla la lista'''

  def __repr__(self):
    strOut = ""
    if not self.estaVacia():
      strOut = self.primero.__repr__()
    strOut += " -|"
    return strOut

  '''estaLaCancion(self, cancion): Recibe una cancion y devuelve True o False. 
  Si esta o no la cancion en la lista'''

  def estaLaCancion(self, cancion):
    respuesta = False
    if cancion == self.primero.dato:
        respuesta = True
    elif self.primero.tieneSiguiente():
        respuesta = self.primero.siguiente.estaLaCancion(cancion)
    return respuesta 

  '''get(self, pos): Obtener el elemento de la lista que se encuentre en dicha posicion'''

  def get(self, pos):
    dato = None
    if 0 <= pos < self.len():
      dato = self.primero.getDato(pos)
    return dato

  '''buscarCancionYRetornarPosicion (self,unaCancion): Recibe una cancion, la busca en la lista,
  y retorna la posicion en la que se encuentra'''

  def buscarCancionYRetornarPosicion (self,unaCancion):
       posAux = 0
       posicion = None
       nodoAux = self.primero
       while nodoAux != None:
           if nodoAux.dato == unaCancion:
               posicion = posAux
           posAux+=1    
           nodoAux = nodoAux.siguiente
       return posicion
