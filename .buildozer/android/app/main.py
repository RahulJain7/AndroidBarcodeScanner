from kivy.app import App
from kivy.lang import Builder

design = Builder.load_file("design.kv")

class MyApp(App):

	def build(self):	
		return design


if __name__ == '__main__':
	MyApp().run()