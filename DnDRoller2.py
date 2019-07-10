import random
import kivy
import ExistingCharacter
import DnDRollerChar
from DnDRollerChar import sheet
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.uix.popup import Popup

from kivmob import KivMob, TestIds

#Grid/main class
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        Window.clearcolor = (1/255,7/255,88/255, 1)
        
        self.character = sheet()
        self.ind = self.character.savePos

        self.title = Label(text = "[color=ffffff]DMpad's D&D Roller",
                           markup = True)
        self.add_widget(self.title)

        self.roller = Button(text = "[color=ffffff]Create a new character", markup = True)
        self.roller.bind(on_press = self.loadRoller)
        self.add_widget(self.roller)

        self.load = Button(text = "[color=ffffff]Load an existing character", markup = True)
        self.load.bind(on_press = self.charList)
        self.add_widget(self.load)

    def loadRoller(self, instance): #loads character builder's initial state
        self.remove_widget(self.title)
        self.remove_widget(self.roller)
        self.remove_widget(self.load)

        self.cExpands = [True, True, True]
        self.rExpands = [True, True, True, True, True, True, True, True]

        self.enterVal = GridLayout()
        self.enterVal.cols = 2
        self.add_widget(self.enterVal)

        self.yn = GridLayout()
        self.yn.cols = 3

        self.raceGrid = GridLayout()
        self.raceGrid.rows = 5

        self.askRandoY(instance)

        self.add_widget(self.yn)
        self.add_widget(self.raceGrid)

    def charList(self, instance):
        self.loadChar = GridLayout()
        self.loadChar.cols = 2

        self.add_widget(self.loadChar)
        
        self.character.loadChar()
        
        self.remove_widget(self.title)
        self.remove_widget(self.roller)
        self.remove_widget(self.load)

        self.title = Label(text = "[color=ffffff]Characters", markup = True)
        self.add_widget(self.title)

        count = 0
        self.charDel = []
        for i in self.character.charNames: #create a unique button for each saved character
            self.tempChar = Button(text = "[color=ffffff]" + i,
                                   markup = True)
            self.tempChar.bind(on_press = self.displayChar)
            self.loadChar.add_widget(self.tempChar)

            self.charDel.append(Button(text = "[color=ffffff]Delete " + i,
                                   markup = True))
            self.charDel[count].bind(on_press = self.deletePopup)
            self.loadChar.add_widget(self.charDel[count])
            print(self.charDel[count])
            count += 1

        self.menuBtn = Button(text = "[color=ffffff]Return to Menu",
                                   markup = True)
        self.menuBtn.bind(on_press = self.returnToMenu)
        self.add_widget(self.menuBtn)

    def returnToMenu(self, instance):
        self.clear_widgets()
        self.__init__()

    def displayChar(self, instance):
        temp = instance.text.split("]")
        temp2 = temp[1]
        self.ind = self.character.charNames.index(temp2)
                
        self.clear_widgets()
        ExistingCharacter.Scene1.manager(self.ind)

    def deleteChar(self, instance):
        temp = self.character.characters2.pop(self.ind)
        self.character.forceSave()
        self.delPopup.dismiss()
        self.clear_widgets()
        self.charList(instance)

    def deletePopup(self, instance):                
        self.bye = instance.text.split()
        self.ind = self.character.charNames.index(self.bye[1])

        self.popupGrid = GridLayout(size_hint_y=None)
        self.popupGrid.cols = 1
        self.popupBtns = GridLayout(size_hint_y=None)
        self.popupBtns.cols = 2

        self.delPopup = Popup(title='Delete', size_hint=(None, None),
                                      size=(250, 250))

        self.delTitle = Label(text = "[color=ffffff]Are you sure you want to delete " + self.bye[1] + "?",
                                       markup = True, size_hint_y = None, height = 20)

        self.keep = Button(text = "[color=ffffff]Keep",
                                     markup = True, size_hint_y = None, height = 20)
        self.keep.bind(on_press = self.delPopup.dismiss)
        
        self.delC = Button(text = "[color=ffffff]Delete",
                                     markup = True, size_hint_y = None, height = 20)
        self.delC.bind(on_press = self.deleteChar)

        self.delPopup.add_widget(self.popupGrid)
        self.popupGrid.add_widget(self.delTitle)
        self.popupGrid.add_widget(self.popupBtns)
        self.popupBtns.add_widget(self.keep)
        self.popupBtns.add_widget(self.delC)
        
        self.delPopup.open()

#//////////////////////////////////////STATS///////////////////////////////////////

    def askRandoY(self, instance): #randomize anything yes
        self.randoSome = Label(text = "[color=ffffff]Randomize stats?", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askStatsY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askStatsN)
        self.yn.add_widget(self.randoN)

        self.randoM = Button(text = "[color=ffffff]No, manualy input stats", markup = True)
        self.randoM.bind(on_press = self.manualStats)
        self.yn.add_widget(self.randoM)

    def askStatsY(self, instance): #randomize stats yes
        rolls = []
        for i in range(6):
            r = []
            r.append(random.randint(1,6))
            r.append(random.randint(1,6))
            r.append(random.randint(1,6))
            r.append(random.randint(1,6))
            r.sort()
            r.pop(0)
            rolls.append(r[0] + r[1] + r[2])

        self.character.stats = rolls
        print(self.character.stats)

        self.askStatPlace(instance)

    def askStatsN(self, instance): #randomize stats no
        self.character.stats = [15,14,13,12,10,8]
        print(self.character.stats)
        self.askStatPlace(instance)

