#20201201 - Here i am going to start with 2 libraries which are for widget and another for UI based
from kivy.app import App
from kivy.uix.label import Label

#class must have subcalss in kivy which means every kivy application should have subcalss App
class MainApp(App):
    #now i am taking the label function which can call the UI  based code for widget
    def build(self):
        #now labelling the text for widget
        label = Label(text = 'Hello KIVY!, Welcome to Logical SciTech...',
        size_hint = (0.5,0.5),
        pos_hint = {'center_x':0.5, 'center_y':0.5})#here one is for text size and another is for text position where it should be

        return label

if __name__=='__main__':
    #assiging to an object
    app=MainApp()
    app.run()

    #let me run the code

    #here the test runs at the backend which means this text will be useful for debugging later

    #thats it for today and i hope you understood the concept of basic KIVY widget
    #next video will be on Images
    # thank you guys and please subscribe