import sys

tag = "span"

for x in range(0, 125000):
	sys.stdout.write("<" + tag + ">")
	if((x+1) % 1000 == 0):
		sys.stdout.write("\n")		
		

sys.stdout.write("\n")		
sys.stdout.write("my deep deep text")
sys.stdout.write("\n")		
sys.stdout.write("\n")		

for x in range(0, 125000):
	sys.stdout.write("</" + tag + ">")
	if((x+1) % 1000 == 0):
		sys.stdout.write("\n")		

sys.stdout.write("\n")		
sys.stdout.write("the end of text")
sys.stdout.write("\n")		
sys.stdout.write("\n")		