#******************Manual stat input********************************************

    def manualStats(self, instance):
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        self.yn.remove_widget(self.randoM)
        
        self.manualStr = Label(text ="[color=ffffff]Strength: ", markup = True)
        self.enterVal.add_widget(self.manualStr)
        self.tStr = TextInput(multiline = False)
        self.enterVal.add_widget(self.tStr)

        self.manualDex = Label(text ="[color=ffffff]Dexterity: ", markup = True)
        self.enterVal.add_widget(self.manualDex)
        self.tDex = TextInput(multiline = False)
        self.enterVal.add_widget(self.tDex)

        self.manualCon = Label(text ="[color=ffffff]Constitution: ", markup = True)
        self.enterVal.add_widget(self.manualCon)
        self.tCon = TextInput(multiline = False)
        self.enterVal.add_widget(self.tCon)

        self.manualInt = Label(text ="[color=ffffff]Intelegence: ", markup = True)
        self.enterVal.add_widget(self.manualInt)
        self.tInt = TextInput(multiline = False)
        self.enterVal.add_widget(self.tInt)

        self.manualWis = Label(text ="[color=ffffff]Wisdom: ", markup = True)
        self.enterVal.add_widget(self.manualWis)
        self.tWis = TextInput(multiline = False)
        self.enterVal.add_widget(self.tWis)

        self.manualChar = Label(text ="[color=ffffff]Charisma: ", markup = True)
        self.enterVal.add_widget(self.manualChar)
        self.tChar = TextInput(multiline = False)
        self.enterVal.add_widget(self.tChar)

        self.randoY = Button(text = "[color=ffffff]Confirm Stats", markup = True)
        self.randoY.bind(on_press = self.confirmStats)
        self.yn.add_widget(self.randoY)

    def confirmStats(self, instance):
        tempStr = self.tStr.text
        tempDex = self.tDex.text
        tempCon = self.tCon.text
        tempInt = self.tInt.text
        tempWis = self.tWis.text
        tempChar = self.tChar.text
        rolls = []
        good = False
        if(tempStr.isdigit() and int(tempStr) >= 0 and int(tempStr) <= 20):
            if(tempDex.isdigit() and int(tempDex) >= 0 and int(tempDex) <= 20):
                if(tempCon.isdigit() and int(tempCon) >= 0 and int(tempCon) <= 20):
                    if(tempInt.isdigit() and int(tempInt) >= 0 and int(tempInt) <= 20):
                        if(tempWis.isdigit() and int(tempWis) >= 0 and int(tempWis) <= 20):
                            if(tempChar.isdigit() and int(tempChar) >= 0 and int(tempChar) <= 20):
                                good = True
        if(good == True):
            rolls.append(int(tempStr))
            rolls.append(int(tempDex))
            rolls.append(int(tempCon))
            rolls.append(int(tempInt))
            rolls.append(int(tempWis))
            rolls.append(int(tempChar))
            self.character.stats = rolls

            self.enterVal.remove_widget(self.manualStr)
            self.enterVal.remove_widget(self.tStr)
            self.enterVal.remove_widget(self.manualDex)
            self.enterVal.remove_widget(self.tDex)
            self.enterVal.remove_widget(self.manualCon)
            self.enterVal.remove_widget(self.tCon)
            self.enterVal.remove_widget(self.manualInt)
            self.enterVal.remove_widget(self.tInt)
            self.enterVal.remove_widget(self.manualWis)
            self.enterVal.remove_widget(self.tWis)
            self.enterVal.remove_widget(self.manualChar)
            self.enterVal.remove_widget(self.tChar)

            self.askClass(instance)
        else:
            pass #popup warning to give a valid integer from 0-20

#****************Malual stat placement******************************************

    def askStatPlace(self, instance): #ask about placing values with specific stats
        self.display1 = Label(text = "[color=ffffff]Stats (str, dex, con, int," +
                              " wis, char): " + str(self.character.stats),
                              markup = True) #display stats
        self.add_widget(self.display1)

        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        self.yn.remove_widget(self.randoM)
        
        self.randoSome = Label(text = "[color=ffffff]Place stats in a different order?", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askSPlaceY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askClass)
        self.yn.add_widget(self.randoN)
        
#************************Strength Change***************************************
        
    def askSPlaceY(self, instance): #ask about placing value in str
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Strength?", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]" + str(self.character.stats[0]), markup = True)
        self.randoY.bind(on_press = self.askSPDex)
        self.yn.add_widget(self.randoY)

        self.randoY1 = Button(text = "[color=ffffff]" + str(self.character.stats[1]), markup = True)
        self.randoY1.bind(on_press = self.str1)
        self.yn.add_widget(self.randoY1)

        self.randoY2 = Button(text = "[color=ffffff]" + str(self.character.stats[2]), markup = True)
        self.randoY2.bind(on_press = self.str2)
        self.yn.add_widget(self.randoY2)

        self.randoY3 = Button(text = "[color=ffffff]" + str(self.character.stats[3]), markup = True)
        self.randoY3.bind(on_press = self.str3)
        self.yn.add_widget(self.randoY3)

        self.randoY4 = Button(text = "[color=ffffff]" + str(self.character.stats[4]), markup = True)
        self.randoY4.bind(on_press = self.str4)
        self.yn.add_widget(self.randoY4)

        self.randoY5 = Button(text = "[color=ffffff]" + str(self.character.stats[5]), markup = True)
        self.randoY5.bind(on_press = self.str5)
        self.yn.add_widget(self.randoY5)

    def str1(self, instance):
        temp = self.character.stats[0] #store original str value
        self.character.stats[0] = self.character.stats[1] #place new str value
        self.character.stats[1] = temp #place old str value in the swapped place
        self.askSPDex(instance)

    def str2(self, instance):
        temp = self.character.stats[0] #store original str value
        self.character.stats[0] = self.character.stats[2] #place new str value
        self.character.stats[2] = temp #place old str value in the swapped place
        self.askSPDex(instance)

    def str3(self, instance):
        temp = self.character.stats[0] #store original str value
        self.character.stats[0] = self.character.stats[3] #place new str value
        self.character.stats[3] = temp #place old str value in the swapped place
        self.askSPDex(instance)

    def str4(self, instance):
        temp = self.character.stats[0] #store original str value
        self.character.stats[0] = self.character.stats[4] #place new str value
        self.character.stats[4] = temp #place old str value in the swapped place
        self.askSPDex(instance)

    def str5(self, instance):
        temp = self.character.stats[0] #store original str value
        self.character.stats[0] = self.character.stats[5] #place new str value
        self.character.stats[5] = temp #place old str value in the swapped place
        self.askSPDex(instance)
        
