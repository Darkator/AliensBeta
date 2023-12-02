from CvPythonExtensions import *

gc = CyGlobalContext()

# def TeamResarchREDadd(iPlayer):
#	pPlayer = gc.getPlayer(iPlayer)
#	iTech = pPlayer.getCurrentResearch()
#	iTeam = pPlayer.getTeam()
#	ipenatly = 0
#	if gc.getTeam(iTeam).getNumMembers() > 1:
#		ipenatly = gc.getTeam(iTeam).getNumMembers() * 10
#		iBonusResearch = ipenatly/100
#		pPlayer.changeCommercePercent(CommerceTypes.COMMERCE_RESEARCH, iBonusResearch)
##9


#ipenatly = 0
#	pPlayer = gc.getPlayer(iPlayer)
#	iTeam = pPlayer.getTeam()
#	iTech = pPlayer.getCurrentResearch()
#	if gc.getTeam(iTeam).getNumMembers() == 9:
#		ipenatly = gc.getTeam(iTeam).getNumMembers() * 15000
#		iBonusResearch = pPlayer.getCommerceRate(CommerceTypes.COMMERCE_RESEARCH) * ipenatly/100
#		gc.getTeam(pPlayer.getTeam()).changeResearchProgress(iTech, iBonusResearch, iPlayer)


# if iGameTurn == 60:
#			###declare war begin###
#			iTypeDeclaringCiv = gc.getInfoTypeForString("CIVILIZATION_ALIEN")
#			iTypeVictim = gc.getInfoTypeForString("CIVILIZATION_WW2_IBERIA")
#			iDeclaringPlayer = -1
#			iVictimPlayer = -1
#			iMaxCiv = gc.getMAX_PLAYERS()
#			for iCivs in range(iMaxCiv):
#					pPlayer = gc.getPlayer(iCivs)
#					if pPlayer.getCivilizationType ()==iTypeDeclaringCiv:
#						iDeclaringPlayer = iCivs
#					elif pPlayer.getCivilizationType ()==iTypeVictim:
#						iVictimPlayer = iCivs
#			if iDeclaringPlayer ==-1 or iVictimPlayer ==-1:
#						return
#			gc.getTeam(gc.getPlayer(iDeclaringPlayer).getTeam()).declareWar(iVictimPlayer, false, WarPlanTypes.WARPLAN_TOTAL)

def addSpeed(iPlayer):
			pPlayer = gc.getPlayer(iPlayer)
			iTeam = pPlayer.getTeam()
			
			iTech = pPlayer.getCurrentResearch()
					###declare war begin###
			#####ONLE ALAIES######
			iTypeBonusCiv = gc.getInfoTypeForString("CIVILIZATION_ENGLAND")
			iDeclaringPlayer = -1
			iMaxCiv = gc.getMAX_PLAYERS()
			for iCivs in range(iMaxCiv):
					piPlayer = gc.getPlayer(iCivs)
					if piPlayer.getCivilizationType ()==iTypeBonusCiv:
						iDeclaringPlayer = iCivs
			if iDeclaringPlayer ==-1:
						return
			ipenatly = gc.getTeam(iTeam).getNumMembers() * 420
			iBonusResearch = pPlayer.getCommerceRate(CommerceTypes.COMMERCE_RESEARCH) * ipenatly/100
			gc.getTeam(gc.getPlayer(iDeclaringPlayer).getTeam()).changeResearchProgress(iTech, iBonusResearch, iPlayer)
		
	
def Axisspeed(iPlayer):	
			pPlayer = gc.getPlayer(iPlayer)
			iTeam = pPlayer.getTeam()
			
			iTech = pPlayer.getCurrentResearch()
			###declare war begin###
			iTypeBonusCiv = gc.getInfoTypeForString("CIVILIZATION_GERMANY")
			iDeclaringPlayer = -1
			iMaxCiv = gc.getMAX_PLAYERS()
			for iCivs in range(iMaxCiv):
					piPlayer = gc.getPlayer(iCivs)
					if piPlayer.getCivilizationType ()==iTypeBonusCiv:
						iDeclaringPlayer = iCivs
			if iDeclaringPlayer ==-1:
						return
			ipenatly = gc.getTeam(iTeam).getNumMembers() * 70
			iBonusResearch = pPlayer.getCommerceRate(CommerceTypes.COMMERCE_RESEARCH) * ipenatly/100
			gc.getTeam(gc.getPlayer(iDeclaringPlayer).getTeam()).changeResearchProgress(iTech, iBonusResearch, iPlayer)
						