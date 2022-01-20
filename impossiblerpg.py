# Jeffrey Zhou
# Sources: images were downloaded from flaticon.com and forums.rpgmakerweb.com,

import pygame
import random
import math

# class for player
class Player:
    def __init__(self, strength, attack, health, max_health, level, experience, exp_cap):  # initial stats
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.strength = strength
        self.level = level
        self.experience = experience
        self.exp_cap = exp_cap

# class for monsters
class Monster:
    def __init__(self, name, attack, health, max_health, exp):  # values/stats
        self.name = name
        self.attack = attack
        self.health = health
        self.max_health = max_health
        self.exp = exp

# death function.
def death():
    global playerX, playerY
    Main_char.health = Main_char.max_health
    playerX = 300
    playerY = 480
    screen.blit(background2, (0,0))
    screen.blit(godImg, (125,100))
    font = pygame.font.Font("freesansbold.ttf", 15)
    Death_message = font.render("You have died. But not all is lost. I can revive you, but... for a price. Press r to respawn", True, (255, 255, 255))
    screen.blit(Death_message, (50, 50))

# level up function. Each time the user levels up, all stats doubles.
def level_up(self):
    while self.experience >= self.exp_cap:
        self.max_health = self.max_health * 2
        self.health = self.max_health
        self.strength = self.strength * 2
        self.attack *= 2
        self.experience -= self.exp_cap
        self.exp_cap *= 2
        self.level += 1

# function for monster to give exp
def give_loot(monster):
    Main_char.experience += monster.exp


#function for doing damage
def attack(attacker, defender):
    damage = attacker.attack
    defender.health -= damage

# function to display the targets for the first quest
def target(x, y):
    screen.blit(background2, (0, 0))
    screen.blit(targetImg, (x, y))
    font = pygame.font.Font("freesansbold.ttf", 15)
    target = font.render("Practice mission: hit 5 targets",True,(255,255,255))
    screen.blit(target,(10,30))

# function to blit the fireballs of monsthers
def shoot_fire(x, y):
    screen.blit(fireImg, (x, y))


# funciton to display the boss monster reflection
def reflection(x,y):
    screen.blit(bullet_reflection, (x-400,y-200))

# function to show status of each building in the map
def show_status():
    global win_state
    if locke == "defeatedboss":
        quest_two = "accomplished"
    elif lockb == "twolocked":
        quest_two = "locked"
    elif lockb == "twounlocked":
        quest_two = "unlocked"
    else:
        quest_two = "accomplished, can try unlimited amount of times"
    if lockd == "threelocked":
        quest_three = "locked"
    elif lockd == "threeunlocked":
        quest_three = "unlocked"
    else:
        quest_three = lockd
    font = pygame.font.Font("freesansbold.ttf", 15)
    quest1_stat = font.render("quest1: " + str(lockf),True, (0,0,0))
    quest2_stat = font.render("quest2: " + str(quest_two),True, (0,0,0))
    quest3_stat = font.render("quest3: " + str(quest_three),True, (0,0,0))
    if locke == "bosslocked":
        secret_boss = font.render("?????",True, (0,0,0))
    elif locke == "boss":
        secret_boss = font.render("boss location revealed",True, (0,0,0))
    else:
        secret_boss = font.render("you defeated the boss!",True, (0,0,0))
    if win_state == True:
        inn_stat = font.render("inn: closed",True,(0,0,0))
    else:
        inn_stat = font.render("inn: open",True,(0,0,0))
    shop_stat = font.render("stats: open",True, (0,0,0))
    screen.blit(shop_stat, (30, 120))
    screen.blit(inn_stat, (30, 330))
    screen.blit(quest3_stat, (240, 0))
    screen.blit(quest2_stat, (240, 210))
    screen.blit(secret_boss, (450, 0))
    screen.blit(quest1_stat, (570, 300))

# function to show player stats while in combat
def show_score(x, y, enemy):
    font = pygame.font.Font("freesansbold.ttf", 15)
    player_health = font.render("player health: " + str(int(Main_char.health)), True, (255, 255, 255))
    player_attack = font.render("player attack: " + str(int(Main_char.attack)), True, (255, 255, 255))
    player_level = font.render("player level: " + str(int(Main_char.level)), True, (255, 255, 255))
    enemy_health = font.render("enemy health: " + str(int(enemy.health)), True, (255, 255, 255))
    screen.blit(player_health, (x, y))
    screen.blit(enemy_health, (x, y + 20))
    screen.blit(player_attack, (x+200, y))
    screen.blit(player_level, (x+400, y))

