#NAME: Mr. B
#DATE: May 8, 2025
#This is a multi-room maze game that shows how we can form new levels

import pygame
import random
import math
import threading 

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
purple = (128, 0, 128)

#same wall class as before, these are our boundaries
class Wall(pygame.sprite.Sprite):

  def __init__(self, x, y, width, height, colour):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([width, height])
    self.image.fill(colour)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

#Same player that we've been using throughout
class Player(pygame.sprite.Sprite):

  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([20, 20])
    self.image.fill(green)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.xvel = 0
    self.yvel = 0

  def changespeed(self, x, y):
    self.xvel += x
    self.yvel += y

#This detects when we hit the walls
  def update(self, walls):
    self.rect.x += self.xvel
    wall_hit_list = pygame.sprite.spritecollide(self, walls, False)
    for block in wall_hit_list:
      if self.xvel > 0:
        self.rect.right = block.rect.left
      else:
        self.rect.left = block.rect.right

    self.rect.y += self.yvel
    wall_hit_list = pygame.sprite.spritecollide(self, walls, False)
    for block in wall_hit_list:
      if self.yvel > 0:
        self.rect.bottom = block.rect.top
      else:
        self.rect.top = block.rect.bottom
class enemy1(pygame.sprite.Sprite):

  def __init__(self, player):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([20, 20])
    self.image.fill(red)
    self.rect = self.image.get_rect()
    self.rect.x = 550
    self.rect.y = 180
    self.xvel = 0
    self.yvel = 0
    #acceleration variables aming player
    self.accAng = 0
    #max acc(constant)
    self.acc = 3
    self.m_player = player
    self.flg = True
    self.roomNum = 0

  def update(self, walls, roomNum):
    
    if self.isRoomChanged(roomNum):
      self.rect.x = 300
      self.rect.y = 200

    print(self.acc)
    # print(self.flg)
    self.accAng = math.atan2(self.m_player.rect.y + self.m_player.yvel - self.rect.y, self.m_player.rect.x + self.m_player.xvel - self.rect.x)
    self.xvel = math.cos(self.accAng) * self.acc
    self.yvel = math.sin(self.accAng) * self.acc
    self.rect.x += self.xvel
    

    
    wall_hit_list = pygame.sprite.spritecollide(self, walls, False)
    for block in wall_hit_list:
      if self.xvel > 0:
        self.rect.right = block.rect.left
      else:
        self.rect.left = block.rect.right
        
    self.rect.y += self.yvel
    wall_hit_list = pygame.sprite.spritecollide(self, walls, False)
    for block in wall_hit_list:
      if self.yvel > 0:
        self.rect.bottom = block.rect.top
      else:
        self.rect.top = block.rect.bottom


  def changeflg(self):
    self.flg = not self.flg
    if self.flg:
        self.image.fill(blue)
        self.acc = 4
    else:
        self.image.fill(red)
        self.acc = 6
    # this is a thread that will run every 2 seconds it only run once so need to keep calling it

    threading.Timer(4, self.changeflg).start()
  def isRoomChanged(self, roomNum):
    if self.roomNum != roomNum:
      self.roomNum = roomNum
      return True
    else:
      return False

#basic room class, with list of walls present
class Room():
  wall_list = []

  def __init__(self):
    self.wall_list = pygame.sprite.Group()

#we make a specific class for each room
class Room1(Room):
  def __init__(self):
    Room.__init__(self)

    walls = [ [0, 0, 20, 170, black],
              [0, 210, 20, 190, black],
              [0, 0, 600, 20, black],
              [0, 380, 600, 20, black],
              [580, 0, 20, 170, black],
              [580, 210, 20, 190, black],
              [250, 200, 20, 110, black]
            ]

    for item in walls:
    #item[0] = x, item[1] = y, item[2] = width, item[3] = ht, item[4] = colour
      wall = Wall(item[0], item[1], item[2], item[3], item[4])
      self.wall_list.add(wall)
    #quickest way to create all the walls 

class Room2(Room):
  def __init__(self):
    Room.__init__(self)

    walls = [ [0, 0, 20, 170, blue],
              [0, 210, 20, 190, blue],
              [0, 0, 280, 20, blue],
              [320, 0, 280, 20, blue],
              [0, 380, 280, 20, blue], # bottom left
              [320, 380, 280, 20, blue], # bottom right
              [580, 0, 20, 170, blue],
              [580, 210, 20, 190, blue],
              [80, 50, 20, 310, blue],
              [500, 50, 20, 310, blue]
            ]

    for item in walls:
      wall = Wall(item[0], item[1], item[2], item[3], item[4])
      self.wall_list.add(wall)

class Room3(Room):
  def __init__(self):
    Room.__init__(self)

    walls = [ [0, 0, 20, 170, red],
              [0, 210, 20, 190, red],
              [0, 0, 600, 20, red],
              [0, 380, 600, 20, red],
              [580, 0, 20, 170, red],
              [580, 210, 20, 190, red],
              [250, 200, 20, 110, red],
              [350, 90, 20, 110, red]
            ]

    for item in walls:
      wall = Wall(item[0], item[1], item[2], item[3], item[4])
      self.wall_list.add(wall)

