# Aiyu Kamate, Jeffrey Zhou
# February 23, 2020
# OMH
# in this game, we have a simple graphic. When the user enters the area in 450 < X < 600 and 250 < Y < 400, the combat starts. The computer will always shoot fire towards the user, so the user needs to dodge and kill the computer by shooting bullets. Very skill based!
# we will add quests/ more combats/ levels etc to this for our next benchmark.
# images were downloaded from flaticon.com
import pygame
import random
import math

# class for player
class Player:
    def __init__(self, strength, attack, health, max_health, level, experience, exp_cap, money, weapons = None,
                 armor = None, mana=10, max_mana=10, profession = None):  # initial stats
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.strength = strength
        self.level = level
        self.experience = experience
        self.exp_cap = exp_cap
        self.money = money
        self.weapons = weapons
        self.armor = armor
        self.mana = mana
        self.max_mana = max_mana
        self.profession = profession


# class for monsters
class Monster:
    def __init__(self, name, attack, health, max_health, exp, gold, type):  # values/stats
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = max_health
        self.exp = exp
        self.gold = gold
        self.type = type

l = 750
w = 540
# Intialize the pygame
pygame.init()
direction = "normal"
# create the screen
screen = pygame.display.set_mode((l, w))  # width, height

mission1 = False
# Player
# playerImg = pygame.image.load('space-invaders.png')
playerImg = pygame.image.load('japanguy.png')
leftImg = pygame.image.load('leftguy.png')
rightImg = pygame.image.load('rightguy.png')
backImg = pygame.image.load('backguy.png')
playerX = 370
playerY = 480


# image of bullet, x and y coordinate of bullet, and change in coordinates of bullet.
bulletImg = pygame.image.load('bullet.png')
bulletX = -100
bulletY = -100
bulletY_change = 20
bullet_state = "ready"
battle_state = False

# image of enemy, x and y coordinate of enemy, and change in coordinates of enemy.
enemyImg = pygame.image.load('skull.png')
enemyX = -10000
enemyY = -10000
enemyX_change = random.randint(4, 8)
enemyY_change = 10 - enemyX_change
skull = Monster("skull.png", 30, 50, 50, 10, 10, "mage")

# image of fire, x and y coordinate of fire, and change in coordinates of fire.
fireImg = pygame.image.load('fire.png')
fireX = enemyX
fireY = enemyY
fireX_change = 10
fireY_change = 10
fire_state = "fire"

inventory = []

Main_char = Player(20, 20, 100, 100, 1, 0, 10, 0)



# class for professions
class Profession:
    def __init__(self, health_pl, str_pl, expcap_pl, mana_pl):
        self.health_pl = health_pl
        self.str_pl = str_pl
        self.expcap_pl = expcap_pl
        self.mana_pl = mana_pl

def attack(attacker, defender):
    damage = attacker.attack
    defender.health -= damage


def shoot_fire(x, y):
    screen.blit(fireImg, (x, y))




def show_score(x, y):
    font = pygame.font.Font("freesansbold.ttf", 15)
    player_health = font.render("player health: " + str(Main_char.health), True, (255, 255, 255))
    enemy_health = font.render("enemy health: " + str(skull.health), True, (255, 255, 255))
    screen.blit(player_health, (x, y))
    screen.blit(enemy_health, (x, y+20))


def before_batt():
    screen.blit(before_battle, (0, 0))
    screen.blit(enemyImg, (0, 0))


def player(x, y, a):
    if a == "normal":
        screen.blit(playerImg, (x, y))
    elif a == "left":
        screen.blit(leftImg, (x, y))
    elif a == "right":
        screen.blit(rightImg, (x, y))
    elif a == "back":
        screen.blit(backImg, (x, y))
    # draw


def enemy(x, y):
    screen.blit(enemyImg, (x, y))  # draw


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY, d):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < d:
        return True
    else:
        return False


def boundaries(x1, x2, y1, y2):
    w = 30
    global playerX, playerY
    if x1*w-2*w<=playerX<=x1*w-2*w+5 and y1*w-2*w<playerY<y2*w:
        playerX = x1*w-2*w
    elif x2*w-5<=playerX<=x2*w and y1*w-2*w<playerY<y2*w:
        playerX = x2*w
    elif y1*w-2*w<=playerY<=y1*w-2*w+5 and x1*w-2*w<playerX<x2*w:
        playerY = y1*w-2*w
    elif y2*w>=playerY>=y2*w-5 and x1*w-2*w<playerX<x2*w:
        playerY = y2*w


def combat_system():
    screen.blit(background2, (0, 0))
    show_score(10,10)
    enemy(enemyX, enemyY)


get_ready = False
parx = 0
pary = 0
# background
background = pygame.image.load('map2.png')
background = pygame.transform.scale(background, (l, w))

background2 = pygame.image.load("before_battle.jpg")
background2 = pygame.transform.scale(background2, (l, w))