# display the amount of target left in the first quest
def target_left(t):
    global target_life
    font = pygame.font.Font("freesansbold.ttf", 15)
    target_lives = font.render("Targets left: " + str(t), True, (255, 255, 255))
    screen.blit(target_lives, (10, 10))

# function that creates the screen before fighting the 3 baby skulls
def before_batt():
    screen.blit(before_battle, (0, 0))
    font = pygame.font.Font("freesansbold.ttf", 15)
    explain = font.render("mission: find 3 baby fire skulls. Hint: you might want to walk around.",True, (255,255,255))
    screen.blit(explain, (0, 0))

# function that displays player stats in the stats building
def display_stats():
    screen.blit(blackImg, (0, 0))
    font = pygame.font.Font("freesansbold.ttf", 15)
    health = font.render("health: "+str(int(Main_char.health)), True, (255, 255, 255))
    attack = font.render("attack: "+str(int(Main_char.attack)), True, (255,255,255))
    level = font.render("level: "+str(Main_char.level),True,(255,255,255))
    exp = font.render("exp: "+ str(Main_char.experience),True,(255,255,255))
    expcap = font.render("exp cap:"+ str(Main_char.exp_cap),True,(255,255,255))
    nextlevel = font.render(str(int(Main_char.exp_cap-Main_char.experience))+" experience till next level",True,(255,255,255))
    instruction = font.render("to leave, press q",True, (255,255,255))
    screen.blit(health, (0, 0))
    screen.blit(attack, (0, 20))
    screen.blit(level, (0, 40))
    screen.blit(exp,(0,60))
    screen.blit(expcap,(0,80))
    screen.blit(nextlevel,(0,100))
    screen.blit(instruction, (0, 140))

# function that changes player direction when the user moves in different direction.
def player(x, y, a):
    if a == "normal":
        screen.blit(playerImg, (x, y))
    elif a == "left":
        screen.blit(leftImg, (x, y))
    elif a == "right":
        screen.blit(rightImg, (x, y))
    elif a == "back":
        screen.blit(backImg, (x, y))

# function that displays the baby skulls
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# function that displays the second quest screen.
def goon_fight(x,y):
    global goonImg, gooon
    screen.blit(background2, (0,0))
    screen.blit(goonImg, (x,y))
    font = pygame.font.Font("freesansbold.ttf", 15)
    bad = font.render("A "+str(gooon)+" appeared. Kill him before he catches you. Beware: he respawns after catching you.", True, (255, 255, 255))
    screen.blit(bad,(0,520))

# function that makes the player's energy ball shoot
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x - 25, y - 5))

# function that detects collision between enemy and energy ball or enemy and player or enemy's fire and player.
def isCollision(enemyX, enemyY, bulletX, bulletY, d):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < d:
        return True
    else:
        return False

# function that displays the image "you win" when player defeats the boss
def you_win():
    screen.blit(winImg, (0, 0))

