import numpy as np
from PIL import Image
'''
class Canvas:
    def __init__(self, x,y,color):
        self.x=x
        self.y=y
        self.color= color

        # make a 3d array with all values initialized as 0

        self.data= np.zeros((self.x , self.y, 3) , dtype=np.uint8)
            
            
            # to fill colors in the canvas
        self.data[ : ] = self.color
    #converts array to image
    def make(self , imagepath):
        
        self.imagepath= imagepath
        img= Image.fromarray(self.data, 'RGB')
        
        img.save(imagepath)
        img.show()
'''
class Canvas:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        
        # Ensure color is a tuple of 3 integers in the range 0-255
        if len(color) != 3 or not all(0 <= c <= 255 for c in color):
            raise ValueError("Color must be a tuple of 3 integers in the range 0-255")

        # Make a 3D array with all values initialized as 0
        self.data = np.zeros((self.x, self.y, 3), dtype=np.uint8)
        
        # Fill the entire canvas with the specified color
        self.data[:] = self.color

    # Converts the array to an image
    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
        img.show()


