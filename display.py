#Owen Riske

import pygame
import settings
from PIL import Image


# input box
def input_box(width, height, x, y):
    clock = pygame.time.Clock()
    base_font = pygame.font.Font(None, int(settings.height // 4))
    user_text = ''
    input_rect = pygame.Rect(x, y, width, height)
    color_active = pygame.Color(235, 235, 235)
    color_passive = pygame.Color(185, 185, 185)
    color = color_passive
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if next((chr for chr in user_text if chr.isdigit()), None):
                        return int(user_text)
                    else:
                        return str(user_text)
                        # pygame.quit()

                        # Unicode standard is used for string
                        # formation
                else:
                    user_text += event.unicode

        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(settings.screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))
        settings.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, width)
        pygame.display.flip()
        clock.tick(60)


# setup image
def image(im,x,y):
    image = pygame.image.load(im)
    imageRect = image.get_rect()
    imageRect.x=x
    imageRect.y=y
    settings.screen.blit(image, imageRect)
    return imageRect


# resize image
def image_resize(image,width,height):
    image1 = Image.open(f"image/{image}")
    image1 = image1.resize((int(width),int(height)), Image.ANTIALIAS)
    image1.save(fp=f"image/new{image}")
    return image1


# setup text
def text(message, size, x, y, colour):
    font = pygame.font.Font('freesansbold.ttf', int(size))
    text = font.render(message, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    settings.screen.blit(text, textRect)


# setup rectangle
def rect(colour, x, y, width, height, border):
    if border > 0:
        rectangle = pygame.draw.rect(settings.screen, colour,
                                     pygame.Rect(x - width // 2, y - height // 2, width, height), int(border))
    else:
        rectangle = pygame.draw.rect(settings.screen, colour,
                                     pygame.Rect(x - width // 2, y - height // 2, width, height))
        return rectangle


# make button
def button(message, size, textsize, x, y, colour1):
    image_resize("button_layout.png", size, size // 2)
    button = image("image/newbutton_layout.png", x - size // 2, y - size // 4)
    text(message, textsize // 6, x, y, colour1)
    return button




# clickable image
def clickable_image(Image, message, size, textsize, x, y, colour):
    image_resize(f"{Image}", size, size // 2)
    button = image(f'image/new{Image}', x - size // 2, y - size // 4)
    text(message, textsize // 6, x, y + size // 3, colour)
    return button


# set logo and game name
def pygame_present(logo, name):
    image_resize(logo, 32, 32)
    Logo = pygame.image.load(f"image/{logo}")
    pygame.display.set_icon(Logo)
    pygame.display.set_caption(name)


# preset colours
def colour(colour):
    if colour.lower() == "black":
        colour = (0, 0, 0)
    elif colour.lower() == "white":
        colour = (255, 255, 255)
    elif colour.lower() == "grey":
        colour = (112, 112, 112)
    elif colour.lower() == "light grey":
        colour = (168, 168, 168)
    elif colour.lower() == "dark grey":
        colour = (56, 56, 56)
    elif colour.lower() == "red":
        colour = (255, 0, 0)
    elif colour.lower() == "orange":
        colour = (255, 145, 0)
    elif colour.lower() == "yellow":
        colour = (255, 255, 0)
    elif colour.lower() == "green":
        colour = (0, 255, 0)
    elif colour.lower() == "turquoise" or colour.lower() == "blue green" or colour.lower() == "green blue":
        colour = (0, 255, 135)
    elif colour.lower() == "light blue":
        colour = (0, 255, 255)
    elif colour.lower() == "blue":
        colour = (0, 0, 255)
    elif colour.lower() == "purple":
        colour = (200, 0, 255)
    elif colour.lower() == "magenta":
        colour = (255, 0, 240)
    elif colour.lower() == "pink":
        colour = (255, 160, 160)
    elif colour.lower() == "brown":
        colour = (140, 95, 255)
    elif colour.lower() == "dark brown":
        colour = (105, 70, 0)
    elif colour.lower() == "light brown":
        colour = (120, 130, 0)
    elif colour.lower() == "dark green":
        colour = (0, 175, 0)
    else:
        colour = (185, 190, 0)
    return colour

    # multiply line text





def multi_text(size, x, y, colour, message1, message2, message3, message4, message5, message6, message7, message8,
               message9, message10, message11):
    if message1 != "":
        text(message1, size, x, y - size * 5, colour)
    if message2 != "":
        text(message2, size, x, y - size * 4, colour)
    if message3 != "":
        text(message3, size, x, y - size * 3, colour)
    if message4 != "":
        text(message4, size, x, y - size * 2, colour)
    if message5 != "":
        text(message5, size, x, y - size, colour)
    if message6 != "":
        text(message6, size, x, y, colour)
    if message7 != "":
        text(message7, size, x, y + size, colour)
    if message8 != "":
        text(message8, size, x, y + size * 2, colour)
    if message9 != "":
        text(message9, size, x, y + size * 3, colour)
    if message10 != "":
        text(message10, size, x, y + size * 4, colour)
    if message11 != "":
        text(message11, size, x, y + size * 5, colour)
    if message1 != "" and message2 != "" and message3 != "" and message4 != "" and message5 != "" and message6 != "" and message7 != "" and message8 != "" and message9 != "" and message10 != "" and message11 != "":
        text("ERROR", size, x, y, colour)





# background function
def background(backgroundImage):
    image_resize(f"{backgroundImage}", settings.width, settings.width)
    image(f"image/new{backgroundImage}", 0, 0)


# line function
def line(size, x1, y1, x2, y2, colour):
    pygame.draw.line(settings.screen, colour, (x1, y1), (x2, y2), size)


# circle function
def circle(radius, thickness, centerX, centerY, colour):
    pygame.draw.circle(settings.screen,
                       colour, (centerX, centerY), radius, thickness)


def adjustableNum(messageTitle,message, y, textColour):
    text(messageTitle,settings.width * 0.025, settings.width * 0.5, y-settings.height * 0.05,textColour)

    text(message, settings.width * 0.05, settings.width * 0.5,y, textColour)
    smaller=button("<", settings.width * 0.1, settings.width * 0.25,settings.width * 0.375, y, (0, 0, 0))
    bigger=button(">", settings.width * 0.1, settings.width * 0.25,settings.width * 0.625, y, (0, 0, 0))
    return smaller, bigger

def adjustableNumButtonCollidePoint(smallerButton, biggerButton, numToBeChanged, event):
    if smallerButton.collidepoint(event.pos) and numToBeChanged>0:
        numToBeChanged -= 1
    elif biggerButton.collidepoint(event.pos):
        numToBeChanged += 1

    return numToBeChanged

def adjustableNumButtonCollidePointWithMax(smallerButton, biggerButton, numToBeChanged, max, event):
    if smallerButton.collidepoint(event.pos) and numToBeChanged>0:
        numToBeChanged -= 1
    elif biggerButton.collidepoint(event.pos) and numToBeChanged<max:
        numToBeChanged += 1

    return numToBeChanged

