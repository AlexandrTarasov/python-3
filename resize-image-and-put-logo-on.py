from PIL import Image
import os, sys

path = "."

files = os.listdir( path )

def scale_image(input_image_path, output_image_path, water_m,  water_tel, watermar_in, width=None, height=None, position=(0,0)):
    
    original_image = Image.open(input_image_path)
    
    
    w, h = original_image.size
    #print('The original image size is {wide} wide x {height} ' 'high'.format(wide=w, height=h))
 
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')
 
    
    #original_image.paste(water_m, position) 
    original_image.thumbnail(max_size, Image.ANTIALIAS)
    
    
    w, h = original_image.size

    if watermar_in == 1:
        
        mark = Image.open(water_m)
        mark_t = Image.open(water_tel)
        
        mw, mh = mark_t.size
        
        original_image.paste(mark, (position), mark) 
        original_image.paste(mark_t, (w-mw,h-mh), mark_t) 
    
    original_image.save(output_image_path)

 
 
if __name__ == '__main__':

    image_name_object = filter(lambda x: x.endswith('.jpg'), files) 
    for image_name in image_name_object:
        scale_image(input_image_path=image_name, output_image_path='tumb-900/'+image_name, water_m='marker-autoritet.png', 
        water_tel='tel-stencil-autoritet.png', watermar_in=1, width=900, height=None )
        scale_image(input_image_path=image_name, output_image_path='tumb-230/'+image_name, water_m='',  water_tel='',  watermar_in=0, 
        width=230, height=None)

