import sys

for x in range(0, 125000):
	sys.stdout.write("<span>")
	if((x+1) % 1000 == 0):
		sys.stdout.write("\n")		
		

sys.stdout.write("\n")		
sys.stdout.write("my deep deep text")
sys.stdout.write("\n")		
sys.stdout.write("\n")		

for x in range(0, 125000):
	sys.stdout.write("</span>")
	if((x+1) % 1000 == 0):
		sys.stdout.write("\n")		

