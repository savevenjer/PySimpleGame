import pgzrun
from random import randint

# Initialize the game window
TITLE = 'Meow'
WIDTH = 800
HEIGHT = 600

# Define game states
MENU = 0
GAME = 1
GAMEN = 2
GAMEH = 3

# Initialize the current game state
current_state = MENU

# Game variables
Score = 0
Time = 30
Lives = 20
Game_Over = False
MAX_TIME = 0

cat = Actor('cat', (WIDTH/2,HEIGHT/500))
apple = Actor('apple')
orange = Actor('orange')
cherry = Actor('cherry')
pineapple = Actor('pineapple')
watermelon = Actor('watermalon')
backgroundmenu = 'page.png'
background1 = 'page1.png'
background2 = 'page2.png'
background3 = 'page3.png'
endbackground = 'endpage.png'

# Function to draw the game screen
def draw():
    if current_state == MENU:
        screen.blit(backgroundmenu,(0,0))
        screen.draw.text("Press Z to Easy Mode", (200, 200), fontsize=30, color='white')
        screen.draw.text("Press N to Normal Mode", (200, 250), fontsize=30, color='white')
        screen.draw.text("Press H to Hard Mode", (200, 300), fontsize=30, color='white')
    
    elif current_state == GAME:
        if Game_Over:
            screen.blit(endbackground,(0,0))
            screen.draw.text(f' Game Over ! Your score: {Score}', (200, 20), fontsize=50)
            screen.draw.text(f' Press X to Restart', (200, 60), fontsize=50)
        else:
            screen.blit(background1,(0,0))
            screen.draw.text(f'Lives: {Lives}', (5, 50), fontsize=30)
            screen.draw.text(f'Score: {Score}', (5, 10), fontsize=30)
            screen.draw.text(f'Time: {Time}', (690, 10), fontsize=30)
            cat.draw()
            apple.draw()
            orange.draw()
            cherry.draw()
            screen.blit('ground', (0, 150))

    elif current_state == GAMEN:
        if Game_Over:
            screen.blit(endbackground,(0,0))
            screen.draw.text(f' Game Over ! Your score: {Score}', (200, 10), fontsize=50)
            screen.draw.text(f' Press X to Restart', (200, 50), fontsize=50)
        else:
            screen.blit(background2,(0,0))
            screen.draw.text(f'Lives: {Lives}', (5, 50), fontsize=30)
            screen.draw.text(f'Score: {Score}', (5, 10), fontsize=30)
            screen.draw.text(f'Time: {Time}', (690, 10), fontsize=30)
            cat.draw()
            apple.draw()
            orange.draw()
            cherry.draw()
            pineapple.draw()
            screen.blit('ground', (0, 150))
            
    elif current_state == GAMEH:
        if Game_Over:
            screen.blit(endbackground,(0,0))
            screen.draw.text(f' Game Over ! Your score: {Score}', (200, 10), fontsize=50)
            screen.draw.text(f' Press X to Restart', (200, 50), fontsize=50)
        else:
            screen.blit(background3,(0,0))
            screen.draw.text(f'Lives: {Lives}', (5, 50), fontsize=30)
            screen.draw.text(f'Score: {Score}', (5, 10), fontsize=30)
            screen.draw.text(f'Time: {Time}', (690, 10), fontsize=30)
            cat.draw()
            apple.draw()
            orange.draw()
            cherry.draw()
            pineapple.draw()
            watermelon.draw()
            screen.blit('ground', (0, 150))
    
    

# Function to handle key presses
def on_key_down(key, mod, unicode):
    global Score, Time, Game_Over, Lives, current_state

    if current_state == MENU:
        if key == keys.Z:  # Enter Z to start the easy mode
            current_state = GAME
            reset_game()
            
        if key == keys.N:  # Enter N to start the Normal mode
            current_state = GAMEN
            reset_gameN()
            
        if key == keys.H:  # Enter H to start the Hard mode
            current_state = GAMEH
            reset_gameH()
           
            
    elif current_state == GAME:
        if Game_Over:
            if key == keys.X:  # Enter to restart the game
                current_state = GAME
                reset_game()
        else:
            if key == keys.P:  # Enter P for back to menu
                current_state = MENU
                clock.unschedule(count_time)

    elif current_state == GAMEN:
        if Game_Over:
            if key == keys.X:  # Enter to restart the game
                current_state = GAMEN
                reset_gameN()
        else:
            if key == keys.P:  # Enter P for back to menu
                current_state = MENU
                clock.unschedule(count_time)

    elif current_state == GAMEH:
        if Game_Over:
            if key == keys.X:  # Enter to restart the game
                current_state = GAMEH
                reset_gameH()
        else:
            if key == keys.P:  # Enter P for back to menu
                current_state = MENU
                clock.unschedule(count_time)
                
  
    

# Function to update the game state
def update():
    global Score, Lives, Game_Over
    
    if current_state == GAME: 
        if Game_Over :
            return
        
        if keyboard.left and cat.x > 28:
            cat.x -= 8
        elif keyboard.right and cat.x < 767:
            cat.x += 8

        apple.y += apple.speed
        orange.y += orange.speed
        cherry.y += cherry.speed

        if apple.y == 500:
            Lives -= 1
        if orange.y == 500:
            Lives -= 1
        if cherry.y == 500:
            Lives -= 1
        if Lives == 0:
            Game_Over = True
            clock.unschedule(count_time)

        if apple.y > HEIGHT:
            place_apple()
        if orange.y > HEIGHT:
            place_orange()
        if cherry.y > HEIGHT:
            place_cherry()

        for n in [apple, orange, cherry]:
                if cat.colliderect(n):
                    sounds.meow.play()
                    Score += 1
                    if n == apple:
                        place_apple()
                    elif n == orange:
                        place_orange()
                    elif n == cherry:
                        place_cherry()
                   
                
                    
