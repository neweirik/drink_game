import pygame
import sys
import random
import math



# Akevitt
# "Gratulerer! Du har fått Akevitt - Nå blir det skikkelig norsk fest!"
# "Hipp hurra! Akevitt i glasset, nå blir det stemning!"
# "Akevitt på menyen - det blir ikke mer tradisjonelt enn dette!"
# "Skål for deg med Akevitt - Norges stolthet i et glass!"
# "Med Akevitt i hånden er du klar for enhver skål!"

# Jägermeister
# "Gratulerer! Jägermeister vunnet - Tid for en skikkelig jegerfest!"
# "Jägermeister? Nå snakker vi! Bli klar for en vilt god tid!"
# "Med Jägermeister i spill blir det jakt på gode stunder!"
# "Skål og velkommen til Jägermeister-klubben!"
# "Jägermeister: Fordi noen kvelder krever litt ekstra jaktinstinkt!"

# Små Sure
# "Hurra! Du vant Små Sure - Surprisen er på din side!"
# "Små Sure i premie, det blir en smaksfest!"
# "Med Små Sure blir det aldri en kjedelig stund!"
# "Små Sure for deg - Tid for å piffe opp festen!"
# "Vinneren får Små Sure - Fordi livet trenger litt syrlighet!"

# Tequila
# "Gratulerer! Tequila er din - Nå blir det meksikansk stemning!"
# "Tequila vunnet! Gjør deg klar for en natt med salsa og salt!"
# "Med Tequila i glasset er det tid for fiesta og moro!"
# "Skål med Tequila - La sombrerofesten starte!"
# "Tequila? Siestaen er over, nå starter festen!"

# Gin
# "Gratulerer! En Gin til deg - Nå blir det sofistikert stemning!"
# "Gin i premie - Tid for en drink med stil og klasse!"
# "Med Gin i glasset er du klar for enhver cocktailtime!"
# "En skål med Gin - Fordi noen kvelder krever finesse!"
# "Gin for vinneren - Fordi det er alltid tid for en gin-tonic!"

# Bayleys
# "Gratulerer! Bayleys for deg - En søt seier!"
# "Bayleys vunnet - Kremet nytelse venter!"
# "Med Bayleys blir det en smak av luksus!"
# "En skål med Bayleys - Fordi hver seier er søt!"
# "Bayleys til deg - Nå blir det dessert i glasset!"

# Fireball
# "Gratulerer! Fireball er din - Nå blir det fyr i peisen!"
# "Fireball vunnet! Tid for en kveld med ekstra glød!"
# "Med Fireball i glasset blir det het stemning i kveld!"
# "En skål med Fireball - La oss tenne på festfyrverkeriet!"
# "Fireball til deg - Fordi kvelden fortjener litt ekstra krydder!"


# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# Colors and settings for wheel generation
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [
    (23, 89, 135),   # Darkened Deep Blue
    (191, 95, 10),   # Darkened Vibrant Orange
    (33, 120, 33),   # Darkened Rich Green
    (160, 29, 30),   # Darkened Bold Red
    (111, 77, 141),  # Darkened Muted Purple
    (105, 64, 56),   # Darkened Warm Brown
    (170, 89, 145)   # Darkened Soft Pink
]
WHEEL_CENTER = (500, 500)
WHEEL_RADIUS = 500
DRINKS = ["Akevitt", "Jägermeister", "Små Sure", "Tequila", "Gin", "Baileys", "Fireball"]
DRINKS = [drink.upper() for drink in DRINKS]

