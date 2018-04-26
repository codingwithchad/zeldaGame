import pygame, sys
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *

# INSTANCES OF GAME OBJECTS
PLAYER = heroes.LINK()
WAND = items.WAND()
GOLD = items.GOLD()
BEAST = enemies.BEAST()

print(GOLD.POS)

# OTHER CONFIG
INVFONT = pygame.font.SysFont('FreeSansBold.ttf', 20)

GAME_OVER = False
# GAME LOOP
while not GAME_OVER:

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == pygame.locals.KEYDOWN):
            # MOVE RIGHT
            if (event.key == K_RIGHT) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
                PLAYER.PLAYER_POS[0] += 1
            # MOVE LEFT
            elif (event.key == K_LEFT) and PLAYER.PLAYER_POS[0] > 0:
                PLAYER.PLAYER_POS[0] -=1
            # MOVE UP
            elif (event.key == K_UP) and PLAYER.PLAYER_POS[1] > 0:
                PLAYER.PLAYER_POS[1] -= 1
            elif (event.key == K_DOWN) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
                PLAYER.PLAYER_POS[1] += 1

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
            DISPLAYSURFACE.blit(PLAYER.PLAYER, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
            DISPLAYSURFACE.blit(BEAST.BEAST, (BEAST.BEAST_POS[0]*TILESIZE, BEAST.BEAST_POS[1]*TILESIZE))

            if WAND.PLACED:
                DISPLAYSURFACE.blit(WAND.IMAGE, (WAND.POS[0]*TILESIZE, WAND.POS[1]*TILESIZE))
            if GOLD.PLACED:
                DISPLAYSURFACE.blit(GOLD.IMAGE, (GOLD.POS[0]*TILESIZE, GOLD.POS[1]*TILESIZE))
    
    # PICKUP ITEM CONDITIONS
    if PLAYER.PLAYER_POS == WAND.POS and WAND.PLACED:
        PLAYER.PLAYER_INV.append(WAND)
        WAND.PLACED = False
    
    if PLAYER.PLAYER_POS == GOLD.POS and GOLD.PLACED:
        PLAYER.PLAYER_INV.append(GOLD)
        GOLD.PLACED = False
        
    INVENTORY_POSITION = 15 
    for item in PLAYER.PLAYER_INV:
        DISPLAYSURFACE.blit(item.IMAGE, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+35))
        INVENTORY_POSITION += 25 
        INVENTORY_TEXT = INVFONT.render(item.NAME, True, WHITE, BLACK)
        DISPLAYSURFACE.blit(INVENTORY_TEXT, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+20))
        INVENTORY_POSITION += 75

    pygame.display.update()


