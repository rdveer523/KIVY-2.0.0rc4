#20201202 load and displaying an image
#_-------------------------------------
# There is a standard Image class for image related in KIVY
# 1. use "Image" to load local images
# 2. "AsyncImage" to load an image from URL

from kivy.app import App
from kivy.uix.image import Image, AsyncImage
# Image is for local and Async is for URL path based can load images

#now take the calss and already discussed that KIVY calss should contain subclass App
class MainApp(App):
    def build(self):
        #note: Image class consider different parameters so here important point is "source" because 
        # to load image we should provide the path riht and here it consideered as source
        #this is for local
        img = Image(source = 'E:\\5---beeware_kivy_env\\youtube-my\\20201202\\LogicalSciTech.jpg',
        size_hint = (1,0.5),
        pos_hint={'center_x':0.5, 'center_y':0.5})
        #AsyncImage from URL
        img = AsyncImage(source='https://1.bp.blogspot.com/-3IoD6_z6eG0/X8ajOwfjIXI/AAAAAAAAAd8/eetGz0eQJT0OtUaEltuJlc8SlX3lCWxZQCNcBGAsYHQ/s960/LOGO---LogicalSciTech.jpg')
#you can take size_hint or not but its not mandatory
        return img

if __name__=='__main__':
    #calling the class by assigning it to an object
    #app = MainApp()
    #run
    #app.run()
    #or you can take as 
    MainApp().run()

    # Thank you guys and please don't forget to subscribe and tomorrow will discuss about buttons, widgets, some other important topics. Thank you