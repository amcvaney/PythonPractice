# hw9.py
# Abigayle McVaney, 3/20/21
# A simple example to demonstrate basic usage of tkinter.
# To complete the assignment, you only need to
# modify the draw() method; you don't need to make any
# other changes anywhere else in the code.

import tkinter as tk


# Define a class for our application,
# which inherits from tk.Frame.
class MyApplication(tk.Frame):
    ##########################################
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        # self.handle_list is to remember handles
        # to some of the things we draw,
        # so that we can erase them later.
        self.handle_list = []
        # Create all the widgets we want in
        # our window at the beginning.
        self.create_widgets()

    ##########################################
    def create_widgets(self):
        # Create the widgets we want our window to have at startup.

        # First, a Canvas widget that we can draw on.
        # It will be 800 pixels wide, and 600 pixels tall.
        self.canvas = tk.Canvas(self.master, width=800, height=600, background="white")
        # This 'pack' method packs it into the top-level window.        
        self.canvas.pack()

        

        # Create a button with label "Draw", which calls the member
        # function self.draw() below when it's activated.
        self.draw_button = tk.Button(text="Draw", command=self.draw)
        # Pack the button into the window.
        self.draw_button.pack()

        # Create another button, with label "Clear" which calls the
        # member function self.clear() when it's activated.
        self.clear_button = tk.Button(text="Clear", command=self.clear)
        self.clear_button.pack()
        
    def draw(self):
        #############################################
        # Add your code to this method. Be sure to  #
        # store the 'handles' in the same way as    #
        # the sample code, so that the objects      #
        # will be removed when the 'clear button'   #
        # is clicked.                               #
        # You can delete all of the existing code   #
        # that's in this method right now - it is   #
        # here just as an example of drawing some   #
        # things and storing the handles.           #
        #############################################


        print("draw")
        
        # The canvas methods .create_XXXXX actually return
        # an internal name (integer) corresponding to each
        # object we create, called a 'handle. 
        # We will store those handles so that when the 'clear button'
        # is clicked, we can ask the canvas to remove them.


        # Draw a rectangle on the canvas. The first two arguments,
        # (250, 150) specify the upper-left hand corner of the rectangle,
        # the next two (550, 450) specify the lower-right hand corner.
        # 'fill' is an optional argument specifying the color that
        # the interior should be filled with. TKinter knows some
        # colors by string names, like "white", "blue", "red", ...
        # but we can specify any color using HTML color coding syntax 
        # as we do here:


       
        # rectangle = self.canvas.create_rectangle(300,300.400)

        k = self.canvas.create_line(80,100,80,300)
        self.handle_list.append(k)

        k = self.canvas.create_line(10,200,80,250)
        self.handle_list.append(k)

        k = self.canvas.create_line(180,200,80,250)
        self.handle_list.append(k)

        k = self.canvas.create_line(100,250,10,400)
        self.handle_list.append(k)


        k = self.canvas.create_line(100,300,150,400)
        self.handle_list.append(k)


        k = self.canvas.create_rectangle(60, 300, 100, 230, fill="pink")
        self.handle_list.append(k)

    
        h = self.canvas.create_oval(10,50,150,200,fill="#F9E4B7")
        self.handle_list.append(h)

        k = self.canvas.create_line(100,150,60,150)
        self.handle_list.append(k)

        h = self.canvas.create_oval(50,100,80,70,fill="black")
        self.handle_list.append(h)

        h = self.canvas.create_oval(90,100,120,70,fill="black")
        self.handle_list.append(h)

        h = self.canvas.create_oval(70,50,120,10,fill="yellow")
        self.handle_list.append(h)

        h = self.canvas.create_oval(150,290,20,320,fill="pink")
        self.handle_list.append(h)

        k = self.canvas.create_rectangle(60, 300, 100, 230, fill="pink")
        self.handle_list.append(k)

        

        '''

        # Draw a bunch of lines.
        for n in range(0,300,20):
        
            # Create a line segment from (400, n) to (400+n, 300).
            h = self.canvas.create_line(400,n,400+n,300)
            self.handle_list.append(h)
            
            # Create a line segment from (400+n, 300) to (400, 600-n).
            h = self.canvas.create_line(400+n,300,400,600-n)
            self.handle_list.append(h)
            
            h = self.canvas.create_line(400,600-n,400-n,300)
            self.handle_list.append(h)
            
            h = self.canvas.create_line(400-n,300,400,n)
            self.handle_list.append(h)

        h = self.canvas.create_arc(10,10,110,110,start=45,extent=270,fill="yellow")
        self.handle_list.append(h)

        h = self.canvas.create_polygon(200,10,250,60,200,110,150,60,fill="",outline="black")
        self.handle_list.append(h)
        '''
    ##############################################
    def clear(self):
        
        print("clear")
        
        # To clear the things we drew in the 'draw'
        # function, we just ask the canvas to delete them,
        # one at a time, by their handles.
        # You should not need to modify anythingin this method.
        while len(self.handle_list)>0:
            h = self.handle_list.pop()
            self.canvas.delete(h)


########################################
# Do not change anything below here!   #
########################################
# Instantiate the Tk class.
# This should only ever be done once in a program.
# Think of it as 'firing up' the library, getting it ready to do stuff.
root = tk.Tk()

# Create an instance of the MyApplication class we defined above.
app = MyApplication(root)

# Pass flow control over to the Tkinter library, so it can do things
# like wait for keyboard and mouse events, redraw the window when needed,...
# One of the things it will do is watch for buttons we created and invoke
# the 'callback functions' we gave them. It will run indefinitely,
# until the operating system sends it a 'quit' command (e.g.,
# if we close the window).
app.mainloop()
