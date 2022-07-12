#import os
from random import*
#from time import*
import time
#from donnéesWild import*
from math import*

a=input("Configurer ?")
if a=="o":
	config=input("Configuration")
	timeSpeed=input("Time speed ???")
	if timeSpeed=="":
		timeSpeed=2
	saveFrequence=input("Fréquence des saves:")
elif a=="s": #Slow
	config="a"
	timeSpeed=2
	saveFrequence=50
else:
	config="n"
	timeSpeed=2
	saveFrequence=450
clic=0
cinq=5
dix=10
vingt=20
herbivores=list()
carnivores=list()
H=dict()
C=dict()
pop=0
combat=0
fuite=0

print("Création des individus")
while clic<=dix:
	H["vie"]=randrange(9,12)
	H["degats"]=randrange(2,4)
	H["speed"]=randrange(4,7)
	H["reponse"]=randrange(40,61) #probalité de réponse physique en cas d'attaque (/100)
	H["hostilite"]=randrange(40,61) #hostilité envers d'autres population
	H["sociabilite"]=randrange(40,61) #probabilité de symbiose envers deux individues de même population
	H["food"]=5
	H["age"]=0

	herbivores.append(H)
	H=dict()
	print("clic")
	clic+=1
print("----")
clic=0

while clic<=dix:
	C["vie"]=randrange(9,12)
	C["degats"]=randrange(1,4)
	C["speed"]=randrange(4,7)
	C["reponse"]=randrange(40,61) #probalité de réponse physique en cas d'attaque (/100)
	C["hostilite"]=randrange(40,61) #hostilité envers d'autres population
	C["sociabilite"]=randrange(40,61) #probabilité de symbiose envers deux individus de même population
	C["food"]=5
	C["age"]=0

	carnivores.append(C)
	clic+=1
	C=dict()
	print("clic")
clic=0



print("\nCLAC ! ! !\n")


