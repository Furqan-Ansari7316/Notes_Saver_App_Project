# Notes saver app.
print("Menu : ")
print("1.Read")
print("2.Write")
print("3.Append")
print("4.Word Count")
choice=int(input("Enter choice from the menu : "))
if(choice==1):
    with open("3.py","r") as file:
        content=file.read()
        print(content)
elif(choice==2):
    notes=input("Enter Text for Notes : ")
    with open("3.py","w") as file:
        file.write(notes+"\n")
        print("Notes Saved!")
elif(choice==3):
    note=input("Enter Text for Note : ")
    with open("3.py","a") as file:
        file.write(note+"\n") 
        print("Notes Saved!")     
elif(choice==4):
    with open("3.py","r")as file:
        content=file.read()
        words=content.split()
        print("Total words : ",len(words))          
else:
    print("ERROR!!! Please enter a valid choice.")        