#************************Dexterity Change**************************************
        
    def askSPDex(self, instance): #ask about placing value in Dex
        self.remove_widget(self.display1)
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoY1)
        self.yn.remove_widget(self.randoY2)
        self.yn.remove_widget(self.randoY3)
        self.yn.remove_widget(self.randoY4)
        self.yn.remove_widget(self.randoY5)

        self.display1 = Label(text = "[color=ffffff]Stats (str, dex, con, int," +
                              " wis, char): " + str(self.character.stats),
                              markup = True) #display stats
        self.add_widget(self.display1)
        
        self.randoSome = Label(text = "[color=ffffff]Dexterity?", markup = True)
        self.yn.add_widget(self.randoSome)

        self.randoY = Button(text = "[color=ffffff]" + str(self.character.stats[1]), markup = True)
        self.randoY.bind(on_press = self.askSPCon)
        self.yn.add_widget(self.randoY)

        self.randoY2 = Button(text = "[color=ffffff]" + str(self.character.stats[2]), markup = True)
        self.randoY2.bind(on_press = self.dex2)
        self.yn.add_widget(self.randoY2)

        self.randoY3 = Button(text = "[color=ffffff]" + str(self.character.stats[3]), markup = True)
        self.randoY3.bind(on_press = self.dex3)
        self.yn.add_widget(self.randoY3)

        self.randoY4 = Button(text = "[color=ffffff]" + str(self.character.stats[4]), markup = True)
        self.randoY4.bind(on_press = self.dex4)
        self.yn.add_widget(self.randoY4)

        self.randoY5 = Button(text = "[color=ffffff]" + str(self.character.stats[5]), markup = True)
        self.randoY5.bind(on_press = self.dex5)
        self.yn.add_widget(self.randoY5)

    def dex2(self, instance):
        temp = self.character.stats[1] #store original dex value
        self.character.stats[1] = self.character.stats[2] #place new dex value
        self.character.stats[2] = temp #place old dex value in the swapped place
        self.askSPCon(instance)

    def dex3(self, instance):
        temp = self.character.stats[1] #store original dex value
        self.character.stats[1] = self.character.stats[3] #place new dex value
        self.character.stats[3] = temp #place old dex value in the swapped place
        self.askSPCon(instance)

    def dex4(self, instance):
        temp = self.character.stats[1] #store original dex value
        self.character.stats[1] = self.character.stats[4] #place new dex value
        self.character.stats[4] = temp #place old dex value in the swapped place
        self.askSPCon(instance)

    def dex5(self, instance):
        temp = self.character.stats[1] #store original dex value
        self.character.stats[1] = self.character.stats[5] #place new dex value
        self.character.stats[5] = temp #place old dex value in the swapped place
        self.askSPCon(instance)
        
#************************Constitution Change***********************************
        
    def askSPCon(self, instance): #ask about placing value in Con
        self.remove_widget(self.display1)
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoY2)
        self.yn.remove_widget(self.randoY3)
        self.yn.remove_widget(self.randoY4)
        self.yn.remove_widget(self.randoY5)

        self.display1 = Label(text = "[color=ffffff]Stats (str, dex, con, int," +
                              " wis, char): " + str(self.character.stats),
                              markup = True) #display stats
        self.add_widget(self.display1)

        self.randoSome = Label(text = "[color=ffffff]Constitution?", markup = True)
        self.yn.add_widget(self.randoSome)

        self.randoY = Button(text = "[color=ffffff]" + str(self.character.stats[2]), markup = True)
        self.randoY.bind(on_press = self.askSPInt)
        self.yn.add_widget(self.randoY)

        self.randoY3 = Button(text = "[color=ffffff]" + str(self.character.stats[3]), markup = True)
        self.randoY3.bind(on_press = self.con3)
        self.yn.add_widget(self.randoY3)

        self.randoY4 = Button(text = "[color=ffffff]" + str(self.character.stats[4]), markup = True)
        self.randoY4.bind(on_press = self.con4)
        self.yn.add_widget(self.randoY4)

        self.randoY5 = Button(text = "[color=ffffff]" + str(self.character.stats[5]), markup = True)
        self.randoY5.bind(on_press = self.con5)
        self.yn.add_widget(self.randoY5)

    def con3(self, instance):
        temp = self.character.stats[2] #store original con value
        self.character.stats[2] = self.character.stats[3] #place new con value
        self.character.stats[3] = temp #place old con value in the swapped place
        self.askSPInt(instance)

    def con4(self, instance):
        temp = self.character.stats[2] #store original con value
        self.character.stats[2] = self.character.stats[4] #place new con value
        self.character.stats[4] = temp #place old con value in the swapped place
        self.askSPInt(instance)

    def con5(self, instance):
        temp = self.character.stats[2] #store original con value
        self.character.stats[2] = self.character.stats[5] #place new con value
        self.character.stats[5] = temp #place old con value in the swapped place
        self.askSPInt(instance)
        
#************************Intelegence Change************************************
        
    def askSPInt(self, instance): #ask about placing value in Int
        self.remove_widget(self.display1)
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoY3)
        self.yn.remove_widget(self.randoY4)
        self.yn.remove_widget(self.randoY5)

        self.display1 = Label(text = "[color=ffffff]Stats (str, dex, con, int," +
                              " wis, char): " + str(self.character.stats),
                              markup = True) #display stats
        self.add_widget(self.display1)

        self.randoSome = Label(text = "[color=ffffff]Intelegence?", markup = True)
        self.yn.add_widget(self.randoSome)

        self.randoY = Button(text = "[color=ffffff]" + str(self.character.stats[3]), markup = True)
        self.randoY.bind(on_press = self.askSPWis)
        self.yn.add_widget(self.randoY)

        self.randoY4 = Button(text = "[color=ffffff]" + str(self.character.stats[4]), markup = True)
        self.randoY4.bind(on_press = self.int4)
        self.yn.add_widget(self.randoY4)

        self.randoY5 = Button(text = "[color=ffffff]" + str(self.character.stats[5]), markup = True)
        self.randoY5.bind(on_press = self.int5)
        self.yn.add_widget(self.randoY5)

    def int4(self, instance):
        temp = self.character.stats[3] #store original int value
        self.character.stats[3] = self.character.stats[4] #place new int value
        self.character.stats[4] = temp #place old int value in the swapped place
        self.askSPWis(instance)

    def int5(self, instance):
        temp = self.character.stats[3] #store original int value
        self.character.stats[3] = self.character.stats[5] #place new int value
        self.character.stats[5] = temp #place old int value in the swapped place
        self.askSPWis(instance)
        
