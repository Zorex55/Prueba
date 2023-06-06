import tkinter as tk
from tkinter import *
import random as rd
from PIL import Image, ImageTk
import tkinter.font as tF  
#import pygame as pg
import time
import threading
global click_contA #Al declarar global antes de una variable, quiero decir que quiero modificar la variable con mismo nombre en lugar de declararla solo como si fuera global, aunque de todas formas tengo que declarala antes de la función, le asigné 0 porque si la dejo así no funciona
global TPA

direction = 1
direction2 = 1
TPA = 25
TPI = 18
TPC = 15
TPE = 15
click_contA = 0
click_contI = 0
click_contC = 0
click_contE = 0
clicks_maxA  = 25
clicks_maxI = 18
clicks_maxC = 15
clicks_maxE = 15              
click_Vid = 0
clicks_maxV = 3
Poc = 3

def juegoDigg():
     Juego.destroy()
     juegoDigg = tk.Tk()
     juegoDigg.title("Pokemón")
     canvas = tk.Canvas(juegoDigg, width = 500, height= 500)
     canvas.pack()
     BG = PhotoImage(file = 'C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/POO/BG.png')
     canvas.create_image(0,0, anchor="nw", image = BG)

     #Asigna un total de vida, atque y defensa
     GOP = tk.Label()
     GOD = tk.Label()
     MOP = tk.Label()
     MOD = tk.Label()
     CRT = tk.Label()
     CRT2 = tk.Label()
     VID = tk.Label()
     pikachu_HP = tk.StringVar()
     pikachu_HP.set("150")
     diglett_HP = tk.StringVar()
     diglett_HP.set("120")

     #pg.mixer.init()

     
     #Fuente de texto
     Digfont = tF.Font(family = "Helvetica", size = 12) 
     

     def move_imageP(image_id):
          
          global direction
          canvas.move(image_id, 0, direction * 5)  # Mueve la imagen según la dirección
          y = canvas.coords(image_id)[1]  # Obtiene la coordenada Y de la imagen
          if y <= 150 or y >= 170:
               direction *= -1  # Cambia la dirección si alcanza los límites superior o inferior
          canvas.after(270, move_imageP, image_id)  # Llama a la función cada 50 milisegundos
          

     def move_imageD(image_id2):
          global direction2
          canvas.move(image_id2, 0, direction * 5)  # Mueve la imagen según la dirección
          y = canvas.coords(image_id2)[1]  # Obtiene la coordenada Y de la imagen
          if y <= 80 or y >= 100:
               direction2 *= -1  # Cambia la dirección si alcanza los límites superior o inferior
               canvas.after(270, move_imageD, image_id2)  # Llama a la función cada 50 milisegundos
          


     #Probabilidad de hacer golpe crítico
     def Crítico(CRT, text, delay):
          for i in range(len(text)):
               CRT.config(text = CRT.cget("text")+text[i])
               CRT.update()
               time.sleep(delay)
               CRT.after(2000, lambda: CRT.config(text = ''))

     def Crítico(CRT2, text, delay):
          for i in range(len(text)):
               CRT2.config(text = CRT2.cget("text")+text[i])
               CRT2.update()
               time.sleep(delay)
               CRT2.after(2000, lambda: CRT2.config(text = ''))

     #Imprime el texto lentamente cuando seleccionas un movimiento
     def Label_por_letra(MOP, text, delay): #Label en donde se escribe, texto a escribir, tiempo que tarda entre letra y letra
          for i in range(len(text)): #Usamos un for para recorrer el texto
               MOP.config(text=MOP.cget("text") + text[i]) #cget obtiene el texto actual que se declaró al mandar a llamar la función, y lo va imprimiendo conforme lo recorre
               MOP.update() #Va imprimiendo las letras sin quedarse en espera hasta que pase el tiempo total, como en los pokemon 
               time.sleep(delay) #Tiempo que se va a "dormir" entre letra y letra
               MOP.after(2000, lambda: MOP.config(text='')) #after ejecuta un comando sobre que hacer una vez que se ha hecho lo que que hizo con el label, primero el tiempo que va a tardar, después el comando; lambda actúa como una función, solo que declarada en la misma línea de código, siempre y cuando sean simples y cortas, aunque se puede declarar una función aparte y mandarla a llamar 

     #Función que puede ser mandada a llamar en lugar del lambda        
     #def after():
          #MOP.config(text='')

     def Label_por_letra(MOD, text, delay):
          for i in range(len(text)):
               MOD.config(text=MOD.cget("text") + text[i]) 
               MOD.update()
               time.sleep(delay)
               MOD.after(2000, lambda: MOD.config(text = ''))

     def Label_por_letra(VID, text, delay):
          for i in range(len(text)):
               VID.config(text=VID.cget("text") + text[i]) 
               VID.update()
               time.sleep(delay)
               VID.after(2000, lambda: VID.config(text = ''))

     def Label_por_letra(GOD, text, delay):
          for i in range(len(text)):
               GOD.config(text=GOD.cget("text") + text[i]) 
               GOD.update()
               time.sleep(delay)
               GOD.after(2000, lambda: GOD.config(text = ''))

     def Label_por_letra(GOP, text, delay):
          for i in range(len(text)):
               GOP.config(text=GOP.cget("text") + text[i]) 
               GOP.update()
               time.sleep(delay)
               GOP.after(2000, lambda: GOP.config(text = ''))

     #Efectos de sonido

     #Movimientos que Diglett puede hacer
     def GolpeRoca():
          Crt = rd.randint(1,15) #Valor que define si sale crítico o no
          if(Crt == 2 or Crt == 5):
               CRT.place(x = 250, y = 300)
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Golpe Roca", 0.05) #Label en donde se escribe, texto a escribir, tiempo de escritura que manda a "dormir" la consola entre letra y letra
               Crítico(CRT, "¡Golpe Crítico!", 0.05) #Lo mismo que el anterior
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 24
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               CRT.place_forget()
               GameO()
          else:
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 12
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Golpe Roca", 0.05)
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               GameO()
          

     def Cuchillada():
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt == 5):
               CRT.place(x = 250, y = 300)
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Cuchillada", 0.05)
               Crítico(CRT, "¡Golpe Crítico!", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 18
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               CRT.place_forget()
               GameO()
          else:
               MOD.place(x = 50, y = 450)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 9
               Label_por_letra(MOD, "Diglett ha usado Cuchillada", 0.05)
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               GameO()      

     def Fisura():
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt == 5):
               CRT.place(x = 250, y = 300)
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Fisura", 0.05)
               Crítico(CRT, "¡Golpe Crítico!", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 22
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               CRT.place_forget()
               MOD.place_forget()
               GameO()
          else:
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Fisura", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 12
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               GameO()

     def Terremoto():
          Crt = rd.randint(1,15)
          if(Crt == 2, Crt == 5):
               CRT.place(x = 250, y = 300)
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Terremoto", 0.05)
               Crítico(CRT, "¡Golpe Crítico!", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 25
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               CRT.place_forget()
               MOD.place_forget()
               GameO()
          else:
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Terremoto", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 15
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               GameO()
          

     #Imagen de Diglett
     Diglett = tk.PhotoImage(file = 'C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/SeekPng.com_diglett-png_2282423-removebg-preview.png')
     Diglett.width() //2
     Diglett.height() //2
     Diglett = Diglett.subsample(2)
     image_id2 = canvas.create_image(350, 130, image = Diglett)
     move_imageD(image_id2)
     #Iniciar_MovimientoD()
     #DiglettTk = ImageTk.PhotoImage(Diglett)
     #DiglettLbl = tk.Label(juegoDigg, image=DiglettTk)

     #Vida de Diglett impresa en la interfaz
     DigHP = tk.Label(juegoDigg, textvariable = diglett_HP, font = Digfont)
     DigHP.place(x = 120, y = 50)
     Barra = tk.Label(juegoDigg, text = "/")
     Barra.place(x = 150, y =50)
     DigHP2 = tk.Label(juegoDigg, text = '120', font = Digfont)
     DigHP2.place(x = 170, y = 50)

     DigLbl = tk.Label(juegoDigg, text = "Diglett Nvl 30", font=Digfont)
     DigLbl.place(x = 110, y = 20)

     #Caja clásica de Pokemón
     Caja = Image.open('C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/DS DSi - Pokemon Platinum - Text Box Styles.png')
     Caja = Caja.resize((500,100))
     CajaTk = ImageTk.PhotoImage(Caja)
     CajaLbl = tk.Label(juegoDigg, image=CajaTk)
     CajaLbl.place(x = 0, y=400)

     #Imagen de Pikachu
     Pikachu = tk.PhotoImage(file = 'C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/imgbin_pikachu-sprite-pokémon-png.png')
     Pikachu.width() //2
     Pikachu.height() //2
     Pikachu = Pikachu.subsample(2)
     image_id = canvas.create_image(150, 320,  image = Pikachu)
     move_imageP(image_id)
     #Iniciar_MovimientoP()
     #Pikachu = Pikachu.resize((300,250))
     #PikachuTk = ImageTk.PhotoImage(Pikachu)
     #PikachuLbl = tk.Label(juegoDigg, image=PikachuTk)
     #PikachuLbl.place(x=0, y = 150)


     #Vida de Pikachu
     Digfont = tF.Font(family = "Helvetica", size = 12)
     PikHP = tk.Label(juegoDigg, textvariable = pikachu_HP , font = Digfont)
     PikHP.place(x = 265, y = 250)
     Barra = tk.Label(juegoDigg, text = "/")
     Barra.place(x = 310, y =250)
     PikHP2 = tk.Label(juegoDigg, text = '150', font = Digfont)
     PikHP2.place(x = 320, y = 250)

     #Labels en donde se escriben los movimientos de Pikachu, Diglett y si sale crítico
     MOP = tk.Label(juegoDigg, text = '', font = Digfont)

     MOD = tk.Label(juegoDigg, text = '', font = Digfont)

     CRT = tk.Label(juegoDigg, text = '', font = Digfont)

     CRT2 = tk.Label(juegoDigg, text = '', font = Digfont)

     VID = tk.Label(juegoDigg, text = '', font = Digfont, width = 20, height = 2)

     GOD = tk.Label(juegoDigg, text = '', font = Digfont)

     GOP = tk.Label(juegoDigg, text = '', font = Digfont)

     PikLbl = tk.Label(juegoDigg, text = "Pikachu Nvl 30", font=Digfont)
     PikLbl.place(x = 280, y = 210)
     PikHPL = tk.Label(juegoDigg, text = "PS: ", font = Digfont)
     PikHPL.place(x = 225, y = 250)
     DigHPL = tk.Label(juegoDigg, text = "PS: ", font = Digfont)
     DigHPL.place(x = 75, y = 50)

     #Movimientos de Pikachu
     def Arañazo():
          diglett_HP
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt ==5):    
               MOP.place(x = 50, y = 420)
               CRT2.place(x = 250, y = 320)
               Label_por_letra(MOP, "Pikachu ha usado Arañazo", 0.05)
               Crítico(CRT2, "¡Golpe Crítico!", 0.05)
               #Reproducir_Slam(r"C:\Users\unity\Downloads\Slam.wav")
               time.sleep(0.5)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 18
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP) #Actualiza la vida
               MOP.place_forget()
               CRT2.place_forget()
               time.sleep(0.8)
               GameO()
          else:
               MOP.place(x = 50, y = 420)
               Label_por_letra(MOP, "Pikachu ha usado Arañazo", 0.05)
               #Reproducir_Slam(r"C:\Users\unity\Downloads\Slam.wav")
               time.sleep(0.5)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 18
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP) #Actualiza la vida
               MOP.place_forget()
               time.sleep(0.8)
               GameO()
               
               
          Defi = rd.randint(1, 4) #Valor que define que movimiento va a usar Diglett en el sig. turno

          if(Defi == 1):
                    GolpeRoca()
                   

          if (Defi == 2):
                    Cuchillada()
                    

          if (Defi == 3):
                    Fisura()
                    

          if (Defi == 4):
                    Terremoto()
                    
     def Impactrueno():
          diglett_HP
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt == 5):
               MOP.place(x = 50, y = 420)
               CRT2.place(x = 250, y = 320)
               Label_por_letra(MOP, "Pikachu ha usado Impactrueno", 0.05)
               Crítico(CRT2, "¡Golpe Crítico", 0.05)
               #Reproducir_Impactrueno(r"C:\Users\unity\Downloads\Thunderbolt.wav")
               time.sleep(1.9)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 6
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               CRT2.place_forget()
               time.sleep(0.8)
               GameO()
          else:
               MOP.place(x = 50, y = 420)
               Label_por_letra(MOP, "Pikachu ha usado Impactrueno", 0.05)
               #Reproducir_Impactrueno(r"C:\Users\unity\Downloads\Thunderbolt.wav")
               time.sleep(1.9)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 3
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               time.sleep(0.8)
               GameO()
          
          Defi = rd.randint(1, 4)

          if(Defi == 1):
                    GolpeRoca()

          if (Defi == 2):
                    Cuchillada()

          if (Defi == 3):
                    Fisura()

          if (Defi == 4):
                    Terremoto()

     def ColaHierro():
          diglett_HP
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt == 5):
               MOP.place(x = 50, y = 420)
               CRT2.place(x = 250, y = 300)
               Label_por_letra(MOP, "Pikachu ha usado Cola de Hierro", 0.05)
               Crítico(CRT2, "¡Golpe Crítico!", 0.1)
               #Reproducir_Cola(r"C:\Users\unity\Downloads\Iron-Tail.wav")
               time.sleep(1.2)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 20
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               CRT2.place_forget()
               time.sleep(0.8)
               GameO()
          else:
               MOP.place(x = 50, y = 420)
               Label_por_letra(MOP, "Pikachu ha usado Cola de Hierro", 0.05)
               #Reproducir_Cola(r"C:\Users\unity\Downloads\Iron-Tail.wav")
               time.sleep(1.2)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 10
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               time.sleep(0.8)
               GameO()
          
          Defi = rd.randint(1, 4)

          if(Defi == 1):
                    GolpeRoca()

          if (Defi == 2):
                    Cuchillada()

          if (Defi == 3):
                    Fisura()

          if (Defi == 4):
                    Terremoto()


     def Electrobola():
          pikachu_HP
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt==5):
               MOP.place(x = 50, y = 420)
               CRT2.place(x = 250, y = 320)
               Label_por_letra(MOP, "Pikachu ha usado Electrobola", 0.05)
               Crítico(CRT2, "¡Golpe Crítico!", 0.1)
               #Reproducir_Electrobola(r"C:\Users\unity\Downloads\Thunder-Shock.wav")
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 8
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               CRT2.place_forget()
               time.sleep(0.8)
               GameO()
          else:
               MOP.place(x = 50, y = 420)
               Label_por_letra(MOP, "Pikachu ha usado Electrobola", 0.05)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 4
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               time.sleep(0.8)
               GameO()
               
          Defi = rd.randint(1, 4)
          
          if(Defi == 1):
                    GolpeRoca()

          if (Defi == 2):
                    Cuchillada()

          if (Defi == 3):
                    Fisura()

          if (Defi == 4):
                    Terremoto()


     def Vida():
          Defi = rd.randint(1, 4)
          current_HP = int(pikachu_HP.get())
          if current_HP + 30 >= 150:
               new_HP = 150
               VID.place(x = 300, y = 350)
               Label_por_letra(VID, "Los PS están al máximo", 0.05)
               time.sleep(0.8)
               pikachu_HP.set(str(new_HP))
               VID.place_forget()
               if(Defi == 1):
                    GolpeRoca()

               if (Defi == 2):
                    Cuchillada()

               if (Defi == 3):
                    Fisura()

               if (Defi == 4):
                    Terremoto()
          else:
               new_HP = current_HP + 30
               Label_por_letra(VID, "La vida ha incrementado", 0.05)
               pikachu_HP.set(str(new_HP))
               if(Defi == 1):
                    GolpeRoca()

               if (Defi == 2):
                    Cuchillada()

               if (Defi == 3):
                    Fisura()

               if (Defi == 4):
                    Terremoto()

     #Contadores de movimientos y usos máximos 
     

     def click_max5():
          global click_Vid
          global Poc
          click_Vid += 1
          Poc = Poc -1
          contador5.config(text="Res: "+str(Poc))
          if click_Vid >= clicks_maxV:
               vida.config(state = "disabled")
     #Contabiliza los movimientos que ha hecho Pikachu, desabilita el botón si lo ha usado un máximo de veces
     def click_max1():
          global click_contA
          global TPA
          click_contA += 1 #Contador de clicks
          TPA = TPA - 1 #Valor que imprime cuantas veces faltan antes de que se quede sin movimientos
          contador.config(text="TP: "+str(TPA))
          if click_contA >= clicks_maxA:
               boton_aranazo.config(state = tk.DISABLED) #Deshabilita el botón definitivamente al alcanzar el mínimo de TP
          

     def click_max2():
          global click_contI
          global TPI
          click_contI += 1
          TPI = TPI - 1 
          contador2.config(text="TP: "+str(TPI))
          if click_contI >= clicks_maxI:
               boton_Impactrueno.config(state = tk.DISABLED)

     def click_max3():
          global click_contC
          global TPC
          click_contC += 1
          TPC = TPC - 1
          contador3.config(text="TP: "+str(TPC))
          if click_contC >= clicks_maxC:
               boton_ColaHierro.config(state = tk.DISABLED)

     def click_max4():
          global click_contE
          global TPE
          click_contE += 1
          TPE = TPE - 1
          contador4.config(text="TP: "+str(TPE))
          if click_contE >= clicks_maxE:
               boton_Electrobola.config(state = tk.DISABLED)

     #Comando de comandos, solo se puede asignar un comando a la vez por botón, así que estas funciones ejecutan todos los comandos que deberían ejecutarse al presionar un botón
     def Cuadruple_ComandoA():
          hide()
          Arañazo()
          click_max1()
          show()

     def Cuadruple_ComandoI():
          hide()
          Impactrueno()
          click_max2()
          show()

     def Cuadruple_ComandoC():
          hide()
          ColaHierro()
          click_max3()
          show()

     def Cuadruple_ComandoE():
          hide()
          Electrobola()
          click_max4()
          show()

     def VidaS():
          hide()
          Vida()
          click_max5()
          show()
     #Deshabilita todos los botones durante un movimiento
     def hide():
          boton_aranazo.place_forget()
          boton_ColaHierro.place_forget()
          boton_Electrobola.place_forget()
          boton_Impactrueno.place_forget()
          contador.place_forget()
          contador1_2.place_forget()
          contador2.place_forget()
          contador3.place_forget()
          contador4.place_forget()
          vida.place_forget()
          contador5.place_forget()

     #Habilita los botones al terminar el movimiento
     def show():
          time.sleep(0.8)
          boton_aranazo.place(x = 50, y = 420)
          boton_ColaHierro.place(x = 150, y = 420)
          boton_Electrobola.place(x = 250, y = 420)
          boton_Impactrueno.place(x = 350, y = 420)
          vida.place(x = 370, y = 375)
          contador.place(x = 50, y = 470)
          contador1_2.place(x = 90, y = 470)
          contador2.place(x = 150, y = 470)
          contador3.place(x = 250, y = 470)
          contador4.place(x = 350, y = 470)
          contador5.place(x = 450, y = 375)

     def GameO():
               new_HPD = int(diglett_HP.get())
               new_HPP = int(pikachu_HP.get())
               for thread in threading.enumerate():   
                    if(new_HPD <= 0):
                         if thread != threading.current_thread():
                              thread.stop()
                         diglett_HP.set(str(0))
                         canvas.delete(image_id2)
                         GOD.place(x = 50, y = 420)
                         GOP.place(x = 50, y = 450)
                         Label_por_letra(GOD, "Diglett enemigo ha perdido la pelea", 0.05)
                         Label_por_letra(GOP, "Pikachu es el ganador", 0.05)
                         GOD.place_forget()
                         GOP.place_forget()
                         time.sleep(1.8)
                         juegoDigg.after(5000, juegoDigg.destroy())
                    if(new_HPP <= 0):
                         if thread != threading.current_thread():
                              thread.stop()
                         pikachu_HP.set(str(0))
                         canvas.delete(image_id)
                         GOD.place(x = 50, y = 420)
                         GOP.place(x = 50, y = 450)
                         Label_por_letra(GOD, "Pikachu ha perdido la pelea", 0.05)
                         Label_por_letra(GOP, "Diglett enemigo ha ganado la pelea", 0.05)
                         GOD.place_forget()
                         GOP.place_forget()
                         time.sleep(1.8)
                         juegoDigg.after(5000, juegoDigg.destroy())        

     #Labels donde se van imprimiendo los TP restantes
     contador = tk.Label(juegoDigg, text = "TP: 25")
     contador.place(x = 50, y = 470)
     contador1_2 = tk.Label(juegoDigg, text = "/")
     contador1_2.place(x = 90, y = 470)

     contador2 = tk.Label(juegoDigg, text= "TP: 18")
     contador2.place(x = 150, y = 470)

     contador3 = tk.Label(juegoDigg, text="TP: 15")
     contador3.place(x = 250, y = 470)

     contador4 = tk.Label(juegoDigg, text="TP: 15")
     contador4.place(x = 350, y = 470)

     contador5 = tk.Label(juegoDigg, text = "Res: 3")
     contador5.place(x = 450, y = 375)

     #Botones de movimientos
     boton_aranazo = tk.Button(juegoDigg, text = "Arañazo", command = Cuadruple_ComandoA)
     boton_aranazo.place(x = 50, y = 420)

     boton_Impactrueno = tk.Button(juegoDigg, text = "Impactrueno", command = Cuadruple_ComandoI)
     boton_Impactrueno.place(x = 150, y = 420)

     boton_ColaHierro = tk.Button(juegoDigg, text = "Cola de Hierro", command = Cuadruple_ComandoC)
     boton_ColaHierro.place(x = 250, y = 420)

     boton_Electrobola = tk.Button(juegoDigg, text = "Electrobola", command = Cuadruple_ComandoE)
     boton_Electrobola.place(x = 350, y = 420)

     vida = tk.Button(juegoDigg, text = "Usar Poción", command = VidaS)
     vida.place(x = 370, y = 375)


     juegoDigg.mainloop()

