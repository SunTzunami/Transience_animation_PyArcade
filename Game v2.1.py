import arcade
import time
import random
import sys
import keyboard
s_width=800
s_height=600
def draw_bg(u):
        draw_bg.t+=5
        if(draw_bg.t<=1500):
                bg=arcade.load_texture("bg1.png")
        elif(draw_bg.t<=2550):
                bg=arcade.load_texture("bg0.png")
        else:
                bg=arcade.load_texture("bg2.png")
        arcade.draw_lrwh_rectangle_textured(0, 0, s_width, s_height, bg)
        if(draw_bg.t<200):
                name="lo{}.png".format(draw_bg.t%10)
                size=1.2
        elif(draw_bg.t<300):
                name="ha{}.png".format(draw_bg.t%10)
                size=1.2
        else:
                name="pe{}.png".format(draw_bg.t%10)
                size=1.4
        lh=arcade.Sprite(name, size)
        for i in range(200):
                y=random.randint(0, 230)
                x=random.randint(0, 800)
                arcade.draw_line(x, y, x+random.randint(10, 40), y, arcade.color.BLACK, 2)
        lh.center_x=470
        lh.center_y=350
        lh.draw()
        #draw_trees()
        anime()
draw_bg.t=0
def anime():
        i=anime.ini_x%5
        anime.ini_c+=5
        #if(anime.age>4):
          #      quit()
        #d=random.randint(0, 5)
        namet="tc{}.png".format(anime.tt)
        tree=arcade.Sprite(namet, anime.tree_size)
        tree.center_y=anime.tc
        tree.center_x=anime.ini_t-anime.ini_c
        if(anime.ini_x>tree.center_x and anime.c>0):
                anime.age+=1
                anime.c-=1
        if(anime.age<2):
                name="kid_itachi/{}.png".format(i)
                atg=arcade.Sprite(name, 1.8)
        if(anime.age==2):
                name="{}.png".format(i)
                atg=arcade.Sprite(name, 1.7)
        if(anime.age>2):
                name='Aka/{}.png'.format(i)
                atg=arcade.Sprite(name, 1.9)
        tree.draw()
        atg.center_x=anime.ini_x
        atg.center_y=anime.ini_y
        anime.ini_x+=2
        if(anime.ini_x>350):
                anime.ini_x-=10
        if(anime.ini_c<440):
                anime.ini_y+=0.15
        else:
                anime.ini_y-=0.1
        #atg.draw()
        if(tree.center_x<-250):
                anime.ini_c=0
                anime.tt=random.randint(0, 4)
                anime.tc=random.randint(170, 190)
                anime.tree_size=random.uniform(2, 2.5)
                #draw_bg.t=0
                anime.c+=1
        atg.draw()
anime.age=0
anime.ini_x=330
anime.ini_t=825
anime.ini_c=1
anime.tree_size=random.uniform(2, 2.5)
anime.tc=random.randint(160, 180)
anime.tt=random.randint(0, 3)
anime.ini_y=90
anime.c=1
def main():
        s_title="Dattebayo!"
        #background_music = arcade.load_sound("Fea.mp3")
        #arcade.play_sound(background_music)
        arcade.open_window(s_width, s_height, s_title)
        arcade.schedule(draw_bg, 1/30)
        arcade.run()
main()
#print(draw_bg.t)


