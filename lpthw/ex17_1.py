from sys import argv

script, from_file, to_file = argv

#打个即将操作的提示
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input("?")

open(to_file,'w').write(open(from_file).read());open(from_file).close();open(to_file).close()

#open(from_file).close();open(to_file).close()
#open(to_file).close()