def juegoDigg1():
     Juego.destroy()
     juegoDigg = tk.Tk()
     juegoDigg.title("Pokemón")
     canvas = tk.Canvas(juegoDigg, width = 500, height= 500)
     canvas.pack()
     BG = PhotoImage(file = 'C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/POO/BG.png')
     canvas.create_image(0,0, anchor="nw", image = BG)

     #Asigna un total de vida, atque y defensa
     GOP = tk.Label()
     GOD = tk.Label()
     MOP = tk.Label()
     MOD = tk.Label()
     CRT = tk.Label()
     CRT2 = tk.Label()
     VID = tk.Label()
     pikachu_HP = tk.StringVar()
     pikachu_HP.set("150")
     diglett_HP = tk.StringVar()
     diglett_HP.set("120")

     #pg.mixer.init()

     
     #Fuente de texto
     Digfont = tF.Font(family = "Helvetica", size = 12) 
     

     def move_imageP(image_id):
          
          global direction
          canvas.move(image_id, 0, direction * 5)  # Mueve la imagen según la dirección
          y = canvas.coords(image_id)[1]  # Obtiene la coordenada Y de la imagen
          if y <= 150 or y >= 170:
               direction *= -1  # Cambia la dirección si alcanza los límites superior o inferior
          canvas.after(270, move_imageP, image_id)  # Llama a la función cada 50 milisegundos
          

     def move_imageD(image_id2):
          global direction2
          canvas.move(image_id2, 0, direction * 5)  # Mueve la imagen según la dirección
          y = canvas.coords(image_id2)[1]  # Obtiene la coordenada Y de la imagen
          if y <= 80 or y >= 100:
               direction2 *= -1  # Cambia la dirección si alcanza los límites superior o inferior
               canvas.after(270, move_imageD, image_id2)  # Llama a la función cada 50 milisegundos
          


     #Probabilidad de hacer golpe crítico
     def Crítico(CRT, text, delay):
          for i in range(len(text)):
               CRT.config(text = CRT.cget("text")+text[i])
               CRT.update()
               time.sleep(delay)
               CRT.after(2000, lambda: CRT.config(text = ''))

     def Crítico(CRT2, text, delay):
          for i in range(len(text)):
               CRT2.config(text = CRT2.cget("text")+text[i])
               CRT2.update()
               time.sleep(delay)
               CRT2.after(2000, lambda: CRT2.config(text = ''))

     #Imprime el texto lentamente cuando seleccionas un movimiento
     def Label_por_letra(MOP, text, delay): #Label en donde se escribe, texto a escribir, tiempo que tarda entre letra y letra
          for i in range(len(text)): #Usamos un for para recorrer el texto
               MOP.config(text=MOP.cget("text") + text[i]) #cget obtiene el texto actual que se declaró al mandar a llamar la función, y lo va imprimiendo conforme lo recorre
               MOP.update() #Va imprimiendo las letras sin quedarse en espera hasta que pase el tiempo total, como en los pokemon 
               time.sleep(delay) #Tiempo que se va a "dormir" entre letra y letra
               MOP.after(2000, lambda: MOP.config(text='')) #after ejecuta un comando sobre que hacer una vez que se ha hecho lo que que hizo con el label, primero el tiempo que va a tardar, después el comando; lambda actúa como una función, solo que declarada en la misma línea de código, siempre y cuando sean simples y cortas, aunque se puede declarar una función aparte y mandarla a llamar 

     #Función que puede ser mandada a llamar en lugar del lambda        
     #def after():
          #MOP.config(text='')

     def Label_por_letra(MOD, text, delay):
          for i in range(len(text)):
               MOD.config(text=MOD.cget("text") + text[i]) 
               MOD.update()
               time.sleep(delay)
               MOD.after(2000, lambda: MOD.config(text = ''))

     def Label_por_letra(VID, text, delay):
          for i in range(len(text)):
               VID.config(text=VID.cget("text") + text[i]) 
               VID.update()
               time.sleep(delay)
               VID.after(2000, lambda: VID.config(text = ''))

     def Label_por_letra(GOD, text, delay):
          for i in range(len(text)):
               GOD.config(text=GOD.cget("text") + text[i]) 
               GOD.update()
               time.sleep(delay)
               GOD.after(2000, lambda: GOD.config(text = ''))

     def Label_por_letra(GOP, text, delay):
          for i in range(len(text)):
               GOP.config(text=GOP.cget("text") + text[i]) 
               GOP.update()
               time.sleep(delay)
               GOP.after(2000, lambda: GOP.config(text = ''))

     #Efectos de sonido

     #Movimientos que Diglett puede hacer
     def GolpeRoca():
          Crt = rd.randint(1,15) #Valor que define si sale crítico o no
          if(Crt == 2 or Crt == 5):
               CRT.place(x = 250, y = 300)
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Golpe Roca", 0.05) #Label en donde se escribe, texto a escribir, tiempo de escritura que manda a "dormir" la consola entre letra y letra
               Crítico(CRT, "¡Golpe Crítico!", 0.05) #Lo mismo que el anterior
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 24
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               CRT.place_forget()
               GameO()
          else:
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 12
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Golpe Roca", 0.05)
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               GameO()
          

     def Cuchillada():
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt == 5):
               CRT.place(x = 250, y = 300)
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Cuchillada", 0.05)
               Crítico(CRT, "¡Golpe Crítico!", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 18
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               CRT.place_forget()
               GameO()
          else:
               MOD.place(x = 50, y = 450)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 9
               Label_por_letra(MOD, "Diglett ha usado Cuchillada", 0.05)
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               GameO()      

     def Fisura():
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt == 5):
               CRT.place(x = 250, y = 300)
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Fisura", 0.05)
               Crítico(CRT, "¡Golpe Crítico!", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 22
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               CRT.place_forget()
               MOD.place_forget()
               GameO()
          else:
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Fisura", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 12
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               GameO()

     def Terremoto():
          Crt = rd.randint(1,15)
          if(Crt == 2, Crt == 5):
               CRT.place(x = 250, y = 300)
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Terremoto", 0.05)
               Crítico(CRT, "¡Golpe Crítico!", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 25
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               CRT.place_forget()
               MOD.place_forget()
               GameO()
          else:
               MOD.place(x = 50, y = 450)
               Label_por_letra(MOD, "Diglett ha usado Terremoto", 0.05)
               current_HP = int(pikachu_HP.get())
               new_HP = current_HP - 15
               pikachu_HP.set(str(new_HP))
               PikHP.configure(text=pikachu_HP)
               MOD.place_forget()
               GameO()
          

     #Imagen de Diglett
     Diglett = tk.PhotoImage(file = 'C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/SeekPng.com_diglett-png_2282423-removebg-preview.png')
     Diglett.width() //2
     Diglett.height() //2
     Diglett = Diglett.subsample(2)
     image_id2 = canvas.create_image(350, 130, image = Diglett)
     move_imageD(image_id2)
     #Iniciar_MovimientoD()
     #DiglettTk = ImageTk.PhotoImage(Diglett)
     #DiglettLbl = tk.Label(juegoDigg, image=DiglettTk)

     #Vida de Diglett impresa en la interfaz
     DigHP = tk.Label(juegoDigg, textvariable = diglett_HP, font = Digfont)
     DigHP.place(x = 120, y = 50)
     Barra = tk.Label(juegoDigg, text = "/")
     Barra.place(x = 150, y =50)
     DigHP2 = tk.Label(juegoDigg, text = '120', font = Digfont)
     DigHP2.place(x = 170, y = 50)

     DigLbl = tk.Label(juegoDigg, text = "Diglett Nvl 30", font=Digfont)
     DigLbl.place(x = 110, y = 20)

     #Caja clásica de Pokemón
     Caja = Image.open('C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/DS DSi - Pokemon Platinum - Text Box Styles.png')
     Caja = Caja.resize((500,100))
     CajaTk = ImageTk.PhotoImage(Caja)
     CajaLbl = tk.Label(juegoDigg, image=CajaTk)
     CajaLbl.place(x = 0, y=400)

     #Imagen de Pikachu
     Pikachu = tk.PhotoImage(file = 'C:/Users/pacoe/OneDrive/Documentos/Escuela/2do semestre/ELECTRONICA/Imagenes Poke/imgbin_pikachu-sprite-pokémon-png.png')
     Pikachu.width() //2
     Pikachu.height() //2
     Pikachu = Pikachu.subsample(2)
     image_id = canvas.create_image(150, 320,  image = Pikachu)
     move_imageP(image_id)
     #Iniciar_MovimientoP()
     #Pikachu = Pikachu.resize((300,250))
     #PikachuTk = ImageTk.PhotoImage(Pikachu)
     #PikachuLbl = tk.Label(juegoDigg, image=PikachuTk)
     #PikachuLbl.place(x=0, y = 150)


     #Vida de Pikachu
     Digfont = tF.Font(family = "Helvetica", size = 12)
     PikHP = tk.Label(juegoDigg, textvariable = pikachu_HP , font = Digfont)
     PikHP.place(x = 265, y = 250)
     Barra = tk.Label(juegoDigg, text = "/")
     Barra.place(x = 310, y =250)
     PikHP2 = tk.Label(juegoDigg, text = '150', font = Digfont)
     PikHP2.place(x = 320, y = 250)

     #Labels en donde se escriben los movimientos de Pikachu, Diglett y si sale crítico
     MOP = tk.Label(juegoDigg, text = '', font = Digfont)

     MOD = tk.Label(juegoDigg, text = '', font = Digfont)

     CRT = tk.Label(juegoDigg, text = '', font = Digfont)

     CRT2 = tk.Label(juegoDigg, text = '', font = Digfont)

     VID = tk.Label(juegoDigg, text = '', font = Digfont, width = 20, height = 2)

     GOD = tk.Label(juegoDigg, text = '', font = Digfont)

     GOP = tk.Label(juegoDigg, text = '', font = Digfont)

     PikLbl = tk.Label(juegoDigg, text = "Pikachu Nvl 30", font=Digfont)
     PikLbl.place(x = 280, y = 210)
     PikHPL = tk.Label(juegoDigg, text = "PS: ", font = Digfont)
     PikHPL.place(x = 225, y = 250)
     DigHPL = tk.Label(juegoDigg, text = "PS: ", font = Digfont)
     DigHPL.place(x = 75, y = 50)

     #Movimientos de Pikachu
     def Arañazo():
          diglett_HP
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt ==5):    
               MOP.place(x = 50, y = 420)
               CRT2.place(x = 250, y = 320)
               Label_por_letra(MOP, "Pikachu ha usado Arañazo", 0.05)
               Crítico(CRT2, "¡Golpe Crítico!", 0.05)
               #Reproducir_Slam(r"C:\Users\unity\Downloads\Slam.wav")
               time.sleep(0.5)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 18
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP) #Actualiza la vida
               MOP.place_forget()
               CRT2.place_forget()
               time.sleep(0.8)
               GameO()
          else:
               MOP.place(x = 50, y = 420)
               Label_por_letra(MOP, "Pikachu ha usado Arañazo", 0.05)
               #Reproducir_Slam(r"C:\Users\unity\Downloads\Slam.wav")
               time.sleep(0.5)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 18
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP) #Actualiza la vida
               MOP.place_forget()
               time.sleep(0.8)
               GameO()
               
               
          Defi = rd.randint(1, 4) #Valor que define que movimiento va a usar Diglett en el sig. turno

          if(Defi == 1):
                    GolpeRoca()
                   

          if (Defi == 2):
                    Cuchillada()
                    

          if (Defi == 3):
                    Fisura()
                    

          if (Defi == 4):
                    Terremoto()
                    
     def Impactrueno():
          diglett_HP
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt == 5):
               MOP.place(x = 50, y = 420)
               CRT2.place(x = 250, y = 320)
               Label_por_letra(MOP, "Pikachu ha usado Impactrueno", 0.05)
               Crítico(CRT2, "¡Golpe Crítico", 0.05)
               #Reproducir_Impactrueno(r"C:\Users\unity\Downloads\Thunderbolt.wav")
               time.sleep(1.9)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 6
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               CRT2.place_forget()
               time.sleep(0.8)
               GameO()
          else:
               MOP.place(x = 50, y = 420)
               Label_por_letra(MOP, "Pikachu ha usado Impactrueno", 0.05)
               #Reproducir_Impactrueno(r"C:\Users\unity\Downloads\Thunderbolt.wav")
               time.sleep(1.9)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 3
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               time.sleep(0.8)
               GameO()
          
          Defi = rd.randint(1, 4)

          if(Defi == 1):
                    GolpeRoca()

          if (Defi == 2):
                    Cuchillada()

          if (Defi == 3):
                    Fisura()

          if (Defi == 4):
                    Terremoto()

     def ColaHierro():
          diglett_HP
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt == 5):
               MOP.place(x = 50, y = 420)
               CRT2.place(x = 250, y = 300)
               Label_por_letra(MOP, "Pikachu ha usado Cola de Hierro", 0.05)
               Crítico(CRT2, "¡Golpe Crítico!", 0.1)
               #Reproducir_Cola(r"C:\Users\unity\Downloads\Iron-Tail.wav")
               time.sleep(1.2)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 20
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               CRT2.place_forget()
               time.sleep(0.8)
               GameO()
          else:
               MOP.place(x = 50, y = 420)
               Label_por_letra(MOP, "Pikachu ha usado Cola de Hierro", 0.05)
               #Reproducir_Cola(r"C:\Users\unity\Downloads\Iron-Tail.wav")
               time.sleep(1.2)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 10
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               time.sleep(0.8)
               GameO()
          
          Defi = rd.randint(1, 4)

          if(Defi == 1):
                    GolpeRoca()

          if (Defi == 2):
                    Cuchillada()

          if (Defi == 3):
                    Fisura()

          if (Defi == 4):
                    Terremoto()


     def Electrobola():
          pikachu_HP
          Crt = rd.randint(1,15)
          if(Crt == 2 or Crt==5):
               MOP.place(x = 50, y = 420)
               CRT2.place(x = 250, y = 320)
               Label_por_letra(MOP, "Pikachu ha usado Electrobola", 0.05)
               Crítico(CRT2, "¡Golpe Crítico!", 0.1)
               #Reproducir_Electrobola(r"C:\Users\unity\Downloads\Thunder-Shock.wav")
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 8
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               CRT2.place_forget()
               time.sleep(0.8)
               GameO()
          else:
               MOP.place(x = 50, y = 420)
               Label_por_letra(MOP, "Pikachu ha usado Electrobola", 0.05)
               current_HP = int(diglett_HP.get())
               new_HP = current_HP - 4
               diglett_HP.set(str(new_HP))
               DigHP.configure(text = diglett_HP)
               MOP.place_forget()
               time.sleep(0.8)
               GameO()
               
          Defi = rd.randint(1, 4)
          
          if(Defi == 1):
                    GolpeRoca()

          if (Defi == 2):
                    Cuchillada()

          if (Defi == 3):
                    Fisura()

          if (Defi == 4):
                    Terremoto()


     def Vida():
          Defi = rd.randint(1, 4)
          current_HP = int(pikachu_HP.get())
          if current_HP + 30 >= 150:
               new_HP = 150
               VID.place(x = 300, y = 350)
               Label_por_letra(VID, "Los PS están al máximo", 0.05)
               time.sleep(0.8)
               pikachu_HP.set(str(new_HP))
               VID.place_forget()
               if(Defi == 1):
                    GolpeRoca()

               if (Defi == 2):
                    Cuchillada()

               if (Defi == 3):
                    Fisura()

               if (Defi == 4):
                    Terremoto()
          else:
               new_HP = current_HP + 30
               Label_por_letra(VID, "La vida ha incrementado", 0.05)
               pikachu_HP.set(str(new_HP))
               if(Defi == 1):
                    GolpeRoca()

               if (Defi == 2):
                    Cuchillada()

               if (Defi == 3):
                    Fisura()

               if (Defi == 4):
                    Terremoto()

     #Contadores de movimientos y usos máximos 
     

     def click_max5():
          global click_Vid
          global Poc
          click_Vid += 1
          Poc = Poc -1
          contador5.config(text="Res: "+str(Poc))
          if click_Vid >= clicks_maxV:
               vida.config(state = "disabled")
     #Contabiliza los movimientos que ha hecho Pikachu, desabilita el botón si lo ha usado un máximo de veces
     def click_max1():
          global click_contA
          global TPA
          click_contA += 1 #Contador de clicks
          TPA = TPA - 1 #Valor que imprime cuantas veces faltan antes de que se quede sin movimientos
          contador.config(text="TP: "+str(TPA))
          if click_contA >= clicks_maxA:
               boton_aranazo.config(state = tk.DISABLED) #Deshabilita el botón definitivamente al alcanzar el mínimo de TP
          

     def click_max2():
          global click_contI
          global TPI
          click_contI += 1
          TPI = TPI - 1 
          contador2.config(text="TP: "+str(TPI))
          if click_contI >= clicks_maxI:
               boton_Impactrueno.config(state = tk.DISABLED)

     def click_max3():
          global click_contC
          global TPC
          click_contC += 1
          TPC = TPC - 1
          contador3.config(text="TP: "+str(TPC))
          if click_contC >= clicks_maxC:
               boton_ColaHierro.config(state = tk.DISABLED)

     def click_max4():
          global click_contE
          global TPE
          click_contE += 1
          TPE = TPE - 1
          contador4.config(text="TP: "+str(TPE))
          if click_contE >= clicks_maxE:
               boton_Electrobola.config(state = tk.DISABLED)

     #Comando de comandos, solo se puede asignar un comando a la vez por botón, así que estas funciones ejecutan todos los comandos que deberían ejecutarse al presionar un botón
     def Cuadruple_ComandoA():
          hide()
          Arañazo()
          click_max1()
          show()

     def Cuadruple_ComandoI():
          hide()
          Impactrueno()
          click_max2()
          show()

     def Cuadruple_ComandoC():
          hide()
          ColaHierro()
          click_max3()
          show()

     def Cuadruple_ComandoE():
          hide()
          Electrobola()
          click_max4()
          show()

     def VidaS():
          hide()
          Vida()
          click_max5()
          show()
     #Deshabilita todos los botones durante un movimiento
     def hide():
          boton_aranazo.place_forget()
          boton_ColaHierro.place_forget()
          boton_Electrobola.place_forget()
          boton_Impactrueno.place_forget()
          contador.place_forget()
          contador1_2.place_forget()
          contador2.place_forget()
          contador3.place_forget()
          contador4.place_forget()
          vida.place_forget()
          contador5.place_forget()

     #Habilita los botones al terminar el movimiento
     def show():
          time.sleep(0.8)
          boton_aranazo.place(x = 50, y = 420)
          boton_ColaHierro.place(x = 150, y = 420)
          boton_Electrobola.place(x = 250, y = 420)
          boton_Impactrueno.place(x = 350, y = 420)
          vida.place(x = 370, y = 375)
          contador.place(x = 50, y = 470)
          contador1_2.place(x = 90, y = 470)
          contador2.place(x = 150, y = 470)
          contador3.place(x = 250, y = 470)
          contador4.place(x = 350, y = 470)
          contador5.place(x = 450, y = 375)

     def GameO():
               new_HPD = int(diglett_HP.get())
               new_HPP = int(pikachu_HP.get())
               for thread in threading.enumerate():   
                    if(new_HPD <= 0):
                         if thread != threading.current_thread():
                              thread.stop()
                         diglett_HP.set(str(0))
                         canvas.delete(image_id2)
                         GOD.place(x = 50, y = 420)
                         GOP.place(x = 50, y = 450)
                         Label_por_letra(GOD, "Diglett enemigo ha perdido la pelea", 0.05)
                         Label_por_letra(GOP, "Pikachu es el ganador", 0.05)
                         GOD.place_forget()
                         GOP.place_forget()
                         time.sleep(1.8)
                         juegoDigg.after(5000, juegoDigg.destroy())
                    if(new_HPP <= 0):
                         if thread != threading.current_thread():
                              thread.stop()
                         pikachu_HP.set(str(0))
                         canvas.delete(image_id)
                         GOD.place(x = 50, y = 420)
                         GOP.place(x = 50, y = 450)
                         Label_por_letra(GOD, "Pikachu ha perdido la pelea", 0.05)
                         Label_por_letra(GOP, "Diglett enemigo ha ganado la pelea", 0.05)
                         GOD.place_forget()
                         GOP.place_forget()
                         time.sleep(1.8)
                         juegoDigg.after(5000, juegoDigg.destroy())        

     #Labels donde se van imprimiendo los TP restantes
     contador = tk.Label(juegoDigg, text = "TP: 25")
     contador.place(x = 50, y = 470)
     contador1_2 = tk.Label(juegoDigg, text = "/")
     contador1_2.place(x = 90, y = 470)

     contador2 = tk.Label(juegoDigg, text= "TP: 18")
     contador2.place(x = 150, y = 470)

     contador3 = tk.Label(juegoDigg, text="TP: 15")
     contador3.place(x = 250, y = 470)

     contador4 = tk.Label(juegoDigg, text="TP: 15")
     contador4.place(x = 350, y = 470)

     contador5 = tk.Label(juegoDigg, text = "Res: 3")
     contador5.place(x = 450, y = 375)

     #Botones de movimientos
     boton_aranazo = tk.Button(juegoDigg, text = "Arañazo", command = Cuadruple_ComandoA)
     boton_aranazo.place(x = 50, y = 420)

     boton_Impactrueno = tk.Button(juegoDigg, text = "Impactrueno", command = Cuadruple_ComandoI)
     boton_Impactrueno.place(x = 150, y = 420)

     boton_ColaHierro = tk.Button(juegoDigg, text = "Cola de Hierro", command = Cuadruple_ComandoC)
     boton_ColaHierro.place(x = 250, y = 420)

     boton_Electrobola = tk.Button(juegoDigg, text = "Electrobola", command = Cuadruple_ComandoE)
     boton_Electrobola.place(x = 350, y = 420)

     vida = tk.Button(juegoDigg, text = "Usar Poción", command = VidaS)
     vida.place(x = 370, y = 375)


     juegoDigg.mainloop()

Juego=tk.Tk()

Juego.title("Pokemon")
Juego.geometry('200x200')
JuegoDigglet = tk.Button(text = "Pikachu", command = juegoDigg)
JuegoDigglet.grid(column=0,row=0)
JuegoDigglet = tk.Button(text = "Pikachu1", command = juegoDigg1)
JuegoDigglet.grid(column=1,row=0)
Juego.mainloop()
