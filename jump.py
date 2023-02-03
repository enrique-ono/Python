import pygame 
pygame.init() 
 
win = pygame.display.set_mode((500,500)) 
pygame.display.set_caption("First Game") 
 
x = 50 
y = 50 
width = 40 
height = 60 
vel = 5 
 
isJump = False 
jumpCount = 10 
 
run = True 
 
while run:     
    pygame.time.delay(10) 
 
    for event in pygame.event.get():         
        if event.type == pygame.QUIT:             
            run = False 
 
    keys = pygame.key.get_pressed()          
    
    if keys[pygame.K_LEFT] and x > vel:          
        x -= vel 
 
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:           
        x += vel              
        
    if not(isJump):          
        if keys[pygame.K_UP] and y > vel:             
            y -= vel 
 
        if keys[pygame.K_DOWN] and y < 500 - height - vel:             
            y += vel 
 
        if keys[pygame.K_SPACE]:             
            isJump = True     
    else:         
        if jumpCount >= -10:             
            y -= (jumpCount * abs(jumpCount)) * 0.5             
            jumpCount -= 1         
        else:              
            jumpCount = 10             
            isJump = False 

    win.fill((0,0,0))     
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))        
    pygame.display.update()       
pygame.quit()
if keys[pygame.K_LEFT] and x > vel:  # Stelltsicher, dass die obere linke Position unseres Charakters grösser ist als die Variable "vel", damit wir uns nie vom Bildschirm entfernen.
    x -= vel
if keys[pygame.K_RIGHT] and x < 500 -vel -width:  # Stellt sicher, dass die obere rechte Ecke unseres Charakters kleiner ist als die Bildschirmbreite minus seiner Breite.
    x += vel
if keys[pygame.K_UP] and y > vel:  # Für die y-Koordinate gelten die gleichen Prinzipien
    y -= vel
if keys[pygame.K_DOWN] and y < 500 -height -vel:
    y += vel
# Dies geht fast an den Anfang des Programms, ausserhalb der while-Schleife.
isJump = False
jumpCount = 10
# Befindetsich in der while-Schleife, unter dem Event zum Abwärts bewegen.
if keys[pygame.K_SPACE]:
    isJump = True
if not(isJump):# Prüft, ob der Benutzer nicht springt
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 -height -vel:
        y += vel
    if keys[pygame.K_SPACE]:
        isJump = True
else:
    # Das wird passieren, wenn wir springen
    if jumpCount >= -10:
        y -= (jumpCount * abs(jumpCount)) * 0.5
        jumpCount -= 1
    else: # Dies wird ausgeführt, wenn der Sprung beendet ist.
        jumpCount = 10
        isJump = False
        # Zurücksetzen unserer Variablen