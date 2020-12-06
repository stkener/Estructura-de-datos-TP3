###################################################################
#################### TP 3 LISTAS Y ARBOLES ########################
###################################################################

###################### KENER SEBASTIAN ############################


###################################################################
####################### TDA NODO LISTA ############################
###################################################################

class NodoLista:
  def __init__(self, dato):
    self.dato = dato
    self.siguiente = None

  def tieneSiguiente(self):
    return self.siguiente != None

  def len(self):
    cant = 0
    if not self.tieneSiguiente():
      cant = 1
    else:
      cant = 1 + self.siguiente.len()
    return cant

  def append(self, nuevo):
    if not self.tieneSiguiente():
      self.siguiente = nuevo
    else:
      self.siguiente.append(nuevo)

  def getDato(self, pos, posAct = 0):
    dato = None
    if pos == posAct:
      dato = self.dato
    else:
      dato = self.siguiente.getDato(pos, posAct+1)
    return dato

  def insert(self, nuevo, posIns, posAct = 0):
    if posAct == posIns-1:
      nuevo.siguiente = self.siguiente
      self.siguiente = nuevo
    else:
      self.siguiente.insert(nuevo, posIns, posAct+1)

  def clonar(self, listaClon):
    listaClon.append(self.dato)
    if self.tieneSiguiente():
      self.siguiente.clonar(listaClon)

  def pop(self, posDel, posAct = 0):
    dato = None
    if posAct == posDel-1:
      dato = self.siguiente.dato
      self.siguiente = self.siguiente.siguiente
    else:
      dato = self.siguiente.pop(posDel, posAct+1)
    return dato

  def __repr__(self):
    strOut = str(self.dato)
    if self.tieneSiguiente():
      strOut = strOut + " -> " + self.siguiente.__repr__()
    return strOut

  def estaLaCancion(self, cancion):
    respuesta = None
    if cancion == self.dato:
        respuesta = True
    if self.tieneSiguiente():
        respuesta = self.siguiente.estaLaCancion(cancion)
    return respuesta