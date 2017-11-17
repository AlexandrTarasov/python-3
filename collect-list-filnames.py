from PIL import Image
import os, sys

path = "."

files = os.listdir( path )



def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))
 
    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')
 
    original_image.thumbnail(max_size, Image.ANTIALIAS)
   # original_image.save(output_image_path)
 
    #scaled_image = Image.open(output_image_path)
    #width, height = scaled_image.size
    #print('The scaled image size is {wide} wide x {height} '
    #     'high'.format(wide=width, height=height))
 
 
if __name__ == '__main__':

    image_name_object = filter(lambda x: x.endswith('.jpg'), files) 
    for image_name in image_name_object:
        #print (d)
        scale_image(input_image_path=image_name, output_image_path='54938_new.jpg',width=900)
