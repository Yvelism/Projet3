import pyxel

# personnage
taille_perso_x = 10
taille_perso_y = 15
# saut
taille_saut = 56

# mouvement perso
pvitesse_mouv_dg = 2.5  # vitesse de mouvement du personnage vers la gauche ou la droite (mouvement horizontal)
pvitesse_mouv_haut = 7  # vitesse de mouvement du personnage en montée (vers le haut)
pvitesse_mouv_bas = 8  # vitesse de mouvement du personnage en descente (vers le haut)


# general
playing = 0  # variable pour changer entre les différent(e)s vues/écrans du jeu
scroll = 0  # variable pour compter l'avancement en termes de position dans un niveau, peut monter et descendre,
# sert à faire bouger correctement les plateformes, les ennemies et le personnage
continuous_scroll = 0  # variable pour compter l'avancement en termes de position dans un niveau, peut seulement
# monter, sert à ce que les ennemies ne spawn/apparaissent qu'une seule fois (même après avoir reculé)
ecran_bord = 256  # bord de l'écran de jeu, toujours fixe
scroll_limitd = 150  # limite le mouvement du personnage vers la droite de l'écran(pour qu'il ne sorte pas de l'écran)
scroll_limitg = 80  # limite le mouvement du personnage vers la gauche de l'écran

floor_base = 192  # "sol" toujours égal à la même valeur (pas comme floor qui dépend du personnage)
last_scroll = scroll  # permet de savoir si et comment le scroll (avancement dans le niveau) change au cours de l'action

niveau = 0
compteur = 0  # pour initialiser une seule fois les variables au début du niveau
star1 = 25 
star2 = 25 
star3 = 25  

# plateforme
hauteur_1 = 60
hauteur_2 = 90
hauteur_3 = 115
# 2 hauteurs fixent pour les plateformes
taille_plateforme = 10
plvitesse_mouv = pvitesse_mouv_dg  # vitesse de mouvement des plateformes


# etoiles
star_liste = []
taille_star_x = 5
taille_star_y = 10
hauteur_0_star = floor - taille_star_y
hauteur_1_star = hauteur_1 - taille_star_y
hauteur_2_star = hauteur_2 - taille_star_y
hauteur_3_star = hauteur_3 - taille_star_y
regular_points = 25

