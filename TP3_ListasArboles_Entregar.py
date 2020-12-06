###################################################################
#################### TP 3 LISTAS Y ARBOLES ########################
###################################################################

###################### KENER SEBASTIAN ############################


from TDA_NodoArbol import*    

###################################################################
################### TDA ARBOL DE CANCIONES ########################
###################################################################
class ArbolDeCanciones:
  def __init__(self):
    self.raiz = None
    
  def estaVacio(self):
    return self.raiz == None

  '''insertarCanciones(listaCanciones, nombreInterprete): Inserta cada una de las canciones
  de la lista en el árbol. Si el intérprete ya existe en el árbol, agrega cada canción a
  la lista de canciones (se debe verificar previamente si la canción está en la lista, para no
  duplicar información). Si el intérprete no existe en el árbol, agrega un nuevo nodo con el
  nuevo intérprete y las canciones en el lugar correspondiente. Nota: La lista de canciones de
  entrada NO tiene canciones duplicadas.'''

  def insertarCanciones(self, listaCanciones, nombreInterprete):
    nuevoNodo = NodoArbolDeCanciones(nombreInterprete,listaCanciones)
    if self.estaVacio():
      self.raiz = nuevoNodo
    else:
      self.raiz.insertarInterprete(nuevoNodo)

  '''OTRA VERSION DE INTERTAR CANCIONES'''

  '''def insertarCanciones(self, listaCanciones, nombreInterprete):
       nuevoNodo = NodoArbolDeCanciones(nombreInterprete, listaCanciones)
       if self.estaVacio():
        self.raiz = nuevoNodo
       elif self.tieneIzquierdo():
        if not self.estaLaCancion():
          nuevoNodo = self.izquierdo.append(self.canciones)
       elif self.tieneDerecho():
          nuevoNodo = self.derecho.append(self.canciones)
       else:
        self.raiz.insertarInterprete(nuevoNodo)'''

  '''interpretesDeCancion(nombreCancion): Recibe el nombre de una canción y retorna
  una lista de todos los interpretes que tienen una canción con ese nombre (pueden ser uno o
  más intérpretes). Si no hay ninguna canción con ese nombre almacenada en el árbol, retorna
  una lista vacía.''' 

  def interpretesDeCancion(self, nombreCancion):
        listaInterpretes = Lista()
        listaInterpretes = self.raiz.interpretesDeCanciones(nombreCancion)
        return listaInterpretes

  '''buscarCanciones(listaInterpretes): Recibe una lista con los intérpretes buscados. Retorna
  una lista con los nombres de las canciones compartidas por todos los intérpretes de
  la lista de entrada. Si no hay ninguna canción compatida por todos los intérpretes, debe
  retornar una lista vacía.'''

  def buscarCanciones(self, listaInterpretes):
    listaDeCancionesCompartidas = Lista()
    if self.raiz != None:
      listaDeCancionesCompartidas = self.raiz.buscarCanciones(listaInterpretes)
    return listaDeCancionesCompartidas

  '''OTRA VERSION DE BUSCAR CANCIONES COMPARTIDAS, DONDE DEVUELVE LA CANTIDAD DE CANCIONES COMPARTIDAS''' 

  '''def buscarCanciones(self, listaInterpretes):
      listaDeCancionesCompartidas = Lista()
      listaAux = Lista()
      pos = 0
      whilw pos < listaInterpretes.len():
        interprete listaInterpretes.get(pos)
        nodoInterprete = self.raiz.buscarInterprete(interprete)
        if nodoInterprete != None:
          listaAux = self.raiz.buscarCanciones(nodoInterprete, listaDeCancionesCompartidas)
          listaDeCancionesCompartidas = ListaAux
          pos+=1
        else:
          pos+=1
      return listaDeCancionesCompartidas'''


  '''eliminarInterprete(nombreInterprete): Elimina del árbol el intérprete que recibe por
  parámetros.'''

  def eliminarInterprete(self, nombreInterprete):
    if not self.estaVacio():
      if nombreInterprete == self.raiz.interprete:
        if self.raiz.grado() == 2:
          nodoPred = self.raiz.predecesor()
          self.eliminarInterprete(nodoPred.interprete)
          nodoPred.izquierdo = self.raiz.izquierdo
          nodoPred.derecho = self.raiz.derecho
          self.raiz = nodoPred
        elif self.raiz.tieneIzquierdo():
          self.raiz = self.raiz.izquierdo
        elif self.raiz.tieneDerecho():
          self.raiz = self.raiz.derecho
        else:
          self.raiz = None
      else:
        self.raiz.eliminarInterprete(nombreInterprete)

  '''eliminarCanción(nombreCancion): Elimina del árbol la canción que recibe por parámetro.
  Debe eliminarla de todos los nodos del árbol donde se encuentre.'''
  
  def eliminarCancion(self,nombreCancion):
        if not self.estaVacio():
           self.raiz.eliminaCancion(nombreCancion)


  '''cantidadTotalInterpretes(Palabra): Recibe una palabra por parámetro y retorna la cantidad
  total de intérpretes almacenados en el árbol que tienen esa palabra formando parte
  de su nombre (completa o como parte de otra. Ej: La palabra jugando forma parte de la
  palabra conjugando).'''

  def cantidadTotalInterpretes(self, Palabra):
    listaInterprete = Lista()
    if not self.estaVacio():
      resultado = self.raiz.cantidadTotalInterpretes(Palabra, listaInterprete)
    return resultado.len()

  '''raizBalanceada(): Retorna True si la diferencia de altura entre los subárboles hijos de la
  raiz es menor o igual a 1 y False en caso contrario.'''
  
  def raizBalanceada(self):
        salida = False
        if self.raiz.grado() == 2:
          if self.raiz.diferenciaDeAltura() <=1:
            salida = True
        return salida


  '''cancionesEnNivel(nivel): Recibe un nivel y retorna una lista con las canciones de todos
  los intérpretes que están en ese nivel del árbol. La lista no debe tener canciones repetidas.
  Si en ese nivel no hay nada, retorna una lista vacía.'''

  def cancionesEnNivel(self,nivel):   
        lista=Lista()
        if not self.estaVacio():
            self.raiz.cancionesEnNivel(lista,nivel,0)
        return lista

  '''interpretesConMasCanciones(cantidadCancionesMinima): Recibe una cantidad de
  canciones por parámetro y retorna la cantidad de intérpretes que tienen esa cantidad de
  canciones o más almacenadas en el árbol.'''
  
  def interpretesConMasCanciones(self,cantidadCancionesMinima):
         masCanciones=0
         lista=Lista()
         if not self.estaVacio():
            self.raiz.interpretesConMasCanciones(cantidadCancionesMinima,lista)
            masCanciones=lista.len()
         return masCanciones

  '''internosAlfabetico(): Retorna una lista con los intérpretes que se encuentran en un nodo
  interno del árbol (no hojas). La lista debe contener los nombres de los intérpretes en orden
  alfabético.'''

  def internosAlfabetico(self):
         lista=Lista()
         if not self.estaVacio():
           self.raiz.internosAlfabetico(lista)          
         return lista

