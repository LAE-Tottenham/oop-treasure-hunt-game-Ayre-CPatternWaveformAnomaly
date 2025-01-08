import ascii_magic

def convert(imagepath,size):
    my_art = ascii_magic.from_image(imagepath)
    my_art.to_terminal(columns=size)