# function that creates the combat system during the quest
def quest(badguyX, badguyY):
    global fire_state, fireX, fireY, fireX_change, fireY_change, playerX, playerY, bulletX, bulletY, bullet_state, boss_state, x, y
    if boss_state != True and target_state != True and easy_state!=True and tutorial_state != True: # enemy fires only in quest 3
        if fire_state == "fire":
            fire_state = "shooting"
            x = playerX - fireX # fire shoots from the enemy towards the player
            y = playerY - fireY
            if boss_battle_state == True:
                fireX_change = x * 10 / math.sqrt(x ** 2 + y ** 2) * 2.5 # fire speed is 2.5 times faster for the boss fire skull
                fireY_change = y * 10 / math.sqrt(x ** 2 + y ** 2) * 2.5
            else:
                fireX_change = x * 10 / math.sqrt(x ** 2 + y ** 2)
                fireY_change = y * 10 / math.sqrt(x ** 2 + y ** 2)
            fireX += fireX_change
            fireY += fireY_change
            shoot_fire(fireX, fireY)
        # movement of fire is always a line.
        if fire_state == "shooting": # when fire is shooting, it moves in a straight line
            fireX += fireX_change
            fireY += fireY_change
            shoot_fire(fireX, fireY)
            if fireX < -10 or fireX > l - 30 or fireY < 0 or fireY > w - 30: # if fire goes out of the screen
                if boss_battle_state:
                    Main_char.health -= 100 # user loses 100 health against boss fire skull even if the user dodges the fire
                fireX = badguyX # fireX and fireY is set to the enemy's X and Y coordinates again
                fireY = badguyY
                fire_state = "fire"
    if bullet_state is "fire":
        bullet_state = "shooting" # player shoots
        bulletX_change = xx * 20 / math.sqrt(xx ** 2 + yy ** 2)
        bulletY_change = yy * 20 / math.sqrt(xx ** 2 + yy ** 2)
        bulletX += bulletX_change
        bulletY += bulletY_change
        fire_bullet(bulletX, bulletY)
        # if bullets goes out of screen, user can shoot bullet again.
    if bulletY <= 0 or bulletY >= 540 or bulletX >= 750 or bulletX <= 0:
        bullet_state = "ready"
        bulletY = playerY # player can shoot again after energy ball goes out of range

# function that makes the boundaries in the map. The player cannot enter buildings when their walls. Only when the door is unlocked, the player can enter the building from the door
def boundaries(x1, x2, y1, y2, door1, lock=None):
    w = 30
    global playerX, playerY, get_ready, parx, pary, boss_state, stats_state, playerY_change, target_state, easy_state, tutorial_state, goonImg, gooon
    if playerY_change < 0 and y2 * w >= playerY >= y2 * w - 5 and door1 * w - w - 15 <= playerX <= door1 * w - 15: # if player enters the door while moving up
        font = pygame.font.Font("freesansbold.ttf", 15)
        if lock == "unlocked": # quest 1
            parx = playerX # player's X and Y values are stored in parx and pary, so when the player leaves the quest, he will go back to his original position.
            pary = playerY
            target_state = True
        elif (lock == "twounlocked" or lock == "twoaccomplished") and locke != "defeatedboss": # quest 2
            randnum = random.randint(0,2) # different enemy's appear in quest 2
            if randnum == 0:
                goonImg = parImg1
                gooon = "evil warrior"
            elif randnum == 1:
                goonImg = parImg2
                gooon = "devil"
            else:
                gooon = "werewolf"
                goonImg = parImg3
            parx = playerX
            pary = playerY
            easy_state = True
        elif lock == "threeunlocked": # quest 3
            get_ready = True
            parx = playerX
            pary = playerY
            playerX = 370
            playerY = 500
        elif lock == "shop": # stats
            stats_state = True
            parx = playerX
            pary = playerY
            playerX = 370
            playerY = 500
        elif lock == "boss": # boss
            boss_state = True
            playerX = 0
        elif lock == "inn": # inn
            tutorial_state = True
            parx = playerX
            pary = playerY
    # if the player is not entering the door, player cannot enter the building
    if x1 * w - 2 * w <= playerX <= x1 * w - 2 * w + 5 and y1 * w - 2 * w < playerY < y2 * w:
        playerX = x1 * 30 - 2 * 30
    elif x2 * w - 5 <= playerX <= x2 * w and y1 * w - 2 * w < playerY < y2 * w:
        playerX = x2 * w
    elif y1 * w - 2 * w <= playerY <= y1 * w - 2 * w + 5 and x1 * w - 2 * w < playerX < x2 * w:
        playerY = y1 * w - 2 * w
    elif y2 * w >= playerY >= y2 * w - 5 and x1 * w - 2 * w < playerX < x2 * w:
        playerY = y2 * w

# combat system against the baby skull.
def combat_system():
    screen.blit(background2, (0, 0))
    show_score(10, 10, skull)
    enemy(enemyX, enemyY)

# displays the combat against the boss fire skull.
def bosss(XX,YY):
    screen.blit(fire_screen, (0, 0))
    screen.blit(boss_skullImg, (XX, YY))
    show_score(400, 400, boss_skull)
    font = pygame.font.Font("freesansbold.ttf", 15)
    hint = font.render("Here's the boss skull! Beware: he only gets damage if you aim him in the exact center.", True, (255, 255, 255))
    screen.blit(hint, (10, 510))

