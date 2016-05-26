from tkinter import *
from nltk.tokenize import sent_tokenize, word_tokenize

root = Tk()
myTextWidget=Text(root,bg="red")
myFile=open("sampletext.txt","r")
myText=myFile.read()
array=word_tokenize(myText)
myFile.close()
for i in array:
 myTextWidget.insert(0.0,i)
myTextWidget.pack(fill=BOTH)

root.mainloop()

