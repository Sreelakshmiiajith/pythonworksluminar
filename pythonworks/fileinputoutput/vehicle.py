fi=open("C:\\Users\\91759\\Desktop\\pythonworks\\fileinputoutput\\number.txt")
numbers = [line.rstrip("\n") for line in fi]

keralanumbers = [n for n in numbers if n.startswith("kl")]
print(keralanumbers)
