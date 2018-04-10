import sys

tag = "span"

for x in range(0, 62500):
	sys.stdout.write("<" + tag + "></" + tag + ">")
	if((x+1) % 500 == 0):
		sys.stdout.write("\n")		

sys.stdout.write("\n")		
sys.stdout.write("the middle of text")
sys.stdout.write("\n")		
sys.stdout.write("\n")		

for x in range(0, 62500):
	sys.stdout.write("<" + tag + "></" + tag + ">")
	if((x+1) % 500 == 0):
		sys.stdout.write("\n")		

sys.stdout.write("\n")		
sys.stdout.write("the end of text")
sys.stdout.write("\n")		
sys.stdout.write("\n")		