#************************Wisdom Change****************************************
        
    def askSPWis(self, instance): #ask about placing value in Wis
        self.remove_widget(self.display1)
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoY4)
        self.yn.remove_widget(self.randoY5)

        self.display1 = Label(text = "[color=ffffff]Stats (str, dex, con, int," +
                              " wis, char): " + str(self.character.stats),
                              markup = True) #display stats
        self.add_widget(self.display1)
        
        self.randoSome = Label(text = "[color=ffffff]Wisdom?", markup = True)
        self.yn.add_widget(self.randoSome)

        self.randoY = Button(text = "[color=ffffff]" + str(self.character.stats[4]), markup = True)
        self.randoY.bind(on_press = self.cleanup0)
        self.yn.add_widget(self.randoY)

        self.randoY5 = Button(text = "[color=ffffff]" + str(self.character.stats[5]), markup = True)
        self.randoY5.bind(on_press = self.wis5)
        self.yn.add_widget(self.randoY5)

    def wis5(self, instance):
        temp = self.character.stats[4] #store original wis value
        self.character.stats[4] = self.character.stats[5] #place new wis value
        self.character.stats[5] = temp #place old wis value in the swapped place

        cleanup0(instance)

    def cleanup0(self, instance):
        self.remove_widget(self.display1)
        self.yn.remove_widget(self.randoY4)
        self.yn.remove_widget(self.randoY5)
        self.askClass(instance)

#///////////////////////////////////CLASS///////////////////////////////////////

    def askClass(self, instance): #ask about class randomization
        self.remove_widget(self.display1)

        self.display1 = Label(text = "[color=ffffff]Stats (str, dex, con, int," +
                              " wis, char): " + str(self.character.stats),
                              markup = True) #display stats
        self.add_widget(self.display1)

        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        self.yn.remove_widget(self.randoM)
        
        self.randoSome = Label(text = "[color=ffffff]Randomize Class?", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askClassY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askClassN)
        self.yn.add_widget(self.randoN)

    def askClassY(self, instance): #randomize class yes
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use all expansions??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.clssRando)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askCExpandN)
        self.yn.add_widget(self.randoN)

#***************Manual Class Select********************************************

    def askClassN(self, instance): #randomize class no
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)

        self.randoSome = Label(text = "[color=ffffff]Which class?", markup = True)
        self.yn.add_widget(self.randoSome)
        
        self.rando1 = Button(text = "[color=ffffff]Barbarian", markup = True)
        self.rando1.bind(on_press = self.selectBarbarian)
        self.yn.add_widget(self.rando1)

        self.rando2 = Button(text = "[color=ffffff]Bard", markup = True)
        self.rando2.bind(on_press = self.selectBard)
        self.yn.add_widget(self.rando2)

        self.rando3 = Button(text = "[color=ffffff]Cleric", markup = True)
        self.rando3.bind(on_press = self.selectCleric)
        self.yn.add_widget(self.rando3)

        self.rando4 = Button(text = "[color=ffffff]Druid", markup = True)
        self.rando4.bind(on_press = self.selectDruid)
        self.yn.add_widget(self.rando4)

        self.rando5 = Button(text = "[color=ffffff]Fighter", markup = True)
        self.rando5.bind(on_press = self.selectFighter)
        self.yn.add_widget(self.rando5)

        self.rando6 = Button(text = "[color=ffffff]Monk", markup = True)
        self.rando6.bind(on_press = self.selectMonk)
        self.yn.add_widget(self.rando6)

        self.rando7 = Button(text = "[color=ffffff]Paladin", markup = True)
        self.rando7.bind(on_press = self.selectPaladin)
        self.yn.add_widget(self.rando7)

        self.rando8 = Button(text = "[color=ffffff]Ranger", markup = True)
        self.rando8.bind(on_press = self.selectRanger)
        self.yn.add_widget(self.rando8)

        self.rando9 = Button(text = "[color=ffffff]Rogue", markup = True)
        self.rando9.bind(on_press = self.selectRogue)
        self.yn.add_widget(self.rando9)

        self.rando10 = Button(text = "[color=ffffff]Sorcerer", markup = True)
        self.rando10.bind(on_press = self.selectSorcerer)
        self.yn.add_widget(self.rando10)

        self.rando11 = Button(text = "[color=ffffff]Warlock", markup = True)
        self.rando11.bind(on_press = self.selectWarlock)
        self.yn.add_widget(self.rando11)

        self.rando12 = Button(text = "[color=ffffff]Wizard", markup = True)
        self.rando12.bind(on_press = self.selectWizard)
        self.yn.add_widget(self.rando12)

        self.rando13 = Button(text = "[color=ffffff]Artificer", markup = True)
        self.rando13.bind(on_press = self.selectArtificer)
        self.yn.add_widget(self.rando13)

        self.rando14 = Button(text = "[color=ffffff]Blood Hunter", markup = True)
        self.rando14.bind(on_press = self.selectBloodHunter)
        self.yn.add_widget(self.rando14)

    def selectBarbarian(self, instance):
        self.character.clss = "Barbarian"
        self.cleanup1(instance)

    def selectBard(self, instance):
        self.character.clss = "Bard"
        self.cleanup1(instance)

    def selectCleric(self, instance):
        self.character.clss = "Cleric"
        self.cleanup1(instance)

    def selectDruid(self, instance):
        self.character.clss = "Druid"
        self.cleanup1(instance)

    def selectFighter(self, instance):
        self.character.clss = "Fighter"
        self.cleanup1(instance)

    def selectMonk(self, instance):
        self.character.clss = "Monk"
        self.cleanup1(instance)

    def selectPaladin(self, instance):
        self.character.clss = "Paladin"
        self.cleanup1(instance)

    def selectRanger(self, instance):
        self.character.clss = "Ranger"
        self.cleanup1(instance)

    def selectRogue(self, instance):
        self.character.clss = "Rogue"
        self.cleanup1(instance)

    def selectSorcerer(self, instance):
        self.character.clss = "Sorcerer"
        self.cleanup1(instance)

    def selectWarlock(self, instance):
        self.character.clss = "Warlock"
        self.cleanup1(instance)

    def selectWizard(self, instance):
        self.character.clss = "Wizard"
        self.cleanup1(instance)

    def selectArtificer(self, instance):
        self.character.clss = "Artificer"
        self.cleanup1(instance)

    def selectBloodHunter(self, instance):
        self.character.clss = "Blood Hunter"
        self.cleanup1(instance)

    def cleanup1(self, instance): #clears the buttons and question
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.rando1)
        self.yn.remove_widget(self.rando2)
        self.yn.remove_widget(self.rando3)
        self.yn.remove_widget(self.rando4)
        self.yn.remove_widget(self.rando5)
        self.yn.remove_widget(self.rando6)
        self.yn.remove_widget(self.rando7)
        self.yn.remove_widget(self.rando8)
        self.yn.remove_widget(self.rando9)
        self.yn.remove_widget(self.rando10)
        self.yn.remove_widget(self.rando11)
        self.yn.remove_widget(self.rando12)
        self.yn.remove_widget(self.rando13)
        self.yn.remove_widget(self.rando14)

        self.askRace(instance)
        