#==============================================#                   
    if current_state == GAMEN: #Normal mode
        if Game_Over :
            return
        
        if keyboard.left and cat.x > 28:
            cat.x -= 8
        elif keyboard.right and cat.x < 767:
            cat.x += 8

        apple.y += apple.speed
        orange.y += orange.speed
        cherry.y += cherry.speed
        pineapple.y += pineapple.speed

        if apple.y == 500:
            Lives -= 1
        if orange.y == 500:
            Lives -= 1
        if cherry.y == 500:
            Lives -= 1
        if pineapple.y == 500:
            Lives -= 1
        if Lives == 0:
            Game_Over = True
            clock.unschedule(count_time)

        if apple.y > HEIGHT:
            place_apple()
        if orange.y > HEIGHT:
            place_orange()
        if cherry.y > HEIGHT:
            place_cherry()
        if pineapple.y > HEIGHT:
            place_pineapple()

        for n in [apple, orange, cherry,pineapple]:
                if cat.colliderect(n):
                    sounds.meow.play()
                    Score += 1
                    if n == apple:
                        place_apple()
                    elif n == orange:
                        place_orange()
                    elif n == cherry:
                        place_cherry()
                    elif n == pineapple:
                        place_pineapple()
                        
#==============================================#

    if current_state == GAMEH: #Hard mode
        if Game_Over :
            return
        
        if keyboard.left and cat.x > 28:
            cat.x -= 8
        elif keyboard.right and cat.x < 767:
            cat.x += 8

        apple.y += apple.speed
        orange.y += orange.speed
        cherry.y += cherry.speed
        pineapple.y += pineapple.speed
        watermelon.y += watermelon.speed

        if apple.y == 500:
            Lives -= 2
        if orange.y == 500:
            Lives -= 2
        if cherry.y == 500:
            Lives -= 2
        if pineapple.y == 500:
            Lives -= 2
        if watermelon.y == 500:
            Lives -= 2
        if Lives == 0:
            Game_Over = True
            clock.unschedule(count_time)

        if apple.y > HEIGHT:
            place_apple()
        if orange.y > HEIGHT:
            place_orange()
        if cherry.y > HEIGHT:
            place_cherry()
        if pineapple.y > HEIGHT:
            place_pineapple()
        if watermelon.y > HEIGHT:
            place_watermelon()

        for n in [apple, orange, cherry,pineapple,watermelon]:
                if cat.colliderect(n):
                    sounds.meow.play()
                    Score += 1
                    if n == apple:
                        place_apple()
                    elif n == orange:
                        place_orange()
                    elif n == cherry:
                        place_cherry()
                    elif n == pineapple:
                        place_pineapple()
                    elif n == watermelon:
                        place_watermelon()
    

# Function to count time
def count_time():
    global Time, Game_Over

    if current_state == GAME:
        Time -= 1
        if Time == MAX_TIME:
            Game_Over = True
            clock.unschedule(count_time)

    if current_state == GAMEN:
        Time -= 1
        if Time == MAX_TIME:
            Game_Over = True
            clock.unschedule(count_time)

    if current_state == GAMEH:
        Time -= 1
        if Time == MAX_TIME:
            Game_Over = True
            clock.unschedule(count_time)

    

# Function to reset the game
def reset_game():
    global Score,Time,Game_Over,Lives

    Score = 0
    Time = 30
    Lives = 20
    Game_Over = False
    place_apple()
    place_orange()
    place_cherry()
    
    cat.pos = (WIDTH/2 ,500)
    clock.schedule_interval(count_time,1)

def reset_gameN():
    global Score,Time,Game_Over,Lives

    Score = 0
    Time = 30
    Lives = 20
    Game_Over = False
    place_apple()
    place_orange()
    place_cherry()
    place_pineapple()

    cat.pos = (WIDTH/2 ,500)
    clock.schedule_interval(count_time,1)

def reset_gameH():
    global Score,Time,Game_Over,Lives

    Score = 0
    Time = 30
    Lives = 20
    Game_Over = False
    place_apple()
    place_orange()
    place_cherry()
    place_pineapple()
    place_watermelon()

    cat.pos = (WIDTH/2 ,500)
    clock.schedule_interval(count_time,1)

# Function to place an apple
def place_apple():
    apple.x = randint(apple.width, WIDTH - apple.width)
    apple.y = 0
    apple.speed = randint(3, 6)

# Function to place an orange
def place_orange():
    orange.x = randint(orange.width, WIDTH - orange.width)
    orange.y = 0
    orange.speed = randint(3, 6)

# Function to place a cherry
def place_cherry():
    cherry.x = randint(cherry.width, WIDTH - cherry.width)
    cherry.y = 0
    cherry.speed = randint(3, 6)

# Function to place a pineapple
def place_pineapple():
    pineapple.x = randint(pineapple.width, WIDTH - pineapple.width)
    pineapple.y = 0
    pineapple.speed = randint(3, 6)
    
# Function to place a 
def place_watermelon():
    watermelon.x = randint(watermelon.width, WIDTH - watermelon.width)
    watermelon.y = 0
    watermelon.speed = randint(3, 6)


# Run the game
pgzrun.go()
