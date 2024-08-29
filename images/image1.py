from PIL import Image 
x=Image.open("d:/images/02.jpg")
y=x.resize((100,100))
y.save("d:/images/02a.jpg")
x.show()
y.show()