#****************Randomize Class Options***************************************

    def askCExpandN(self, instance): #use class expansions no, ask about class expansion Base
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use base??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askCBaseY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askCBaseN)
        self.yn.add_widget(self.randoN)

    def askCBaseY(self, instance): #use class expansion UA yes
        self.cExpands[0] = True
        self.askCUA(instance)

    def askCBaseN(self, instance): #use class expansion UA no
        self.cExpands[0] = False
        self.askCUA(instance)

    def askCUA(self, instance): #ask about class expansion UA
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Unearthed Arcana??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askCUAY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askCUAN)
        self.yn.add_widget(self.randoN)

    def askCUAY(self, instance): #use class expansion UA yes
        self.cExpands[1] = True
        self.askCCR(instance)

    def askCUAN(self, instance): #use class expansion UA no
        self.cExpands[1] = False
        self.askCCR(instance)

    def askCCR(self, instance): #ask about class expansion CR
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Critical Roll??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askCCRY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askCCRN)
        self.yn.add_widget(self.randoN)

    def askCCRY(self, instance): #use class expansion UA yes
        self.cExpands[2] = True
        self.clssRando(instance)

    def askCCRN(self, instance): #use class expansion UA no
        self.cExpands[2] = False
        self.clssRando(instance)

    def clssRando(self, instance): #select random class
        clsses = []
        if(self.cExpands[0]):
            clsses.extend(["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
                          "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"])
    
        if(self.cExpands[1]):
            clsses.extend(["Artificer"])
        
        if(self.cExpands[2]):
            clsses.extend(["Blood Hunter"])
    
        ran = random.randint(0, (len(clsses) - 1))
        self.character.clss = clsses[ran]
        print(self.character.clss)
        self.askRace(instance)

#///////////////////////////////RACE////////////////////////////////////////////

    def askRace(self, instance): #asks about randomizing race
        self.display2 = Label(text = "[color=ffffff]Class: " + str(self.character.clss)
                              , markup = True) #display class
        self.add_widget(self.display2)
        
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Randomize Race??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRaceY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRaceN)
        self.yn.add_widget(self.randoN)

    def askRaceY(self, instance): #asks about using all expansions
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use all expansions??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.raceRando)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRBase)
        self.yn.add_widget(self.randoN)

