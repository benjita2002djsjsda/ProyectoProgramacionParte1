import pygame  # Se usa para los input,display y cargar imagenes.
import ctypes as ct
# Se define las clases, movimientos en sentido de X e Y de el personaje.

nRES = (690, 800)
x = True

pygame.init


# Entrada:int sFile,int transp=False.
# Salida:int image,retorna a image.
def Load_Image(sFile, transp=False):
    try:
        image = pygame.image.load(sFile)
    except pygame.error.message:
        raise SystemExit.message
    image = image.convert()
    if transp:
        color = image.get_at((0, 0))
        image.set_colorkey(color)
    return image


# Entrada: Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida: int pygame.display.set_mode(nRES).
def PyGame_Init():
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_caption("Proyecto Benja y Amaro")
    return pygame.display.set_mode(nRES)


# Entrada: Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida: int img, retorna la lista vacia.
def Carga_imagenes():
    img = []
    img.append(Load_Image("farmer.png", True))
    img.append(Load_Image("unknown.png", False))
    img.append(Load_Image("T10.png", True))
    return img


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:pinta farmer.
def Pinta_farmer():
    inicia.blit(iniciatiles[0], (310, 440))
    return


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Pinta el fondo.
def pinta_fondo():
    inicia.blit(iniciatiles[1], (0, 0))
    return


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Pinta puntero.
def Pinta_Mouse():
    inicia.blit(iniciatiles[2], (nMx, nMy))
    return


class vaquero(ct.Structure):
    _fields_ = [('Xvaquero', ct.c_short), ('Yvaquero', ct.c_short),
                ('clase ', ct.c_short), ('MovimientoX', ct.c_short),
                ('MovimientoY', ct.c_short)]


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Mueve enemigo.
def Farmer_Init():
    enemigo = vaquero
    enemigo.Xvaquero = 100
    enemigo.Yvaquero = 270
    enemigo.clase = 1
    enemigo.MovimientoX = 0
    enemigo.MovimientoY = 0  # Movimiento (derecha, izquierda)
    return


# Entrada: Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida:Update al enemigo .
def Update_ALGO():
    if enemigo.Xvaquero >= 480:
        enemigo.clase = 2
        enemigo.Movimiento = -2  # ---------------------------------------
    if enemigo.Xvaquero < 100:  # USABLE A FUTURO
        enemigo.Movimiento = 2  # ---------------------------------------
        enemigo.clase = 1
    enemigo.Xvaquero += enemigo.Movimiento
    return


# Entrada:Sin entrada, contiene solamente una única sentencia que es la salida.
# Salida: Pinta enemigo.
def Pinta_vaquero():
    if enemigo.clase == 1:
        inicia.blit(iniciatiles[0], (enemigo.Xvaquero, enemigo.Yvaquero))
    if enemigo.clase == 2:
        inicia.blit(iniciatiles[0], (enemigo.Xvaquero, enemigo.Yvaquero))
    return


Farmer_Init()
inicia = PyGame_Init()
iniciatiles = Carga_imagenes()
Fps = pygame.time.Clock()
enemigo = vaquero

nMx = 0
nMy = 0
# While manejo de eventos.
while x:
    for ev in pygame.event.get():
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                x = False
            if ev.key == pygame.K_d:
                vaquero.MovimientoX += 2
            if ev.key == pygame.K_a:
                vaquero.MovimientoX += -2
            if ev.key == pygame.K_s:
                vaquero.MovimientoY += 2
            if ev.key == pygame.K_w:
                vaquero.MovimientoY += -2
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_d:
                vaquero.MovimientoX += -2
            if ev.key == pygame.K_a:
                vaquero.MovimientoX += 2
            if ev.key == pygame.K_s:
                vaquero.MovimientoY += -2
            if ev.key == pygame.K_w:
                vaquero.MovimientoY += 2
        if ev.type == pygame.QUIT:
            x = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                x = False
        if ev.type == pygame.MOUSEMOTION:
            nMx, nMy = ev.pos

    vaquero.Xvaquero += vaquero.MovimientoX
    vaquero.Yvaquero += vaquero.MovimientoY
    # Llamamos a las funciones.
    pinta_fondo()
    Pinta_vaquero()
    Pinta_Mouse()
    pygame.display.flip()
    Fps.tick(60)
pygame.quit
