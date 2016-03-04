fh = open("bitacoras.txt")
import webbrowser
for line in fh:
	fname = raw_input("Enter para abrir archivo (done para salir):")
	if fname == "done":
		break
	line = line.rstrip()
	webbrowser.open(line)
	print line
print "done"
