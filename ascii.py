import ascii_magic

def convert(imagepath):
    my_art = ascii_magic.from_image(imagepath)
    my_art.to_terminal()

convert("Car.png")