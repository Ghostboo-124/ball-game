import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

green_size = 40
red_size = 40
yellow_size = 40

# Start position of the balls
red_pos = pygame.Vector2(int(screen.get_height()-red_size), (screen.get_width()-red_size))
red_vel = pygame.Vector2(0, 0)
green_pos = pygame.Vector2((screen.get_height()-(green_size+red_size)), (screen.get_width()-(green_size+red_size)))
green_vel = pygame.Vector2(0, 0)
yellow_pos = pygame.Vector2((screen.get_height()-(yellow_size+green_size+red_size)), screen.get_width()-(yellow_size+green_size+red_size))
yellow_vel = pygame.Vector2(0, 0)


gravity = pygame.Vector2(0, 1000)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Apply gravity
    red_vel += gravity * dt
    green_vel += gravity * dt
    yellow_vel += gravity * dt

    # Update player position
    red_pos += red_vel * dt
    green_pos += green_vel * dt
    yellow_pos += yellow_vel * dt

    # Check Red ball collision with screen boundaries
    if red_pos.y > screen.get_height() - red_size:
        red_pos.y = screen.get_height() - red_size
        red_vel.y *= -0.9  # Bounce back with some loss of energy
    if red_pos.y < red_size:
        red_pos.y = red_size
        red_vel.y *= -0.8
    if red_pos.x > screen.get_width() - red_size:
        red_pos.x = screen.get_width() - red_size
        red_vel.x *= -0.8
    if red_pos.x < red_size:
        red_pos.x = red_size
        red_vel.x *= -0.8
    
    # Check Green ball collision with screen boundaries
    if green_pos.y > screen.get_height() - green_size:
        green_pos.y = screen.get_height() - green_size
        green_vel.y *= -0.9 # Bounce back with some loss of energy
    if green_pos.y < green_size:
        green_pos.y = green_size
        green_vel.y *= -0.8
    if green_pos.x > screen.get_width() - green_size:
        green_pos.x = screen.get_width() - green_size
        green_vel.x *= -0.8
    if green_pos.x < green_size:
        green_pos.x = green_size
        green_vel.x *= -0.8
    
    # Check Yellow ball collision with screen boundaries
    if yellow_pos.y > screen.get_height() - yellow_size:
        yellow_pos.y = screen.get_height() - yellow_size
        yellow_vel.y *= -0.9
    if yellow_pos.y < yellow_size:
        yellow_pos.y = yellow_size
        yellow_vel.y *= -0.8
    if yellow_pos.x > screen.get_width() - yellow_size:
        yellow_pos.x = screen.get_width() - yellow_size
        yellow_vel.x *= -0.8
    if yellow_pos.x < yellow_size:
        yellow_pos.x = yellow_size
        yellow_vel.x *= -0.8
    
    # Check collision between Green and Red balls
    if (green_pos - red_pos).length() < (green_size + red_size):
        collision_normal = (green_pos - red_pos).normalize()
        overlap = (red_size + green_size) - (green_pos - red_pos).length()
        green_pos += collision_normal * overlap / 2
        red_pos -= collision_normal * overlap / 2
        
        relative_velocity = green_vel - red_vel
        separation_velocity = relative_velocity.dot(collision_normal)
        
        if separation_velocity < 0:
            impulse = -separation_velocity * collision_normal
            red_vel -= impulse
            green_vel += impulse

    # Check collision between Red and Green balls
    if (red_pos - green_pos).length() < (green_size + red_size):
        collision_normal = (red_pos - green_pos).normalize()
        overlap = (green_size + red_size) - (red_pos - green_pos).length()
        red_pos += collision_normal * overlap / 2
        green_pos -= collision_normal * overlap / 2
        
        relative_velocity = red_vel - green_vel
        separation_velocity = relative_velocity.dot(collision_normal)
        
        if separation_velocity < 0:
            impulse = -separation_velocity * collision_normal
            green_vel += impulse
            red_vel -= impulse

    # Check collision between Yellow and Red balls
    if (yellow_pos - red_pos).length() < (yellow_size + red_size):
        collision_normal = (yellow_pos - red_pos).normalize()
        overlap = (red_size + yellow_size) - (yellow_pos - red_pos).length()
        yellow_pos += collision_normal * overlap / 2
        red_pos -= collision_normal * overlap / 2
        
        relative_velocity = yellow_vel - red_vel
        separation_velocity = relative_velocity.dot(collision_normal)
        
        if separation_velocity < 0:
            impulse = -separation_velocity * collision_normal
            red_vel -= impulse
            yellow_vel += impulse

    # Check collision between Yellow and Green balls
    if (yellow_pos - green_pos).length() < (yellow_size + green_size):
        collision_normal = (yellow_pos - green_pos).normalize()
        overlap = (green_size + yellow_size) - (yellow_pos - green_pos).length()
        yellow_pos += collision_normal * overlap / 2
        green_pos -= collision_normal * overlap / 2
        
        relative_velocity = yellow_vel - green_vel
        separation_velocity = relative_velocity.dot(collision_normal)
        
        if separation_velocity < 0:
            impulse = -separation_velocity * collision_normal
            green_vel -= impulse
            yellow_vel += impulse

    pygame.draw.circle(screen, (255, 0, 0), red_pos, red_size)
    pygame.draw.circle(screen, (0, 255, 0), green_pos, green_size)
    pygame.draw.circle(screen, (0, 0, 255), yellow_pos, yellow_size)

    keys = pygame.key.get_pressed()

    # Red Ball Keys
    if keys[pygame.K_w]:
        red_vel.y -= 1000 * dt
    if keys[pygame.K_s]:
        red_vel.y += 1000 * dt
    if keys[pygame.K_a]:
        red_vel.x -= 1000 * dt
    if keys[pygame.K_d]:
        red_vel.x += 1000 * dt
    if keys[pygame.K_e]:
        red_vel.xy = (0,0)
    
    # Green Ball Keys
    if keys[pygame.K_UP]:
        green_vel.y -= 1000 * dt
    if keys[pygame.K_DOWN]:
        green_vel.y += 1000 * dt
    if keys[pygame.K_LEFT]:
        green_vel.x -= 1000 * dt
    if keys[pygame.K_RIGHT]:
        green_vel.x += 1000 * dt
    if keys[pygame.K_PAGEDOWN]:
        green_vel.xy = (0,0)
    
    # Yellow Ball Keys
    if keys[pygame.K_i]:
        yellow_vel.y -= 1000 * dt
    if keys[pygame.K_k]:
        yellow_vel.y += 1000 * dt
    if keys[pygame.K_j]:
        yellow_vel.x -= 1000 * dt
    if keys[pygame.K_l]:
        yellow_vel.x += 1000 * dt
    if keys[pygame.K_o]:
        yellow_vel.xy = (0,0)

    pygame.display.flip()
    dt = clock.tick(480) / 1000

pygame.quit()