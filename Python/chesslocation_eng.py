import numpy as np
		
matrix = np.array([
	["bGeneral" ,61    ,478  ,1090  ,370  ,-300  ,0    ,-130 ,0],
	["bGuard"   ,62    ,379  ,1010  ,300  ,-220  ,0    ,-150 ,0],
	["bGuard"   ,61    ,577  ,1155  ,475  ,-400  ,0    ,-115 ,0],
	["bElephant",62    ,278  ,908   ,255  ,-135  ,0    ,-170 ,0],
	["bElephant",61    ,677  ,1210  ,610  ,-515  ,0    ,-105 ,0],
	["bChariot" ,63    ,77   ,610   ,200  ,10    ,0    ,-230 ,0],
	["bChariot" ,59    ,877  ,1290  ,1045 ,-800  ,-65  ,0    ,0],
	["bHorse"   ,63    ,177  ,780   ,215  ,-60   ,0    ,-200 ,0],
	["bHorse"   ,60    ,777  ,1255  ,855  ,-690  ,0    ,-95  ,0],
	["bCannon"  ,317   ,180  ,1250  ,215  ,130   ,0    ,-95  ,0],
	["bCannon"  ,312   ,780  ,1525  ,655  ,-545  ,0    ,-40  ,0],
	["bSoldier" ,446   ,80   ,1568  ,329  ,322   ,0    ,0    ,0],
	["bSoldier" ,444   ,283  ,1625  ,215  ,50    ,0    ,-15  ,0],
	["bSoldier" ,442   ,483  ,1650  ,285  ,-170  ,0    ,0    ,0],
	["bSoldier" ,440   ,682  ,1668  ,470  ,-390  ,0    ,0    ,0],
	["bSoldier" ,438   ,882  ,1675  ,915  ,-730  ,0    ,0    ,0],
	["rGeneral" ,1212  ,489  ,2625  ,620  ,-520  ,0    ,200  ,0],
	["rGuard"   ,1213  ,389  ,2720  ,515  ,-433  ,0    ,220  ,0],
	["rGuard"   ,1211  ,589  ,2552  ,790  ,-652  ,0    ,180  ,0],
	["rElephant",1214  ,288  ,2823  ,430  ,-360  ,0    ,240  ,0],
	["rElephant",1209  ,689  ,2480  ,1030 ,-800  ,-25  ,0    ,0],
	["rChariot" ,1216  ,84   ,3070  ,335  ,-260  ,0    ,295  ,0],
	["rChariot" ,1206  ,891  ,2360  ,1068 ,-800  ,-157 ,0    ,0],
	["rHorse"   ,1215  ,186  ,2940  ,370  ,-300  ,0    ,265  ,0],
	["rHorse"   ,1207  ,790  ,2420  ,1055 ,-800  ,-105 ,0    ,0],
	["rCannon"  ,958   ,185  ,2716  ,225  ,-78   ,0    ,220  ,0],
	["rCannon"  ,952   ,789  ,2202  ,895  ,-715  ,0    ,105  ,0],
	["rSoldier" ,831   ,84   ,2712  ,215  ,110   ,0    ,220  ,0],
	["rSoldier" ,829   ,286  ,2405  ,220  ,-65   ,0    ,150  ,0],
	["rSoldier" ,827   ,487  ,2226  ,330  ,-250  ,0    ,115  ,0],
	["rSoldier" ,826   ,686  ,2118  ,550  ,-460  ,0    ,90   ,0],
	["rSoldier" ,823   ,888  ,2046  ,1030 ,-800  ,-25  ,0    ,0],
	["Unknown"   , "missing" , "missing", "missing", "missing", "missing", "missing", "missing",0]
])

def init():
	global chesslocation
	global matrix