class Perso:
  def __init__(self,perso_x=128,perso_y=182,jump = False,compteuranimation1=True,compteuranimation2=True,avatar1=True,\
               avatar2=False,avatar3=False,touche=False,monte = False, descente = False,floor = 192,last_floor = floor):
    self.perso_x=perso_x
    self.perso_y=perso_y
    self.jump=jump
    self.avatar1=avatar1
    self.avatar2=avatar2
    self.avatar3=avatar3
    self.compteuranimation1=compteuranimation1
    self.compteuranimation2=compteuranimation2
    self.touche=touche
    self.monte=monte
    self.descente=descente
    self.floor=floor
    self.last_floor=last_floor
      
  def get_avatar1(self):
    return self.avatar1
      
  def get_avatar2(self):
    return self.avatar2
  
  def get_avatar3(self):
    return self.avatar3      
          
  def get_compteuranimation1(self):
    return self.compteuranimation1
  
  def get_compteuranimation2(self):
    return self.compteuranimation2  
  
  def get_touche(self):
    return self.touche
  
  def get_perso_x(self):
    return self.perso_x
  
  def get_perso_y(self):
    return self.perso_y
  
  def get_jump(self):
    return self.jump
  
  def get_monte(self):
    return self.monte
  
  def get_descente(self):
    return self.descente

  def get_floor(self):
    return self.floor

  def get_last_floor(self):
    return self.last_floor
  
  def set_avatar1(self,nv_avatar1):
    self.avatar1 = nv_avatar1
  
  def set_avatar2(self,nv_avatar2):
    self.avatar2 = nv_avatar2
  
  def set_avatar3(self,nv_avatar3):
    self.avatar3 = nv_avatar3
  
  def set_compteuranimation1(self,nv_compteuranimation1):
    self.compteuranimation1 = nv_compteuranimation1
  
  def set_compteuranimation2(self,nv_compteuranimation2):
    self.compteuranimation2 = nv_compteuranimation2
  
  def set_touche(self,nv_touche):
    self.touche = nv_touche
  
  def set_perso_x(self,nv_perso_x):
    self.perso_x = nv_perso_x
  
  def set_perso_y(self,nv_perso_y):
    self.perso_y = nv_perso_y
    
  def set_jump(self,nv_jump):
    self.jump = nv_jump
    
  def set_monte(self,nv_monte):
    self.monte = nv_monte
    
  def set_descente(self,nv_descente):
    self.descente = nv_descente
    
  def set_floor(self,nvf):
    self.floor=nvf

  def set_last_floor(self,nvlf):
    self.last_floor=nvlf
  
  def update(self): #mise a jour de la position du personnage lorsqu'il avance
    """Déplacement du personnage"""
    global scroll, last_scroll, continuous_scroll, last_perso_x, 
    last_scroll = scroll
    last_perso_x = self.get_perso_x()
    if pyxel.btn(pyxel.KEY_RIGHT):
        if self.perso_x < scroll_limitd:
            self.set_perso_x(self.perso_x + pvitesse_mouv_dg)
        else:
            scroll += 1
            continuous_scroll += 1
    if pyxel.btn(pyxel.KEY_LEFT):
        if self.perso_x > scroll_limitg:
            self.set_perso_x(self.perso_x - pvitesse_mouv_dg)
        elif scroll > 0:
            scroll -= 1
    
    if pyxel.btn(pyxel.KEY_SPACE):
        if not self.jump:
            self.set_last_floor(self.perso_y + taille_perso_y)
            self.set_jump(True)
    
    if self.jump:
        # si la hauteur n'est pas encore atteinte : commencer ou continuer à monter
        if self.last_floor - taille_saut - taille_perso_y <= self.perso_y and not self.descente:
            self.set_monte(True)
        else:  # si la hauteur du saut est atteinte : commencer à descendre
            self.set_monte(False)
            self.set_descente(True)
            # si le personage est atterri sur le sol (qui peut être une plateforme) : fin du saut et
            # réinitialisé emplacement (perso_y) pour être bien aligné
            if self.perso_y + taille_perso_y + pvitesse_mouv_bas >= floor:
                self.set_descente(False)
                self.set_perso_y(self.floor - taille_perso_y)
                self.set_jump(False)
    else:
        # teste si le personnage n'est pas sur le sol
        if self.perso_y + taille_perso_y != self.floor:
            if self.perso_y + taille_perso_y + pvitesse_mouv_bas < self.floor:
                self.set_descente(True)
            else:
                # réinitialiser perso_y pour qu'il ne se retrouve pas dans une plateforme ou dans le sol
                self.set_perso_y(self.floor - taille_perso_y)
                self.set_descente(False)
                self.set_monte(False)
    if self.monte:
        self.set_perso_y(self.perso_y - pvitesse_mouv_haut)
    if self.descente:
        self.set_perso_y(self.perso_y + pvitesse_mouv_bas)
    
    self.contact_star(star)
    
    if last_perso_x > perso_x or last_scroll > scroll:  # donc qui diminue
      if (pyxel.frame_count % 4) == 0:
          compteur_animation_1 = not compteur_animation_1
          
      elif last_perso_x < perso_x or last_scroll < scroll:
          if (pyxel.frame_count % 4) == 0:
              compteur_animation_2 = not compteur_animation_2

  def draw(self):
    if self.compteuranimation1:
      if self.avatar_1:
          pyxel.blt(self.perso_x, self.perso_y, 0, 100, 34, -taille_perso_x, taille_perso_y, 0)#coordonees a adapter aux graphismes (darina)
      elif self.avatar_2:
          pyxel.blt(self.perso_x, self.perso_y, 0, 116, 74, -taille_perso_x, taille_perso_y, 0)
      elif self.avatar_3 :
          pyxel.blt(self.perso_x, self.perso_y, 0, 132, 58, -taille_perso_x, taille_perso_y, 0)

    elif self.compteuranimation2:
        if self.avatar_1:
            pyxel.blt(self.perso_x, self.perso_y, 0, 84, 34, -taille_perso_x, taille_perso_y, 0)
        elif self.avatar_2:
            pyxel.blt(self.perso_x, self.perso_y, 0, 116, 58, -taille_perso_x, taille_perso_y, 0)
        elif self.avatar_3:
            pyxel.blt(self.perso_x, self.perso_y, 0, 132, 74, -taille_perso_x, taille_perso_y, 0)

  