before_battle = pygame.image.load('before_battle.jpg')
before_battle = pygame.transform.scale(before_battle, (l, w))
# Game loop
playerX_change = 0
playerY_change = 0
running = True
#player(playerX, playerY, "normal")
while running:
    if battle_state == False and get_ready == False:
        boundaries(2, 6, 13, 16)
        boundaries(9, 12, 9, 11)
        boundaries(2, 4, 6, 6)
        boundaries(1, 5, 7, 10)
        boundaries(9, 13, 2, 3)
        boundaries(9, 12, 4, 4)
        boundaries(16, 18, 2, 2)
        boundaries(15, 19, 3, 6)
        boundaries(14, 16, 15, 17)
        boundaries(20, 23, 12, 14)

    collision2 = isCollision(fireX, fireY, playerX, playerY, 27)
    collision3 = isCollision(enemyX, enemyY, playerX, playerY, 27)
    if collision2 or collision3 and battle_state == True:
        attack(skull, Main_char)
        fireX = -100
        if Main_char.health <= 0:
            running = False
    # enemy needs to be within the screen
    # if (360 < playerY < 530 and 170<= playerX <= 190) or (160 < playerY < 340 and 150<=playerX <= 160) or (370<= playerX <= 380 and 220 < playerY < 370) or (0 <= playerY < 140 and 370<= playerX <= 380):
    # playerX += 10
    # if 360 < playerY < 530 and 0 <= playerX <= 10:
    # playerX -=10
    if playerY > w - 30:
        playerY -= 5
    elif playerY < 0:
        playerY += 5
    elif playerX > l - 30:
        playerX -= 5
    elif playerX < 0:
        playerX = 0
    screen.fill((0, 0, 0))  # rgb values

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():  # looping through all events
        if event.type == pygame.QUIT:  # the X out
            running = False  # window closes
        # if keystroke is pressed check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
                playerX_change = -10
            elif event.key == pygame.K_RIGHT:
                direction = "right"
                playerX_change = 10
            elif event.key == pygame.K_UP:
                direction = "back"
                playerY_change = -10
            elif event.key == pygame.K_DOWN:
                direction = "normal"
                playerY_change = 10
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready" and battle_state == True:  # can only fire when its ready/reset
                    # get the current x coord of statement, not changing
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

                    # stops moving when key is not pressed
        if event.type == pygame.KEYUP:
            direction = "normal"
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or pygame.K_LEFT:
                playerY_change = 0

    # player
    playerX += playerX_change
    playerY += playerY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY, 27)
    if collision:
        attack(Main_char, skull)
        bulletY = -100
    # if player hits the enemy or the fire, the game ends.
    if skull.health<=0:
        bulletY = playerY
        bullet_state = "ready"
        battle_state = False
        playerX = parx
        playerY = pary
        Main_char.health = Main_char.max_health
        skull.health+=skull.max_health

    if battle_state == True and (enemyY > 490 or enemyY < 0):
        enemyY_change *= -1
    elif battle_state == True and (enemyX > 700 or enemyX < 0):
        enemyX_change *= -1

    if battle_state == True:
        enemyX += enemyX_change
        enemyY += enemyY_change

    # shoots towards the user

    # combat starts if user enters this area.
    if 1 * 30 <= playerX <= 2 * 30 and 0 * 30 <= playerY <= 1 * 30:
        get_ready = True
        parx = playerX
        pary = playerY
        playerX = 370
        playerY = 500
    if get_ready == True and mission1 == False:
        before_batt()
    if get_ready == True and mission1 == True:
        screen.blit(background, (0, 0))

    if get_ready == True and isCollision(playerX, playerY, 0, 0, 27) and mission1 == False and battle_state == False:
        enemyX = 370
        enemyY = 200
        battle_state = True
        playerX = 370
        playerY = 500
    if battle_state == True:
        combat_system()
        pointx = playerX
        pointy = playerY
    if fire_state == "fire" and battle_state == True:
        fire_state = "shooting"
        x = playerX - fireX
        y = playerY - fireY
        fireX_change = x * 10 / math.sqrt(x ** 2 + y ** 2)
        fireY_change = y * 10 / math.sqrt(x ** 2 + y ** 2)
        fireX += fireX_change
        fireY += fireY_change
        shoot_fire(fireX, fireY)
    # movement of fire is always a line.
    if fire_state == "shooting" and battle_state == True:
        fireX += fireX_change
        fireY += fireY_change
        shoot_fire(fireX, fireY)
        if fireX < -10 or fireX > l - 30 or fireY < 0 or fireY > w - 30:
            fireX = enemyX
            fireY = enemyY
            fire_state = "fire"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        # if bullets goes out of screen, user can shoot bullet again.
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = playerY
        # player needs to be within the screen
    player(playerX, playerY, direction)
    # print("emenyx", playerX, "enemyy", playerY)
    pygame.display.update()





