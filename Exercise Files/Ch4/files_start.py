#
# Read and write files using the built-in Python file methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():  
	# Open a file for writing and create it if it doesn't exist
	# f = open("textfile.txt","w+")
	
	# append to file
	f = open("textfile.txt","a+")

	for i in range(10):
		f.write("This is the line %d\r\n" % (i+1))

	#close the file when done
	f.close

if __name__ == "__main__":
  main()