#***************Manual Race Select**********************************************

    def askRaceN(self, instance):
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)

        self.randoSome = Label(text = "[color=ffffff]Which Race?", markup = True)
        self.raceGrid.add_widget(self.randoSome)
        
        self.rando1 = Button(text = "[color=ffffff]DragonBorn", markup = True)
        self.rando1.bind(on_press = self.selectDragonborn)
        self.raceGrid.add_widget(self.rando1)

        self.rando2 = Button(text = "[color=ffffff]Dwarf", markup = True)
        self.rando2.bind(on_press = self.selectDwarf)
        self.raceGrid.add_widget(self.rando2)

        self.rando3 = Button(text = "[color=ffffff]Elf", markup = True)
        self.rando3.bind(on_press = self.selectElf)
        self.raceGrid.add_widget(self.rando3)

        self.rando4 = Button(text = "[color=ffffff]Gnome", markup = True)
        self.rando4.bind(on_press = self.selectGnome)
        self.raceGrid.add_widget(self.rando4)

        self.rando5 = Button(text = "[color=ffffff]Half-Elf", markup = True)
        self.rando5.bind(on_press = self.selectHalfElf)
        self.raceGrid.add_widget(self.rando5)

        self.rando6 = Button(text = "[color=ffffff]Halfling", markup = True)
        self.rando6.bind(on_press = self.selectHalfling)
        self.raceGrid.add_widget(self.rando6)

        self.rando7 = Button(text = "[color=ffffff]Half-Orc", markup = True)
        self.rando7.bind(on_press = self.selectHalfOrc)
        self.raceGrid.add_widget(self.rando7)

        self.rando8 = Button(text = "[color=ffffff]Human", markup = True)
        self.rando8.bind(on_press = self.selectHuman)
        self.raceGrid.add_widget(self.rando8)

        self.rando9 = Button(text = "[color=ffffff]Tiefling", markup = True)
        self.rando9.bind(on_press = self.selectTiefling)
        self.raceGrid.add_widget(self.rando9)

        self.rando10 = Button(text = "[color=ffffff]Aarakocra", markup = True)
        self.rando10.bind(on_press = self.selectAarakocra)
        self.raceGrid.add_widget(self.rando10)

        self.rando11 = Button(text = "[color=ffffff]Genasi", markup = True)
        self.rando11.bind(on_press = self.selectGenasi)
        self.raceGrid.add_widget(self.rando11)

        self.rando12 = Button(text = "[color=ffffff]Goliath", markup = True)
        self.rando12.bind(on_press = self.selectGoliath)
        self.raceGrid.add_widget(self.rando12)

        self.rando13 = Button(text = "[color=ffffff]Aasimar", markup = True)
        self.rando13.bind(on_press = self.selectAasimar)
        self.raceGrid.add_widget(self.rando13)

        self.rando14 = Button(text = "[color=ffffff]Bugbear", markup = True)
        self.rando14.bind(on_press = self.selectBugbear)
        self.raceGrid.add_widget(self.rando14)

        self.rando15 = Button(text = "[color=ffffff]Firbolg", markup = True)
        self.rando15.bind(on_press = self.selectFirbolg)
        self.raceGrid.add_widget(self.rando15)

        self.rando16 = Button(text = "[color=ffffff]Goblin", markup = True)
        self.rando16.bind(on_press = self.selectGoblin)
        self.raceGrid.add_widget(self.rando16)

        self.rando17 = Button(text = "[color=ffffff]Hobgoblin", markup = True)
        self.rando17.bind(on_press = self.selectHobgoblin)
        self.raceGrid.add_widget(self.rando17)

        self.rando18 = Button(text = "[color=ffffff]Kenku", markup = True)
        self.rando18.bind(on_press = self.selectKenku)
        self.raceGrid.add_widget(self.rando18)

        self.rando19 = Button(text = "[color=ffffff]Kobold", markup = True)
        self.rando19.bind(on_press = self.selectKobold)
        self.raceGrid.add_widget(self.rando19)

        self.rando20 = Button(text = "[color=ffffff]Lizardfolk", markup = True)
        self.rando20.bind(on_press = self.selectLizardfolk)
        self.raceGrid.add_widget(self.rando20)

        self.rando21 = Button(text = "[color=ffffff]Orc", markup = True)
        self.rando21.bind(on_press = self.selectOrc)
        self.raceGrid.add_widget(self.rando21)

        self.rando22 = Button(text = "[color=ffffff]Tabaxi", markup = True)
        self.rando22.bind(on_press = self.selectTabaxi)
        self.raceGrid.add_widget(self.rando22)

        self.rando23 = Button(text = "[color=ffffff]Triton", markup = True)
        self.rando23.bind(on_press = self.selectTriton)
        self.raceGrid.add_widget(self.rando23)

        self.rando24 = Button(text = "[color=ffffff]Yuan-ti Pureblood", markup = True)
        self.rando24.bind(on_press = self.selectYuanTi)
        self.raceGrid.add_widget(self.rando24)

        self.rando25 = Button(text = "[color=ffffff]Feral Tiefling", markup = True)
        self.rando25.bind(on_press = self.selectFeralTiefling)
        self.raceGrid.add_widget(self.rando25)

        self.rando26 = Button(text = "[color=ffffff]Tortle", markup = True)
        self.rando26.bind(on_press = self.selectTortle)
        self.raceGrid.add_widget(self.rando26)

        self.rando27 = Button(text = "[color=ffffff]Gith", markup = True)
        self.rando27.bind(on_press = self.selectGith)
        self.raceGrid.add_widget(self.rando27)

        self.rando28 = Button(text = "[color=ffffff]Changeling", markup = True)
        self.rando28.bind(on_press = self.selectChangeling)
        self.raceGrid.add_widget(self.rando28)

        self.rando29 = Button(text = "[color=ffffff]Kalashtar", markup = True)
        self.rando29.bind(on_press = self.selectKalashtar)
        self.raceGrid.add_widget(self.rando29)

        self.rando30 = Button(text = "[color=ffffff]Shifter", markup = True)
        self.rando30.bind(on_press = self.selectShifter)
        self.raceGrid.add_widget(self.rando30)

        self.rando31 = Button(text = "[color=ffffff]Warforged", markup = True)
        self.rando31.bind(on_press = self.selectWarforged)
        self.raceGrid.add_widget(self.rando31)

        self.rando32 = Button(text = "[color=ffffff]Centaur", markup = True)
        self.rando32.bind(on_press = self.selectCentaur)
        self.raceGrid.add_widget(self.rando32)

        self.rando33 = Button(text = "[color=ffffff]Loxodon", markup = True)
        self.rando33.bind(on_press = self.selectLoxodon)
        self.raceGrid.add_widget(self.rando33)

        self.rando34 = Button(text = "[color=ffffff]Minotaur", markup = True)
        self.rando34.bind(on_press = self.selectMinotaur)
        self.raceGrid.add_widget(self.rando34)

        self.rando35 = Button(text = "[color=ffffff]Simic Hybrid", markup = True)
        self.rando35.bind(on_press = self.selectSimicHybrid)
        self.raceGrid.add_widget(self.rando35)

        self.rando36 = Button(text = "[color=ffffff]Vedalken", markup = True)
        self.rando36.bind(on_press = self.selectVedalken)
        self.raceGrid.add_widget(self.rando36)

    def selectDragonborn(self, instance):
        self.character.race = "Dragonborn"
        self.cleanup2(instance)

    def selectDwarf(self, instance):
        self.character.race = "Dwarf"
        self.cleanup2(instance)

    def selectElf(self, instance):
        self.character.race = "Elf"
        self.cleanup2(instance)

    def selectGnome(self, instance):
        self.character.race = "Gnome"
        self.cleanup2(instance)

    def selectHalfElf(self, instance):
        self.character.race = "Half-Elf"
        self.cleanup2(instance)

    def selectHalfling(self, instance):
        self.character.race = "Halfling"
        self.cleanup2(instance)

    def selectHalfOrc(self, instance):
        self.character.race = "Half-Orc"
        self.cleanup2(instance)

    def selectHuman(self, instance):
        self.character.race = "Human"
        self.cleanup2(instance)

    def selectTiefling(self, instance):
        self.character.race = "Tiefling"
        self.cleanup2(instance)

    def selectAarakocra(self, instance):
        self.character.race = "Aarakocra"
        self.cleanup2(instance)

    def selectGenasi(self, instance):
        self.character.race = "Genasi"
        self.cleanup2(instance)

    def selectGoliath(self, instance):
        self.character.race = "Goliath"
        self.cleanup2(instance)

    def selectAasimar(self, instance):
        self.character.race = "Aasimar"
        self.cleanup2(instance)

    def selectBugbear(self, instance):
        self.character.race = "Bugbear"
        self.cleanup2(instance)

    def selectFirbolg(self, instance):
        self.character.race = "Firbolg"
        self.cleanup2(instance)

    def selectGoblin(self, instance):
        self.character.race = "Goblin"
        self.cleanup2(instance)

    def selectHobgoblin(self, instance):
        self.character.race = "Hobgoblin"
        self.cleanup2(instance)

    def selectKenku(self, instance):
        self.character.race = "Kenku"
        self.cleanup2(instance)

    def selectKobold(self, instance):
        self.character.race = "Kobold"
        self.cleanup2(instance)

    def selectLizardfolk(self, instance):
        self.character.race = "Lizardfolk"
        self.cleanup2(instance)

    def selectOrc(self, instance):
        self.character.race = "Orc"
        self.cleanup2(instance)

    def selectTabaxi(self, instance):
        self.character.race = "Tabaxi"
        self.cleanup2(instance)

    def selectTriton(self, instance):
        self.character.race = "Triton"
        self.cleanup2(instance)

    def selectYuanTi(self, instance):
        self.character.race = "Yuan-ti Pureblood"
        self.cleanup2(instance)

    def selectFeralTiefling(self, instance):
        self.character.race = "Feral Tiefling"
        self.cleanup2(instance)

    def selectTortle(self, instance):
        self.character.race = "Tortle"
        self.cleanup2(instance)

    def selectGith(self, instance):
        self.character.race = "Gith"
        self.cleanup2(instance)

    def selectChangeling(self, instance):
        self.character.race = "Changeling"
        self.cleanup2(instance)

    def selectKalashtar(self, instance):
        self.character.race = "Kalashtar"
        self.cleanup2(instance)

    def selectShifter(self, instance):
        self.character.race = "Shifter"
        self.cleanup2(instance)

    def selectWarforged(self, instance):
        self.character.race = "Warforged"
        self.cleanup2(instance)

    def selectCentaur(self, instance):
        self.character.race = "Centaur"
        self.cleanup2(instance)

    def selectLoxodon(self, instance):
        self.character.race = "Loxodon"
        self.cleanup2(instance)

    def selectMinotaur(self, instance):
        self.character.race = "Minotaur"
        self.cleanup2(instance)

    def selectSimicHybrid(self, instance):
        self.character.race = "SimicHybrid"
        self.cleanup2(instance)

    def selectVedalken(self, instance):
        self.character.race = "Vedalken"
        self.cleanup2(instance)

    def cleanup2(self, instance): #clears the buttons and question
        self.raceGrid.remove_widget(self.randoSome)
        self.raceGrid.remove_widget(self.rando1)
        self.raceGrid.remove_widget(self.rando2)
        self.raceGrid.remove_widget(self.rando3)
        self.raceGrid.remove_widget(self.rando4)
        self.raceGrid.remove_widget(self.rando5)
        self.raceGrid.remove_widget(self.rando6)
        self.raceGrid.remove_widget(self.rando7)
        self.raceGrid.remove_widget(self.rando8)
        self.raceGrid.remove_widget(self.rando9)
        self.raceGrid.remove_widget(self.rando10)
        self.raceGrid.remove_widget(self.rando11)
        self.raceGrid.remove_widget(self.rando12)
        self.raceGrid.remove_widget(self.rando13)
        self.raceGrid.remove_widget(self.rando14)
        self.raceGrid.remove_widget(self.rando15)
        self.raceGrid.remove_widget(self.rando16)
        self.raceGrid.remove_widget(self.rando17)
        self.raceGrid.remove_widget(self.rando18)
        self.raceGrid.remove_widget(self.rando19)
        self.raceGrid.remove_widget(self.rando20)
        self.raceGrid.remove_widget(self.rando21)
        self.raceGrid.remove_widget(self.rando22)
        self.raceGrid.remove_widget(self.rando23)
        self.raceGrid.remove_widget(self.rando24)
        self.raceGrid.remove_widget(self.rando25)
        self.raceGrid.remove_widget(self.rando26)
        self.raceGrid.remove_widget(self.rando27)
        self.raceGrid.remove_widget(self.rando28)
        self.raceGrid.remove_widget(self.rando29)
        self.raceGrid.remove_widget(self.rando30)
        self.raceGrid.remove_widget(self.rando31)
        self.raceGrid.remove_widget(self.rando32)
        self.raceGrid.remove_widget(self.rando33)
        self.raceGrid.remove_widget(self.rando34)
        self.raceGrid.remove_widget(self.rando35)
        self.raceGrid.remove_widget(self.rando36)

        self.confirm(instance)