class Room4(Room):
  def __init__(self):
    Room.__init__(self)
    
    walls = [ [0, 0, 20, 400, orange], # left
              [580, 0, 20, 400, orange], # right
              [0, 0, 600, 20, orange], # top
              [0, 380, 280, 20, orange], # bottom left
              [320, 380, 280, 20, orange], # bottom right
              [100, 100, 20, 100, orange],
              [100, 100, 100, 20, orange],
              [250, 200, 20, 100, orange],
              [250, 200, 100, 20, orange], 
              [400, 100, 20, 100, orange],
              [400, 100, 100, 20, orange]
            ]

    for item in walls:
      wall = Wall(item[0], item[1], item[2], item[3], item[4])
      self.wall_list.add(wall)

class Room5(Room):
  def __init__(self):
    Room.__init__(self)
    
    walls = [ [0, 0, 20, 400, purple], # left
              [580, 0, 20, 400, purple], # right
              [0, 380, 600, 20, purple], # bottom
              [0, 0, 280, 20, purple], # top left
              [320, 0, 280, 20, purple] # top right
            ]

    for item in walls:
      wall = Wall(item[0], item[1], item[2], item[3], item[4])
      self.wall_list.add(wall)
def main():
  pygame.init()
  screen = pygame.display.set_mode([600, 400])
  pygame.display.set_caption("Multiple Maze Madness")

  #starting location of player, right in middle of opening
  player = Player(10, 180)
  enemy = enemy1(player)

  enemy.changeflg()

  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)
  all_sprites.add(enemy)

  clock = pygame.time.Clock()

  done = False

  #create a list of rooms so we can access each 
  rooms = []

  #rooms[0]
  room = Room1()
  rooms.append(room)

  #rooms[1]
  room = Room2()
  rooms.append(room)

  #rooms[2]
  room = Room3()
  rooms.append(room)

  #rooms[3]
  room = Room4()
  rooms.append(room)

  #rooms[4]
  room = Room5()
  rooms.append(room)

  roomNum = 3     #starting room
  currentRoom = rooms[roomNum]

  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          player.changespeed(-5, 0)

        elif event.key == pygame.K_RIGHT:
          player.changespeed(5, 0)

        elif event.key == pygame.K_UP:
          player.changespeed(0, -5)

        elif event.key == pygame.K_DOWN:
          player.changespeed(0, 5)

      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          player.changespeed(5, 0)
        elif event.key == pygame.K_RIGHT:
          player.changespeed(-5, 0)
        elif event.key == pygame.K_UP:
          player.changespeed(0, 5)
        elif event.key == pygame.K_DOWN:
          player.changespeed(0, -5)

    #updates the player with the walls of the current room to detect collision
    player.update(currentRoom.wall_list)

    enemy.update(currentRoom.wall_list, roomNum)

    wall_hit_list = pygame.sprite.collide_rect(player, enemy)

    if wall_hit_list:
      done = True
      
    #this handles when to swithf to the next room based on location of player
    #first if controls when the player exits screen left
    if player.rect.x < -10:
      if roomNum == 0:
        roomNum = 2
        currentRoom = rooms[roomNum]
        player.rect.x = 590
      elif roomNum == 2:
        roomNum = 1
        currentRoom = rooms[roomNum]
        player.rect.x = 590
      elif roomNum == 1:
        roomNum = 0
        currentRoom = rooms[roomNum]
        player.rect.x = 590
    #first if controls when the player exits screen right
    if player.rect.x > 590:
      if roomNum == 0:
        roomNum = 1
        currentRoom = rooms[roomNum]
        player.rect.x = -10
      elif roomNum == 1:
        roomNum = 2
        currentRoom = rooms[roomNum]
        player.rect.x = -10
      elif roomNum == 2:
        roomNum = 0
        currentRoom = rooms[roomNum]
        player.rect.x = -10
    
    # set up for only 
    if player.rect.y < -10:
      if roomNum == 1:
        roomNum = 3
        currentRoom = rooms[roomNum]
        player.rect.y = 410
      elif roomNum == 4:
        roomNum = 1
        currentRoom = rooms[roomNum]
        player.rect.y = 410
    elif player.rect.y > 410:
      if roomNum == 1:
        roomNum = 4
        currentRoom = rooms[roomNum]
        player.rect.y = -10
      elif roomNum == 3:
        roomNum = 1
        currentRoom = rooms[roomNum]
        player.rect.y = -10

    screen.fill(white)
    all_sprites.draw(screen)
    currentRoom.wall_list.draw(screen)

    pygame.display.flip()
    clock.tick(30)

  font = pygame.font.SysFont("calibri", 25)
  text = font.render("Game Over, (q to quit, c to contiune)", True, white)
  screen.fill(black)
  screen.blit(text, [110, 150])
  pygame.display.flip()

  xxx = True
  while xxx:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          xxx = False
          break
        elif event.key == pygame.K_c:
          main()
  pygame.quit()
  
main()