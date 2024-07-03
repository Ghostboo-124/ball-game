try:
    from random import randint as ran
    import pygame
    import sys

    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # Ball Size
    size = 40

    # Ball Pos
    ran0x = ran(1,1880)
    ran0y = ran(1,1040)

    ran1x = ran(1,1880)
    ran1y = ran(1,1040)

    ran2x = ran(1,1880)
    ran2y = ran(1,1040)

    ran3x = ran(1,1880)
    ran3y = ran(1,1040)

    ran4x = ran(1,1880)
    ran4y = ran(1,1040)

    ran5x = ran(1,1880)
    ran5y = ran(1,1040)

    # Start position of the balls
    ball0_pos = pygame.Vector2(ran0x, ran0y)
    ball0_vel = pygame.Vector2(0, 0)

    ball1_pos = pygame.Vector2(ran1x, ran1y)
    ball1_vel = pygame.Vector2(0, 0)

    ball2_pos = pygame.Vector2(ran2x, ran2y)
    ball2_vel = pygame.Vector2(0, 0)

    ball3_pos = pygame.Vector2(ran3x, ran3y)
    ball3_vel = pygame.Vector2(0, 0)

    ball4_pos = pygame.Vector2(ran4x, ran4y)
    ball4_vel = pygame.Vector2(0, 0)

    ball5_pos = pygame.Vector2(ran5x, ran5y)
    ball5_vel = pygame.Vector2(0, 0)

    # Gravity
    gravity = pygame.Vector2(0, 0)

    # Main loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Apply gravity
        
        ball1_vel += gravity * dt
        ball2_vel += gravity * dt
        ball3_vel += gravity * dt

        # Update player position
        ball1_pos += ball1_vel * dt
        ball2_pos += ball2_vel * dt
        ball3_pos += ball3_vel * dt

        # Check Red ball collision with screen boundaries
        if ball1_pos.y > screen.get_height() - size:
            ball1_pos.y = screen.get_height() - size
            ball1_vel.y *= -1  # Invert vertical velocity to bounce back
        if ball1_pos.y < size:
            ball1_pos.y = size
            ball1_vel.y *= -1
        if ball1_pos.x > screen.get_width() - size:
            ball1_pos.x = screen.get_width() - size
            ball1_vel.x *= -1  # Invert horizontal velocity to bounce back
        if ball1_pos.x < size:
            ball1_pos.x = size
            ball1_vel.x *= -1

        # Check Green ball collision with screen boundaries
        if ball2_pos.y > screen.get_height() - size:
            ball2_pos.y = screen.get_height() - size
            ball2_vel.y *= -1  # Invert vertical velocity to bounce back
        if ball2_pos.y < size:
            ball2_pos.y = size
            ball2_vel.y *= -1
        if ball2_pos.x > screen.get_width() - size:
            ball2_pos.x = screen.get_width() - size
            ball2_vel.x *= -1  # Invert horizontal velocity to bounce back
        if ball2_pos.x < size:
            ball2_pos.x = size
            ball2_vel.x *= -1

        # Check Yellow ball collision with screen boundaries
        if ball3_pos.y > screen.get_height() - size:
            ball3_pos.y = screen.get_height() - size
            ball3_vel.y *= -1  # Invert vertical velocity to bounce back
        if ball3_pos.y < size:
            ball3_pos.y = size
            ball3_vel.y *= -1
        if ball3_pos.x > screen.get_width() - size:
            ball3_pos.x = screen.get_width() - size
            ball3_vel.x *= -1  # Invert horizontal velocity to bounce back
        if ball3_pos.x < size:
            ball3_pos.x = size
            ball3_vel.x *= -1
        
        # Check collision between ball1 and ball0
        if (ball1_pos - ball0_pos).length() < (size + size):
            collision_normal = (ball1_pos - ball0_pos).normalize()
            overlap = (size + size) - (ball1_pos - ball0_pos).length()
            ball1_pos += collision_normal * overlap / 2
            ball0_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball1_vel - ball0_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball0_vel -= impulse
                ball1_vel += impulse

        # Check collision between ball1 and ball2
        if (ball1_pos - ball2_pos).length() < (size + size) and ball1_pos != ball2_pos:
            collision_normal = (ball1_pos - ball2_pos).normalize()
            overlap = (size + size) - (ball1_pos - ball2_pos).length()
            ball1_pos += collision_normal * overlap / 2
            ball2_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball1_vel - ball2_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball2_vel -= impulse
                ball1_vel += impulse
        
        # Check collision between ball1 and ball3
        if (ball1_pos - ball3_pos).length() < (size + size) and ball1_pos != ball3_pos:
            collision_normal = (ball1_pos - ball3_pos).normalize()
            overlap = (size + size) - (ball1_pos - ball3_pos).length()
            ball1_pos += collision_normal * overlap / 2
            ball3_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball1_vel - ball3_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball3_vel -= impulse
                ball1_vel += impulse
        
        # Check collision between ball1 and ball4
        if (ball1_pos - ball4_pos).length() < (size + size):
            collision_normal = (ball1_pos - ball4_pos).normalize()
            overlap = (size + size) - (ball1_pos - ball4_pos).length()
            ball1_pos += collision_normal * overlap / 2
            ball4_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball1_vel - ball4_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball4_vel -= impulse
                ball1_vel += impulse
        
        # Check collision between ball1 and ball5
        if (ball1_pos - ball5_pos).length() < (size + size):
            collision_normal = (ball1_pos - ball5_pos).normalize()
            overlap = (size + size) - (ball1_pos - ball5_pos).length()
            ball1_pos += collision_normal * overlap / 2
            ball5_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball1_vel - ball5_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball5_vel -= impulse
                ball1_vel += impulse
        
        # Check collision between ball2 and ball0
        if (ball2_pos - ball0_pos).length() < (size + size):
            collision_normal = (ball2_pos - ball0_pos).normalize()
            overlap = (size + size) - (ball2_pos - ball0_pos).length()
            ball2_pos += collision_normal * overlap / 2
            ball0_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball2_vel - ball0_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball0_vel -= impulse
                ball2_vel += impulse

        # Check collision between ball2 and ball1
        if (ball2_pos - ball1_pos).length() < (size + size) and ball2_pos != ball1_pos:
            collision_normal = (ball2_pos - ball1_pos).normalize()
            overlap = (size + size) - (ball2_pos - ball1_pos).length()
            ball2_pos += collision_normal * overlap / 2
            ball1_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball2_vel - ball1_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball1_vel -= impulse
                ball2_vel += impulse
        
        # Check collision between ball2 and ball3
        if (ball2_pos - ball3_pos).length() < (size + size) and ball2_pos != ball3_pos:
            collision_normal = (ball2_pos - ball3_pos).normalize()
            overlap = (size + size) - (ball2_pos - ball3_pos).length()
            ball2_pos += collision_normal * overlap / 2
            ball3_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball2_vel - ball3_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball3_vel -= impulse
                ball2_vel += impulse
        
        # Check collision between ball2 and ball4
        if (ball2_pos - ball4_pos).length() < (size + size):
            collision_normal = (ball2_pos - ball4_pos).normalize()
            overlap = (size + size) - (ball2_pos - ball4_pos).length()
            ball2_pos += collision_normal * overlap / 2
            ball4_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball2_vel - ball4_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball4_vel -= impulse
                ball2_vel += impulse
        
        # Check collision between ball2 and ball5
        if (ball2_pos - ball5_pos).length() < (size + size):
            collision_normal = (ball2_pos - ball5_pos).normalize()
            overlap = (size + size) - (ball2_pos - ball5_pos).length()
            ball2_pos += collision_normal * overlap / 2
            ball5_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball2_vel - ball5_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball5_vel -= impulse
                ball2_vel += impulse

        # Check collision between ball3 and ball0
        if (ball3_pos - ball0_pos).length() < (size + size):
            collision_normal = (ball3_pos - ball0_pos).normalize()
            overlap = (size + size) - (ball3_pos - ball0_pos).length()
            ball3_pos += collision_normal * overlap / 2
            ball0_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball3_vel - ball0_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball0_vel -= impulse
                ball3_vel += impulse
        
        # Check collision between ball3 and ball1
        if (ball3_pos - ball1_pos).length() < (size + size) and ball3_pos != ball1_pos:
            collision_normal = (ball3_pos - ball1_pos).normalize()
            overlap = (size + size) - (ball3_pos - ball1_pos).length()
            ball3_pos += collision_normal * overlap / 2
            ball1_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball3_vel - ball1_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball1_vel -= impulse
                ball3_vel += impulse
        
        # Check collision between ball3 and ball2
        if (ball3_pos - ball2_pos).length() < (size + size) and ball3_pos != ball2_pos:
            collision_normal = (ball3_pos - ball2_pos).normalize()
            overlap = (size + size) - (ball3_pos - ball2_pos).length()
            ball3_pos += collision_normal * overlap / 2
            ball2_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball3_vel - ball2_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball2_vel -= impulse
                ball3_vel += impulse
        
        # Check collision between ball3 and ball4
        if (ball3_pos - ball4_pos).length() < (size + size):
            collision_normal = (ball3_pos - ball4_pos).normalize()
            overlap = (size + size) - (ball3_pos - ball4_pos).length()
            ball3_pos += collision_normal * overlap / 2
            ball4_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball3_vel - ball4_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball4_vel -= impulse
                ball3_vel += impulse

        # Check collision between ball3 and ball5
        if (ball3_pos - ball5_pos).length() < (size + size):
            collision_normal = (ball3_pos - ball5_pos).normalize()
            overlap = (size + size) - (ball3_pos - ball5_pos).length()
            ball3_pos += collision_normal * overlap / 2
            ball5_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball3_vel - ball5_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball5_vel -= impulse
                ball3_vel += impulse
        
        # Check collision between ball4 and ball0
        if (ball4_pos - ball0_pos).length() < (size + size):
            collision_normal = (ball4_pos - ball0_pos).normalize()
            overlap = (size + size) - (ball4_pos - ball0_pos).length()
            ball4_pos += collision_normal * overlap / 2
            ball0_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball4_vel - ball0_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball0_vel -= impulse
                ball4_vel += impulse

        # Check collision between ball4 and ball1
        if (ball4_pos - ball1_pos).length() < (size + size):
            collision_normal = (ball4_pos - ball1_pos).normalize()
            overlap = (size + size) - (ball4_pos - ball1_pos).length()
            ball4_pos += collision_normal * overlap / 2
            ball1_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball4_vel - ball1_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball1_vel -= impulse
                ball4_vel += impulse
        
        # Check collision between ball4 and ball2
        if (ball4_pos - ball2_pos).length() < (size + size):
            collision_normal = (ball4_pos - ball2_pos).normalize()
            overlap = (size + size) - (ball4_pos - ball2_pos).length()
            ball4_pos += collision_normal * overlap / 2
            ball2_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball4_vel - ball2_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball2_vel -= impulse
                ball4_vel += impulse
        
        # Check collision between ball4 and ball3
        if (ball4_pos - ball3_pos).length() < (size + size):
            collision_normal = (ball4_pos - ball3_pos).normalize()
            overlap = (size + size) - (ball4_pos - ball3_pos).length()
            ball4_pos += collision_normal * overlap / 2
            ball3_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball4_vel - ball3_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball3_vel -= impulse
                ball4_vel += impulse

        # Check collision between ball4 and ball5
        if (ball4_pos - ball5_pos).length() < (size + size):
            collision_normal = (ball4_pos - ball5_pos).normalize()
            overlap = (size + size) - (ball4_pos - ball5_pos).length()
            ball4_pos += collision_normal * overlap / 2
            ball5_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball4_vel - ball5_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball5_vel -= impulse
                ball4_vel += impulse
        
        # Check collision between ball5 and ball0
        if (ball5_pos - ball0_pos).length() < (size + size) and ball0_pos != ball5_pos:
            collision_normal = (ball5_pos - ball0_pos).normalize()
            overlap = (size + size) - (ball5_pos - ball0_pos).length()
            ball5_pos += collision_normal * overlap / 2
            ball0_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball5_vel - ball0_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball0_vel -= impulse
                ball5_vel += impulse
        
        # Check collision between ball5 and ball1
        if (ball5_pos - ball1_pos).length() < (size + size):
            collision_normal = (ball5_pos - ball1_pos).normalize()
            overlap = (size + size) - (ball5_pos - ball1_pos).length()
            ball5_pos += collision_normal * overlap / 2
            ball1_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball5_vel - ball1_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball1_vel -= impulse
                ball5_vel += impulse
        
        # Check collision between ball5 and ball2
        if (ball5_pos - ball2_pos).length() < (size + size):
            collision_normal = (ball5_pos - ball2_pos).normalize()
            overlap = (size + size) - (ball5_pos - ball2_pos).length()
            ball5_pos += collision_normal * overlap / 2
            ball2_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball5_vel - ball2_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball2_vel -= impulse
                ball5_vel += impulse
        
        # Check collision between ball5 and ball3
        if (ball5_pos - ball3_pos).length() < (size + size):
            collision_normal = (ball5_pos - ball3_pos).normalize()
            overlap = (size + size) - (ball5_pos - ball3_pos).length()
            ball5_pos += collision_normal * overlap / 2
            ball3_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball5_vel - ball3_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball3_vel -= impulse
                ball5_vel += impulse
        
        # Check collision between ball5 and ball4
        if (ball5_pos - ball4_pos).length() < (size + size):
            collision_normal = (ball5_pos - ball4_pos).normalize()
            overlap = (size + size) - (ball5_pos - ball4_pos).length()
            ball5_pos += collision_normal * overlap / 2
            ball4_pos -= collision_normal * overlap / 2
            
            relative_velocity = ball5_vel - ball4_vel
            separation_velocity = relative_velocity.dot(collision_normal)
            
            if separation_velocity < 0:
                impulse = -separation_velocity * collision_normal
                ball4_vel -= impulse
                ball5_vel += impulse

        pygame.draw.circle(screen, (47, 141, 255), ball0_pos, size)
        pygame.draw.circle(screen, (47, 141, 255), ball1_pos, size)
        pygame.draw.circle(screen, (47, 141, 255), ball2_pos, size)
        pygame.draw.circle(screen, (47, 141, 255), ball3_pos, size)
        pygame.draw.circle(screen, (47, 141, 255), ball4_pos, size)
        pygame.draw.circle(screen, (47, 141, 255), ball5_pos, size)

        keys = pygame.key.get_pressed()

        # Send Balls In Random Direction
        if keys[pygame.K_o]:
            ball0_vel.xy = (ran(255,5000),ran(255,5000))
            ball1_vel.xy = (ran(255,5000),ran(255,5000))
            ball2_vel.xy = (ran(255,5000),ran(255,5000))
            ball3_vel.xy = (ran(255,5000),ran(255,5000))
            ball4_vel.xy = (ran(255,5000),ran(255,5000))
            ball5_vel.xy = (ran(255,5000),ran(255,5000))

        # Stop balls
        if keys[pygame.K_e]:
            ball0_vel.xy = (0,0)
            ball1_vel.xy = (0,0)
            ball2_vel.xy = (0,0)
            ball3_vel.xy = (0,0)
            ball4_vel.xy = (0,0)
            ball5_vel.xy = (0,0)

        pygame.display.flip()
        dt = clock.tick(480) / 1000
    pygame.quit()
except(KeyboardInterrupt):
    print("You have done a keyboard interrupt, closing now")
    pygame.quit()
    sys.exit()