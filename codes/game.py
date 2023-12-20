import pygame
# pygame setup
pygame.init()
screen_width=800
screen_height=600
clock = pygame.time.Clock()
running = True


bg=pygame.image.load('./codes/img/grass.png')
class Player:
    def __init__(self,top,left):
        self.images={
            'R':pygame.image.load('./codes/img/player.png'),
            'L':pygame.image.load('./codes/img/playerl.png'),      
        }
        self.speed=2
        self.image_direction='R'
        self.image=self.images.get(self.image_direction)
        self.player_rect=self.image.get_rect()
        self.player_rect.x=left
        self.player_rect.y=top
    def move(self):

        if self.direction=='R':
            if self.player_rect.x+self.speed<screen_width-50:
                self.player_rect.x+=self.speed
        if self.direction=='L':
            if self.player_rect.x-self.speed>0:
                self.player_rect.x-=self.speed
        if self.direction=='U':
            if self.player_rect.y-self.speed>0:
                self.player_rect.y-=self.speed
        if self.direction=='D':
            if self.player_rect.y+self.speed<screen_height-50:
                self.player_rect.y+=self.speed
    def display_player(self):
        self.image=self.images.get(self.image_direction)
        self.image=pygame.transform.scale(self.image,(50,50))
        MainGame.screen.blit(self.image,self.player_rect)


class MainGame:
    player=None
    screen=None
    def start_game(self):
        pygame.display.init()
        MainGame.screen=pygame.display.set_mode((screen_width,screen_height))
        pygame.display.set_caption("TIME CASHIER!1.0")
        MainGame.player=Player(300,350)
        while True:
            self.key_events()

            MainGame.screen.blit(bg,(0,0))
            MainGame.player.display_player()


 #           dt = clock.tick(60) / 1000
            pygame.display.update()

    def key_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_game()



        keys = pygame.key.get_pressed()

            
        if keys[pygame.K_w]:
            if MainGame.player.player_rect.y-MainGame.player.speed>0:
                MainGame.player.player_rect.y-=MainGame.player.speed
        if keys[pygame.K_s]:
            if MainGame.player.player_rect.y+MainGame.player.speed<screen_height-50:
                MainGame.player.player_rect.y+=MainGame.player.speed
        if keys[pygame.K_a]:
            if MainGame.player.player_rect.x-MainGame.player.speed>0:
                MainGame.player.player_rect.x-=MainGame.player.speed
                MainGame.player.image_direction='L'
        if keys[pygame.K_d]:
            if MainGame.player.player_rect.x+MainGame.player.speed<screen_width-50:
                MainGame.player.player_rect.x+=MainGame.player.speed
                MainGame.player.image_direction='R'



    def end_game(self):
        print("See you ~♥")
        exit()
        



if __name__=="__main__":
    MainGame().start_game()


    