# displays the combat against the final boss
def boss_monster():
    screen.blit(background2, (0, 0))
    screen.blit(bossImg, (bossX, bossY))
    show_score(10, 10, Boss)
    font = pygame.font.Font("freesansbold.ttf", 15)
    hint = font.render("This was the secret home of the boss! Hint: aim his face.", True, (255, 255, 255))
    screen.blit(hint, (10, 510))

# displays the tutorial. Tutorial is at the start of the game, and can be checked any time during the game in the inn.
def tutorial():
    screen.blit(blackImg, (0, 0))
    font = pygame.font.Font("freesansbold.ttf", 15)
    tutorial_text1 = font.render("In this game, you will accomplish a couple quests in order to unlock the boss stage;",True,(255,255,255))
    tutorial_text2 = font.render("you win if you beat the boss. To move your player, press w, a, s, or d.",True,(255,255,255))
    tutorial_text3 = font.render("w is up, a is left, s is down, and d is right.",True,(255,255,255))
    tutorial_text4 = font.render("During a quest, you will be able to shoot energy balls using the space key.",True,(255,255,255))
    tutorial_text5 = font.render("Use your mouse to aim the enemy.",True,(255,255,255))
    tutorial_text6 = font.render("Beware: it is very skilled based and casual players are not advised to play.",True,(255,255,255))
    tutorial_text7 = font.render("Press 1 to continue.",True,(255,255,255))
    screen.blit(tutorial_text1, (100, 0))
    screen.blit(tutorial_text2, (150, 60))
    screen.blit(tutorial_text3, (230, 120))
    screen.blit(tutorial_text4, (120, 180))
    screen.blit(tutorial_text5, (260, 240))
    screen.blit(tutorial_text6, (115, 300))
    screen.blit(tutorial_text7, (290, 360))

# Intialize the pygame
pygame.init()
# name of the game
pygame.display.set_caption("Adventure Game")
l = 750
w = 540
screen = pygame.display.set_mode((l, w))  # width, height of the game screen
# default player direction is front
direction = "normal"
# user starts at the start
Main_char = Player(20, 20, 100, 100, 1, 0, 10)
# black image used for the tutorial
blackImg = pygame.image.load('black.png')
blackImg = pygame.transform.scale(blackImg, (l,w))

# Player images in all four directions
playerImg = pygame.image.load('japanguy.png')
leftImg = pygame.image.load('leftguy.png')
rightImg = pygame.image.load('rightguy.png')
backImg = pygame.image.load('backguy.png')

# player position at first
playerX = 300
playerY = 480

# image used after player wins
winImg = pygame.image.load('win.png')
winImg = pygame.transform.scale(winImg, (200, 100))

# boss fire skull image. He is set out of screen at first.
boss_skullImg = pygame.image.load('skully.png')
boss_skullImg = pygame.transform.scale(boss_skullImg, (200, 200))
boss_skullX = -10000
boss_skullY = -10000

# Boss image.
bossImg = pygame.image.load('boss.png')
bossX = 400
bossY = 100
# boss monster stats
Boss = Monster("Boss", 1000, 50000, 50000, 100000)

# Monster used in the 2nd quest. Different monsters appears everytime.
parImg1 = pygame.image.load("cartoon.png")
parImg2 = pygame.image.load("devil.png")
parImg3 = pygame.image.load("werewolf.png")
goonX = 370
goonY = 100
cartoonY = 0

# goon monster stats
goon = Monster("goon", 80, 200, 200, 20)

# Target, it's position is random.
targetImg = pygame.image.load('target.png')
targetImg = pygame.transform.scale(targetImg, (50, 50))
target_life = 5
targetX = random.randint(100, 500)
targetY = random.randint(100, 400)

# goddess in the death screen
godImg = pygame.image.load('goddess.png')
godImg = pygame.transform.scale(godImg, (500,400))

quest1 = "not done"
quest2 = "not done"
quest3 = "not done"
# numfire is number of baby skulls that was fought. when numfire>3, goes to boss skull.
numfire = 0

