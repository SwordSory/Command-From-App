#imports
import pygame
from pygame.locals import *
import subprocess
import psutil


#Functions
def on_button_maker(height):
    pygame.draw.rect(screen, "Green", (410, height, 170, 70), 100)
    pygame.draw.rect(screen, "Black", (410, height, 170, 70), 8)
    pygame.draw.rect(screen, "White", (525, height + 15, 40, 40), 100)
    pygame.draw.rect(screen, "Black", (525, height + 15, 40, 40), 5)
    screen.blit(font.render("On", True, "White"), (435, height + 15))   


def get_xset_led_state():
    try:
        result = subprocess.check_output("xset -q | grep 'Caps Lock:'", shell=True, text=True)
        return "on" if "on" in result else "off"
    except subprocess.CalledProcessError:
        return "off"


def is_steam_running():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'steam':
            return True
    return False



#Basic
pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Ubuntu_Utility_Beta_1.0")
font = pygame.font.Font(None, 70)
clock = pygame.time.Clock()



#Button Clickers
steam_click = pygame.Rect(410, 110, 170, 70)
backlight_click = pygame.Rect(410, 210, 170, 70)



#App Loop
steam = False
steam_counter = 0
if is_steam_running():
    steam_counter = 1
if steam_counter == 1:
    steam = True


backlight = False
backlight_counter = 0
if get_xset_led_state() == "on":
    backlight_counter = 1
if backlight_counter == 1:
    backlight = True


running = True
while running:


    #App_Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                running = False

        elif event.type == VIDEORESIZE:
                pygame.display.set_mode((600, 800))
        
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()


            if steam_click.collidepoint(pos) and event.button == 1:

                steam_counter += 1
                
                if steam_counter%2 != 0:
                    steam = True
                    if steam == True:
                        subprocess.Popen(['nohup', 'flatpak', 'run', 'com.valvesoftware.Steam', '&'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                else:
                    steam = False


            elif backlight_click.collidepoint(pos) and event.button == 1:

                backlight_counter += 1
                
                if backlight_counter%2 != 0:
                    backlight = True
                else:
                    backlight = False

                


    #Blits
    screen.fill((100, 100, 100))
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, 600, 100), 100)


    grid_height = 100
    while grid_height <= 800:
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, grid_height), 10)
        grid_height += 100


    pygame.draw.line(screen, (0, 0, 0), (395, 0), (395, 800), 10)


    screen.blit(font.render("Function", True, (220, 220, 220)), (20, 35))
    screen.blit(font.render("Run Steam", True, (220, 220, 220)), (20, 135))
    screen.blit(font.render("Backlight On", True, (220, 220, 220)), (20, 235))
    screen.blit(font.render("Coming Soon!", True, (220, 220, 220)), (20, 335))
    screen.blit(font.render("Coming Soon!", True, (220, 220, 220)), (20, 435))
    screen.blit(font.render("Coming Soon!", True, (220, 220, 220)), (20, 535))
    screen.blit(font.render("Coming Soon!", True, (220, 220, 220)), (20, 635))
    screen.blit(font.render("Coming Soon!", True, (220, 220, 220)), (20, 735))


    screen.blit(font.render("On/Off", True, (220, 220, 220)), (417, 35))


    d_110 = 110
    d_125 = 125
    button_counter = 1
    while button_counter <= 8:

        pygame.draw.rect(screen, "Red", (410, d_110, 170, 70), 100)
        pygame.draw.rect(screen, "Black", (410, d_110, 170, 70), 8)
        pygame.draw.rect(screen, "White", (425, d_125, 40, 40), 100)
        pygame.draw.rect(screen, "Black", (425, d_125, 40, 40), 5)
        screen.blit(font.render("Off", True, "White"), (485, d_125))

        d_110 += 100
        d_125 += 100
        button_counter += 1


    #ifs
    if steam == True:
        on_button_maker(110)
    else:
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'steam':
                process.terminate()


    if backlight == True:
        on_button_maker(210)
        subprocess.run("xset led on", shell=True, check=True, capture_output=True, text=True)
    else:
        subprocess.run("xset led off", shell=True, check=True, capture_output=True, text=True)


    #End
    pygame.display.flip()
    clock.tick(60)

pygame.quit()