drink1_sounds = [pygame.mixer.Sound("Recording 11.mp3"), pygame.mixer.Sound("Recording 12.mp3"), pygame.mixer.Sound("Recording 13.mp3"), pygame.mixer.Sound("Recording 14.mp3"), pygame.mixer.Sound("Recording 15.mp3")]
drink2_sounds = [pygame.mixer.Sound("Recording 16.mp3"), pygame.mixer.Sound("Recording 17.mp3"), pygame.mixer.Sound("Recording 18.mp3"), pygame.mixer.Sound("Recording 19.mp3"), pygame.mixer.Sound("Recording 20.mp3")]
drink3_sounds = [pygame.mixer.Sound("Recording 21.mp3"), pygame.mixer.Sound("Recording 22.mp3"), pygame.mixer.Sound("Recording 23.mp3"), pygame.mixer.Sound("Recording 24.mp3"), pygame.mixer.Sound("Recording 25.mp3")]
drink4_sounds = [pygame.mixer.Sound("Recording 26.mp3"), pygame.mixer.Sound("Recording 27.mp3"), pygame.mixer.Sound("Recording 28.mp3"), pygame.mixer.Sound("Recording 29.mp3"), pygame.mixer.Sound("Recording 30.mp3")]
drink5_sounds = [pygame.mixer.Sound("Recording 31.mp3"), pygame.mixer.Sound("Recording 32.mp3"), pygame.mixer.Sound("Recording 33.mp3"), pygame.mixer.Sound("Recording 34.mp3"), pygame.mixer.Sound("Recording 35.mp3")]
drink6_sounds = [pygame.mixer.Sound("Recording 36.mp3"), pygame.mixer.Sound("Recording 37.mp3"), pygame.mixer.Sound("Recording 38.mp3"), pygame.mixer.Sound("Recording 39.mp3"), pygame.mixer.Sound("Recording 40.mp3")]
drink7_sounds = [pygame.mixer.Sound("Recording 41.mp3"), pygame.mixer.Sound("Recording 42.mp3"), pygame.mixer.Sound("Recording 43.mp3"), pygame.mixer.Sound("Recording 44.mp3"), pygame.mixer.Sound("Recording 45.mp3"), pygame.mixer.Sound("Recording 46.mp3")]

tick_sound = pygame.mixer.Sound("tick.mp3")
tick_sound.set_volume(0.2)


sounds = [drink1_sounds, drink2_sounds, drink3_sounds, drink4_sounds, drink5_sounds, drink6_sounds, drink7_sounds]
ANGLE = 2 * math.pi / len(DRINKS)
FONT = pygame.font.SysFont(None, 70, bold=True)

last_field = ""

drink_counts = {drink: 0 for drink in DRINKS}

POPUP_FONT_SIZE = 100  # Increase font size for larger text
POPUP_BACKGROUND_COLOR = (0, 0, 0)  # Black background for contrast
POPUP_TEXT_COLOR = (255, 255, 255)  # White text
POPUP_FONT = pygame.font.SysFont(None, POPUP_FONT_SIZE, bold=True)
POPUP_DISPLAY_DURATION = 5000  # Duration to display the popup in milliseconds

# Function to display drink counts
def display_drink_counts():
    y = 300
    for drink, count in drink_counts.items():
        text = FONT.render(f"{drink}: {count}", True, BLACK)
        screen.blit(text, (1100, y))
        y += 80

# Function to draw an arrow
def draw_arrow(flip=False):
    if flip:
        pygame.draw.polygon(screen, (10, 0, 0), [(960, 500), (1040, 460),  (1040, 540)])
    else:
        pygame.draw.polygon(screen, (10, 0, 0), [(1000, 500), (1080, 460),  (1040, 540)])

# Popup variables
popup_surface = None
popup_time = 0

def draw_segment(start_angle, end_angle, color, surface):
    # Draw a filled segment
    points = [WHEEL_CENTER]
    for n in range(int(start_angle * 180 / math.pi), int(end_angle * 180 / math.pi) + 1):
        x = WHEEL_CENTER[0] + WHEEL_RADIUS * math.cos(n * math.pi / 180)
        y = WHEEL_CENTER[1] + WHEEL_RADIUS * math.sin(n * math.pi / 180)
        points.append((x, y))
    pygame.draw.polygon(surface, color, points)