# image of bullet, x and y coordinate of bullet, and change in coordinates of bullet.
bulletImg = pygame.image.load('energy.png')
bulletImg = pygame.transform.scale(bulletImg, (80, 56))
bulletX = -100
bulletY = -100
# energy ball that is shot by the boss
bullet_reflection = pygame.image.load('energy.png')
reflectX = 800
reflectY = -100


# image of baby skull, x and y coordinate of it so that it is not in the screen at first, and change in coordinates of it.
enemyImg = pygame.image.load('skull.png')
enemyX = -10000
enemyY = -10000
enemyX_change = random.randint(4, 8)
enemyY_change = 10 - enemyX_change

# baby skull and boss skull stats
skull = Monster("Skull", 30,150 ,150 , 10)
boss_skull = Monster("Boss Skull", 30, 750, 750, 200)

# image of fire, x and y coordinate of fire, and change in coordinates of fire.
fireImg = pygame.image.load('fire.png')
fireX = enemyX
fireY = enemyY
fireX_change = 10
fireY_change = 10
fire_state = "fire"

# fire screen in quest 3 against the boss
fire_screen = pygame.image.load('fire2.png')
fire_screen = pygame.transform.scale(fire_screen, (l, w))

# background image
background = pygame.image.load('map2.png')
background = pygame.transform.scale(background, (l, w))

# image used in combat against baby skull and goon.
background2 = pygame.image.load("before_battle.jpg")
background2 = pygame.transform.scale(background2, (l, w))

# image used before combat against baby skull and boss skull.
before_battle = pygame.image.load('fireplace.png')
before_battle = pygame.transform.scale(before_battle, (l, w))


# different stats in the code.
ismoving = False # state is player is moving
stats_state = False # state that checks if the player is in the stats building
target_state = False # state that checks if quest1 is going on
easy_state = False # state that checks if quest2 is going on
bullet_state = "ready" # state that checks the energy ball state
get_ready = False # state that checks if quest3 is going on.
battle_state = False # state that checks if player is fighting the baby skull
boss_battle_state = False # state that checks if player is fighting boss skull
boss_state = False # state that checks if player is fighting the boss
death_state = False # state that checks if the player is in the death screen
tutorial_state = True # state that checks if the player is in the inn building
attack_back = False # state that happens when player attacks the final boss
win_state = False # state that checks if the player won the game

# default lock state for each door
locka = "inn"
lockb = "twolocked"
lockc = "shop"
lockd = "threelocked"
locke = "bosslocked"
lockf = "unlocked"

# parameter used so that player x and y returns to original position after quests.
parx = 0
pary = 0

