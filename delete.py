'''import os
os.remove("demofile.txt")

f = open("demofile.txt", "a")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile.txt", "r")
print(f.read())'''


import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


import os
os.rmdir("myfolder")
