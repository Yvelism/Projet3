# Pyxel Studio

import pyxel

SCREEN_WIDTH=256
SCREEN_HEIGHT=256
pyxel.load("art.pyxres")

vie=3
niveau=0

hauteur_1 =140
hauteur_2 =120
hauteur_3 =90
descente = False
compteur_animation_1 = True
compteur_animation_2 = True
touche = False
avatar_1 = True
avatar_2 = False
avatar_3 = False
pvitesse_mouv_bas = 8

floor = 190
last_floor = floor  # permet de savoir si le "sol" du personnage change
floor_base = floor #inchangé


playing = 0 
compteur = 0  

plateforme_liste = []
taille_plateforme = 8

star_liste=[]
taille_star_x= 5
taille_star_y= 10
hauteur_0_star = floor - taille_star_y
hauteur_1_star = hauteur_1 - taille_star_y
hauteur_2_star  = hauteur_2 - taille_star_y
hauteur_3_star = hauteur_3 - taille_star_y

background = 0
tuto = False



class perso:
    def __init__(self,choisi, avance, x, y, taille_x=15, taille_y=15, vitesseh=3, vitessev=8, tombe=False):
        self.choisi= choisi #bool choix perso
        self.avance=avance #bool marche/arret
        self.x=x
        self.y=y
        self.taille_x=taille_x
        self.taille_y=taille_y
        self.vitesseh=vitesseh
        self.vitessev=vitessev
        self.tombe=tombe #bool, si le perso est en chute
        
    def get_y(self):
        return self.y
    def get_x(self):
        return self.x
    def get_taillex(self):
        return self.taille_x
    def get_tailley(self):
        return self.taille_y
        
    def mouvementh(self):
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.x<pyxel.mouse_x<(self.x+self.taille_x) and self.y<pyxel.mouse_x<(self.y+self.taille_y)  :
            self.avance = not self.avance
        while self.avance:
            self.x+= self.vitesseh

    def mouvementv(self):
        floor=self.y+self.taille_y
        
        
        if 
         
        if tombe:
            while (self.y+self.taille_y) > (floor_base-vitessev):
                self.y+=vitessev
            self.y=floor_base


        
        
class objet:
    def __init__(self,actif):
        self.actif=actif #bool 
 

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Sugarush", capture_scale=1)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if playing==0:
            """choix perso, en fonction de l'avatar choisi, on initialise à true celui-ci"""
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) #and x<pyxel.mouse_x<x+taillex and y<pyxel.mouse_y<y+taille_x
                avatar1=True#coordonee de l'affichage du1er avatar 
                avatar2,avatar3=False,False
                playing=1
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) #and x<pyxel.mouse_x<x+taillex and y<pyxel.mouse_y<y+taille_y
                avatar2=True#coordonne du 2e
                avatar1,avatar3=False,False
                playing=1
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) #and x<pyxel.mouse_x<x+taillex and y<pyxel.mouse_y<y+taille_y
                avatar3=True#coordonee du 3e
                avatar2,avatar1=False,False
                playing=1
                
        if playing==1:#ecran du choix de niveau
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) #and x<pyxel.mouse_x<x+taillex and y<pyxel.mouse_y<y+taille_x
                niveau=1#coordone du niv 1 ds
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) #and x<pyxel.mouse_x<x+taillex and y<pyxel.mouse_y<y+taille_x
                niveau=2#coordone du niv 2 ds
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) #and x<pyxel.mouse_x<x+taillex and y<pyxel.mouse_y<y+taille_x
                niveau=3#coordone du niv 3 ds
                
        if playing==2:
            if niveau==1:
                
            if niveau==2:
                
            if niveau==3:# ...
                
                
                
                
                
                
                
                
    def draw(self):
        pyxel.cls(0)
        if playing == 0:  # écran d'intro, choix perso
            #pyxel.blt(x, y, img, u, v,-perso.taille_x, perso.taille_y, [colkey])
            #pyxel.blt(x, y, img, u, v,-perso.taille_x, perso.taille_y, [colkey]) affichage des avatars
            #pyxel.blt(x, y, img, u, v,-perso.taille_x, perso.taille_y, [colkey])
            pyxel.text(90,85,"choose your avatar", 11)
            pyxel.text(101, 230, "press Q to quit", 11)
            pyxel.text(75, 245, "credits: Alis, Darina, Imane", 3)
        
    
        if playing == 1:  # écran quand on joue
            if compteur != 0:
                if background >= 256:
                    background = 0
                pyxel.bltm(0, 0, 0, background, 0, 256, floor_base)
                pyxel.bltm(0, floor_base, 0, 0, floor_base, 256, 66)
    
                for plateforme in plateforme_liste:
                    pyxel.blt(plateforme[0], plateforme[1], 0, 16, 8, taille_plateforme, taille_plateforme)
                for star in star_liste:
                    pyxel.blt(star[0], star[1], 0, 85, 53, taille_star_x, taille_star_y, 0)
               
                if vie >= 1:
                    pyxel.blt(15, 20, 0, 29, 6, 6, 5, 0) # valeur à ajuster une fois les "coeurs" dessinés
                    if vie >= 2:
                        pyxel.blt(25, 20, 0, 29, 6, 6, 5, 0)
                        if vie == 3:
                            pyxel.blt(35, 20, 0, 29, 6, 6, 5, 0)
                        else:
                            pyxel.blt(35, 20, 0, 45, 6, 6, 5, 0)
                    else:
                        pyxel.blt(25, 20, 0, 45, 6, 6, 5, 0)
                        pyxel.blt(35, 20, 0, 45, 6, 6, 5, 0)

        if tuto:
            pyxel.text(86, 70, "press on the character to make it move", 4)
            pyxel.text(56, 80, "try to catch the 3 stars !", 4)
    
        if playing == 2:  # écran qui s'affiche quand on gagne
            pyxel.blt(90, 100, 0, 16, 96, 80, 32, 0)
            pyxel.text(77, 185, "press N to pick a new level", 9)
            pyxel.text(101, 230, "press Q to quit", 10)
            
            if niveau < 3:
                pyxel.text(70, 195, "press S to start the next level", 9)
            else:
                pyxel.text(55, 200, "You completed the last and hardest level", 10)
    
        if playing == 3:  # écran qui s'affiche quand on perd
            pyxel.blt(87, 100, 0, 0, 136, 80, 32, 0)
            pyxel.text(92, 180, "press R to restart", 8)
    
        if playing == 4:  # menu pour choisir un niveau
            pyxel.text(86, 100, "Chose a level", 11)
           
    
        
App()