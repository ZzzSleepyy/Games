import pygame
import random


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

text_font = pygame.font.SysFont("MS Comic Sans", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
    
running = True
is_shooting = False
dt = 0

bullets = []
bullet_speed = 10

enemies = []
enemy_speed = 7

score = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:    
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_shooting = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_shooting = False
    screen.fill("purple")

    player = pygame.draw.circle(screen, "white", player_pos, 20)

    if keys[pygame.K_w]:
        player_pos.y -= 200 * dt
    if keys[pygame.K_s]:
        player_pos.y += 200 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 200 * dt
    if keys[pygame.K_d]:
        player_pos.x += 200 * dt     

    for enemy_rect in enemies[:]:
            if player.colliderect(enemy_rect):
                running = False
    
    if is_shooting:
        bullet = pygame.Rect(player_pos.x - 2, player_pos.y, 4, 10)
        bullets.append(bullet)
        
    
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
        for enemy_rect in enemies[:]: 
            if bullet.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemies.remove(enemy_rect)
                score += 1
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)
        
    draw_text(f"SCORE: {score}", text_font, (0,0,0), 100, 0)

    
    if random.randint(0, 100) < 5: 
        enemy_x = random.randint(0, screen.get_width())
        enemy_y = 0
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 30, 30)  
        enemies.append(enemy_rect)

    # Move and draw enemies
    for enemy_rect in enemies:
        enemy_rect.y += enemy_speed
        pygame.draw.rect(screen, (255, 0, 0), enemy_rect)
        
        
    pygame.display.flip()

    draw_text(f"FPS: {int(clock.get_fps())}", text_font, (0,0,0), 0, 0)
    pygame.display.update()
    dt = clock.tick(60) / 1000
    

pygame.quit()