#**************Randomized Race**************************************************

    def askRBase(self, instance): #asks about race expansion base
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use base??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRBaseY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRBaseN)
        self.yn.add_widget(self.randoN)

    def askRBaseY(self, instance): #use class expansion base yes
        self.rExpands[0] = True
        self.askRElem(instance)

    def askRBaseN(self, instance): #use class expansion base no
        self.rExpands[0] = False
        self.askRElem(instance)

    def askRElem(self, instance): #asks about race expansion Elem
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Elemental Evil Companion??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRElemY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRElemN)
        self.yn.add_widget(self.randoN)

    def askRElemY(self, instance): #use class expansion Elem yes
        self.rExpands[1] = True
        self.askRVolo(instance)

    def askRElemN(self, instance): #use class expansion Elem no
        self.rExpands[1] = False
        self.askRVolo(instance)

    def askRVolo(self, instance): #asks about race expansion Volo
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Volo's Guide to Monsters??", markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRVoloY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRVoloN)
        self.yn.add_widget(self.randoN)

    def askRVoloY(self, instance): #use class expansion Volo yes
        self.rExpands[2] = True
        self.askRSword(instance)

    def askRVoloN(self, instance): #use class expansion Volo no
        self.rExpands[2] = False
        self.askRSword(instance)

    def askRSword(self, instance): #asks about race expansion Sword
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Sword coast adventurer's guide??"
                               , markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRSwordY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRSwordN)
        self.yn.add_widget(self.randoN)

    def askRSwordY(self, instance): #use class expansion Sword yes
        self.rExpands[3] = True
        self.askRTort(instance)

    def askRSwordN(self, instance): #use class expansion Sword no
        self.rExpands[3] = False
        self.askRTort(instance)

    def askRTort(self, instance): #asks about race expansion Tort
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Tortle Package??"
                               , markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRTortY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRTortN)
        self.yn.add_widget(self.randoN)

    def askRTortY(self, instance): #use class expansion Tort yes
        self.rExpands[4] = True
        self.askRMord(instance)

    def askRTortN(self, instance): #use class expansion Tort no
        self.rExpands[4] = False
        self.askRMord(instance)

    def askRMord(self, instance): #asks about race expansion Mord
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Mordenkainen's Tome of Foes??"
                               , markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRMordY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRMordN)
        self.yn.add_widget(self.randoN)

    def askRMordY(self, instance): #use class expansion Mord yes
        self.rExpands[5] = True
        self.askRWay(instance)

    def askRMordN(self, instance): #use class expansion Mord no
        self.rExpands[5] = False
        self.askRWay(instance)

    def askRWay(self, instance): #asks about race expansion Way
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Wayfinder's Guide to Eberron??"
                               , markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRWayY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRWayN)
        self.yn.add_widget(self.randoN)

    def askRWayY(self, instance): #use class expansion Way yes
        self.rExpands[6] = True
        self.askRRav(instance)

    def askRWayN(self, instance): #use class expansion Way no
        self.rExpands[6] = False
        self.askRRav(instance)

    def askRRav(self, instance): #asks about race expansion Way
        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)
        
        self.randoSome = Label(text = "[color=ffffff]Use Guildmasters' Guide to Ravnica??"
                               , markup = True)
        self.yn.add_widget(self.randoSome)
        self.randoY = Button(text = "[color=ffffff]Yes", markup = True)
        self.randoY.bind(on_press = self.askRRavY)
        self.yn.add_widget(self.randoY)

        self.randoN = Button(text = "[color=ffffff]No", markup = True)
        self.randoN.bind(on_press = self.askRRavN)
        self.yn.add_widget(self.randoN)

    def askRRavY(self, instance): #use class expansion Rav yes
        self.rExpands[7] = True
        self.raceRando(instance)

    def askRRavN(self, instance): #use class expansion Rav no
        self.rExpands[7] = False
        self.raceRando(instance)

    def raceRando(self, instance):
        races = []
        if(self.rExpands[0]):
            races.extend(["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling",
                        "Half-Orc", "Human", "Tiefling"])
        if(self.rExpands[1]):
            races.extend(["Aarakocra", "Genasi", "Goliath"])
        if(self.rExpands[2]):
            races.extend(["Aasimar", "Bugbear", "Firbolg", "Goblin", "Hobgoblin", "Kenku",
                        "Kobold", "Lizardfolk", "Orc", "Tabaxi" "Triton", "Yuan-ti Pureblood"])
        if(self.rExpands[3]):
            races.extend(["Feral Tiefling"])
        if(self.rExpands[4]):
            races.extend(["Totrle"])
        if(self.rExpands[5]):
            races.extend(["Gith"])
        if(self.rExpands[6]):
            races.extend(["Changeling", "Kalashtar", "Shifter", "Warforged"])
        if(self.rExpands[7]):
            races.extend(["Centaur", "Loxodon", "Minotaur", "Simic Hybrid", "Vedalken"])
        
        ran = random.randint(0, (len(races) - 1))
        self.character.race = races[ran]
        print(self.character.race)
        self.confirm(instance)

