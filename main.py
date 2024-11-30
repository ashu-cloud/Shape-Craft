import shapes
from canvaspainter import Canvas

def main():
    canvas_height= int(input(" Enter the height of the canvas : "))
    canvas_width= int(input(" Enter the width of the canvas: ")) 
    colors= {
        "white": (255,255,255),
        "black": (0,0,0)
    }
    canvas_color= input("choose whether you want the canvas to be black or white: ")

    canvas=canvas_dimensions(x= canvas_height,y= canvas_width, color=colors[canvas_color])

    get_shapes_from_user(canvas)




def canvas_dimensions(x,y,color):
    canvas= Canvas(x,y,color)
    return canvas




def get_shapes_from_user(canvas):
    while True:
        print("if you want to quit, just type quit :)")
        user_shape= input("Enter the shape you want to craft: ")
        if user_shape.lower().strip()=="rectangle":
            x= int(input("Enter the value of x coordinate of the rectangle: "))
            y= int(input("Enter the value of y coordinate of the rectangle: "))
            height= int(input("Enter the value of length of the rectangle: "))
            width= int(input("Enter the value of width of the rectangle: "))
            red= int(input("How much red do you want your rectangele to be:   "))
           
            green= int(input("How much green do you want your rectangle to be :  "))
            blue= int(input("How much blue do you want your rectangle to be:   "))
            
            s3= shapes.Rectangle(x=x,y=y,length=height,width=width,color=(red,green,blue))
            s3.draw(canvas)
            

        if user_shape.lower().strip()=="square":
            x= int(input("Enter the value of x coordinate of the square: "))
            y= int(input("Enter the value of y coordinate of the square: "))
            sidelength= int(input("Enter the value of sidelength of the square: "))
          
            red= int(input("How much red do you want your square to be :  "))
           
            green= int(input("How much green do you want your square to be :  "))
            blue= int(input("How much blue do you want your square to be :  "))

            
            s3= shapes.Square(x=x,y=y,sidelength=sidelength,color=(red,green,blue))
            s3.draw(canvas)
            
            
        if user_shape.lower().strip()== "circle":
            x= int(input("Enter the value of x coordinate of the center of the circle: "))
            
            y= int(input("Enter the value of y coordinate of the center of the circle: "))
            
            radius= int(input("Enter the value of radius of the circle: "))
            red= int(input("How much red do you want your circle to be : "))
           
            green= int(input("How much green do you want your circle to be :  "))
            blue= int(input("How much blue do you want your circle to be :  "))


            s3= shapes.Circle(center_x=x,center_y=y,radius=radius,color=(red,green,blue))
            s3.draw(canvas)

            
        if user_shape.lower().strip()=="quit":
            break
        else:
            print(" Enter a valid shape ")

        
        canvas.make("canvas.png")


    return

if __name__=="__main__":
    main()