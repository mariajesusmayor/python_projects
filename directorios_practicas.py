import os, sys

#directorio = "C:\\Users\\mjm\\ownCloud\\UOC\\2018-19_Sem01\\MLEG\\PEC"

#for i in range (3):
	#os.mkdir (directorio + str(i+1))

#print ("yatá")


directorioBase = "C:\\Users\\mjm\\ownCloud\\UOC\\2018-19_Sem01\\"

#directorioMLEG = directorioBase + "MLEG"

directorioPRID = directorioBase + "PRID\\PEC"

directorioRSCO = directorioBase + "RSOC\\PEC"

directorioTGCO = directorioBase + "TGCO\\PEC"

for i in range (4):
	os.mkdir (directorioPRID + str(i + 1))
	print (directorioPRID)
	os.mkdir (directorioRSCO + str(i + 1))
	print(directorioRSCO)
	os.mkdir (directorioTGCO + str(i + 1))
	print(directorioTGCO)

print ("Hecho")




#declarar variable x
#declarar variable y
#crear el bucle for 
#etc