#///////////////////////////////Confirm Choice//////////////////////////////////

    def confirm(self, instance):
        self.display3 = Label(text = "[color=ffffff]Race: " + str(self.character.race)
                              , markup = True) #display race
        self.add_widget(self.display3)

        self.yn.remove_widget(self.randoSome)
        self.yn.remove_widget(self.randoY)
        self.yn.remove_widget(self.randoN)

        self.charTxt = Label(text ="[color=ffffff]Character Name: ", markup = True)
        self.enterVal.add_widget(self.charTxt)
        self.name = TextInput(multiline = False)
        self.enterVal.add_widget(self.name)

        self.cnfrm = Button(text = "[color=ffffff]Confirm", markup = True)
        self.cnfrm.bind(on_press = self.newSave)
        self.add_widget(self.cnfrm)

#////////////////////////////////SAVE///////////////////////////////////////////

    def newSave(self, instance):
        self.character.name = self.name.text
        print(self.character.name)
        
        self.remove_widget(self.cnfrm)
        self.enterVal.clear_widgets()
        #self.enterVal.remove_widget(self.name)
        
        self.display4 = Label(text = "[color=ffffff]Name: " + str(self.character.name)
                              , markup = True) #display name
        self.add_widget(self.display4)

        self.character.exp = 0
        self.character.level = 1
        self.character.setBaseHp()
        self.character.store()
        self.clear_widgets()
        ExistingCharacter.Scene1.manager(self.ind)

#//////////////////////////MISC.////////////////////////////////////////////////

class MyApp(App):
    def build(self):
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER, False)
        self.ads.request_banner()
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
    
