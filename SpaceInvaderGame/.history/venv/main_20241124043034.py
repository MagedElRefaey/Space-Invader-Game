import pygame 
import random 
# importing random library as a guide for random movement to enemy in specicic path 
from math import * 
# in order to solve equations by roots we need to use math library 
from pygame import mixer 
# to use sound and music we import mixer library 
# that initialize or start the game 
pygame.init() 
width = 800 
height = 600 
red = 0 
green = 0 
blue = 0 
# we put width and height in variables so we could be able to change and express it whenever we want 
screen = pygame.display.set_mode((width, height)) 
spacebackground = pygame.image.load('Space Background.jpg') 
# creating background by loading image same as enemy and player 
 
 
mixer.music.load('background.wav') 
# background music 
mixer.music.play(-1) 
# -1 to play at non stoping order 
pygame.display.set_caption("shooter") 
# create game name at top of window 
icon = pygame.image.load('project.png') 
pygame.display.set_icon(icon) 
# create player by using same option as icon 
playerPlace = pygame.image.load("spaceship.png") 
X = 360 
# refers to player position ox x-axis 
Y = 480 
# refers to player position on y axis 
X_change = 0 
# refers to player speed 
# create enemy by using same option as icon 
# creating the invaders 
EnemyPlace = [] 
enemyX_axis= [] 
enemyY_axis= [] 
enemyX_axis_change= [] 
enemyY_axis_change= [] 
no_of_enemies=6 
 
# to create multiple enemies we used list to put enemies in it and specicify whic enemy to do stuff with 
for i in range (no_of_enemies): 
    EnemyPlace.append(pygame.image.load("space invaders.png")) 
    enemyX_axis.append(random.randint(0, 800)) 
    # refers to enemy position ox x-axis 
    enemyY_axis.append(random.randint(50, 150)) 
    # refers to enemy position on y axis 
    enemyX_axis_change.append(4) 
    enemyY_axis_change.append(40) 
# in order to make multiple enemies we need to append(add) informations for one enemy to each one of them in order to do what is done with one enemy to every enemy 
bulletPlace = pygame.image.load("bullet.png") 
# drawing bullet 
bulletX = 0 
# refers to bullet position ox x-axis 
bulletY = 480 
# refers to bullet position on y axis 
bulletX_change = 0 
# refers to bullet positions on x axis and it zero because bullet goes up 
bulletY_change = 10 
# bullet position on y axis 
bullet_condition = "ready" 
 
# bullet in spaceship hasn't been fired yet 
 
 
 
# we create the player position using width and height by determining which position is going to start at 
score_value= 0 
# score at begininig or with no hits 
font =pygame.font.Font('freesansbold.ttf',32) 
# create what font to write at 
textX= 10 
testY= 10 
 
over_font =pygame.font.Font('freesansbold.ttf',64) 
 
def show_score (x, y): 
    score=font.render('score :'+ str(score_value), True, (255,255,255)) 
    screen.blit(score, (x, y)) 
 # function of score named as show_score 
 # score is showing score value displayed as score in at (True to be shown) in white color 
 # score is showed using x and y in function at cordinates we adjust it below 
 
def game_over_text(): 
    over_text = over_font.render("GAME OVER" , True, (255, 255, 255)) 
    screen.blit(over_text, (200,250)) 
 
# the game over display after losing, function is game_over_text 
# over_text to be desplayed its value will display game over 
# blit will draw over_text(which we made as game over) 
# is going to be diplayed once we call fuction below to appear when losing 
 
def player(x, y): 
    screen.blit(playerPlace, (x, y)) 
# palyer function is drawing its position \ 
# to be showed at x and y axis coordinates 
 
def enemy(x, y , i): 
    screen.blit(EnemyPlace[i], (x, y)) 
# enemy place ,but with specifying which enemy as we create a list above 
 
def shoot_bullet(x, y): 
    global bullet_condition 
    bullet_condition = "fire" 
    screen.blit(bulletPlace, (x + 16, y + 10)) 
 
# the bullet function which we made that it in case of firing 
# to be draw in position appear from center of spaceship and in y axis position at 10 
# creaiting bullet function and draw it 
 
def shooting(enemyX_axis, enemyY_axis, bulletX, bulletY): 
    point = sqrt((enemyX_axis - bulletX) ** 2 + (enemyY_axis - bulletY) ** 2) 
    if point <=27: 
        return True 
    else: 
        False 
 