class Star:
  def __init__(self,liste):
    self.liste=liste
    
  def get_liste(self):
    return self.liste
    
  def set_liste(self,nv_reoetoile):
    self.etoile = nvetoile
  
  def remove(self,etoile):
    self.liste.remove(etoile)
      
  def get_liste(self):
    return self.liste
  
  def update(self):
    """Déplacement des etoiles avec les plateformes"""
    if last_scroll > scroll:
        for element in self.liste:
            if element[2] < scroll:
                element[0] += plvitesse_mouv
    if last_scroll < scroll:
        for element in self.liste:
            if element[2] < scroll:
                element[0] -= plvitesse_mouv
    
  def draw(self): #affiche les étoiles
    for star in self.liste:
        if star[2] <= scroll:
            pyxel.blt(star[0], star[1], 0, 85, 53, taille_star_x, taille_star_y, 0)
          

class plateforme:
  def __init__(self,liste):
    self.liste=liste
    
  def get_liste(self):
    return self.liste
      
  def update(self):
      """Déplacement des plateformes"""
      if last_scroll > scroll:
          for plateforme in self.liste:
              if plateforme[2] < scroll: # si la valeur x de la plateforme est inferieur au x de la derniere apparition de la plateforme. 
                  plateforme[0] += plvitesse_mouv #on ajoute la vitesse à la quel se déplace les plateformes
      if last_scroll < scroll:
          for plateforme in self.liste:
              if plateforme[2] < scroll:
                  plateforme[0] -= plvitesse_mouv
        
  def draw(self):
    for plateforme in self.liste:
      if plateforme[2] <= scroll:
          pyxel.blt(plateforme[0], plateforme[1], 0, 16, 8, taille_plateforme, taille_plateforme)#coordonées darina


  def contact_star(perso, star): # verifie s'il y a un contact entre le perso et les etoiles
    for star in star.get_liste():
    if perso.get_perso_y() < star[1] + taille_star_y and perso.get_perso_y() + taille_perso_y > star[1] \
            and perso.get_perso_x() + taille_perso_x > star[0] and perso.get_perso_x() < star[0] + taille_star_x:
        star.remove(star)#s'il y a un contact alors l'etoile disparait


  def floor_is(perso, plateforme):#Définit le sol du perso à un moment donné, pour savoir si celui-ci doit descendre ou rester à la même hauteur
    for plateforme in plateforme.get_liste():
      if perso.get_perso_y() + taille_perso_y <= plateforme[1] and perso.get_perso_x() + taille_perso_x > plateforme[0] and\
          perso.get_perso_x() < plateforme[0] + taille_plateforme:
          perso.set_floor(plateforme[1])
      #perso.set_floor(192)
  
def reset():#Remettre les variables à leur valeur de base
    global  scroll, continuous_scroll, floor, last_floor, \
        last_scroll, points, \
        star_liste, last_perso_x
    perso=Perso()
    last_perso_x = perso.get_perso_x()
    scroll = 0
    continuous_scroll = 0
    floor = 190
    last_floor = floor
    last_scroll = scroll
    points = 0
    
