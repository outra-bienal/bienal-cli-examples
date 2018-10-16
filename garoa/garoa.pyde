from bienal import BienalClient, get_deep_ai_caption_position
from random import choice

img = None
analysis = None

def settings():
    global img, analysis
    
    bienal = BienalClient()
    print("### GET IMAGE")    
    analysis = bienal.get_collection_image(col_id=11, image_id=741)  

    url = analysis['image']
    img = loadImage(url)
    img.resize(900, 0)
    print(img.width, img.height) 
    size(img.width, img.height)
    print('DONE')
    
def setup():
    pass
    
def draw():
    properties = analysis.google.image_properties_annotation
    
    colors = [c['color'] for c in properties['dominantColors']['colors']]
    img.loadPixels()
    
    for y in range(height):
        max_x = int(noise(y / 89.0) * width)
        if random(1) > 0.83:
            continue
        
        for x in range(max_x):
            index = x + y * width
            c = choice(colors)
            img.pixels[index] = color(c['red'], c['green'], c['blue'])
            
    
    img.updatePixels()
    image(img, 0, 0)
    saveFrame("img_001.png")        
    noLoop()
