import arcade
import random
import sys           # not required as of now
import time          # not required as of now
import keyboard      # not required as of now
s_width=800             #width of the screen (in pixels)
s_height=600            #height of the screen (in pixels)
k=173
l=[i for i in range(5)] #list to store the indexes of the background objects (trees, shrines, statues etc.)
def draw_bg(u):         #function to render the background                                                          
        draw_bg.t+=5
        if(draw_bg.t<0 and draw_bg.end==0):
                draw_bg.t-=5
                draw_bg.t+=1
                if(draw_bg.t==-132):
                         arcade.Window.music.play(0.3)
                if(draw_bg.t>-23):
                         bg=arcade.load_texture("title/{}.png".format(draw_bg.t%23))
                else:
                        bg=arcade.load_texture("title/0.png")
                arcade.draw_lrwh_rectangle_textured(0, 0, s_width, s_height, bg)
        elif(draw_bg.t>=0 and draw_bg.end==0):
                if(anime.age<=1):
                        bg=arcade.load_texture("backgrounds/bgl{}.png".format(draw_bg.t%10))
                elif(anime.age<=3):
                        bg=arcade.load_texture("backgrounds/bgm{}.png".format(draw_bg.t%10))
                elif(anime.age<5):
                        bg=arcade.load_texture("backgrounds/bgd{}.png".format(draw_bg.t%10))
                if(draw_bg.t>k*28-10):
                        draw_bg.t=0
                arcade.draw_lrwh_rectangle_textured(0, 0, s_width, s_height, bg)
                if(draw_bg.t<k):
                        name="text/evil{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*2):#340):
                        name="text/good{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*3):
                        name="text/life{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*4):
                        name="text/death{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*5):
                        name="text/hate{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*6):
                        name="text/love{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*7):
                        name="text/peace{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*8):
                        name="text/war{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*9):
                        name="text/pain{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*10):
                        name="text/joy{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*11):
                        name="text/meek{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*12):
                        name="text/bold{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*13):
                        name="text/weak{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*14):
                        name="text/strong{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*15):
                        name="text/true{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*16):
                        name="text/false{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*17):
                        name="text/clan{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*18):
                        name="text/world{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*19):
                        name="text/mean{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*20):
                        name="text/kind{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*21):
                        name="text/begin{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*22):
                        name="text/end{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*23):
                        name="text/sane{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*24):
                        name="text/insane{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*25):
                        name="text/fame{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*26):
                        name="text/vain{}.png".format(draw_bg.t%10)
                elif(draw_bg.t<k*27):
                        name="text/fate{}.png".format(draw_bg.t%10)
                else:
                        name="text/hope{}.png".format(draw_bg.t%10)
                size=0.7
                lh=arcade.Sprite(name, size)
                for i in range(300):
                        y=random.randint(50, 120)
                        x=random.randint(0, 800)
                        arcade.draw_line(x, y, x+random.randint(10, 40), y, arcade.color.LICORICE, 2)  #other options- CHARLSESTON_GREEN, KOMBU_GREEN
                lh.center_x=470
                lh.center_y=330
                lh.draw()
                anime()
        elif(draw_bg.end>0):                    #to render the outro
                draw_bg.end+=1
                if(draw_bg.end<21):
                        bg=arcade.load_texture("end/{}.png".format(draw_bg.end-2))
                elif(draw_bg.end in range(21, 240)):
                        bg=arcade.load_texture("end/18.png")
                elif(draw_bg.end>=240 and draw_bg.end<250):
                        bg=arcade.load_texture("end/fade/{}.png".format(draw_bg.end%10))
                elif(draw_bg.end>=250):
                        bg=arcade.load_texture("end/fade/9.png")
                if(draw_bg.end==325):
                       arcade.Window.music.stop()
                arcade.draw_lrwh_rectangle_textured(0, 0, s_width, s_height, bg)
                if(draw_bg.end<240):
                        anime()
draw_bg.t=-250
draw_bg.counter=0
draw_bg.text=160
draw_bg.end=0


def anime():
        """                     #clouds (optional)
        for i in range(4):
                x=random.randint(0, 800)
                y=random.uniform(450, 455)
                h=random.randint(100, 130)
                d=random.uniform(5, 10)
                cl=arcade.color.STORMCLOUD
                arcade.draw_ellipse_filled(x, y,  h*1.8, 9, cl, 0)
               # arcade.draw_ellipse_filled(x+30, 275-d,  h*0.1.5, h*0.9-80, cl, 0)
              #  if(x%2==0):
                #        arcade.draw_ellipse_filled(x-30, 288,  h*0.9, h*0.7-20, cl, 0)
        """
        i=anime.ini_x%5
        anime.ini_c+=5
        namet="props/tc{}.png".format(anime.tt)
        tree=arcade.Sprite(namet, anime.tree_size)
        tree.center_y=anime.tc
        tree.center_x=anime.ini_t-anime.ini_c
        if(anime.ini_x>tree.center_x and anime.c>0):
                anime.c-=1
                anime.age+=1
        if(anime.age<=1):
                name="kid_Itachi/{}.png".format(i)
                atg=arcade.Sprite(name, 1.65)
        elif(anime.age<=3):
                name="teen_Itachi/{}.png".format(i)
                atg=arcade.Sprite(name, 1.7)
        else:
                name='Aka_Itachi/{}.png'.format(i)
                atg=arcade.Sprite(name, 1.8)
                if(anime.age==5 and draw_bg.end==0):
                        draw_bg.end+=1
        if(draw_bg.end>0):
                name="Edo_Itachi/{}.png".format(i)
                atg=arcade.Sprite(name, 1.8)
        if(draw_bg.end<=20):
                tree.draw()
        atg.center_x=anime.ini_x
        atg.center_y=anime.ini_y
        anime.ini_x+=1
        if(anime.ini_x>355):
                anime.ini_x-=5
        if(anime.ini_c<440):
                anime.ini_y+=0.15
        else:
                anime.ini_y-=0.1
        if(tree.center_x<-250):
                anime.ini_c=0
                if(draw_bg.end<=20):
                        x=l[draw_bg.counter]
                        draw_bg.counter+=1
                        anime.tt=x
                anime.tc=random.randint(168, 175)
                anime.tree_size=random.uniform(1.8, 2.1)
                anime.c+=1
        atg.draw()
anime.age=0
anime.ini_x=350
anime.ini_t=825
anime.ini_c=1
anime.tree_size=random.uniform(1.8, 2.1)
anime.tc=random.randint(168, 175)
x=l[draw_bg.counter]
draw_bg.counter+=1
anime.tt=x
anime.ini_y=83
anime.c=1


def main():                          #main function
        s_title="Peace"
        arcade.Window.music = arcade.Sound("buck251.mp3", streaming=True)
        arcade.open_window(s_width, s_height, s_title)
        arcade.schedule(draw_bg, 1/23)
        #arcade.Window.music.play(0.3)
        arcade.run()
main()
#print(draw_bg.t)