bin=1
time.time()
print(time.time())
clicSave=0
while 0==0:
	clicSave+=1
	if clicSave==saveFrequence:
		bin=1
		clicSave=0
	#////////////// SAVE
	if bin==1:
		bin=0
		print("\n\n\n\n\n\n\n\n\n\n=============================== SAVE !!! =====================================")
		clic=0
		herbivoresListVie=list()
		herbivoresListDegat=list()
		herbivoresListAge=list()
		herbivoresListSpeed=list()
		herbivoresListFood=list()
		herbivoresListHostilite=list()
		herbivoresListReponse=list()
		while clic<len(herbivores): #Calcul moyenne hostilité herbivores	
			herbivoresVie=herbivores[clic] ["vie"]
			herbivoresDegat=herbivores[clic] ["degats"]
			herbivoresAge=herbivores[clic] ["age"]
			herbivoresSpeed=herbivores[clic] ["speed"]
			herbivoresFood=herbivores[clic] ["food"]
			herbivoresHostilite=herbivores[clic] ["hostilite"]
			herbivoresReponse=herbivores[clic] ["reponse"]

			herbivoresListVie.append(herbivoresVie)
			herbivoresListDegat.append(herbivoresDegat)
			herbivoresListAge.append(herbivoresAge)
			herbivoresListSpeed.append(herbivoresSpeed)
			herbivoresListFood.append(herbivoresFood)
			herbivoresListHostilite.append(herbivoresHostilite)
			herbivoresListReponse.append(herbivoresReponse)

			herbivoresMoyenneVie=sum(herbivoresListVie)/len(herbivoresListVie)
			herbivoresMoyenneDegat=sum(herbivoresListDegat)/len(herbivoresListDegat)
			herbivoresMoyenneAge=sum(herbivoresListAge)/len(herbivoresListAge)
			herbivoresMoyenneSpeed=sum(herbivoresListSpeed)/len(herbivoresListSpeed)
			herbivoresMoyenneFood=sum(herbivoresListFood)/len(herbivoresListFood)
			herbivoresMoyenneHostilite=sum(herbivoresListHostilite)/len(herbivoresListHostilite)
			herbivoresMoyenneReponse=sum(herbivoresListReponse)/len(herbivoresListReponse)
			clic+=1
		clic=0


		carnivoresListVie=list()
		carnivoresListDegat=list()
		carnivoresListAge=list()
		carnivoresListSpeed=list()
		carnivoresListFood=list()
		carnivoresListHostilite=list()
		carnivoresListReponse=list()
		while clic<len(carnivores): #Calcul moyenne hostilité carnivores
			carnivoresVie=carnivores[clic] ["vie"]
			carnivoresDegat=carnivores[clic] ["degats"]
			carnivoresAge=carnivores[clic] ["age"]
			carnivoresSpeed=carnivores[clic] ["speed"]
			carnivoresFood=carnivores[clic] ["food"]
			carnivoresHostilite=carnivores[clic] ["hostilite"]
			carnivoresReponse=carnivores[clic] ["reponse"]

			carnivoresListVie.append(carnivoresVie)
			carnivoresListDegat.append(carnivoresDegat)
			carnivoresListAge.append(carnivoresAge)
			carnivoresListSpeed.append(carnivoresSpeed)
			carnivoresListFood.append(carnivoresFood)
			carnivoresListHostilite.append(carnivoresHostilite)
			carnivoresListReponse.append(carnivoresReponse)

			carnivoresMoyenneVie=sum(carnivoresListVie)/len(carnivoresListVie)
			carnivoresMoyenneDegat=sum(carnivoresListDegat)/len(carnivoresListDegat)
			carnivoresMoyenneAge=sum(carnivoresListAge)/len(carnivoresListAge)
			carnivoresMoyenneSpeed=sum(carnivoresListSpeed)/len(carnivoresListSpeed)
			carnivoresMoyenneFood=sum(carnivoresListFood)/len(carnivoresListFood)
			carnivoresMoyenneHostilite=sum(carnivoresListHostilite)/len(carnivoresListHostilite)
			carnivoresMoyenneReponse=sum(carnivoresListReponse)/len(carnivoresListReponse)
			clic+=1
		clic=0
		print("!!! Word age:", time.time(), "!!!")
		print("\nHERBIVORES ======================= CARNIVORES")
		print(" | ", len(herbivores)," | =======Population======= | ", len(carnivores)," | \n")
		print(round(herbivoresMoyenneVie, 1), "===============LIFE============", round(carnivoresMoyenneVie, 1))
		print(round(herbivoresMoyenneDegat, 1), "=================DPS=============", round(carnivoresMoyenneDegat, 1))
		print(round(herbivoresMoyenneSpeed, 1), "=================SPEED===========", round(carnivoresMoyenneSpeed, 1),"\n")
		print(round(herbivoresMoyenneFood, 1), "==================Food=============", round(carnivoresMoyenneFood, 1))
		print(round(herbivoresMoyenneAge, 1), "==================Age================", round(carnivoresMoyenneAge, 1))
		print(round(herbivoresMoyenneHostilite, 1), "===============Hostilité========", round(carnivoresMoyenneHostilite, 1))
		print(round(herbivoresMoyenneReponse, 1), "===============Réponse=========", round(carnivoresMoyenneReponse, 1))
		print("timeSpeed:", timeSpeed)
		print("=============================== !!!! !!!! =====================================\nEND ***\n\n")
		#while ceil(time.time())%30==0 or ceil(time.time())==0:
		#	z=0
		time.sleep(1)





	if ceil(time.time())%float(timeSpeed)==0:                             # ////////// AGE
		if config=="a":
			print(" = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
		#time+=1
		if time.time()%int(saveFrequence)==0:
			bin=1
		clic=0
		combat=0
		while clic<len(herbivores):
			herbivores[clic] ["age"]+=1
			pop=0
			herbivores[clic] ["food"]-=.1
			if herbivores[clic] ["food"]<=0:
				variable="de faim"
				pop=1
			elif herbivores[clic] ["food"]>10:
				herbivores[clic] ["food"]=10

			if herbivores[clic] ["age"]>36:
				variable="de viellesse"
				pop=1

			elif herbivores[clic] ["vie"]<1:
				variable="du coma"
				pop=1

			elif herbivores[clic] ["age"]<1:
				variable="infentile"
				pop=1

			if pop==1:
				del herbivores[clic]
				if config=="a":																	#print						
					print("Mort", variable, "(H)")												

			clic+=1

		clic=0
		while clic<len(carnivores):
			carnivores[clic] ["age"]+=1
			pop=0
			carnivores[clic] ["food"]-=.1
			if carnivores[clic] ["food"]<=0:
				variable="de faim"
				pop=1
			elif carnivores[clic] ["food"]>10:
				carnivores[clic] ["food"]=10

			if carnivores[clic] ["age"]>36:
				variable="de viellesse"
				pop=1

			elif carnivores[clic] ["vie"]<1:
				variable="du coma"
				pop=1

			elif carnivores[clic] ["age"]<1:
				variable="infentile"
				pop=1

			if pop==1:
				del carnivores[clic]
				if config=="a":																	#print
					print("Mort", variable, "(C)")

			clic+=1
		clic=0






#/////////// NAISSANCE
		declic=len(carnivores)/10
		while declic>0:
			declic-=1
			z=randrange(len(carnivores))
			pere=carnivores[z]

			y=randrange(len(carnivores))
			mere=carnivores[y]
			C=dict()

		#FOOD
			C["food"]=1
		#VIE
			o=randrange(2)
			if o==0:
				C["vie"]=pere["vie"]
			else:
				C["vie"]=mere["vie"]

			oo=randrange(10)
			if oo==0:
					oo=randrange(2)
					if oo==0:
						C["vie"]=round(C["vie"]+1, 1)
						if config=="a":																	#print
							print("mutatation vie ! ++")
					else:
						C["vie"]=round(C["vie"]-1, 1)
						if config=="a":																	#print
							print("mutatation vie ! --")


		#DEGATS
			o=randrange(2)
			if o==0:
				C["degats"]=pere["degats"]
			else:
				C["degats"]=mere["degats"]

			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					C["degats"]=round(C["degats"]+1)
					if config=="a":																	#print
						print("mutatation dégats ! ++")
				else:
					C["degats"]=round(C["degats"]-1)
					if config=="a":																	#print
						print("mutatation dégats ! --")
					if C["degats"]<1:
							C["degats"]=1

		#SPEED
			o=randrange(2)
			if o==0:
				C["speed"]=pere["speed"]
			else:
				C["speed"]=mere["speed"]
				
			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					C["speed"]=round(C["speed"]+1, 1)
					if config=="a":																	#print
						print("mutatation speed ! ++")
				else:
					C["speed"]=round(C["speed"]-1, 1)
					if config=="a":																	#print
						print("mutatation speed ! --")
						if C["speed"]<1:
							C["speed"]=1

		#REPONSE
			o=randrange(2)
			if o==0:
				C["reponse"]=pere["reponse"]
			else:
				C["reponse"]=mere["reponse"]
			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					C["reponse"]=round(C["reponse"]+1, 1)
					if config=="a":																	#print
						print("mutatation réponse ! ++")
				else:
					C["reponse"]=round(C["reponse"]-1, 1)
					if config=="a":																	#print
						print("mutatation réponse ! --")

		#HOSTILITE
			o=randrange(2)
			if o==0:
				C["hostilite"]=pere["hostilite"]
			else:
				C["hostilite"]=mere["hostilite"]
			
			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					C["hostilite"]=round(C["hostilite"]+1, 1)
					if config=="a":																	#print
						print("mutatation hostilite ! ++")
				else:
					C["hostilite"]=round(C["hostilite"]-1, 1)
					if config=="a":																	#print
						print("mutatation hostilite ! --")
				
		#SOCIABILITE
			o=randrange(2)
			if o==0:
				C["sociabilite"]=pere["sociabilite"]
			else:
				C["sociabilite"]=mere["sociabilite"]

			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					C["sociabilite"]=round(C["sociabilite"]+1, 1)
					if config=="a":																	#print
						print("mutatation sociabilité ! ++")
				else:
					C["sociabilite"]=round(C["sociabilite"]-1, 1)
					if config=="a":																	#print
						print("mutatation sociabilite ! --")

			C["age"]=0

		

			pere=dict()
			mere=dict()

			if C["vie"]>1:
				if config=="a":																	#print
					print("pop ! ", C["vie"], "(C)")
				carnivores.append(C)
			else:
				if config=="a":																	#print
					print("mort infentile")


		declic=0

		




	#VIE
		declic=len(herbivores)/10
		while declic>0:
			declic-=1
			z=randrange(len(herbivores))
			pere=herbivores[z]

			y=randrange(len(herbivores))
			mere=herbivores[y]

			H=dict()

		#FOOD
			H["food"]=1

			o=randrange(2)
			if o==0:
				H["vie"]=pere["vie"]
			else:
				H["vie"]=mere["vie"]

			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					H["vie"]=round(H["vie"]+1, 1)
					if config=="a":																	#print
						print("mutatation vie ! ++")
				else:
					H["vie"]=round(H["vie"]-1, 1)
					if config=="a":																	#print
						print("mutatation vie ! --")

		#DEGATS
			o=randrange(2)
			if o==0:
				H["degats"]=pere["degats"]
			else:
				H["degats"]=mere["degats"]

			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					H["degats"]=round(H["degats"]+1, 1)
					if config=="a":																	#print
						print("mutatation dégats ! ++")
				else:
					H["degats"]=round(H["degats"]-1, 1)
					if config=="a":																	#print
						print("mutatation dégats ! --")
					if H["degats"]<1:
							H["degats"]=1





		#SPEED
			o=randrange(2)
			if o==0:
				H["speed"]=pere["speed"]
			else:
				H["speed"]=mere["speed"]
				
			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					H["speed"]=round(H["speed"]+1, 1)
					if config=="a":																	#print
						print("mutatation speed ! ++")
				else:
					H["speed"]=round(H["speed"]-1, 1)
					if config=="a":																	#print
						print("mutatation speed ! --")
					if H["speed"]<1:
							H["speed"]=1

		#REPONSE
			o=randrange(2)
			if o==0:
				H["reponse"]=pere["reponse"]
			else:
				H["reponse"]=mere["reponse"]
			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					H["reponse"]=round(H["reponse"]+1, 1)
					if config=="a":																	#print
						print("mutatation réponse ! ++")
				else:
					H["reponse"]=round(H["reponse"]-1, 1)
					if config=="a":																	#print
						print("mutatation réponse ! --")

		#HOSTILITE
			o=randrange(2)
			if o==0:
				H["hostilite"]=pere["hostilite"]
			else:
				H["hostilite"]=mere["hostilite"]
			
			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					H["hostilite"]=round(H["hostilite"]+1, 1)
					if config=="a":																	#print
						print("mutatation hostilite ! ++")
				else:
					H["hostilite"]=round(H["hostilite"]-1, 1)
					if config=="a":																	#print
						print("mutatation hostilite ! --")
				
		#SOCIABILITE
			o=randrange(2)
			if o==0:
				H["sociabilite"]=pere["sociabilite"]
			else:
				H["sociabilite"]=mere["sociabilite"]

			oo=randrange(10)
			if oo==0:
				oo=randrange(2)
				if oo==0:
					H["sociabilite"]=round(H["sociabilite"]+1, 1)
					if config=="a":																	#print
						print("mutatation sociabilité ! ++")
				else:
					H["sociabilite"]=round(H["sociabilite"]-1, 1)
					if config=="a":																	#print
						print("mutatation sociabilite ! --")

			H["age"]=0

			pere=dict()
			mere=dict()

			if H["vie"]>1:
				if config=="a":																	#print
					print("pop ! ", H["vie"], "(H)")
				herbivores.append(H)
			else:
				if config=="a":																	#print
					print("mort infentile")
		declic=0


# CONTACTS
		declic=len(herbivores)/10
		while declic>0:
			declic-=1
			z=len(carnivores)+len(herbivores)
			o=randrange(100)
			if z>o:							#contact !
				y=randrange(len(herbivores)) 
				x=randrange(len(carnivores))
				H=herbivores[y]
				C=carnivores[x]
				h=herbivores[y] ["vie"]
				c=carnivores[x] ["vie"]
				del herbivores[y]
				del carnivores[x]

				o=randrange(100)			#analyse hostilité"
				if o<H["hostilite"]:
					combat=1
				else:
					fuite=1		#fuite = 1 pour Herbivores
				if o<C["hostilite"]:
					combat=1
				else:
					fuite=2  #fuite = 2 pour Carnivores
				if combat==1:
					while H["vie"] and C["vie"]>=1:
						o=randrange(2)
						if o==0:
							if C["vie"]<c/3 or fuite==2:				#proba de fuite à moins d'un tiers de vie
								o=randrange(100)
								if o>C["reponse"]:
									if C["speed"]>H["speed"]:
										if config=="a":																	#print
											print("C tente de fuir...")
											print("\n->->-> C s'est enfuit [", C["speed"],">",H["speed"],"] ->->->" )
										H["vie"]=h
										C["vie"]=c
										if config=="a":																	#print
											print("=== H(",H["vie"],") et C(",C["vie"],") rétablies) ===\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n\n\n" )
										herbivores.append(H)
										carnivores.append(C)
										break
									else:
										if config=="a":																	#print
											print("C n'a pas réussi à s'enfuir le combat continue...")
								else:
									z=0
							C["vie"]=C["vie"]-H["degats"]
							if config=="a":																	#print
								print("H inflige", H["degats"], "à C (vie restante:", C["vie"], "/",  c,")")
							
							if C["vie"]<1:
								H["vie"]=h
								H["food"]+=1
								herbivores.append(H)
								if config=="a":																	#print
									print("\nC est mort au combat tué par H !")
									print("=== H(",H["vie"],") rétablie === \n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n\n\n")
								break
						else:
							if H["vie"]<h/3 or fuite==1:				#proba de fuite à moins d'un tiers de vie
								o=randrange(100)
								if o>H["reponse"]:
									if H["speed"]>C["speed"]:
										if config=="a":																	#print
											print("\n->->-> H s'est enfuit (", H["speed"],">",C["speed"],") ->->->" )
										H["vie"]=h
										C["vie"]=c
										if config=="a":																	#print
											print("=== H(",H["vie"],") et C(",C["vie"],") rétablies) ===\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n\n\n" )
										herbivores.append(H)
										carnivores.append(C)
										break
									else:
										if config=="a":																	#print
											print("H n'a pas réussi à s'enfuir le combat continue...")
								else:
									z=0

							H["vie"]=H["vie"]-C["degats"]
							if config=="a":																	#print
								print("C inflige", C["degats"], "à H (vie restante:", H["vie"], "/",  h,")")

							if H["vie"]<1:
								C["vie"]=c
								C["food"]+=1
								carnivores.append(C)
								if config=="a":																	#print
									print("\nH est mort au combat tué par C !")
									print("=== C(",C["vie"],") rétablie === \n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n\n\n")
								break
						fuite=0

				else:
					if config=="a":																	#print
						print("le combat n'a pas eu lieu")



		while ceil(time.time())%float(timeSpeed)==0:
			z=0
			#print(ceil(time.time()))