class App:
    def __init__(self):
      pyxel.init(256, 256, title="Sugarush")
      pyxel.load("Design.pyxres")
      pyxel.run(self.update, self.draw)

    def update(self):
        """Mise à jour des variables (30 fois par seconde)"""
        
        global scroll, last_scroll, floor, playing, continuous_scroll, \
            niveau, compteur, regular_points
        reset()
        # boutons toujours utilisable
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_A):
            playing = 3
        if pyxel.btnp(pyxel.KEY_F):
            print("here", scroll, perso.get_perso_x())
        if playing == 0:
            if pyxel.btn(pyxel.KEY_S):
                playing = 1
                niveau = 1

        if playing == 3: #choisir son avatar
            if pyxel.btnp(pyxel.KEY_1):
                perso.set_avatar_1(True)
                perso.set_avatar_2(False)
                perso.set_avatar_3(False)
                playing = 0
            elif pyxel.btnp(pyxel.KEY_2):
                perso.set_avatar_1(False)
                perso.set_avatar_2(True)
                perso.set_avatar_3(False)
                playing = 0
            elif pyxel.btnp(pyxel.KEY_3):
                perso.set_avatar_1(False)
                perso.set_avatar_2(False)
                perso.set_avatar_3(True)
                playing = 0

        if playing == 1:
            if niveau == 1:
                if compteur == 0:
                    plateforme = plateforme([[ecran_bord, hauteur_1, 4], [ecran_bord, hauteur_1, 6],
                                        [ecran_bord, hauteur_1, 8], [ecran_bord, hauteur_1, 10],
                                        [ecran_bord, hauteur_1, 12], [ecran_bord, hauteur_1, 14],
                                        [ecran_bord, hauteur_1, 16],
                                        [ecran_bord, hauteur_2, 25],
                                        [ecran_bord, hauteur_2, 27], [ecran_bord, hauteur_2, 29],
                                        [ecran_bord, hauteur_1, 35], [ecran_bord, hauteur_1, 37],
                                        [ecran_bord, hauteur_1, 39],
                                        [ecran_bord, hauteur_3, 46], [ecran_bord, hauteur_3, 48],
                                        [ecran_bord, hauteur_3, 50],
                                        [ecran_bord, hauteur_1, 58], [ecran_bord, hauteur_1, 60],
                                        [ecran_bord, hauteur_2, 70], [ecran_bord, hauteur_2, 72],
                                        [ecran_bord, hauteur_2, 74], [ecran_bord, hauteur_2, 76],
                                        [ecran_bord, hauteur_2, 78], [ecran_bord, hauteur_2, 80],
                                        [ecran_bord, hauteur_3, 92], [ecran_bord, hauteur_3, 94],
                                        [ecran_bord, hauteur_3, 96], [ecran_bord, hauteur_3, 98],
                                        [ecran_bord, hauteur_1, 106], [ecran_bord, hauteur_1, 108],
                                        [ecran_bord, hauteur_2, 116], [ecran_bord, hauteur_2, 118],
                                        [ecran_bord, hauteur_2, 120], [ecran_bord, hauteur_2, 122],
                                        [ecran_bord, hauteur_1, 136], [ecran_bord, hauteur_1, 138],
                                        [ecran_bord, hauteur_1, 140], [ecran_bord, hauteur_1, 142],
                                        [ecran_bord, hauteur_3, 150], [ecran_bord, hauteur_3, 152],
                                        [ecran_bord, hauteur_3, 154], [ecran_bord, hauteur_3, 156],
                                        [ecran_bord, hauteur_3, 158], [ecran_bord, hauteur_3, 160],
                                        [ecran_bord, hauteur_1, 170], [ecran_bord, hauteur_1, 172],
                                        [ecran_bord, hauteur_1, 174], [ecran_bord, hauteur_1, 176],
                                        [ecran_bord, hauteur_1, 178], [ecran_bord, hauteur_3, 190],
                                        [ecran_bord, hauteur_3, 192], [ecran_bord, hauteur_3, 194],
                                        [ecran_bord, hauteur_3, 196], [ecran_bord, hauteur_3, 198],
                                        [ecran_bord, hauteur_3, 200], [ecran_bord, hauteur_3, 202],
                                        [ecran_bord, hauteur_1, 214], [ecran_bord, hauteur_1, 216],
                                        [ecran_bord, hauteur_1, 218], [ecran_bord, hauteur_1, 220],
                                        [ecran_bord, hauteur_2, 232], [ecran_bord, hauteur_2, 234],
                                        [ecran_bord, hauteur_2, 236], [ecran_bord, hauteur_2, 238],
                                        [ecran_bord, hauteur_2, 240], [ecran_bord, hauteur_2, 242],
                                        [ecran_bord, hauteur_2, 244], [ecran_bord, hauteur_2, 246],
                                        [ecran_bord, hauteur_2, 248], [ecran_bord, hauteur_2, 250],
                                        [ecran_bord, hauteur_1, 256], [ecran_bord, hauteur_1, 258],
                                        [ecran_bord, hauteur_1, 260], [ecran_bord, hauteur_1, 262],
                                        [ecran_bord, hauteur_3, 274], [ecran_bord, hauteur_3, 276],
                                        [ecran_bord, hauteur_3, 278], [ecran_bord, hauteur_3, 298],
                                        [ecran_bord, hauteur_3, 300], [ecran_bord, hauteur_3, 302],
                                        [ecran_bord, hauteur_1, 314], [ecran_bord, hauteur_1, 316],
                                        [ecran_bord, hauteur_1, 318], [ecran_bord, hauteur_1, 320],
                                        [ecran_bord, hauteur_1, 333], [ecran_bord, hauteur_1, 335],
                                        [ecran_bord, hauteur_1, 337], [ecran_bord, hauteur_3, 346],
                                        [ecran_bord, hauteur_3, 348], [ecran_bord, hauteur_3, 350],
                                        [ecran_bord, hauteur_3, 352], [ecran_bord, hauteur_2, 364],
                                        [ecran_bord, hauteur_2, 366], [ecran_bord, hauteur_2, 368],
                                        [ecran_bord, hauteur_2, 370], [ecran_bord, hauteur_2, 372],
                                        [ecran_bord, hauteur_2, 386], [ecran_bord, hauteur_2, 388],
                                        [ecran_bord, hauteur_2, 390],
                                        [ecran_bord, hauteur_3, 400], [ecran_bord, hauteur_3, 402],
                                        [ecran_bord, hauteur_3, 404], [ecran_bord, hauteur_3, 406],
                                        [ecran_bord, hauteur_3, 408],
                                        [ecran_bord, hauteur_3, 410], [ecran_bord, hauteur_3, 412],
                                        [ecran_bord, hauteur_3, 414], [ecran_bord, hauteur_1, 428],
                                        [ecran_bord, hauteur_1, 430], [ecran_bord, hauteur_1, 432],
                                        [ecran_bord, hauteur_1, 434],
                                        [ecran_bord, hauteur_2, 448],
                                        [ecran_bord, hauteur_2, 450], [ecran_bord, hauteur_2, 452],
                                        [ecran_bord, hauteur_2, 454], [ecran_bord, hauteur_2, 456],
                                        [ecran_bord, hauteur_2, 458], [ecran_bord, hauteur_2, 460],
                                        [ecran_bord, hauteur_1, 469], [ecran_bord, hauteur_1, 471],
                                        [ecran_bord, hauteur_1, 473], [ecran_bord, hauteur_1, 475],
                                        [ecran_bord, hauteur_3, 486], [ecran_bord, hauteur_3, 488],
                                        [ecran_bord, hauteur_2, 500], [ecran_bord, hauteur_2, 502],
                                        [ecran_bord, hauteur_2, 504], [ecran_bord, hauteur_2, 506],
                                        [ecran_bord, hauteur_3, 518],
                                        [ecran_bord, hauteur_3, 520], [ecran_bord, hauteur_3, 522],
                                        [ecran_bord, hauteur_3, 524], [ecran_bord, hauteur_3, 526],
                                        [ecran_bord, hauteur_3, 546], [ecran_bord, hauteur_3, 548],
                                        [ecran_bord, hauteur_3, 550], [ecran_bord, hauteur_3, 552],
                                        [ecran_bord, hauteur_1, 568], [ecran_bord, hauteur_1, 570],
                                        [ecran_bord, hauteur_1, 572], [ecran_bord, hauteur_1, 574],
                                        [ecran_bord, hauteur_2, 582], [ecran_bord, hauteur_2, 584],
                                        [ecran_bord, hauteur_2, 586],
                                        [ecran_bord, hauteur_2, 588], [ecran_bord, hauteur_2, 590],
                                        [ecran_bord, hauteur_3, 602], [ecran_bord, hauteur_3, 604],
                                        [ecran_bord, hauteur_3, 606], [ecran_bord, hauteur_3, 608],
                                        [ecran_bord, hauteur_3, 622], [ecran_bord, hauteur_3, 624],
                                        [ecran_bord, hauteur_3, 626], [ecran_bord, hauteur_3, 640],
                                        [ecran_bord, hauteur_3, 642], [ecran_bord, hauteur_3, 644],
                                        [ecran_bord, hauteur_3, 646], [ecran_bord, hauteur_3, 664],
                                        [ecran_bord, hauteur_3, 666], [ecran_bord, hauteur_3, 668],
                                        [ecran_bord, hauteur_1, 680], [ecran_bord, hauteur_1, 682],
                                        [ecran_bord, hauteur_1, 684], [ecran_bord, hauteur_1, 686], ])
                    
                    # dans plateforme_liste [x, y, scroll d'apparition] qui utilise deux hauteurs y différentes et
                    # toujours le même bord x
                    star = Star([[ecran_bord, hauteur_3_star, 50], [ecran_bord, hauteur_3_star, 152],
                                [ecran_bord, hauteur_0_star, 172], [ecran_bord, hauteur_2_star, 234],
                                [ecran_bord, hauteur_3_star, 300], [ecran_bord, hauteur_0_star, 378],
                                [ecran_bord, hauteur_1_star, 432], [ecran_bord, hauteur_3_star, 520],
                                [ecran_bord, hauteur_3_star, 624], [ecran_bord, hauteur_1_star, 685], ])
                    
                    
                    compteur += 1
                  
                if scroll >= 750:
                    playing = 2
            
            perso.update()

            if last_scroll != scroll:
                plateforme.update()
                star.update()
            contact_star(perso,star)
            floor_is(perso,plateforme) #fonctions a revoir, methode de classe ? laquelle ?
            

        if playing == 2:
            compteur = 0
            if pyxel.btnp(pyxel.KEY_S) and niveau !=1:
                niveau=1
                playing = 1
              


    def draw(): # from line 762
        """Création des objets (30 fois par seconde)"""
        global floor, tuto
        pyxel.cls(0)
        if playing == 0:  # écran d'intro
            pyxel.text(84, 160, "taper S pour commencer", 7)
            pyxel.text(101, 230, "press Q to quit", 11)
            pyxel.text(75, 185 , "press A to change your Avatar", 13)
            pyxel.blt(89, 100, 0, 0, 48, 80, 32)

        if playing == 1:  # écran quand on joue
            if compteur != 0:
                pyxel.bltm(0, floor_base, 0, 0, floor_base, 256, 66)   
                perso.draw()
                plateforme.draw()
                star.draw()
              
                pyxel.text(215, 20, str(points), 9)
                pyxel.blt(205, 19, 0, 85, 53, taille_star_x, taille_star_y, 0)
     
        if playing == 2:  # écran qui s'affiche quand on gagne
            pyxel.text(108, 142, "avec", 9)
            pyxel.text(138, 142, str(points), 9)
            pyxel.blt(128, 140, 0, 85, 53, taille_star_x, taille_star_y, 0)
            pyxel.blt(90, 100, 0, 16, 96, 80, 32, 0)
            pyxel.text(77, 185, "press S to restart", 9)
            pyxel.text(101, 230, "press Q to quit", 10)

        if playing == 3:  # menu pour choisir un avatar
            pyxel.blt(70, 120, 0, 20, 26, -taille_perso_x, taille_perso_y,0)
            pyxel.blt(125, 120, 0, 116, 42, -taille_perso_x, taille_perso_y, 0)
            pyxel.blt(180, 120, 0, 132, 42, -taille_perso_x, taille_perso_y, 12)
            pyxel.text(90,85,"choose your avatar", 11)
            pyxel.text(60,140,"press 1 ", 13)
            pyxel.text(115,140,"press 2 ", 13)
            pyxel.text(165,140,"press 3 ", 13)

  
App()