def draw_wheel(surface):
    for i, drink in enumerate(DRINKS):
        # Segment
        start_angle = ANGLE * i
        end_angle = start_angle + ANGLE

        # Draw filled segment
        draw_segment(start_angle, end_angle, COLORS[i % len(COLORS)], surface)

        # Text
        text_angle = start_angle + ANGLE / 2
        text_x = WHEEL_CENTER[0] + WHEEL_RADIUS * 0.5 * math.cos(text_angle)
        text_y = WHEEL_CENTER[1] + WHEEL_RADIUS * 0.5 * math.sin(text_angle)
        text = FONT.render(drink, True, WHITE)
        text_surface = pygame.transform.rotate(text, 90-text_angle * 180 / math.pi - 90)
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        surface.blit(text_surface, text_rect)

def show_popup(text, surface, duration):
    global popup_surface, popup_time
    text_surface = POPUP_FONT.render(text, True, POPUP_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Create a background rectangle slightly larger than the text
    background_rect = pygame.Rect(text_rect.left - 10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20)
    pygame.draw.rect(surface, POPUP_BACKGROUND_COLOR, background_rect)
    surface.blit(text_surface, text_rect)

    popup_time = pygame.time.get_ticks()  # Reset the popup timer


def create_wheel_image():
    wheel_surface = pygame.Surface((WHEEL_RADIUS * 2, WHEEL_RADIUS * 2), pygame.SRCALPHA)
    draw_wheel(wheel_surface)
    pygame.image.save(wheel_surface, "drink_wheel.png")
    return pygame.image.load("drink_wheel.png")

# Create and load the wheel image
wheel_image = create_wheel_image()
wheel_rect = wheel_image.get_rect(center=WHEEL_CENTER)

# Game variables
angle = 0
spin_speed = 0
spinning = False
popup_shown = False

sound_played = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spinning = True
                spin_speed = spin_speed + random.choice([ 3, 30, 15, 6, 12, 10, 20, 12])
                spin_speed = min(spin_speed, 30)
                sound_played = False
                popup_shown = True

    angle += spin_speed

    if spin_speed > 0:
        spin_speed -= 0.1
        angle += spin_speed

    # Determine current field
    index = int((angle%360) / (360 / len(DRINKS)))
    current_drink = DRINKS[index]


    screen.fill(WHITE)
    rotated_wheel = pygame.transform.rotate(wheel_image, angle)
    new_rect = rotated_wheel.get_rect(center=wheel_rect.center)

    screen.blit(rotated_wheel, new_rect.topleft)

    clock.tick(60)

    if spin_speed <= 0 and spinning:
        drink_counts[current_drink] += 1
        popup_surface = FONT.render(f"Du fikk {current_drink}", True, (255, 100, 100))
        popup_shown = False
        popup_time = pygame.time.get_ticks()
        spin_speed = 0

    # Clear the screen and draw the wheel
    screen.fill(WHITE)
    rotated_wheel = pygame.transform.rotate(wheel_image, angle)
    new_rect = rotated_wheel.get_rect(center=wheel_rect.center)
    screen.blit(rotated_wheel, new_rect.topleft)

    # Draw the arrow

    # Display drink counts
    display_drink_counts()

    if current_drink != last_field:
        tick_sound.play()
        last_field = current_drink
        draw_arrow()

    else:
        draw_arrow(True)

    # Display popup if needed
    if popup_surface and (pygame.time.get_ticks() - popup_time) <= 10000 and not popup_shown:
        # screen.blit(popup_surface, (WHEEL_CENTER[0] - 100, WHEEL_CENTER[1] + 200))
        show_popup(f"Du fikk {current_drink}", screen, POPUP_DISPLAY_DURATION)
        if sound_played is False:
            random.choice(sounds[index]).play()
            sound_played = True
            spinning = False
            
        popup_shown = False

    pygame.display.flip()
    clock.tick(60)