# shooting fuction as we create clashing point in which enemy is going to be hit 
# if we reach that point by calculating coordinates we give it to him sing midpoint law 
# check if point less than or equal 27 which is point is at enemy place 
# to return true as it correct saved in shooting function to be used in further using 
 
 
# creating screen 
# creating game name by (set caption) 
# we made a icon above the screen as a image for the game using (icon) 
# now it turns on only for few seconds and then off we what to make it lasts 
sign = True 
while sign: 
    screen.fill((red, green, blue)) 
    screen.blit(spacebackground, (0, 0)) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sign = False 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                X_change = -5 
            if event.key == pygame.K_RIGHT: 
                X_change = 5 
            if event.key == pygame.K_SPACE: 
                if bullet_condition is "ready": 
                    bullet_Sound = mixer.Sound('laser.wav') 
                    bullet_Sound.play() 
                    # create sound of bullet whic is played in ready condition 
                    bulletX = X 
                    shoot_bullet(bulletX, bulletY) 
    # check if bullet not fired store position of x in bullet x to make bullet at spaceship + bullet y to make it move at 10 or change with 10 
    if event.type == pygame.KEYUP: 
        if event.key == pygame.K_RIGHT or pygame.K_LEFT: 
            X_change = 0 
    # we put an variable name event to make sure of capturing every action(get) 
    # now we assign value (true) to sign to make sure if user pressed n x(false) the program quits 
    # now we want to know is the key is being pressed and what is it's type 
    # also, to check is the key released(key up)or not 
    # now we ask if the key is pressed look if: 
    # left move left by subtracting value from X_change(0) 
    # right move right by adding value to X_change(0) 
    # when key is released it stops(0) 
    # if pressed space fire 
    X += X_change 
    # that one to change the position of the space ship by making it + or = the speed value of space ship depending on left or right key 
    if X <= 0: 
        X = 0 
    elif X >= 736: 
        X = 736 
        # in order to set the boundaries we make it if it reach specific area to stop as that its limit 
        # its = 736 as our screen = 800 px and spaceship = 64 px (800(the limit)-64) = (736 px) so by subtracting we're having 736 as wall 
    for i in range(no_of_enemies): 
        if enemyY_axis[i] > 400: 
            for j in range (no_of_enemies): 
                enemyX_axis[j]=2000 
            game_over_text() 
            break 
    # now it check if enemy also by specify whic one in list is in range(distance) of our spaceship to be rested at 2000 whic is outside screen 
        # if that true display game over function 
        enemyX_axis[i] +=enemyX_axis_change[i] 
        if enemyX_axis[i] <= 0: 
            enemyX_axis_change[i] = 4 
            enemyY_axis[i] += enemyY_axis_change[i] 
# that to reset enemy position upon hitting wall  to reset it 
# check of enemy reach wall to move it down 
        elif enemyX_axis[i] >= 736: 
            enemyX_axis_change[i] = -4 
            enemyY_axis[i] += enemyY_axis_change[i] 
 
        hit = shooting(enemyX_axis[i], enemyY_axis[i], bulletX, bulletY) 
        if hit: 
            bomb_Sound = mixer.Sound('explosion.wav') 
            bomb_Sound.play() 
            bulletY = 480 
            bullet_condition = "ready" 
            score_value = score_value+1 
            enemyX_axis[i] = random.randint(0, 736) 
            enemyY_axis[i] = random.randint(50, 150) 
# check hitting if it hit set bullet back to its position 
# set enemy back to its random state above in x and y axis 
        enemy(enemyX_axis[i], enemyY_axis[i], i) 
# calling enemy function to appear at x axis and y axis coordinates also i to dispalyed in restting form 
 
    if bulletY <= 0: 
        bulletY = 480 
        bullet_condition = "ready" 
# check if bullet is pass wall to reset it in ready form which in space ship at its mid 
    if bullet_condition is 'fire': 
        shoot_bullet(bulletX, bulletY) 
        bulletY -= bulletY_change 
# if bullet if at its fire state 
# call shoot bullet fuction to set it's position  at it's original one to make it move as it move along y axis it decreases 
# y axis becomes - or = the y change which we set above =10 cause as we decrease it move higher to reach 0 highest point of screen 
 
 
    player(X, Y) 
    show_score(textX,testY) 
 
    # put function player after screen fill because we build screen first 
    # making function to the enemy ,also after the screen 
    # to make background black we use rgb values for colors when red,blue and green = 0 this means the screen is black 
    pygame.display.update() 
# if you run without update it won't display because it won't catch up with changes so we need to put something(update) to update in  the while loop 

 