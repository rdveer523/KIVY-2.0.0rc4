#20201203 - Laayouts UI
# 1. Tkinter has layout or geometry manager
# 2. wxPython has sizers layout
# In the sameway kivy has different types of layouts and out of them
#     BoxLayout
#     FloatLayout
#     GridLayout

# these three at present i am using and you can checkout the kivy documentation
# now lets try the code
import kivy
import random
# you will know while writing the code why i am using random and we know that random is to generate numbers in random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#we know that these are the packages and modules going to be instantiated here
#now take the colors lists and we know in python GUI the colors considered as RBG
#these colors will be useful for the buttons in the widget and now
red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]
#now we have to take a class and it should have the subclass inside of class
class boxlayout(App):
    def build(self):
        layout = BoxLayout(padding=10)
        #padding is for pixel based and kivy has singular, two argument, four argument 
        # paddings which are called childrens. such type of points will be useful when you prepare for interviews
        colors = [red,green,blue,purple]
        #now i should apply these colors on the buttons which i am going to use in widgetbox
        for i in range(5):
            #buttons
            btn = Button(text="Button #%s" %(i+1),
            background_color = random.choice(colors))
            #here i have taken a variable button and assigned the Button which will be iterate
            #everytime each button will have random color
            layout.add_widget(btn)
            #this means i am going to add the button to widget after iterating 
        return layout

if __name__=='__main__':
     boxlayout().run()
