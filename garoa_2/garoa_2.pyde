from bienal import BienalClient, get_deep_ai_caption_position
from random import choice

img = None
analysis = None

def settings():
    global img, analysis
    
    bienal = BienalClient()
    print("### GET IMAGE")    
    analysis = bienal.get_collection_image(col_id=12, image_id=777)  

    url = analysis['yolo_image']
    img = loadImage(url)
    print(img.width, img.height) 
    size(img.width, img.height)
    print('DONE')
    
def setup():
    strokeWeight(2)
    
def draw():
    dense_cap = analysis.deep_ai.dense_cap

    image(img, 0, 0)    
    ordered_captions = sorted(
        dense_cap['output']['captions'], key=lambda c: c['confidence'], reverse=True
    )   # ordena as captions do resultado com maior confiança para o menor
    caption_points = []
    for caption in ordered_captions[:20]:
        print(caption['confidence'])
        x_y, _ = get_deep_ai_caption_position(img.width, img.height, caption)  # calcula x e y após redimensão do Deep Ai
        caption_points.append((x_y[0], x_y[1], caption['caption']))
   
    current_point = choice(caption_points)  # escolhe um ponto inicial randômicamente
    caption_points.remove(current_point)
    
    while caption_points:  # itera pelos pontos e captions até acabar todos
        px, py, p_caption = current_point
        x, y, caption = choice(caption_points)  # recupera um novo caption randômico
        
        if px > 0 and py > 0:
            stroke(img.get(px, py))  # a cor da linha é a cor do pixel na posição
        line(px, py, x, y)  # desenha uma linha entre os captions
        text(p_caption, px, py)
        
        current_point = (x, y, caption)
        caption_points.remove(current_point)  # remove novo ponto processado    
     
    saveFrame("img_002.png")               
    noLoop()
