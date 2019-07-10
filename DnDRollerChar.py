import random

levelReq = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000,
          120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]

profEffectedBy = [1,4,3,0,5,3,4,5,3,4,3,4,5,5,3,2,2,4]

#Store character in an object
class sheet(object):
    healthVals = {"Barbarian" : (7, 12), "Bard" : (5, 8), "Cleric" : (5, 8), "Druid" : (5, 8), "Fighter" : (6, 10),
             "Monk" : (5, 8), "Paladin" : (6, 10), "Ranger" : (6, 10), "Rogue" : (5, 8), "Sorcerer" : (4, 6), 
             "Warlock" : (5, 8), "Wizard" : (4, 6), "Artificer" : (5, 8), "Blood Hunter" : (6, 10)}
    
    name = "name"
    hp = 0
    race = "race"
    clss = "Barbarian"
    stats = [0, 0, 0, 0, 0, 0] #Strength, Dexterity, Constitution, Intelegence, Wisdom, Charisma
    level =  1
    exp = 0
    background = "background"
    personality = "personality"
    ideals = "ideals"
    bonds = "bonds"
    flaws = "flaws"
    alignment = "alignment"
    backstory = "backstory"
    op = "other proficiencies"
    insp = 0
    ac = 0
    speed = 0
    curHp = 0
    tempHp = 0
    initiative = 0
    profB = 2
    saves = [False, False, False]
    fails = [False, False, False]
    profs = [[0, False],[0, False],[0, False],
             [0, False],[0, False],[0, False],
             [0, False],[0, False],[0, False],
             [0, False],[0, False],[0, False],
             [0, False],[0, False],[0, False],
             [0, False],[0, False],[0, False]]
    st = [[0, False],[0, False],[0, False],
          [0, False],[0, False],[0, False]]

    equipment = "Equipment"
    CP = 0
    SP = 0
    EP = 0
    GP = 0
    PP = 0

    wep = ["name", "name", "name", "name", "name", "name"]
    wepAB = [0, 0, 0, 0, 0, 0]
    wepDmg = ["dmg", "dmg", "dmg", "dmg", "dmg", "dmg"]

    ability = [["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"]]

    SA = 0
    SDC = 0
    SAB = 0

    spellSlots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    remainingSpells = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numOfSpells = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    defaultSpell = "Spell"
    spells = [["Spell"],["Spell"],["Spell"],["Spell"],["Spell"],["Spell"],["Spell"],["Spell"],["Spell"],["Spell"]]

    characters = []
    characters2 = []
    charNames = []
    
    def __init__(self):
        if(self.clss != ""):
            self.hitDice = "d" + str(self.healthVals[self.clss][1])
        
        file = open("SaveFile.txt", "r")
        count = 0
        for line in file:
            count += 1
        self.savePos = count
        file.close()

    def store(self):
        self.updateProfs()
        self.updateST()
        
        nameText = self.name + "*#|@&"
        hpText = str(self.hp) + "*#|@&"
        raceText = self.race + "*#|@&"
        clssText = self.clss + "*#|@&"
        statsText = str(self.stats[0]) + " " + str(self.stats[1]) + " " +str(
            self.stats[2]) + " " + str(self.stats[3]) + " " + str(
            self.stats[4]) + " " + str(self.stats[5]) + "*#|@&"
        levelText = str(self.level) + "*#|@&"
        expText = str(self.exp) + "*#|@&"

        tBackground = self.background.replace("\n", "%|&#")
        backgroundText = tBackground + "*#|@&"

        tPersonality = self.personality.replace("\n", "%|&#")
        personalityText = tPersonality + "*#|@&"

        tIdeals = self.ideals.replace("\n", "%|&#")
        idealsText = tIdeals + "*#|@&"

        tBonds = self.bonds.replace("\n", "%|&#")
        bondsText = tBonds + "*#|@&"

        tFlaws = self.flaws.replace("\n", "%|&#")
        flawsText = tFlaws + "*#|@&"

        tAlignment = self.alignment.replace("\n", "%|&#")
        alignmentText = tAlignment + "*#|@&"

        tBackstory = self.backstory.replace("\n", "%|&#")
        backstoryText = tBackstory + "*#|@&"

        tOp = self.op.replace("\n", "%|&#")
        opText = tOp + "*#|@&"
        
        inspText = str(self.insp) + "*#|@&"
        acText = str(self.ac) + "*#|@&"
        speedText = str(self.speed) + "*#|@&"
        curHpText = str(self.curHp) + "*#|@&"
        tempHpText = str(self.tempHp) + "*#|@&"
        initText = str(self.initiative) + "*#|@&"
        savesText = str(self.saves[0]) + " " + str(self.saves[1]) + " " + str(self.saves[2]) + "*#|@&"
        failsText = str(self.fails[0]) + " " + str(self.fails[1]) + " " + str(self.fails[2]) + "*#|@&"
        profBText = str(self.profB) + "*#|@&"
        profsText = str(self.profs[0][0]) + " " + str(self.profs[0][1]) + " " + \
                        str(self.profs[1][0]) + " " + str(self.profs[1][1]) + " " + \
                        str(self.profs[2][0]) + " " + str(self.profs[2][1]) + " " + \
                        str(self.profs[3][0]) + " " + str(self.profs[3][1]) + " " + \
                        str(self.profs[4][0]) + " " + str(self.profs[4][1]) + " " + \
                        str(self.profs[5][0]) + " " + str(self.profs[5][1]) + " " + \
                        str(self.profs[6][0]) + " " + str(self.profs[6][1]) + " " + \
                        str(self.profs[7][0]) + " " + str(self.profs[7][1]) + " " + \
                        str(self.profs[8][0]) + " " + str(self.profs[8][1]) + " " + \
                        str(self.profs[9][0]) + " " + str(self.profs[9][1]) + " " + \
                        str(self.profs[10][0]) + " " + str(self.profs[10][1]) + " " + \
                        str(self.profs[11][0]) + " " + str(self.profs[11][1]) + " " + \
                        str(self.profs[12][0]) + " " + str(self.profs[12][1]) + " " + \
                        str(self.profs[13][0]) + " " + str(self.profs[13][1]) + " " + \
                        str(self.profs[14][0]) + " " + str(self.profs[14][1]) + " " + \
                        str(self.profs[15][0]) + " " + str(self.profs[15][1]) + " " + \
                        str(self.profs[16][0]) + " " + str(self.profs[16][1]) + " " + \
                        str(self.profs[17][0]) + " " + str(self.profs[17][1]) + "*#|@&"
        stText = str(self.st[0][0]) + " " + str(self.st[0][1]) + " " + \
                        str(self.st[1][0]) + " " + str(self.st[1][1]) + " " + \
                        str(self.st[2][0]) + " " + str(self.st[2][1]) + " " + \
                        str(self.st[3][0]) + " " + str(self.st[3][1]) + " " + \
                        str(self.st[4][0]) + " " + str(self.st[4][1]) + " " + \
                        str(self.st[5][0]) + " " + str(self.st[5][1]) + "*#|@&"
        equipmentText = self.equipment.replace("\n", "|*!&^") + "*#|@&"
        cpText = str(self.CP) + "*#|@&"
        spText = str(self.SP) + "*#|@&"
        epText = str(self.EP) + "*#|@&"
        gpText = str(self.GP) + "*#|@&"
        ppText = str(self.PP) + "*#|@&"

        tWep = ["name", "name", "name", "name", "name", "name"]
        for i in range(len(self.wep)):
            tWep[i] = self.wep[i].replace("%|&#", "\n")
        
        wepText = tWep[0] + "|!^" + tWep[1] + "|!^" + tWep[2] + "|!^" + tWep[3] + "|!^" + \
                  tWep[4] + "|!^" + tWep[5] + "*#|@&"
        wepABText = str(self.wepAB[0]) + " " + str(self.wepAB[1]) + " " + str(self.wepAB[2]) + " " + \
                    str(self.wepAB[3]) + " " + str(self.wepAB[4]) + " " + str(self.wepAB[5]) + "*#|@&"

        tWepDmg = ["dmg", "dmg", "dmg", "dmg", "dmg", "dmg"]
        for i in range(len(self.wepDmg)):
            tWepDmg[i] = self.wepDmg[i].replace("%|&#", "\n")
        
        wepDmgText = tWepDmg[0] + "|!%" + tWepDmg[1] + "|!%" + tWepDmg[2] + "|!%" + tWepDmg[3] + "|!%" + \
                     tWepDmg[4] + "|!%" + tWepDmg[5] + "*#|@&"

        tAbility = [["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"]]
        for i in range(len(self.ability)):
            for j in range(len(self.ability[i])):
                           tAbility[i][j] = self.ability[i][j].replace("\n", "%|&#")
                           
        abilityText = tAbility[0][0] + "|^&" + tAbility[0][1] + " " + tAbility[1][0] + "|^&" + tAbility[1][1] + \
                      " " + tAbility[2][0] + "|^&" + tAbility[2][1] + " " + tAbility[3][0] + "|^&" + tAbility[3][1] + \
                      " " + tAbility[4][0] + "|^&" + tAbility[4][1] + " " + tAbility[5][0] + "|^&" + tAbility[5][1] + \
                      " " + tAbility[6][0] + "|^&" + tAbility[6][1] + " " + tAbility[7][0] + "|^&" + tAbility[7][1] + \
                      " " + tAbility[8][0] + "|^&" + tAbility[8][1] + " " + tAbility[9][0] + "|^&" + tAbility[9][1] + "*#|@&"
        SAText = str(self.SA) + "*#|@&"
        SDCText = str(self.SDC) + "*#|@&"
        SABText = str(self.SAB) + "*#|@&"
        spellSlotsText = str(self.spellSlots[0]) + " " + str(self.spellSlots[1]) + " " + str(self.spellSlots[2]) + " " + str(self.spellSlots[3]) + " " + \
                         str(self.spellSlots[4]) + " " + str(self.spellSlots[5]) + " " + str(self.spellSlots[6]) + " " + str(self.spellSlots[7]) + " " + \
                         str(self.spellSlots[8]) + " " + str(self.spellSlots[9]) + "*#|@&"
        remSpellsText = str(self.remainingSpells[0]) + " " + str(self.remainingSpells[1]) + " " + str(self.remainingSpells[2]) + " " + str(self.remainingSpells[3]) + " " + \
                         str(self.remainingSpells[4]) + " " + str(self.remainingSpells[5]) + " " + str(self.remainingSpells[6]) + " " + str(self.remainingSpells[7]) + " " + \
                         str(self.remainingSpells[8]) + " " + str(self.remainingSpells[9]) + "*#|@&"
        numOfSpellsText = str(self.numOfSpells[0]) + " " + str(self.numOfSpells[1]) + " " + str(self.numOfSpells[2]) + " " + str(self.numOfSpells[3]) + " " + \
                          str(self.numOfSpells[4]) + " " + str(self.numOfSpells[5]) + " " + str(self.numOfSpells[6]) + " " + str(self.numOfSpells[7]) + " " + \
                          str(self.numOfSpells[8]) + " " + str(self.numOfSpells[9]) + "*#|@&" 
        spellsText = ""
        for i in range(len(self.spells)):
            for j in range(len(self.spells[i])):
                spellsText += self.spells[i][j].replace("\n", "%|&#")
                if (j + 1 < len(self.spells[i])):
                    spellsText += "|$^@"
            if (i + 1 < len(self.spells)):
                spellsText += "|#%@"

        file = open("SaveFile.txt", "a")
        if(self.savePos > 0):
            file.write("\n")
            
        file.write(nameText)
        file.write(hpText)
        file.write(raceText)
        file.write(clssText)
        file.write(statsText)
        file.write(levelText)
        file.write(expText)
        file.write(backgroundText)
        file.write(personalityText)
        file.write(idealsText)
        file.write(bondsText)
        file.write(flawsText)
        file.write(alignmentText)
        file.write(backstoryText)
        file.write(opText)
        file.write(inspText)
        file.write(acText)
        file.write(speedText)
        file.write(curHpText)
        file.write(tempHpText)
        file.write(initText)
        file.write(savesText)
        file.write(failsText)
        file.write(profBText)
        file.write(profsText)
        file.write(stText)
        file.write(equipmentText)
        file.write(cpText)
        file.write(spText)
        file.write(epText)
        file.write(gpText)
        file.write(ppText)
        file.write(wepText)
        file.write(wepABText)
        file.write(wepDmgText)
        file.write(abilityText)
        file.write(SAText)
        file.write(SDCText)
        file.write(SABText)
        file.write(spellSlotsText)
        file.write(remSpellsText)
        file.write(numOfSpellsText)
        file.write(spellsText)

        file.close()

    def loadChar(self):
        file = open("SaveFile.txt", "r")
        self.characters = []
        self.charNames = []
        self.characters2 = []

        counter = 0
        for line in file:
            self.characters.append(line)
            self.characters2.append(line)
            self.characters[counter] = self.characters[counter].split("*#|@&")
            self.charNames.append(self.characters[counter][0])
            counter += 1
        
        file.close()

    def forceSave(self):
        file = open("SaveFile.txt", "w")

        for i in range(len(self.characters2)):
            if(self.characters2[i] == ""):
                del self.characters2[i]

        for i in range(len(self.characters2)):
            file.write(self.characters2[i])

        file.close()

    def bootChar(self, ind):
        self.savePos = ind
        tempchar = self.characters[ind]
        self.name = tempchar[0]
        self.hp = int(tempchar[1])
        self.race = tempchar[2]
        self.clss = tempchar[3]
        tempStats = tempchar[4]
        self.stats = tempStats.split()
        for i in range(len(self.stats)):
            self.stats[i] = int(self.stats[i])
            
        self.level = int(tempchar[5])
        self.exp = int(tempchar[6])
        
        self.background = tempchar[7].replace("%|&#", "\n")
        self.personality = tempchar[8].replace("%|&#", "\n")
        self.deals = tempchar[9].replace("%|&#", "\n")
        self.bonds = tempchar[10].replace("%|&#", "\n")
        self.flaws = tempchar[11].replace("%|&#", "\n")
        self.alignment = tempchar[12].replace("%|&#", "\n")
        self.backstory = tempchar[13].replace("%|&#", "\n")
        self.op = tempchar[14].replace("%|&#", "\n")

        
        if(tempchar[15] != ""):
            self.insp = int(tempchar[15])
        if(tempchar[16] != ""): 
            self.ac = int(tempchar[16])
        if(tempchar[17] != ""):
            self.speed = int(tempchar[17])
        if(tempchar[18] != ""):
            self.curHp = int(tempchar[18])
        if(tempchar[19] != ""):
            self.tempHp = int(tempchar[19])
        if(tempchar[20] != ""):
            self.initiative = int(tempchar[20])
        tempSaves = tempchar[21]
        self.saves = tempSaves.split()
        for i in range(len(self.saves)):
            self.saves[i] = self.saves[i]

        tempFails = tempchar[22]
        self.fails = tempFails.split()
        for i in range(len(self.fails)):
            self.fails[i] = self.fails[i]

        if(tempchar[23] != ""):
            self.profB = int(tempchar[23])

        tempProfs = tempchar[24]
        tempProfs2 = tempProfs.split()
        j = 0
        for i in range(len(self.profs)):
            if(i != 0 and i % 2 == 0):
                j = i
            if(i != 0):
                k = i % 2
            else:
                k = 0
            
            self.profs[j][k] = tempProfs2[i]

        tempst = tempchar[25]
        tempst2 = tempst.split()
        j = 0
        for i in range(len(self.st)):
            if(i != 0 and i % 2 == 0):
                j = i
            if(i != 0):
                k = i % 2
            else:
                k = 0
            
            self.st[j][k] = tempst2[i]

        self.equipment = tempchar[26].replace("|*!&^", "\n")
        if(tempchar[27] != ""):
            self.CP = int(tempchar[27])
        if(tempchar[28] != ""):
            self.SP = int(tempchar[28])
        if(tempchar[29] != ""):
            self.EP = int(tempchar[29])
        if(tempchar[30] != ""):
            self.GP = int(tempchar[30])
        if(tempchar[31] != ""):
            self.PP = int(tempchar[31])

        tWep = tempchar[32].split("|!^")
        print(tWep)
        for i in range(len(tWep)):
            self.wep[i] = tWep[i].replace("%|&#", "\n")
        
        tempWepAB = tempchar[33].split()
        for i in range(len(self.wepAB)):
            if(tempWepAB[i] != ""):
                self.wepAB[i] = int(tempWepAB[i])

        tWepDmg = tempchar[34].split("|!%")
        for i in range(len(tWepDmg)):
            self.wepDmg[i] = tWepDmg[i].replace("%|&#", "\n")

        tempAbility = tempchar[35].split()
        for i in range(len(tempAbility)):
            self.ability[i] = tempAbility[i].split("|^&")
            for j in range(len(self.ability[i])):
                self.ability[i][j] = self.ability[i][j].replace("%|&#", "\n")

        if(tempchar[36] != ""):
            self.SA = int(tempchar[36])
        if(tempchar[37] != ""):
            self.SDC = int(tempchar[37])
        if(tempchar[38] != ""):
            self.SAB = int(tempchar[38])

        self.spellSlots = tempchar[39].split()
        self.remainingSpells = tempchar[40].split()
        self.numOfSpells = tempchar[41].split()

        tempSpells1 = tempchar[42].replace("%|&#", "\n")
        tempSpells2 = tempSpells1.split("|#%@")
        for i in range(len(tempSpells2)):
            self.spells[i] = tempSpells2[i].split("|$^@")


        self.updateProfs()
            

    def storeExisting(self):
        self.updateProfs()
        self.updateST()
        
        nameText = self.name + "*#|@&"
        hpText = str(self.hp) + "*#|@&"
        raceText = self.race + "*#|@&"
        clssText = self.clss + "*#|@&"
        statsText = str(self.stats[0]) + " " + str(self.stats[1]) + " " +str(
            self.stats[2]) + " " + str(self.stats[3]) + " " + str(
            self.stats[4]) + " " + str(self.stats[5]) + "*#|@&"
        levelText = str(self.level) + "*#|@&"
        expText = str(self.exp) + "*#|@&"

        tBackground = self.background.replace("\n", "%|&#")
        backgroundText = tBackground + "*#|@&"

        tPersonality = self.personality.replace("\n", "%|&#")
        personalityText = tPersonality + "*#|@&"

        tIdeals = self.ideals.replace("\n", "%|&#")
        idealsText = tIdeals + "*#|@&"

        tBonds = self.bonds.replace("\n", "%|&#")
        bondsText = tBonds + "*#|@&"

        tFlaws = self.flaws.replace("\n", "%|&#")
        flawsText = tFlaws + "*#|@&"

        tAlignment = self.alignment.replace("\n", "%|&#")
        alignmentText = tAlignment + "*#|@&"

        tBackstory = self.backstory.replace("\n", "%|&#")
        backstoryText = tBackstory + "*#|@&"

        tOp = self.op.replace("\n", "%|&#")
        opText = tOp + "*#|@&"
        
        inspText = str(self.insp) + "*#|@&"
        acText = str(self.ac) + "*#|@&"
        speedText = str(self.speed) + "*#|@&"
        curHpText = str(self.curHp) + "*#|@&"
        tempHpText = str(self.tempHp) + "*#|@&"
        initText = str(self.initiative) + "*#|@&"
        savesText = str(self.saves[0]) + " " + str(self.saves[1]) + " " + str(self.saves[2]) + "*#|@&"
        failsText = str(self.fails[0]) + " " + str(self.fails[1]) + " " + str(self.fails[2]) + "*#|@&"
        profBText = str(self.profB) + "*#|@&"
        profsText = str(self.profs[0][0]) + " " + str(self.profs[0][1]) + " " + \
                        str(self.profs[1][0]) + " " + str(self.profs[1][1]) + " " + \
                        str(self.profs[2][0]) + " " + str(self.profs[2][1]) + " " + \
                        str(self.profs[3][0]) + " " + str(self.profs[3][1]) + " " + \
                        str(self.profs[4][0]) + " " + str(self.profs[4][1]) + " " + \
                        str(self.profs[5][0]) + " " + str(self.profs[5][1]) + " " + \
                        str(self.profs[6][0]) + " " + str(self.profs[6][1]) + " " + \
                        str(self.profs[7][0]) + " " + str(self.profs[7][1]) + " " + \
                        str(self.profs[8][0]) + " " + str(self.profs[8][1]) + " " + \
                        str(self.profs[9][0]) + " " + str(self.profs[9][1]) + " " + \
                        str(self.profs[10][0]) + " " + str(self.profs[10][1]) + " " + \
                        str(self.profs[11][0]) + " " + str(self.profs[11][1]) + " " + \
                        str(self.profs[12][0]) + " " + str(self.profs[12][1]) + " " + \
                        str(self.profs[13][0]) + " " + str(self.profs[13][1]) + " " + \
                        str(self.profs[14][0]) + " " + str(self.profs[14][1]) + " " + \
                        str(self.profs[15][0]) + " " + str(self.profs[15][1]) + " " + \
                        str(self.profs[16][0]) + " " + str(self.profs[16][1]) + " " + \
                        str(self.profs[17][0]) + " " + str(self.profs[17][1]) + "*#|@&"
        stText = str(self.st[0][0]) + " " + str(self.st[0][1]) + " " + \
                        str(self.st[1][0]) + " " + str(self.st[1][1]) + " " + \
                        str(self.st[2][0]) + " " + str(self.st[2][1]) + " " + \
                        str(self.st[3][0]) + " " + str(self.st[3][1]) + " " + \
                        str(self.st[4][0]) + " " + str(self.st[4][1]) + " " + \
                        str(self.st[5][0]) + " " + str(self.st[5][1]) + "*#|@&"
        equipmentText = self.equipment.replace("\n", "|*!&^") + "*#|@&"
        cpText = str(self.CP) + "*#|@&"
        spText = str(self.SP) + "*#|@&"
        epText = str(self.EP) + "*#|@&"
        gpText = str(self.GP) + "*#|@&"
        ppText = str(self.PP) + "*#|@&"

        tWep = ["name", "name", "name", "name", "name", "name"]
        for i in range(len(self.wep)):
            tWep[i] = self.wep[i].replace("%|&#", "\n")
        
        wepText = tWep[0] + "|!^" + tWep[1] + "|!^" + tWep[2] + "|!^" + tWep[3] + "|!^" + \
                  tWep[4] + "|!^" + tWep[5] + "*#|@&"
        wepABText = str(self.wepAB[0]) + " " + str(self.wepAB[1]) + " " + str(self.wepAB[2]) + " " + \
                    str(self.wepAB[3]) + " " + str(self.wepAB[4]) + " " + str(self.wepAB[5]) + "*#|@&"

        tWepDmg = ["dmg", "dmg", "dmg", "dmg", "dmg", "dmg"]
        for i in range(len(self.wepDmg)):
            tWepDmg[i] = self.wepDmg[i].replace("%|&#", "\n")
        
        wepDmgText = tWepDmg[0] + "|!%" + tWepDmg[1] + "|!%" + tWepDmg[2] + "|!%" + tWepDmg[3] + "|!%" + \
                     tWepDmg[4] + "|!%" + tWepDmg[5] + "*#|@&"

        tAbility = [["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"], ["Ability", "Description"], ["Ability", "Description"],
               ["Ability", "Description"]]
        for i in range(len(self.ability)):
            for j in range(len(self.ability[i])):
                           tAbility[i][j] = self.ability[i][j].replace("\n", "%|&#")
                           
        abilityText = tAbility[0][0] + "|^&" + tAbility[0][1] + " " + tAbility[1][0] + "|^&" + tAbility[1][1] + \
                      " " + tAbility[2][0] + "|^&" + tAbility[2][1] + " " + tAbility[3][0] + "|^&" + tAbility[3][1] + \
                      " " + tAbility[4][0] + "|^&" + tAbility[4][1] + " " + tAbility[5][0] + "|^&" + tAbility[5][1] + \
                      " " + tAbility[6][0] + "|^&" + tAbility[6][1] + " " + tAbility[7][0] + "|^&" + tAbility[7][1] + \
                      " " + tAbility[8][0] + "|^&" + tAbility[8][1] + " " + tAbility[9][0] + "|^&" + tAbility[9][1] + "*#|@&"
        SAText = str(self.SA) + "*#|@&"
        SDCText = str(self.SDC) + "*#|@&"
        SABText = str(self.SAB) + "*#|@&"
        spellSlotsText = str(self.spellSlots[0]) + " " + str(self.spellSlots[1]) + " " + str(self.spellSlots[2]) + " " + str(self.spellSlots[3]) + " " + \
                         str(self.spellSlots[4]) + " " + str(self.spellSlots[5]) + " " + str(self.spellSlots[6]) + " " + str(self.spellSlots[7]) + " " + \
                         str(self.spellSlots[8]) + " " + str(self.spellSlots[9]) + "*#|@&"
        remSpellsText = str(self.remainingSpells[0]) + " " + str(self.remainingSpells[1]) + " " + str(self.remainingSpells[2]) + " " + str(self.remainingSpells[3]) + " " + \
                         str(self.remainingSpells[4]) + " " + str(self.remainingSpells[5]) + " " + str(self.remainingSpells[6]) + " " + str(self.remainingSpells[7]) + " " + \
                         str(self.remainingSpells[8]) + " " + str(self.remainingSpells[9]) + "*#|@&"
        numOfSpellsText = str(self.numOfSpells[0]) + " " + str(self.numOfSpells[1]) + " " + str(self.numOfSpells[2]) + " " + str(self.numOfSpells[3]) + " " + \
                          str(self.numOfSpells[4]) + " " + str(self.numOfSpells[5]) + " " + str(self.numOfSpells[6]) + " " + str(self.numOfSpells[7]) + " " + \
                          str(self.numOfSpells[8]) + " " + str(self.numOfSpells[9]) + "*#|@&"  
        spellsText = ""
        for i in range(len(self.spells)):
            for j in range(len(self.spells[i])):
                spellsText += self.spells[i][j].replace("\n", "%|&#")
                if (j + 1 < len(self.spells[i])):
                    spellsText += "|$^@"
            if (i + 1 < len(self.spells)):
                spellsText += "|#%@"

        self.loadChar()
        
        file = open("SaveFile.txt", "w")
        
        for count in range(0, len(self.characters)):
            if(count != self.savePos):
                file.write(str(self.characters2[count]))
            else:
                file.write(nameText)
                file.write(hpText)
                file.write(raceText)
                file.write(clssText)
                file.write(statsText)
                file.write(levelText)
                file.write(expText)
                file.write(backgroundText)
                file.write(personalityText)
                file.write(idealsText)
                file.write(bondsText)
                file.write(flawsText)
                file.write(alignmentText)
                file.write(backstoryText)
                file.write(opText)
                file.write(inspText)
                file.write(acText)
                file.write(speedText)
                file.write(curHpText)
                file.write(tempHpText)
                file.write(initText)
                file.write(savesText)
                file.write(failsText)
                file.write(profBText)
                file.write(profsText)
                file.write(stText)
                file.write(equipmentText)
                file.write(cpText)
                file.write(spText)
                file.write(epText)
                file.write(gpText)
                file.write(ppText)
                file.write(wepText)
                file.write(wepABText)
                file.write(wepDmgText)
                file.write(abilityText)
                file.write(SAText)
                file.write(SDCText)
                file.write(SABText)
                file.write(spellSlotsText)
                file.write(remSpellsText)
                file.write(numOfSpellsText)
                file.write(spellsText)

        file.close()
            
    def setBaseHp(self):
        self.hp = ((self.healthVals[self.clss][1]) + int((self.stats[3] - 10) / 2))
    
    def hpAddRoll(self):
        cModifier = int((self.stats[3] - 10) / 2)
        self.hp += cModifier
            
        roll = random.randint(1, self.healthVals[self.clss][1])
        self.hp += roll
            
    def hpAddBasic(self):
        cModifier = int((self.stats[3] - 10) / 2)
        self.hp += cModifier

        self.hp += self.healthVals[self.clss][0]

    #////////////////////////////////LEVELS/////////////////////////////////////////

    def setLevel(self):
        i = 0
        tLevel = 0
        while(self.exp >= levelReq[i]): #loop until exp is < level requirment 
            tLevel = i + 1
            i+= 1
        self.level = tLevel

    #////////////////////////////Prof/ST Mods//////////////////////////////////////

    def updateProfs(self):
        for i in range(len(self.profs)):
            temp = int((self.stats[profEffectedBy[i]] - 10) / 2)
            if("True" == self.profs[i][1]):
                temp += int(self.profB)
                
            self.profs[i][0] = temp

    def updateST(self):
        for i in range(len(self.st)):
            temp = int((self.stats[i] - 10) / 2)
            if("True" == self.st[i][1]):
                temp += int(self.profB)
                
            self.st[i][0] = temp
