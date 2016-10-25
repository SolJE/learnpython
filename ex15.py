from sys import argv
script, filename = argv

#txt = open(filename)

print ("Here's your file %r:" % filename)
#print (txt.read()) #也可以直接写为print (open(filename).read()),而无需原来的txt = opne(filename),下同
txt2 = open(filename).read()
print (txt2)

print ("Type the file name again:")
file_again = input(">")

txt_again = open(file_again)

print (txt_again.read())
txt_again.close()