# Game loop
# playerX change and playerY change is zero at first.
playerX_change = 0
playerY_change = 0
running = True
player(playerX, playerY, "normal")
while running: # the main loop of the game
    if Main_char.health <= 0: # if player dies, all states returns to default.
        if battle_state == True or boss_battle_state == True:
            bulletY = 2500
            boss_battle_state = False
            battle_state = False
            get_ready = False
            numfire = 0
            quest3 = "threeunlocked"
        if easy_state == True:
            easy_state = False
        get_ready = False
        boss_state = False
        death_state = True
    # collision for the baby skull.
    collision2 = isCollision(fireX, fireY, playerX, playerY, 27)
    collision3 = isCollision(enemyX, enemyY, playerX, playerY, 27)
    if collision2 or collision3 and battle_state == True:
        attack(skull, Main_char)
        fireX = -100
    # player needs to be within the screen
    if playerY > w - 30:
        playerY = 510
    elif playerY < 0:
        playerY = 0
    elif playerX > l - 30:
        playerX = 720
    elif playerX < 0:
        playerX = 0
    screen.fill((0, 0, 0))  # rgb values

    # Background image
    screen.blit(background, (0, 0))
    if tutorial_state == True:
        tutorial()
    for event in pygame.event.get():  # looping through all events

        # acquires the coordinates of the mouse
        mouseX, mouseY = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:  # the X out
            running = False  # window closes
        # if keystroke is pressed check whether is right or left

        # stops moving when key is not pressed
        if event.type == pygame.KEYUP:
            direction = "normal"
            if event.key == pygame.K_a or pygame.K_d:
                playerX_change = 0
                ismoving = False
            if event.key == pygame.K_s or pygame.K_w:
                playerY_change = 0
                ismoving = False
        # moves when key is down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                direction = "left"
                playerX_change = -5
                ismoving = True
            elif event.key == pygame.K_d:
                direction = "right"
                playerX_change = 5
                ismoving = True
            elif event.key == pygame.K_w:
                direction = "back"
                playerY_change = -5
                ismoving = True
            elif event.key == pygame.K_s:
                direction = "normal"
                playerY_change = 5
                ismoving = True
            if event.key == pygame.K_SPACE: # shoots if player is in combat
                if bullet_state is "ready" and (battle_state == True or boss_battle_state == True or boss_state == True or target_state == True or easy_state == True or tutorial_state == True) :  # can only fire when its ready/reset
                    # get the current x coord of statement, not changing
                    temp_mouseX = mouseX
                    temp_mouseY = mouseY
                    bulletX = playerX
                    bulletY = playerY
                    xx = temp_mouseX - bulletX
                    yy = temp_mouseY - bulletY
                    fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_r: # player can revive if he/she presses r in the death screen
                if death_state == True:
                    Main_char.max_health *= .9
                    Main_char.health = Main_char.max_health
                    death_state = False
            if event.key == pygame.K_1: # player can leave tutorial if he/she presses 1
                if tutorial_state == True:
                    tutorial_state = False
                    if parx == 0:
                        playerX = 300
                        playerY = 480
                    else:
                        playerX = parx
                        playerY = pary
            if event.key == pygame.K_q and stats_state == True: # player can leave stats building if he/she presses q
                stats_state = False
                playerX = parx
                playerY = pary

    if battle_state == False and get_ready == False and boss_state == False and stats_state == False and target_state == False and easy_state == False and tutorial_state == False: # boundaries occur when player is in the normal map
        show_status()
        boundaries(2, 6, 13, 16, 5, locka)
        boundaries(9, 12, 9, 11, 11, lockb)
        boundaries(2, 4, 6, 6, -1000)
        boundaries(1, 5, 7, 10, 3, lockc)
        boundaries(9, 13, 2, 3, -1000)
        boundaries(9, 12, 4, 4, 11, lockd)
        boundaries(16, 18, 2, 2, -1000)
        boundaries(15, 19, 3, 6, 17, locke)
        boundaries(14, 16, 15, 17, -1000)
        boundaries(20, 23, 12, 14, 22, lockf)

    if death_state: # death
        death()
    if easy_state: # quest 2, goon goes after player, player needs to escape and shoot the goon
        goon_fight(goonX, goonY)
        show_score(10, 10, goon)
        if isCollision(goonX+5, goonY+10, bulletX, bulletY, 30):
            attack(Main_char, goon)
            bullet_state = "ready"
            bulletX = 1000
        if isCollision(playerX, playerY, goonX, goonY, 30):
            attack(goon, Main_char)
            goonX = random.randint(100,500)
            goonY = random.randint(100,500)
        if goon.health<=0:
            easy_state = False
            quest2 = "accomplished"
            give_loot(goon)
            level_up(Main_char)
            goon.health = goon.max_health
            Main_char.health = Main_char.max_health
            playerX = parx
            playerY = pary
        x = playerX - goonX
        y = playerY - goonY
        goonX_change = x * 3 / math.sqrt(x ** 2 + y ** 2)
        goonY_change = y * 3 / math.sqrt(x ** 2 + y ** 2)
        goonX += goonX_change
        goonY += goonY_change

    if target_state: # quest 1. player shoots target 5 times.
        playerX = 370
        playerY = 480
        target(targetX, targetY)
        target_left(target_life)
        if isCollision(targetX - 10, targetY - 10, bulletX, bulletY, 50):
            targetX = random.randint(100, 500)
            targetY = random.randint(100, 400)
            target_life -= 1
            bullet_state = "ready"
            bulletX = playerX
            bulletY = playerY
        if target_life <= 0:
            target_state = False
            quest1 = "accomplished"
            lockf = "accomplished"
            playerX = parx
            playerY = pary

    if boss_state: # final boss. boss does 10 times damage that the player does on him.
        boss_monster()
        if playerX >= 400:
            Main_char.health -= 99
            playerX -= 100
        if Boss.health <= 0:
            locke = "defeatedboss"
            print("here")
            Main_char.health = Main_char.max_health
            boss_state = False
            give_loot(Boss)
            level_up(Main_char)
            playerX = 300
            playerY = 480
        if attack_back == True:
            reflection(reflectX, playerY)
            reflectX-=100
            if reflectX<=playerX:
                attack_back = False
                reflectX = 800
                for i in range(10):
                    attack(Main_char, Main_char)


    # playerX or Y changes
    playerX += playerX_change
    playerY += playerY_change

    # coliision detection with the boss fire skull.
    collision_boss = isCollision(boss_skullX, boss_skullY, bulletX, bulletY, 27)
    if collision_boss and boss_battle_state == True:
        attack(Main_char, boss_skull)
        bulletY = -100
    if isCollision(bossX + 150, bossY + 50, bulletX, bulletY, 25) and boss_state:
        attack(Main_char, Boss)
        bulletX = 1000
        attack_back = True

    # collidion detection with the baby skull
    collision = isCollision(enemyX, enemyY, bulletX, bulletY, 27)
    if collision and battle_state == True:
        attack(Main_char, skull)
        bulletY = -100

    # if baby skull dies.
    if skull.health <= 0:
        numfire += 1
        bulletY = 10000
        bullet_state = "ready"
        battle_state = False
        enemyX = -1000
        enemyY = -1000
        playerX = parx
        playerY = pary
        Main_char.health = Main_char.max_health
        skull.health = skull.max_health
        give_loot(skull)
        level_up(Main_char)

    # if boss skull dies
    if boss_skull.health <= 0:
        quest3 = "accomplished"
        bulletY = -10000
        get_ready = False
        boss_battle_state = False
        battle_state = False
        playerX = parx
        playerY = pary
        Main_char.health = Main_char.max_health
        boss_skull.health = boss_skull.max_health
        give_loot(boss_skull)
        level_up(Main_char)
    # baby skull changes direction when hitting the boundaries on the screen
    if battle_state == True and (enemyY > 490 or enemyY < 0):
        enemyY_change *= -1
    elif battle_state == True and (enemyX > 700 or enemyX < 0):
        enemyX_change *= -1

    # baby skull moves
    if battle_state == True:
        enemyX += enemyX_change
        enemyY += enemyY_change

    # stats building
    if stats_state == True:
        display_stats()

    # quest 3
    if get_ready == True:
        before_batt()
    # in quest 3, player needs to fight 3 baby skulls
    if get_ready == True and ismoving == True and battle_state == False and quest3 != "fighting":
        if numfire >= 3: # after killing 3 baby skulls, player goes to battle against boss skull.
            boss_skullX = 375
            boss_skullY = 270
            quest3 = "final battle"
        else:
            option = random.randint(0, 50)
            if option == 3:
                enemyX = 370
                enemyY = 200
                battle_state = True
                playerX = 370
                playerY = 500

    if quest3 == "final battle" and death_state == False: # boss fire skull.
        quest3 = "fighting"
        playerX = 600
        playerY = 490
        boss_battle_state = True
    if easy_state == True: # quest 2
        quest(goonX, goonY)
    if battle_state == True: # combat against baby skull
        combat_system()
        quest(enemyX, enemyY)
    if boss_battle_state == True: # combat against boss skull
        bosss(boss_skullX-70,boss_skullY-80)
        quest(boss_skullX, boss_skullY)
    if boss_state == True: # combat against boss
        quest(bossX, bossY)
    if target_state == True: # quest 1
        quest(targetX, targetY)
    if tutorial_state == True: # tutorial, can be checked in the inn
        quest(0, 0)
    if win_state == True: # you win!
        locka = "closed"
        lockc = "closed"
        you_win()
    if quest1 == "accomplished" and quest2 != "accomplished": # unlock second quest when first quest is done
        lockb = "twounlocked"
        lockf = "accomplished"
    if quest2 == "accomplished" and quest3 != "accomplished": # unlock third quest when second quest is done
        lockd = "threeunlocked"
        lockb = "twoaccomplished"
    if quest3 == "accomplished" and locke != "defeatedboss": # unlock boss quest when third quest is done
        lockd = "accomplished"
        locke = "boss"
        lockd = "accomplished"
    if locke == "defeatedboss": # win state becomes true after the boss was defeated
        win_state = True

    player(playerX, playerY, direction) # player x and y and direction changes
    pygame.display.update()



