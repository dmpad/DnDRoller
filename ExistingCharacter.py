import random
import time
import kivy
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
from kivy.app import stopTouchApp
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from functools import partial

sm = ScreenManager()

class Scene1(Screen):
        def manager(ind):
                global tempInd
                tempInd = ind
                Scene1()
                
        def __init__(self, **kwargs):
                super(Scene1, self).__init__(**kwargs)
                self.character = DnDRollerChar.sheet()
                self.character.loadChar()
                self.character.bootChar(tempInd)

#*******************Initalize Grids********************************************************

                self.base = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x=1)
                self.base.bind(minimum_height = self.base.setter('height'))
                self.root = ScrollView(size_hint=(None, None), size=(Window.width, Window.height))

                self.fullSheetS = GridLayout(size_hint_y=None)
                self.fullSheetS.cols = 2
                self.base.add_widget(self.fullSheetS)

                self.tabs = GridLayout(size_hint_y=None)
                self.tabs.cols = 3
                self.base.add_widget(self.tabs)
                self.tabs.bind(minimum_height=self.tabs.setter('height'))

                self.colBuilder2 = GridLayout(size_hint_y=None)
                self.colBuilder2.cols = 3
                self.base.add_widget(self.colBuilder2)
                self.colBuilder2.bind(minimum_height=self.colBuilder2.setter('height'))

                self.saveThrows = GridLayout(size_hint_y=None)
                self.saveThrows.cols = 4
                self.colBuilder2.add_widget(self.saveThrows)
                self.saveThrows.bind(minimum_height=self.saveThrows.setter('height'))

                self.colBuilder = GridLayout(cols = 3, spacing=10, size_hint_y=None)
                self.base.add_widget(self.colBuilder)
                self.colBuilder.bind(minimum_height=self.colBuilder.setter('height'))

                self.fullSheetStats = GridLayout(size_hint_y=None)
                self.fullSheetStats.rows = 8
                self.fullSheetStats.cols = 2
                self.colBuilder.add_widget(self.fullSheetStats)
                self.fullSheetStats.bind(minimum_height=self.fullSheetStats.setter('height'))

                self.fullSheetSTTitle = GridLayout(size_hint_y=None)
                self.fullSheetSTTitle.cols = 1
                self.base.add_widget(self.fullSheetSTTitle)
                self.fullSheetSTTitle.bind(minimum_height=self.fullSheetSTTitle.setter('height'))

                self.fullSheetST = GridLayout(size_hint_y=None)
                self.fullSheetST.cols = 2
                self.base.add_widget(self.fullSheetST)
                self.fullSheetST.bind(minimum_height=self.fullSheetST.setter('height'))

                self.fullSheetSkTitle = GridLayout(size_hint_y=None)
                self.fullSheetSkTitle.cols = 1
                self.base.add_widget(self.fullSheetSkTitle)
                self.fullSheetSkTitle.bind(minimum_height=self.fullSheetSkTitle.setter('height'))


                self.fullSheetSkills = GridLayout(size_hint_y=None)
                self.fullSheetSkills.cols = 2
                self.base.add_widget(self.fullSheetSkills)
                self.fullSheetSkills.bind(minimum_height=self.fullSheetSkills.setter('height'))
                        
                self.inputField = GridLayout(size_hint_y=None)
                self.inputField.cols = 2
                self.colBuilder.add_widget(self.inputField)
                self.inputField.bind(minimum_height=self.inputField.setter('height'))

                self.abilityTitle = GridLayout(size_hint_y=None)
                self.abilityTitle.cols = 1
                self.base.add_widget(self.abilityTitle)
                self.abilityTitle.bind(minimum_height=self.abilityTitle.setter('height'))

                self.abilityField = GridLayout(size_hint_y=None)
                self.abilityField.cols = 2
                self.abilityField.row_default_height = 150
                self.base.add_widget(self.abilityField)
                self.abilityField.bind(minimum_height=self.abilityField.setter('height'))

                self.popupGrid = GridLayout(size_hint_y=None)
                self.popupGrid.cols = 1

                self.popupGrid2 = GridLayout(size_hint_y=None)
                self.popupGrid2.cols = 1
                
                self.display1()

                self.root.add_widget(self.base)
                stopTouchApp()
                runTouchApp(self.root)
                
        def switchScenes2(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene2(name = 'scene2'))

        def switchScenes3(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene3(name = 'scene3'))

        def switchScenes4(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene4(name = 'scene4'))

        def retrunToMenu(self):
                self.root.clear_widgets()
                __main__()

        def display1(self):

#******************Tabs for Different Parts of Sheet***************************************

                self.RPInfo = Button(text = "[color=ffffff]RP Info",
                                     markup = True, size_hint_y = None, height = 20)
                self.RPInfo.bind(on_press = self.switchScenes2)
                self.tabs.add_widget(self.RPInfo)

                self.EquipInfo = Button(text = "[color=ffffff]Equipment",
                                     markup = True, size_hint_y = None, height = 20)
                self.EquipInfo.bind(on_press = self.switchScenes3)
                self.tabs.add_widget(self.EquipInfo)

                self.SpellInfo = Button(text = "[color=ffffff]Spells",
                                     markup = True, size_hint_y = None, height = 20)
                self.SpellInfo.bind(on_press = self.switchScenes4)
                self.tabs.add_widget(self.SpellInfo)

#****************Display Data/Data Entry Fields********************************************
        
                self.charName = Label(text = "[color=ffffff]Name: " + self.character.name,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charName)

                self.charRace = Label(text = "[color=ffffff]Race: " + self.character.race,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charRace)

                self.charClss = Label(text = "[color=ffffff]Class: " + self.character.clss,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charClss)

                self.tAlignment = TextInput(size_hint_y = None, height = 30)
                self.tAlignment.text = self.character.alignment
                self.fullSheetS.add_widget(self.tAlignment)

                self.charLevel = Label(text = "[color=ffffff]Level: " + str(self.character.level),
                                       markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charLevel)

#************************EXP PopupB********************************************************

                self.charLevele = Label(text = "[color=ffffff]Level: " + str(self.character.level),
                                       markup = True, size_hint_y = None, height = 20)

                self.charExpe = Label(text = "[color=ffffff]Exp: " + str(self.character.exp),
                                     markup = True, size_hint_y = None, height = 20)

                self.amountExp = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.amountExp.text = "0"

                self.addExp = Button(text = "[color=ffffff]Add Exp",
                                     markup = True, size_hint_y = None, height = 20)
                self.addExp.bind(on_press = self.updateExp)

                self.expPopup = Popup(title='Add exp', size_hint=(None, None),
                                      size=(250, 250))

                self.expPopup.add_widget(self.popupGrid)
                self.popupGrid.add_widget(self.charLevele)
                self.popupGrid.add_widget(self.charExpe)
                self.popupGrid.add_widget(self.amountExp)
                self.popupGrid.add_widget(self.addExp)

#***********************EXP PopupE*********************************************************

                self.charExp = Button(text = "[color=ffffff]Exp: " + str(self.character.exp),
                                     markup = True, size_hint_y = None, height = 20)
                self.charExp.bind(on_press = self.expPopup.open)
                self.fullSheetS.add_widget(self.charExp)

                self.charProfB = Label(text = "[color=ffffff]Proficiency\nBonus: " ,
                                     markup = True, size_hint_y=None, height=20)
                self.fullSheetStats.add_widget(self.charProfB)

                self.pbEdit = TextInput(size_hint_y = None, height = 30, size_hint_x = 0.5,
                                           input_filter = 'int')
                self.pbEdit.text = str(self.character.profB)
                self.fullSheetStats.add_widget(self.pbEdit)
        
                self.charStr = Label(text = "[color=ffffff]Str: ",
                                     markup = True, size_hint_y=None, height=20)
                self.fullSheetStats.add_widget(self.charStr)

                self.tStr = TextInput(size_hint_y = None, height = 30, size_hint_x = 0.5,
                                      input_filter = 'int')
                self.tStr.text = str(self.character.stats[0])
                self.fullSheetStats.add_widget(self.tStr)

                self.charDex = Label(text = "[color=ffffff]Dex: " ,
                                     markup = True, size_hint_y=None, height=20)
                self.fullSheetStats.add_widget(self.charDex)

                self.tDex = TextInput(size_hint_y = None, height = 30, size_hint_x = 0.5,
                                      input_filter = 'int')
                self.tDex.text = str(self.character.stats[1])
                self.fullSheetStats.add_widget(self.tDex)

                self.charCon = Label(text = "[color=ffffff]Con: " ,
                                     markup = True, size_hint_y=None, height=20)
                self.fullSheetStats.add_widget(self.charCon)

                self.tCon = TextInput(size_hint_y = None, height = 30, size_hint_x = 0.5,
                                      input_filter = 'int')
                self.tCon.text = str(self.character.stats[2])
                self.fullSheetStats.add_widget(self.tCon)

                self.charInt = Label(text = "[color=ffffff]Int: " ,
                                     markup = True, size_hint_y=None, height=20)
                self.fullSheetStats.add_widget(self.charInt)

                self.tInt = TextInput(size_hint_y = None, height = 30, size_hint_x = 0.5,
                                      input_filter = 'int')
                self.tInt.text = str(self.character.stats[3])
                self.fullSheetStats.add_widget(self.tInt)

                self.charWis = Label(text = "[color=ffffff]Wis: " ,
                                     markup = True, size_hint_y=None, height=20)
                self.fullSheetStats.add_widget(self.charWis)

                self.tWis = TextInput(size_hint_y = None, height = 30, size_hint_x = 0.5,
                                      input_filter = 'int')
                self.tWis.text = str(self.character.stats[4])
                self.fullSheetStats.add_widget(self.tWis)

                self.charChar = Label(text = "[color=ffffff]Char: ",
                                      markup = True, size_hint_y=None, height=20)
                self.fullSheetStats.add_widget(self.charChar)

                self.tCha = TextInput(size_hint_y = None, height = 30, size_hint_x = 0.5,
                                      input_filter = 'int')
                self.tCha.text = str(self.character.stats[5])
                self.fullSheetStats.add_widget(self.tCha)

#*******************Saving Throws*********************************************************

                self.STTitle = Label(text = "[color=ffffff]Saving Throws",
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSTTitle.add_widget(self.STTitle)
                
                self.charStrT = Label(text = "[color=ffffff]Strength: " + str(self.character.st[0][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetST.add_widget(self.charStrT)

                self.strT = CheckBox(active=("True" ==self.character.st[0][1]), size_hint_x = 0.5)
                self.fullSheetST.add_widget(self.strT)

                self.charDexT = Label(text = "[color=ffffff]Dexterity: " + str(self.character.st[1][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetST.add_widget(self.charDexT)

                self.dexT = CheckBox(active=("True" ==self.character.st[1][1]), size_hint_x = 0.5)
                self.fullSheetST.add_widget(self.dexT)

                self.charConT = Label(text = "[color=ffffff]Constitution: " + str(self.character.st[2][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetST.add_widget(self.charConT)

                self.conT = CheckBox(active=("True" ==self.character.st[2][1]), size_hint_x = 0.5)
                self.fullSheetST.add_widget(self.conT)

                self.charIntT = Label(text = "[color=ffffff]Inteligence: " + str(self.character.st[3][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetST.add_widget(self.charIntT)

                self.intT = CheckBox(active=("True" ==self.character.st[3][1]), size_hint_x = 0.5)
                self.fullSheetST.add_widget(self.intT)

                self.charWisT = Label(text = "[color=ffffff]Wisdom: " + str(self.character.st[4][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetST.add_widget(self.charWisT)

                self.wisT = CheckBox(active=("True" ==self.character.st[4][1]), size_hint_x = 0.5)
                self.fullSheetST.add_widget(self.wisT)

                self.charChaT = Label(text = "[color=ffffff]Charisma: " + str(self.character.st[5][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetST.add_widget(self.charChaT)

                self.chaT = CheckBox(active=("True" ==self.character.st[5][1]), size_hint_x = 0.5)
                self.fullSheetST.add_widget(self.chaT)

#*******************Proficiencies*********************************************************

                self.SkTitle = Label(text = "[color=ffffff]Skills",
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkTitle.add_widget(self.SkTitle)

                self.charAcro = Label(text = "[color=ffffff]Acrobatics: " + str(self.character.profs[0][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charAcro)

                self.acroP = CheckBox(active=("True" ==self.character.profs[0][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.acroP)

                self.charAH = Label(text = "[color=ffffff]Animal Handling: " + str(self.character.profs[1][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charAH)

                self.AHP = CheckBox(active=("True" ==self.character.profs[1][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.AHP)

                self.charArc = Label(text = "[color=ffffff]Arcana: " + str(self.character.profs[2][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charArc)

                self.arcP = CheckBox(active=("True" ==self.character.profs[2][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.arcP)

                self.charAth = Label(text = "[color=ffffff]Athletics: " + str(self.character.profs[3][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charAth)

                self.athP = CheckBox(active=("True" ==self.character.profs[3][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.athP)

                self.charDec = Label(text = "[color=ffffff]Deception: " + str(self.character.profs[4][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charDec)

                self.decP = CheckBox(active=("True" ==self.character.profs[4][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.decP)

                self.charHist = Label(text = "[color=ffffff]History: " + str(self.character.profs[5][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charHist)

                self.histP = CheckBox(active=("True" ==self.character.profs[5][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.histP)

                self.charIns = Label(text = "[color=ffffff]Insight: " + str(self.character.profs[6][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charIns)

                self.insP = CheckBox(active=("True" ==self.character.profs[6][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.insP)

                self.charIntim = Label(text = "[color=ffffff]Intimidation: " + str(self.character.profs[7][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charIntim)

                self.intimP = CheckBox(active=("True" ==self.character.profs[7][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.intimP)

                self.charInvest = Label(text = "[color=ffffff]Investigation: " + str(self.character.profs[8][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charInvest)

                self.investP = CheckBox(active=("True" ==self.character.profs[8][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.investP)

                self.charMed = Label(text = "[color=ffffff]Medicine: " + str(self.character.profs[9][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charMed)

                self.medP = CheckBox(active=("True" ==self.character.profs[9][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.medP)

                self.charNat = Label(text = "[color=ffffff]Nature: " + str(self.character.profs[10][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charNat)

                self.natP = CheckBox(active=("True" ==self.character.profs[10][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.natP)

                self.charPerc = Label(text = "[color=ffffff]Perception: " + str(self.character.profs[11][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charPerc)

                self.percP = CheckBox(active=("True" ==self.character.profs[11][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.percP)

                self.charPerf = Label(text = "[color=ffffff]Performance: " + str(self.character.profs[12][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charPerf)

                self.perfP = CheckBox(active=("True" ==self.character.profs[12][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.perfP)

                self.charPers = Label(text = "[color=ffffff]Persuasion: " + str(self.character.profs[13][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charPers)

                self.persP = CheckBox(active=("True" ==self.character.profs[13][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.persP)

                self.charRel = Label(text = "[color=ffffff]Religion: " + str(self.character.profs[14][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charRel)

                self.relP = CheckBox(active=("True" ==self.character.profs[14][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.relP)

                self.charSli = Label(text = "[color=ffffff]Slieght of Hand: " + str(self.character.profs[15][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charSli)

                self.sliP = CheckBox(active=("True" ==self.character.profs[15][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.sliP)

                self.charStel = Label(text = "[color=ffffff]Stealth: " + str(self.character.profs[16][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charStel)

                self.stelP = CheckBox(active=("True" ==self.character.profs[16][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.stelP)

                self.charSur = Label(text = "[color=ffffff]Survival: " + str(self.character.profs[17][0]) ,
                                       markup = True, size_hint_y=None, height=20)
                self.fullSheetSkills.add_widget(self.charSur)

                self.surP = CheckBox(active=("True" ==self.character.profs[17][1]), size_hint_x = 0.5)
                self.fullSheetSkills.add_widget(self.surP)

#***********************Death Saves*******************************************************

                self.savesText = Label(text = "[color=ffffff]Death Saves\n(successes):",
                                       markup = True, size_hint_y = None, height = 40)
                self.saveThrows.add_widget(self.savesText)

                self.save1 = CheckBox(active=("True" ==self.character.saves[0]), size_hint_x = 0.5)
                self.saveThrows.add_widget(self.save1)

                self.save2 = CheckBox(active=("True" ==self.character.saves[1]), size_hint_x = 0.5)
                self.saveThrows.add_widget(self.save2)

                self.save3 = CheckBox(active=("True" ==self.character.saves[2]), size_hint_x = 0.5)
                self.saveThrows.add_widget(self.save3)

                self.failsText = Label(text = "[color=ffffff]Death Saves\n(failures):",
                                       markup = True, size_hint_y = None, height = 40)
                self.saveThrows.add_widget(self.failsText)

                self.fail1 = CheckBox(active=("True" ==self.character.fails[0]), size_hint_x = 0.5)
                self.saveThrows.add_widget(self.fail1)

                self.fail2 = CheckBox(active=("True" ==self.character.fails[1]), size_hint_x = 0.5)
                self.saveThrows.add_widget(self.fail2)

                self.fail3 = CheckBox(active=("True" ==self.character.fails[2]), size_hint_x = 0.5)
                self.saveThrows.add_widget(self.fail3)

#********************HP********************************************************************

                self.charMaxHpText = Label(text = "[color=ffffff]Max HP: ",
                                       markup = True, size_hint_y = None, height = 20)
                self.inputField.add_widget(self.charMaxHpText)
                self.charMaxHp = Label(text = "[color=ffffff]" + str(self.character.hp),
                                       markup = True, size_hint_y = None, height = 20, size_hint_x = 0.5)
                self.inputField.add_widget(self.charMaxHp)

                self.charCHp = Label(text = "[color=ffffff]Current HP: ",
                                     markup = True, size_hint_y = None, height = 30)
                self.inputField.add_widget(self.charCHp)
                self.tCHp = TextInput(input_filter = 'int', size_hint_x = 0.5)
                self.tCHp.text = str(self.character.curHp)
                self.inputField.add_widget(self.tCHp)

                self.charTHp = Label(text = "[color=ffffff]Temp HP: ",
                                     markup = True, size_hint_y = None, height = 30)
                self.inputField.add_widget(self.charTHp)
                self.tTHp = TextInput(input_filter = 'int', size_hint_x = 0.5)
                self.tTHp.text = str(self.character.tempHp)
                self.inputField.add_widget(self.tTHp)

#*******************Other Numerical Values*************************************************

                self.charInsp = Label(text = "[color=ffffff]Inspiration: ",
                      markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charInsp)
                self.tInsp = TextInput(input_filter = 'int', size_hint_x = 0.5)
                self.tInsp.text = str(self.character.insp)
                self.inputField.add_widget(self.tInsp)

                self.charAC = Label(text = "[color=ffffff]AC: ",
                                    markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charAC)
                self.tAC = TextInput(input_filter = 'int', size_hint_x = 0.5)
                self.tAC.text = str(self.character.ac)
                self.inputField.add_widget(self.tAC)

                self.charSpeed = Label(text = "[color=ffffff]Speed: ",
                                       markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charSpeed)
                self.tSpeed = TextInput(input_filter = 'int', size_hint_x = 0.5)
                self.tSpeed.text = str(self.character.speed)
                self.inputField.add_widget(self.tSpeed)

                self.charInit = Label(text = "[color=ffffff]Initiative: ",
                                      markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charInit)
                self.tInit = TextInput(input_filter = 'int', size_hint_x = 0.5)
                self.tInit.text = str(self.character.initiative)
                self.inputField.add_widget(self.tInit)

#*******************Abilities**************************************************

                self.abilityT = Label(text = "[color=ffffff]Features and Traits",
                                      markup = True, size_hint_y=None, height=30)
                self.abilityTitle.add_widget(self.abilityT)

                self.abilityN0 = TextInput()
                self.abilityN0.text = self.character.ability[0][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[0][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN0)

                self.abilityD0 = TextInput()
                self.abilityD0.text = self.character.ability[0][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[0][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD0)

                self.abilityN1 = TextInput()
                self.abilityN1.text = self.character.ability[1][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[1][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN1)

                self.abilityD1 = TextInput()
                self.abilityD1.text = self.character.ability[1][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[1][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD1)

                self.abilityN2 = TextInput()
                self.abilityN2.text = self.character.ability[2][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[2][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN2)

                self.abilityD2 = TextInput()
                self.abilityD2.text = self.character.ability[2][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[2][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD2)

                self.abilityN3 = TextInput()
                self.abilityN3.text = self.character.ability[3][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[3][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN3)

                self.abilityD3 = TextInput()
                self.abilityD3.text = self.character.ability[3][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[3][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD3)

                self.abilityN4 = TextInput()
                self.abilityN4.text = self.character.ability[4][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[4][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN4)

                self.abilityD4 = TextInput()
                self.abilityD4.text = self.character.ability[4][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[4][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD4)

                self.abilityN5 = TextInput()
                self.abilityN5.text = self.character.ability[5][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[5][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN5)

                self.abilityD5 = TextInput()
                self.abilityD5.text = self.character.ability[5][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[5][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD5)

                self.abilityN6 = TextInput()
                self.abilityN6.text = self.character.ability[6][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[6][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN6)

                self.abilityD6 = TextInput()
                self.abilityD6.text = self.character.ability[6][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[6][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD6)

                self.abilityN7 = TextInput()
                self.abilityN7.text = self.character.ability[7][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[7][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN7)

                self.abilityD7 = TextInput()
                self.abilityD7.text = self.character.ability[7][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[7][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD7)

                self.abilityN8 = TextInput()
                self.abilityN8.text = self.character.ability[8][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[8][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN8)

                self.abilityD8 = TextInput()
                self.abilityD8.text = self.character.ability[8][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[8][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD8)

                self.abilityN9 = TextInput()
                self.abilityN9.text = self.character.ability[9][0]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[9][0].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityN9)

                self.abilityD9 = TextInput()
                self.abilityD9.text = self.character.ability[9][1]
                self.abilityN0.size_hint_y = (self.abilityN0.line_height * (len(self.character.ability[9][1].split("\n")) + 1))
                self.abilityField.add_widget(self.abilityD9)

                self.saveChar = Button(text = "[color=ffffff]Save",
                                       markup = True,size_hint_y = None, height = 50)
                self.saveChar.bind(on_press = lambda x:self.saveExisting())
                self.base.add_widget(self.saveChar)

        def updateExp(self, instance):
                self.character.exp += int(self.amountExp.text)
                self.expPopup.dismiss()
                tempLvl = self.character.level
                self.character.setLevel()
                self.saveExisting()

                self.charLevele.text = "[color=ffffff]Level: " + str(self.character.level)

                self.charExpe.text = "[color=ffffff]Exp: " + str(self.character.exp)
                
                self.charExp.text = "[color=ffffff]Exp: " + str(self.character.exp)
                if(tempLvl < self.character.level):
                        self.updateHp(instance, self.character.level - tempLvl)

        def updateHp(self, instance, difference):
        
                self.addRoll = Button(text = "[color=ffffff]Roll: " + str(self.character.healthVals[self.character.clss][1]),
                                     markup = True, size_hint_y = None, height = 20)
                self.addRoll.bind(on_press = lambda x:self.rollHp(instance, difference))
                self.addBase = Button(text = "[color=ffffff]Base Value: " + str(self.character.healthVals[self.character.clss][0]),
                                     markup = True, size_hint_y = None, height = 20)
                self.addBase.bind(on_press = lambda x:self.baseHp(instance, difference))

                self.levelUp = Popup(title='Roll HP or add base HP?', size_hint=(None, None),
                                      size=(400, 400))

                try:
                        self.levelUp.add_widget(self.popupGrid2)
                except kivy.uix.widget.WidgetException:
                        self.popupGrid2.add_widget(self.addRoll)
                        self.popupGrid2.add_widget(self.addBase)
                        
                self.popupGrid2.add_widget(self.addRoll)
                self.popupGrid2.add_widget(self.addBase)

                self.levelUp.open()

        def baseHp(self, instance, difference):
                self.levelUp.dismiss()
                self.character.hpAddBasic()
                self.saveExisting()
                difference -= 1
                if(difference != 0):
                        self.hpAddBasic(instance, difference)

        def rollHp(self, instance, difference):
                self.levelUp.dismiss()
                self.character.hpAddRoll()
                self.saveExisting()
                difference -= 1
                if(difference != 0):
                        self.hpAddRoll(instance, difference)

        def saveExisting(self):
                self.character.alignment = self.tAlignment.text
                self.character.insp = self.tInsp.text
                self.character.ac = self.tAC.text
                self.character.initiative = self.tInit.text
                self.character.speed = self.tSpeed.text
                self.character.curHp = self.tCHp.text
                self.character.tempHp = self.tTHp.text
                self.character.initiative = self.tInit.text
                self.character.saves[0] = self.save1.active
                self.character.saves[1] = self.save2.active
                self.character.saves[2] = self.save3.active
                self.character.fails[0] = self.fail1.active
                self.character.fails[1] = self.fail2.active
                self.character.fails[2] = self.fail3.active
                self.character.profB = self.pbEdit.text
                self.character.stats[0] = int(self.tStr.text)
                self.character.stats[1] = int(self.tDex.text)
                self.character.stats[2] = int(self.tCon.text)
                self.character.stats[3] = int(self.tInt.text)
                self.character.stats[4] = int(self.tWis.text)
                self.character.stats[5] = int(self.tCha.text)
                
                self.character.profs[0][1] = self.acroP.active
                self.character.profs[1][1] = self.AHP.active
                self.character.profs[2][1] = self.arcP.active
                self.character.profs[3][1] = self.athP.active
                self.character.profs[4][1] = self.decP.active
                self.character.profs[5][1] = self.histP.active
                self.character.profs[6][1] = self.insP.active
                self.character.profs[7][1] = self.intimP.active
                self.character.profs[8][1] = self.investP.active
                self.character.profs[9][1] = self.medP.active
                self.character.profs[10][1] = self.natP.active
                self.character.profs[11][1] = self.percP.active
                self.character.profs[12][1] = self.perfP.active
                self.character.profs[13][1] = self.persP.active
                self.character.profs[14][1] = self.relP.active
                self.character.profs[15][1] = self.sliP.active
                self.character.profs[16][1] = self.stelP.active
                self.character.profs[17][1] = self.surP.active

                self.character.st[0][1] = self.strT.active
                self.character.st[1][1] = self.dexT.active
                self.character.st[2][1] = self.conT.active
                self.character.st[3][1] = self.intT.active
                self.character.st[4][1] = self.wisT.active
                self.character.st[5][1] = self.chaT.active

                self.character.ability[0][0] = self.abilityN0.text
                self.character.ability[0][1] = self.abilityD0.text
                self.character.ability[1][0] = self.abilityN1.text
                self.character.ability[1][1] = self.abilityD1.text
                self.character.ability[2][0] = self.abilityN2.text
                self.character.ability[2][1] = self.abilityD2.text
                self.character.ability[3][0] = self.abilityN3.text
                self.character.ability[3][1] = self.abilityD3.text
                self.character.ability[4][0] = self.abilityN4.text
                self.character.ability[4][1] = self.abilityD4.text
                self.character.ability[5][0] = self.abilityN5.text
                self.character.ability[5][1] = self.abilityD5.text
                self.character.ability[6][0] = self.abilityN6.text
                self.character.ability[6][1] = self.abilityD6.text
                self.character.ability[7][0] = self.abilityN7.text
                self.character.ability[7][1] = self.abilityD7.text
                self.character.ability[8][0] = self.abilityN8.text
                self.character.ability[8][1] = self.abilityD8.text
                self.character.ability[9][0] = self.abilityN9.text
                self.character.ability[9][1] = self.abilityD9.text

                self.charAcro.text = "[color=ffffff]Acrobatics: " + str(self.character.profs[0][0])
                self.charAH.text = "[color=ffffff]Animal Handling: " + str(self.character.profs[1][0])
                self.charArc.text = "[color=ffffff]Arcana: " + str(self.character.profs[2][0])
                self.charAth.text = "[color=ffffff]Athletics: " + str(self.character.profs[3][0])
                self.charDec.text = "[color=ffffff]Deception: " + str(self.character.profs[4][0])
                self.charHist.text = "[color=ffffff]History: " + str(self.character.profs[5][0])
                self.charIns.text = "[color=ffffff]Insight: " + str(self.character.profs[6][0])
                self.charIntim.text = "[color=ffffff]Intimidation: " + str(self.character.profs[7][0])
                self.charInvest.text = "[color=ffffff]Investigation: " + str(self.character.profs[8][0])
                self.charMed.text = "[color=ffffff]Medicine: " + str(self.character.profs[9][0])
                self.charNat.text = "[color=ffffff]Nature: " + str(self.character.profs[10][0])
                self.charPerc.text = "[color=ffffff]Perception: " + str(self.character.profs[11][0])
                self.charPerf.text = "[color=ffffff]Performance: " + str(self.character.profs[12][0])
                self.charPers.text = "[color=ffffff]Persuasion: " + str(self.character.profs[13][0])
                self.charRel.text = "[color=ffffff]Religion: " + str(self.character.profs[14][0])
                self.charSli.text = "[color=ffffff]Sleight of Hand: " + str(self.character.profs[15][0])
                self.charStel.text = "[color=ffffff]Stealth: " + str(self.character.profs[16][0])
                self.charSur.text = "[color=ffffff]Survival: " + str(self.character.profs[17][0])

                self.charStrT.text = "[color=ffffff]Strength: " + str(self.character.st[0][0])
                self.charDexT.text = "[color=ffffff]Dexterity: " + str(self.character.st[1][0])
                self.charConT.text = "[color=ffffff]Constitution: " + str(self.character.st[2][0])
                self.charIntT.text = "[color=ffffff]Inteligence: " + str(self.character.st[3][0])
                self.charWisT.text = "[color=ffffff]Wisdom: " + str(self.character.st[4][0])
                self.charChaT.text = "[color=ffffff]Charisma: " + str(self.character.st[5][0])


                self.character.storeExisting()

class Scene2(Screen):
        def __init__(self, **kwargs):
                super(Scene2, self).__init__(**kwargs)
                self.character = DnDRollerChar.sheet()
                self.character.loadChar()
                self.character.bootChar(tempInd)
                
#*******************Initalize Grids********************************************************

                self.base = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x=1)
                self.base.bind(minimum_height = self.base.setter('height'))
                self.root = ScrollView(size_hint=(None, None), size=(Window.width, Window.height))

                self.fullSheetS = GridLayout(size_hint_y=None)
                self.fullSheetS.cols = 2
                self.base.add_widget(self.fullSheetS)

                self.tabs = GridLayout(size_hint_y=None)
                self.tabs.cols = 3
                self.base.add_widget(self.tabs)

                self.colBuilder = GridLayout(cols = 3, spacing=10, size_hint_y=None)
                self.base.add_widget(self.colBuilder)
                self.colBuilder.bind(minimum_height=self.colBuilder.setter('height'))

                self.inputField = GridLayout(size_hint_y=None)
                self.inputField.cols = 2
                self.colBuilder.add_widget(self.inputField)
                self.inputField.bind(minimum_height=self.inputField.setter('height'))

                self.popupGrid = GridLayout(size_hint_y=None)
                self.popupGrid.cols = 1
                
                self.display2()

                self.root.add_widget(self.base)
                stopTouchApp()
                runTouchApp(self.root)

        def switchScenes1(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene1(name = 'scene1'))

        def switchScenes3(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene3(name = 'scene3'))

        def switchScenes4(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene4(name = 'scene4'))

        def display2(self):
                                 
#******************Tabs for Different Parts of Sheet***************************************

                self.StatsInfo = Button(text = "[color=ffffff]Stats Info",
                                     markup = True, size_hint_y = None, height = 20)
                self.StatsInfo.bind(on_press = self.switchScenes1)
                self.tabs.add_widget(self.StatsInfo)

                self.EquipInfo = Button(text = "[color=ffffff]Equipment",
                                     markup = True, size_hint_y = None, height = 20)
                self.EquipInfo.bind(on_press = self.switchScenes3)
                self.tabs.add_widget(self.EquipInfo)

                self.SpellInfo = Button(text = "[color=ffffff]Spells",
                                     markup = True, size_hint_y = None, height = 20)
                self.SpellInfo.bind(on_press = self.switchScenes4)
                self.tabs.add_widget(self.SpellInfo)

#****************Display Data/Data Entry Fields********************************************
        
                self.charName = Label(text = "[color=ffffff]Name: " + self.character.name,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charName)

                self.charRace = Label(text = "[color=ffffff]Race: " + self.character.race,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charRace)

                self.charClss = Label(text = "[color=ffffff]Class: " + self.character.clss,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charClss)

                self.tAlignment = TextInput(size_hint_y = None, height = 30)
                self.tAlignment.text = self.character.alignment
                self.fullSheetS.add_widget(self.tAlignment)

                self.charLevel = Label(text = "[color=ffffff]Level: " + str(self.character.level),
                                       markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charLevel)

#************************EXP PopupB********************************************************

                self.charLevele = Label(text = "[color=ffffff]Level: " + str(self.character.level),
                                       markup = True, size_hint_y = None, height = 20)

                self.charExpe = Label(text = "[color=ffffff]Exp: " + str(self.character.exp),
                                     markup = True, size_hint_y = None, height = 20)

                self.amountExp = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.amountExp.text = "0"

                self.addExp = Button(text = "[color=ffffff]Add Exp",
                                     markup = True, size_hint_y = None, height = 20)
                self.addExp.bind(on_press = self.updateExp)

                self.expPopup = Popup(title='Add exp', size_hint=(None, None),
                                      size=(250, 250))

                self.expPopup.add_widget(self.popupGrid)
                self.popupGrid.add_widget(self.charLevele)
                self.popupGrid.add_widget(self.charExpe)
                self.popupGrid.add_widget(self.amountExp)
                self.popupGrid.add_widget(self.addExp)

#***********************EXP PopupE*********************************************************

                self.charExp = Button(text = "[color=ffffff]Exp: " + str(self.character.exp),
                                     markup = True, size_hint_y = None, height = 20)
                self.charExp.bind(on_press = self.expPopup.open)
                self.fullSheetS.add_widget(self.charExp)
                
#***********************RP Data************************************************************

                self.charBackground = Label(text = "[color=ffffff]Background: ",
                                            markup = True, size_hint_y = None, height = 150)
                self.inputField.add_widget(self.charBackground)
                self.tBackground = TextInput()
                self.tBackground.text = self.character.background
                self.inputField.add_widget(self.tBackground)

                self.charPT = Label(text = "[color=ffffff]Personality\nTraits: ",
                                    markup = True, size_hint_y=None, height=150)
                self.inputField.add_widget(self.charPT)
                self.tPT = TextInput()
                self.tPT.text = self.character.personality
                self.inputField.add_widget(self.tPT)

                self.charIdeals = Label(text = "[color=ffffff]Ideals: ",
                                        markup = True, size_hint_y=None, height=150)
                self.inputField.add_widget(self.charIdeals)
                self.tIdeals = TextInput()
                self.tIdeals.text = self.character.ideals
                self.inputField.add_widget(self.tIdeals)

                self.charBonds = Label(text = "[color=ffffff]Bonds: ",
                                       markup = True, size_hint_y=None, height=150)
                self.inputField.add_widget(self.charBonds)
                self.tBonds = TextInput()
                self.tBonds.text = self.character.bonds
                self.inputField.add_widget(self.tBonds)

                self.charFlaws = Label(text = "[color=ffffff]Flaws: ",
                                       markup = True, size_hint_y=None, height=150)
                self.inputField.add_widget(self.charFlaws)
                self.tFlaws = TextInput()
                self.tFlaws.text = self.character.flaws
                self.inputField.add_widget(self.tFlaws)

                self.charBackstory = Label(text = "[color=ffffff]Backstory: ",
                                           markup = True, size_hint_y=None, height=150)
                self.inputField.add_widget(self.charBackstory)
                self.tBackstory = TextInput()
                self.tBackstory.text = self.character.backstory
                self.inputField.add_widget(self.tBackstory)

                self.charOP = Label(text = "[color=ffffff]Other\nProficiencies: ",
                                    markup = True, size_hint_y=None, height=150)
                self.inputField.add_widget(self.charOP)
                self.tOP = TextInput()
                self.tOP.text = self.character.op
                self.inputField.add_widget(self.tOP)

                self.saveChar = Button(text = "[color=ffffff]Save",
                                       markup = True,size_hint_y = None, height = 50)
                self.saveChar.bind(on_press = lambda x:self.saveExisting())
                self.base.add_widget(self.saveChar)

        def updateExp(self, instance):
                self.character.exp += int(self.amountExp.text)
                self.expPopup.dismiss()
                tempLvl = self.character.level
                self.character.setLevel()
                self.saveExisting()

                self.charLevele.text = "[color=ffffff]Level: " + str(self.character.level)

                self.charExpe.text = "[color=ffffff]Exp: " + str(self.character.exp)
                
                self.charExp.text = "[color=ffffff]Exp: " + str(self.character.exp)
                if(tempLvl < self.character.level):
                        self.updateHp(instance, self.character.level - tempLvl)

        def updateHp(self, instance, difference):
                self.addRoll = Button(text = "[color=ffffff]Roll: " + str(self.character.healthVals[self.character.clss][1]),
                                     markup = True, size_hint_y = None, height = 20)
                self.addRoll.bind(on_press = lambda x:self.rollHp(instance, difference))
                self.addBase = Button(text = "[color=ffffff]Base Value: " + str(self.character.healthVals[self.character.clss][0]),
                                     markup = True, size_hint_y = None, height = 20)
                self.addBase.bind(on_press = lambda x:self.baseHp(instance, difference))

                self.levelUp = Popup(title='Roll HP or add base HP?', size_hint=(None, None),
                                      size=(400, 400))

                try:
                        self.levelUp.add_widget(self.popupGrid2)
                except kivy.uix.widget.WidgetException:
                        self.popupGrid2.add_widget(self.addRoll)
                        self.popupGrid2.add_widget(self.addBase)
                        
                self.popupGrid2.add_widget(self.addRoll)
                self.popupGrid2.add_widget(self.addBase)

                self.levelUp.open()

        def baseHp(self, instance, difference):
                self.levelUp.dismiss()
                self.character.hpChange(instance, "base")
                self.saveExisting()
                difference -= 1
                if(difference != 0):
                        self.hpAddBasic(instance, difference)

        def rollHp(self, instance, difference):
                self.levelUp.dismiss()
                self.character.hpChange(instance, "roll")
                self.saveExisting()
                difference -= 1
                if(difference != 0):
                        self.hpAddRoll(instance, difference)

        def saveExisting(self):
                self.character.background = self.tBackground.text
                self.character.personality = self.tPT.text
                self.character.ideals = self.tIdeals.text
                self.character.bonds = self.tBonds.text
                self.character.flaws = self.tFlaws.text
                self.character.alignment = self.tAlignment.text
                self.character.backstory = self.tBackstory.text
                self.character.op = self.tOP.text

                self.character.storeExisting()

class Scene3(Screen):
        def __init__(self, **kwargs):
                super(Scene3, self).__init__(**kwargs)
                self.character = DnDRollerChar.sheet()
                self.character.loadChar()
                self.character.bootChar(tempInd)
                
#*******************Initalize Grids********************************************************

                self.base = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x=1)
                self.base.bind(minimum_height = self.base.setter('height'))
                self.root = ScrollView(size_hint=(None, None), size=(Window.width, Window.height))

                self.fullSheetS = GridLayout(size_hint_y=None)
                self.fullSheetS.cols = 2
                self.fullSheetS.bind(minimum_height = self.fullSheetS.setter('height'))
                self.base.add_widget(self.fullSheetS)

                self.tabs = GridLayout(size_hint_y=None)
                self.tabs.cols = 3
                self.tabs.bind(minimum_height = self.tabs.setter('height'))
                self.base.add_widget(self.tabs)

                self.colBuilder = GridLayout(size_hint_y=None)
                self.colBuilder.cols = 1
                self.colBuilder.bind(minimum_height = self.colBuilder.setter('height'))
                self.base.add_widget(self.colBuilder)

                self.wepTitle = GridLayout(size_hint_y=None)
                self.wepTitle.cols = 3
                self.wepTitle.bind(minimum_height = self.wepTitle.setter('height'))
                self.colBuilder.add_widget(self.wepTitle)

                self.wep = GridLayout(size_hint_y=None)
                self.wep.cols = 3
                self.wep.bind(minimum_height = self.wep.setter('height'))
                self.colBuilder.add_widget(self.wep)

                self.inputField = GridLayout(size_hint_y=None)
                self.inputField.cols = 2
                self.inputField.bind(minimum_height = self.inputField.setter('height'))
                self.colBuilder.add_widget(self.inputField)

                self.popupGrid = GridLayout(size_hint_y=None)
                self.popupGrid.cols = 1

                self.display3()

                self.root.add_widget(self.base)
                stopTouchApp()
                runTouchApp(self.root)

        def switchScenes1(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene1(name = 'scene1'))

        def switchScenes2(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene2(name = 'scene2'))

        def switchScenes4(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene4(name = 'scene4'))

        def display3(self):
                                 
#******************Tabs for Different Parts of Sheet***************************************

                self.StatsInfo = Button(text = "[color=ffffff]Stats Info",
                                     markup = True, size_hint_y = None, height = 20)
                self.StatsInfo.bind(on_press = self.switchScenes1)
                self.tabs.add_widget(self.StatsInfo)

                self.RPInfo = Button(text = "[color=ffffff]RP Info",
                                     markup = True, size_hint_y = None, height = 20)
                self.RPInfo.bind(on_press = self.switchScenes2)
                self.tabs.add_widget(self.RPInfo)

                self.SpellInfo = Button(text = "[color=ffffff]Spells",
                                     markup = True, size_hint_y = None, height = 20)
                self.SpellInfo.bind(on_press = self.switchScenes4)
                self.tabs.add_widget(self.SpellInfo)

#****************Display Data/Data Entry Fields********************************************
        
                self.charName = Label(text = "[color=ffffff]Name: " + self.character.name,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charName)

                self.charRace = Label(text = "[color=ffffff]Race: " + self.character.race,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charRace)

                self.charClss = Label(text = "[color=ffffff]Class: " + self.character.clss,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charClss)

                self.tAlignment = TextInput(size_hint_y = None, height = 30)
                self.tAlignment.text = self.character.alignment
                self.fullSheetS.add_widget(self.tAlignment)

                self.charLevel = Label(text = "[color=ffffff]Level: " + str(self.character.level),
                                       markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charLevel)

#************************EXP PopupB********************************************************

                self.charLevele = Label(text = "[color=ffffff]Level: " + str(self.character.level),
                                       markup = True, size_hint_y = None, height = 20)

                self.charExpe = Label(text = "[color=ffffff]Exp: " + str(self.character.exp),
                                     markup = True, size_hint_y = None, height = 20)

                self.amountExp = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.amountExp.text = "0"

                self.addExp = Button(text = "[color=ffffff]Add Exp",
                                     markup = True, size_hint_y = None, height = 20)
                self.addExp.bind(on_press = self.updateExp)

                self.expPopup = Popup(title='Add exp', size_hint=(None, None),
                                      size=(250, 250))

                self.expPopup.add_widget(self.popupGrid)
                self.popupGrid.add_widget(self.charLevele)
                self.popupGrid.add_widget(self.charExpe)
                self.popupGrid.add_widget(self.amountExp)
                self.popupGrid.add_widget(self.addExp)

#***********************EXP PopupE*********************************************************

                self.charExp = Button(text = "[color=ffffff]Exp: " + str(self.character.exp),
                                     markup = True, size_hint_y = None, height = 20)
                self.charExp.bind(on_press = self.expPopup.open)
                self.fullSheetS.add_widget(self.charExp)

#***********************Atacks and Spellcasting(Weapons)**********************************

                self.charWep = Label(text = "[color=ffffff]Attacks and Spellcasting: ",
                                           markup = True, size_hint_y=None, height=20)
                self.wepTitle.add_widget(self.charWep)

                self.charWepN = Label(text = "[color=ffffff]Name",
                                           markup = True, size_hint_y=None, height=20)
                self.wep.add_widget(self.charWepN)

                self.charWepAB = Label(text = "[color=ffffff]Attack Bonus",
                                           markup = True, size_hint_y=None, height=20)
                self.wep.add_widget(self.charWepAB)

                self.charWepD = Label(text = "[color=ffffff]Damage/Type",
                                           markup = True, size_hint_y=None, height=20)
                self.wep.add_widget(self.charWepD)
                
                self.tWep0 = TextInput()
                self.tWep0.text = self.character.wep[0]
                self.wep.add_widget(self.tWep0)

                self.tWepAB0 = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.tWepAB0.text = str(self.character.wepAB[0])
                self.wep.add_widget(self.tWepAB0)

                self.tWepDmg0 = TextInput()
                self.tWepDmg0.text = self.character.wepDmg[0]
                self.wep.add_widget(self.tWepDmg0)

                self.tWep1 = TextInput()
                self.tWep1.text = self.character.wep[1]
                self.wep.add_widget(self.tWep1)

                self.tWepAB1 = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.tWepAB1.text = str(self.character.wepAB[1])
                self.wep.add_widget(self.tWepAB1)

                self.tWepDmg1 = TextInput()
                self.tWepDmg1.text = self.character.wepDmg[1]
                self.wep.add_widget(self.tWepDmg1)

                self.tWep2 = TextInput()
                self.tWep2.text = self.character.wep[2]
                self.wep.add_widget(self.tWep2)

                self.tWepAB2 = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.tWepAB2.text = str(self.character.wepAB[2])
                self.wep.add_widget(self.tWepAB2)

                self.tWepDmg2 = TextInput()
                self.tWepDmg2.text = self.character.wepDmg[2]
                self.wep.add_widget(self.tWepDmg2)

                self.tWep3 = TextInput()
                self.tWep3.text = self.character.wep[3]
                self.wep.add_widget(self.tWep3)

                self.tWepAB3 = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.tWepAB3.text = str(self.character.wepAB[3])
                self.wep.add_widget(self.tWepAB3)

                self.tWepDmg3 = TextInput()
                self.tWepDmg3.text = self.character.wepDmg[3]
                self.wep.add_widget(self.tWepDmg3)

                self.tWep4 = TextInput()
                self.tWep4.text = self.character.wep[4]
                self.wep.add_widget(self.tWep4)

                self.tWepAB4 = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.tWepAB4.text = str(self.character.wepAB[4])
                self.wep.add_widget(self.tWepAB4)

                self.tWepDmg4 = TextInput()
                self.tWepDmg4.text = self.character.wepDmg[4]
                self.wep.add_widget(self.tWepDmg4)

                self.tWep5 = TextInput()
                self.tWep5.text = self.character.wep[5]
                self.wep.add_widget(self.tWep5)

                self.tWepAB5 = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.tWepAB5.text = str(self.character.wepAB[5])
                self.wep.add_widget(self.tWepAB5)

                self.tWepDmg5 = TextInput()
                self.tWepDmg5.text = self.character.wepDmg[5]
                self.wep.add_widget(self.tWepDmg5)
                

#**********************Equipment Data******************************************************

                self.charEquipment = Label(text = "[color=ffffff]Equipment: ",
                                           markup = True, size_hint_y=None, height=200)
                self.inputField.add_widget(self.charEquipment)
                self.tEquipment = TextInput()
                self.tEquipment.text = self.character.equipment
                self.inputField.add_widget(self.tEquipment)

                self.charCP = Label(text = "[color=ffffff]CP: ",
                                           markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charCP)
                self.tCP = TextInput(input_filter = 'int')
                self.tCP.text = str(self.character.CP)
                self.inputField.add_widget(self.tCP)

                self.charSP = Label(text = "[color=ffffff]SP: ",
                                           markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charSP)
                self.tSP = TextInput(input_filter = 'int')
                self.tSP.text = str(self.character.SP)
                self.inputField.add_widget(self.tSP)

                self.charEP = Label(text = "[color=ffffff]EP: ",
                                           markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charEP)
                self.tEP = TextInput(input_filter = 'int')
                self.tEP.text = str(self.character.EP)
                self.inputField.add_widget(self.tEP)

                self.charGP = Label(text = "[color=ffffff]GP: ",
                                           markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charGP)
                self.tGP = TextInput(input_filter = 'int')
                self.tGP.text = str(self.character.GP)
                self.inputField.add_widget(self.tGP)

                self.charPP = Label(text = "[color=ffffff]PP: ",
                                           markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charPP)
                self.tPP = TextInput(input_filter = 'int')
                self.tPP.text = str(self.character.PP)
                self.inputField.add_widget(self.tPP)

                self.saveChar = Button(text = "[color=ffffff]Save",
                                       markup = True,size_hint_y = None, height = 50)
                self.saveChar.bind(on_press = lambda x:self.saveExisting())
                self.base.add_widget(self.saveChar)

        def updateExp(self, instance):
                self.character.exp += int(self.amountExp.text)
                self.expPopup.dismiss()
                tempLvl = self.character.level
                self.character.setLevel()
                self.saveExisting()

                self.charLevele.text = "[color=ffffff]Level: " + str(self.character.level)

                self.charExpe.text = "[color=ffffff]Exp: " + str(self.character.exp)
                
                self.charExp.text = "[color=ffffff]Exp: " + str(self.character.exp)
                if(tempLvl < self.character.level):
                        self.updateHp(instance, self.character.level - tempLvl)

        def updateHp(self, instance, difference):
                self.addRoll = Button(text = "[color=ffffff]Roll: " + str(self.character.healthVals[self.character.clss][1]),
                                     markup = True, size_hint_y = None, height = 20)
                self.addRoll.bind(on_press = lambda x:self.rollHp(instance, difference))
                self.addBase = Button(text = "[color=ffffff]Base Value: " + str(self.character.healthVals[self.character.clss][0]),
                                     markup = True, size_hint_y = None, height = 20)
                self.addBase.bind(on_press = lambda x:self.baseHp(instance, difference))

                self.levelUp = Popup(title='Roll HP or add base HP?', size_hint=(None, None),
                                      size=(400, 400))

                try:
                        self.levelUp.add_widget(self.popupGrid2)
                except kivy.uix.widget.WidgetException:
                        self.popupGrid2.add_widget(self.addRoll)
                        self.popupGrid2.add_widget(self.addBase)
                        
                self.popupGrid2.add_widget(self.addRoll)
                self.popupGrid2.add_widget(self.addBase)

                self.levelUp.open()

        def baseHp(self, instance, difference):
                self.levelUp.dismiss()
                self.character.hpChange(instance, "base")
                self.saveExisting()
                difference -= 1
                if(difference != 0):
                        self.hpAddBasic(instance, difference)

        def rollHp(self, instance, difference):
                self.levelUp.dismiss()
                self.character.hpChange(instance, "roll")
                self.saveExisting()
                difference -= 1
                if(difference != 0):
                        self.hpAddRoll(instance, difference)

        def saveExisting(self):
                self.character.equipment = self.tEquipment.text
                self.character.alignment = self.tAlignment.text
                self.character.CP = self.tCP.text
                self.character.SP = self.tSP.text
                self.character.EP = self.tEP.text
                self.character.GP = self.tGP.text
                self.character.PP = self.tPP.text
                
                self.character.wep[0] = self.tWep0.text
                self.character.wepAB[0] = self.tWepAB0.text
                self.character.wepDmg[0] = self.tWepDmg0.text
                self.character.wep[1] = self.tWep1.text
                self.character.wepAB[1] = self.tWepAB1.text
                self.character.wepDmg[1] = self.tWepDmg1.text
                self.character.wep[2] = self.tWep2.text
                self.character.wepAB[2] = self.tWepAB2.text
                self.character.wepDmg[2] = self.tWepDmg2.text
                self.character.wep[3] = self.tWep3.text
                self.character.wepAB[3] = self.tWepAB3.text
                self.character.wepDmg[3] = self.tWepDmg3.text
                self.character.wep[4] = self.tWep4.text
                self.character.wepAB[4] = self.tWepAB4.text
                self.character.wepDmg[4] = self.tWepDmg4.text
                self.character.wep[5] = self.tWep5.text
                self.character.wepAB[5] = self.tWepAB5.text
                self.character.wepDmg[5] = self.tWepDmg5.text

                self.character.storeExisting()


class Scene4(Screen):
        def __init__(self, **kwargs):
                super(Scene4, self).__init__(**kwargs)
                self.character = DnDRollerChar.sheet()
                self.character.loadChar()
                self.character.bootChar(tempInd)
                
#*******************Initalize Grids********************************************************

                self.base = GridLayout(cols=1, spacing=10, size_hint_y=None, size_hint_x=1)
                self.base.bind(minimum_height = self.base.setter('height'))
                self.root = ScrollView(size_hint=(None, None), size=(Window.width, Window.height))

                self.fullSheetS = GridLayout(size_hint_y=None)
                self.fullSheetS.cols = 2
                self.fullSheetS.bind(minimum_height = self.fullSheetS.setter('height'))
                self.base.add_widget(self.fullSheetS)

                self.tabs = GridLayout(size_hint_y=None)
                self.tabs.cols = 3
                self.tabs.bind(minimum_height = self.tabs.setter('height'))
                self.base.add_widget(self.tabs)

                self.colBuilder = GridLayout(size_hint_y=None)
                self.colBuilder.cols = 1
                self.colBuilder.bind(minimum_height = self.colBuilder.setter('height'))
                self.base.add_widget(self.colBuilder)

                self.inputField = GridLayout(size_hint_y=None)
                self.inputField.cols = 2
                self.inputField.bind(minimum_height = self.inputField.setter('height'))
                self.colBuilder.add_widget(self.inputField)

                self.spellGridT0 = GridLayout(size_hint_y=None)
                self.spellGridT0.cols = 1
                self.spellGridT0.bind(minimum_height = self.spellGridT0.setter('height'))
                self.colBuilder.add_widget(self.spellGridT0)

                self.spellGrid0 = GridLayout(size_hint_y=None)
                self.spellGrid0.cols = 2
                self.spellGrid0.bind(minimum_height = self.spellGrid0.setter('height'))
                self.colBuilder.add_widget(self.spellGrid0)

                self.spellGridT1 = GridLayout(size_hint_y=None)
                self.spellGridT1.cols = 1
                self.spellGridT1.bind(minimum_height = self.spellGridT1.setter('height'))
                self.colBuilder.add_widget(self.spellGridT1)

                self.spellGrid1 = GridLayout(size_hint_y=None)
                self.spellGrid1.cols = 2
                self.spellGrid1.bind(minimum_height = self.spellGrid1.setter('height'))
                self.colBuilder.add_widget(self.spellGrid1)

                self.spellGridT2 = GridLayout(size_hint_y=None)
                self.spellGridT2.cols = 1
                self.spellGridT2.bind(minimum_height = self.spellGridT2.setter('height'))
                self.colBuilder.add_widget(self.spellGridT2)

                self.spellGrid2 = GridLayout(size_hint_y=None)
                self.spellGrid2.cols = 2
                self.spellGrid2.bind(minimum_height = self.spellGrid2.setter('height'))
                self.colBuilder.add_widget(self.spellGrid2)

                self.spellGridT3 = GridLayout(size_hint_y=None)
                self.spellGridT3.cols = 1
                self.spellGridT3.bind(minimum_height = self.spellGridT3.setter('height'))
                self.colBuilder.add_widget(self.spellGridT3)

                self.spellGrid3 = GridLayout(size_hint_y=None)
                self.spellGrid3.cols = 2
                self.spellGrid3.bind(minimum_height = self.spellGrid3.setter('height'))
                self.colBuilder.add_widget(self.spellGrid3)

                self.spellGridT4 = GridLayout(size_hint_y=None)
                self.spellGridT4.cols = 1
                self.spellGridT4.bind(minimum_height = self.spellGridT4.setter('height'))
                self.colBuilder.add_widget(self.spellGridT4)

                self.spellGrid4 = GridLayout(size_hint_y=None)
                self.spellGrid4.cols = 2
                self.spellGrid4.bind(minimum_height = self.spellGrid4.setter('height'))
                self.colBuilder.add_widget(self.spellGrid4)

                self.spellGridT5 = GridLayout(size_hint_y=None)
                self.spellGridT5.cols = 1
                self.spellGridT5.bind(minimum_height = self.spellGridT5.setter('height'))
                self.colBuilder.add_widget(self.spellGridT5)

                self.spellGrid5 = GridLayout(size_hint_y=None)
                self.spellGrid5.cols = 2
                self.spellGrid5.bind(minimum_height = self.spellGrid5.setter('height'))
                self.colBuilder.add_widget(self.spellGrid5)

                self.spellGridT6 = GridLayout(size_hint_y=None)
                self.spellGridT6.cols = 1
                self.spellGridT6.bind(minimum_height = self.spellGridT6.setter('height'))
                self.colBuilder.add_widget(self.spellGridT6)

                self.spellGrid6 = GridLayout(size_hint_y=None)
                self.spellGrid6.cols = 2
                self.spellGrid6.bind(minimum_height = self.spellGrid6.setter('height'))
                self.colBuilder.add_widget(self.spellGrid6)

                self.spellGridT7 = GridLayout(size_hint_y=None)
                self.spellGridT7.cols = 1
                self.spellGridT7.bind(minimum_height = self.spellGridT7.setter('height'))
                self.colBuilder.add_widget(self.spellGridT7)

                self.spellGrid7 = GridLayout(size_hint_y=None)
                self.spellGrid7.cols = 2
                self.spellGrid7.bind(minimum_height = self.spellGrid7.setter('height'))
                self.colBuilder.add_widget(self.spellGrid7)

                self.spellGridT8 = GridLayout(size_hint_y=None)
                self.spellGridT8.cols = 1
                self.spellGridT8.bind(minimum_height = self.spellGridT8.setter('height'))
                self.colBuilder.add_widget(self.spellGridT8)

                self.spellGrid8 = GridLayout(size_hint_y=None)
                self.spellGrid8.cols = 2
                self.spellGrid8.bind(minimum_height = self.spellGrid8.setter('height'))
                self.colBuilder.add_widget(self.spellGrid8)

                self.spellGridT9 = GridLayout(size_hint_y=None)
                self.spellGridT9.cols = 1
                self.spellGridT9.bind(minimum_height = self.spellGridT9.setter('height'))
                self.colBuilder.add_widget(self.spellGridT9)

                self.spellGrid9 = GridLayout(size_hint_y=None)
                self.spellGrid9.cols = 2
                self.spellGrid9.bind(minimum_height = self.spellGrid9.setter('height'))
                self.colBuilder.add_widget(self.spellGrid9)

                self.popupGrid = GridLayout(size_hint_y=None)
                self.popupGrid.cols = 1

                self.display4()

                self.root.add_widget(self.base)
                stopTouchApp()
                runTouchApp(self.root)

        def switchScenes1(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene1(name = 'scene1'))

        def switchScenes2(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene2(name = 'scene2'))

        def switchScenes3(self, instance):
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene3(name = 'scene3'))

        def display4(self):
                                 
#******************Tabs for Different Parts of Sheet***************************************

                self.StatsInfo = Button(text = "[color=ffffff]Stats Info",
                                     markup = True, size_hint_y = None, height = 20)
                self.StatsInfo.bind(on_press = self.switchScenes1)
                self.tabs.add_widget(self.StatsInfo)

                self.RPInfo = Button(text = "[color=ffffff]RP Info",
                                     markup = True, size_hint_y = None, height = 20)
                self.RPInfo.bind(on_press = self.switchScenes2)
                self.tabs.add_widget(self.RPInfo)

                self.EquipInfo = Button(text = "[color=ffffff]Equipment",
                                     markup = True, size_hint_y = None, height = 20)
                self.EquipInfo.bind(on_press = self.switchScenes3)
                self.tabs.add_widget(self.EquipInfo)

#****************Display Data/Data Entry Fields********************************************
        
                self.charName = Label(text = "[color=ffffff]Name: " + self.character.name,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charName)

                self.charRace = Label(text = "[color=ffffff]Race: " + self.character.race,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charRace)

                self.charClss = Label(text = "[color=ffffff]Class: " + self.character.clss,
                                      markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charClss)

                self.tAlignment = TextInput(size_hint_y = None, height = 30)
                self.tAlignment.text = self.character.alignment
                self.fullSheetS.add_widget(self.tAlignment)

                self.charLevel = Label(text = "[color=ffffff]Level: " + str(self.character.level),
                                       markup = True, size_hint_y = None, height = 20)
                self.fullSheetS.add_widget(self.charLevel)

#************************EXP PopupB********************************************************

                self.charLevele = Label(text = "[color=ffffff]Level: " + str(self.character.level),
                                       markup = True, size_hint_y = None, height = 20)

                self.charExpe = Label(text = "[color=ffffff]Exp: " + str(self.character.exp),
                                     markup = True, size_hint_y = None, height = 20)

                self.amountExp = TextInput(size_hint_y = None, height = 30,
                                           input_filter = 'int')
                self.amountExp.text = "0"

                self.addExp = Button(text = "[color=ffffff]Add Exp",
                                     markup = True, size_hint_y = None, height = 20)
                self.addExp.bind(on_press = self.updateExp)

                self.expPopup = Popup(title='Add exp', size_hint=(None, None),
                                      size=(250, 250))

                self.expPopup.add_widget(self.popupGrid)
                self.popupGrid.add_widget(self.charLevele)
                self.popupGrid.add_widget(self.charExpe)
                self.popupGrid.add_widget(self.amountExp)
                self.popupGrid.add_widget(self.addExp)

#***********************EXP PopupE*********************************************************

                self.charExp = Button(text = "[color=ffffff]Exp: " + str(self.character.exp),
                                     markup = True, size_hint_y = None, height = 20)
                self.charExp.bind(on_press = self.expPopup.open)
                self.fullSheetS.add_widget(self.charExp)
                
#********************Spell Caster's data****************************************

                self.charSA = Label(text = "[color=ffffff]Spellcasting Ability: ",
                                           markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charSA)
                self.tSA = TextInput(input_filter = 'int')
                self.tSA.text = str(self.character.SA)
                self.inputField.add_widget(self.tSA)

                self.charSDC = Label(text = "[color=ffffff]Spell Save DC: ",
                                           markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charSDC)
                self.tSDC = TextInput(input_filter = 'int')
                self.tSDC.text = str(self.character.SDC)
                self.inputField.add_widget(self.tSDC)

                self.charSAB = Label(text = "[color=ffffff]Spell Attack Bonus: ",
                                           markup = True, size_hint_y=None, height=30)
                self.inputField.add_widget(self.charSAB)
                self.tSAB = TextInput(input_filter = 'int')
                self.tSAB.text = str(self.character.SAB)
                self.inputField.add_widget(self.tSAB)

                self.spellGen()

                self.saveChar = Button(text = "[color=ffffff]Save",
                                       markup = True,size_hint_y = None, height = 50)
                self.saveChar.bind(on_press = lambda x:self.saveExisting())
                self.base.add_widget(self.saveChar)

#*******************Spell Table************************************************

        def spellGen(self):
                self.cantrips = Label(text = "[color=ffffff]Cantrips",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT0.add_widget(self.cantrips)

                self.tCan = [TextInput(size_hint_y=None, height=150)]
                self.tCan[0].text = self.character.spells[0][0]
                self.spellGrid0.add_widget(self.tCan[0])

                self.deltCan = [Button(text = "[color=ffffff]Delete Spell 0 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.deltCan[0].bind(on_press = self.updateSR)
                self.spellGrid0.add_widget(self.deltCan[0])
                
                for i in range(1 , int(self.character.numOfSpells[0])):
                        self.tCan.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tCan[i].text = self.character.spells[0][i]
                        except IndexError:
                                self.tCan[i].text = self.character.defaultSpell
                        self.spellGrid0.add_widget(self.tCan[i])

                        self.deltCan.append(Button(text = "[color=ffffff]Delete Spell 0 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.deltCan[i].bind(on_press = self.updateSR)
                        self.spellGrid0.add_widget(self.deltCan[i])
                
                self.addCan = Button(text = "[color=ffffff]Add Cantrip",
                                       markup = True,size_hint_y = None, height = 50)
                self.addCan.bind(on_press = lambda x:self.updateSN(self, 0))
                self.spellGrid0.add_widget(self.addCan)

                self.SL1 = Label(text = "[color=ffffff]Spell Level 1",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT1.add_widget(self.SL1)

#~~~~~~~~~~~~~~~~~~~~spell stots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL1TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid1.add_widget(self.SL1TS)

                self.tSL1TS = TextInput(size_hint_y=None, height=30)
                self.tSL1TS.text = self.character.spellSlots[1]
                self.spellGrid1.add_widget(self.tSL1TS)

                self.SL1RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid1.add_widget(self.SL1RS)

                self.tSL1RS = TextInput(size_hint_y=None, height=30)
                self.tSL1RS.text = self.character.remainingSpells[1]
                self.spellGrid1.add_widget(self.tSL1RS)

#~~~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL1 = [TextInput(size_hint_y=None, height=150)]
                self.tSL1[0].text = self.character.spells[1][0]
                self.spellGrid1.add_widget(self.tSL1[0])
                
                self.DeltSL1 = [Button(text = "[color=ffffff]Delete Spell 1 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL1[0].bind(on_press = self.updateSR)
                self.spellGrid1.add_widget(self.DeltSL1[0])
                
                for i in range(1 , int(self.character.numOfSpells[1])):
                        self.tSL1.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL1[i].text = self.character.spells[1][i]
                        except IndexError:
                                self.tSL1[i].text = self.character.defaultSpell
                        self.spellGrid1.add_widget(self.tSL1[i])

                        self.DeltSL1.append(Button(text = "[color=ffffff]Delete Spell 1 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL1[i].bind(on_press = self.updateSR)
                        self.spellGrid1.add_widget(self.DeltSL1[i])
                
                self.addtSL1 = Button(text = "[color=ffffff]Add Level 1 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL1.bind(on_press = lambda x:self.updateSN(self, 1))
                self.spellGrid1.add_widget(self.addtSL1)
                
                self.SL2 = Label(text = "[color=ffffff]Spell Level 2",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT2.add_widget(self.SL2)

#~~~~~~~~~~~~~~~~~~~~~~~~spell slots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL2TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid2.add_widget(self.SL2TS)

                self.tSL2TS = TextInput(size_hint_y=None, height=30)
                self.tSL2TS.text = self.character.spellSlots[2]
                self.spellGrid2.add_widget(self.tSL2TS)

                self.SL2RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid2.add_widget(self.SL2RS)

                self.tSL2RS = TextInput(size_hint_y=None, height=30)
                self.tSL2RS.text = self.character.remainingSpells[2]
                self.spellGrid2.add_widget(self.tSL2RS)

#~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL2 = [TextInput(size_hint_y=None, height=150)]
                self.tSL2[0].text = self.character.spells[2][0]
                self.spellGrid2.add_widget(self.tSL2[0])

                self.DeltSL2 = [Button(text = "[color=ffffff]Delete Spell 2 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL2[0].bind(on_press = self.updateSR)
                self.spellGrid2.add_widget(self.DeltSL2[0])
                
                for i in range(1 , int(self.character.numOfSpells[2])):
                        self.tSL2.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL2[i].text = self.character.spells[2][i]
                        except IndexError:
                                self.tSL2[i].text = self.character.defaultSpell
                        self.spellGrid2.add_widget(self.tSL2[i])

                        self.DeltSL2.append(Button(text = "[color=ffffff]Delete Spell 2 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL2[i].bind(on_press = self.updateSR)
                        self.spellGrid2.add_widget(self.DeltSL2[i])
                
                self.addtSL2 = Button(text = "[color=ffffff]Add Level 2 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL2.bind(on_press = lambda x:self.updateSN(self, 2))
                self.spellGrid2.add_widget(self.addtSL2)

                self.SL3 = Label(text = "[color=ffffff]Spell Level 3",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT3.add_widget(self.SL3)

#~~~~~~~~~~~~~~~~~~~~~~~~spell slots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL3TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid3.add_widget(self.SL3TS)

                self.tSL3TS = TextInput(size_hint_y=None, height=30)
                self.tSL3TS.text = self.character.spellSlots[3]
                self.spellGrid3.add_widget(self.tSL3TS)

                self.SL3RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid3.add_widget(self.SL3RS)

                self.tSL3RS = TextInput(size_hint_y=None, height=30)
                self.tSL3RS.text = self.character.remainingSpells[3]
                self.spellGrid3.add_widget(self.tSL3RS)

#~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL3 = [TextInput(size_hint_y=None, height=150)]
                self.tSL3[0].text = self.character.spells[3][0]
                self.spellGrid3.add_widget(self.tSL3[0])

                self.DeltSL3 = [Button(text = "[color=ffffff]Delete Spell 3 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL3[0].bind(on_press = self.updateSR)
                self.spellGrid3.add_widget(self.DeltSL3[0])
                
                for i in range(1 , int(self.character.numOfSpells[3])):
                        self.tSL3.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL3[i].text = self.character.spells[3][i]
                        except IndexError:
                                self.tSL3[i].text = self.character.defaultSpell
                        self.spellGrid.add_widget(self.tSL3[i])

                        self.DeltSL3.append(Button(text = "[color=ffffff]Delete Spell 3 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL3[i].bind(on_press = self.updateSR)
                        self.spellGrid3.add_widget(self.DeltSL3[i])
                
                self.addtSL3 = Button(text = "[color=ffffff]Add Level 3 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL3.bind(on_press = lambda x:self.updateSN(self, 3))
                self.spellGrid3.add_widget(self.addtSL3)

                self.SL4 = Label(text = "[color=ffffff]Spell Level 4",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT4.add_widget(self.SL4)

#~~~~~~~~~~~~~~~~~~~~~~~~spell slots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL4TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid4.add_widget(self.SL4TS)

                self.tSL4TS = TextInput(size_hint_y=None, height=30)
                self.tSL4TS.text = self.character.spellSlots[4]
                self.spellGrid4.add_widget(self.tSL4TS)

                self.SL4RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid4.add_widget(self.SL4RS)

                self.tSL4RS = TextInput(size_hint_y=None, height=30)
                self.tSL4RS.text = self.character.remainingSpells[4]
                self.spellGrid4.add_widget(self.tSL4RS)

#~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL4 = [TextInput(size_hint_y=None, height=150)]
                self.tSL4[0].text = self.character.spells[4][0]
                self.spellGrid4.add_widget(self.tSL4[0])

                self.DeltSL4 = [Button(text = "[color=ffffff]Delete Spell 4 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL4[0].bind(on_press = self.updateSR)
                self.spellGrid4.add_widget(self.DeltSL4[0])
                
                for i in range(1 , int(self.character.numOfSpells[4])):
                        self.tSL4.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL4[i].text = self.character.spells[4][i]
                        except IndexError:
                                self.tSL4[i].text = self.character.defaultSpell
                        self.spellGrid4.add_widget(self.tSL4[i])

                        self.DeltSL4.append(Button(text = "[color=ffffff]Delete Spell 4 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL4[i].bind(on_press = self.updateSR)
                        self.spellGrid4.add_widget(self.DeltSL4[i])
                
                self.addtSL4 = Button(text = "[color=ffffff]Add Level 4 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL4.bind(on_press = lambda x:self.updateSN(self, 4))
                self.spellGrid4.add_widget(self.addtSL4)

                self.SL5 = Label(text = "[color=ffffff]Spell Level 5",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT5.add_widget(self.SL5)

#~~~~~~~~~~~~~~~~~~~~~~~~spell slots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL5TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid5.add_widget(self.SL5TS)

                self.tSL5TS = TextInput(size_hint_y=None, height=30)
                self.tSL5TS.text = self.character.spellSlots[5]
                self.spellGrid5.add_widget(self.tSL5TS)

                self.SL5RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid5.add_widget(self.SL5RS)

                self.tSL5RS = TextInput(size_hint_y=None, height=30)
                self.tSL5RS.text = self.character.remainingSpells[5]
                self.spellGrid5.add_widget(self.tSL5RS)

#~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL5 = [TextInput(size_hint_y=None, height=150)]
                self.tSL5[0].text = self.character.spells[5][0]
                self.spellGrid5.add_widget(self.tSL5[0])

                self.DeltSL5 = [Button(text = "[color=ffffff]Delete Spell 5 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL5[0].bind(on_press = self.updateSR)
                self.spellGrid5.add_widget(self.DeltSL5[0])
                
                for i in range(1 , int(self.character.numOfSpells[5])):
                        self.tSL5.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL5[i].text = self.character.spells[5][i]
                        except IndexError:
                                self.tSL5[i].text = self.character.defaultSpell
                        self.spellGrid5.add_widget(self.tSL5[i])

                        self.DeltSL5.append(Button(text = "[color=ffffff]Delete Spell 5 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL5[i].bind(on_press = self.updateSR)
                        self.spellGrid5.add_widget(self.DeltSL5[i])
                
                self.addtSL5 = Button(text = "[color=ffffff]Add Level 5 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL5.bind(on_press = lambda x:self.updateSN(self, 5))
                self.spellGrid5.add_widget(self.addtSL5)

                self.SL6 = Label(text = "[color=ffffff]Spell Level 6",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT6.add_widget(self.SL6)

#~~~~~~~~~~~~~~~~~~~~~~~~spell slots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL6TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid6.add_widget(self.SL6TS)

                self.tSL6TS = TextInput(size_hint_y=None, height=30)
                self.tSL6TS.text = self.character.spellSlots[6]
                self.spellGrid6.add_widget(self.tSL6TS)

                self.SL6RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid6.add_widget(self.SL6RS)

                self.tSL6RS = TextInput(size_hint_y=None, height=30)
                self.tSL6RS.text = self.character.remainingSpells[6]
                self.spellGrid6.add_widget(self.tSL6RS)

#~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL6 = [TextInput(size_hint_y=None, height=150)]
                self.tSL6[0].text = self.character.spells[6][0]
                self.spellGrid6.add_widget(self.tSL6[0])

                self.DeltSL6 = [Button(text = "[color=ffffff]Delete Spell 6 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL6[0].bind(on_press = self.updateSR)
                self.spellGrid6.add_widget(self.DeltSL6[0])
                
                for i in range(1 , int(self.character.numOfSpells[6])):
                        self.tSL6.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL6[i].text = self.character.spells[6][i]
                        except IndexError:
                                self.tSL6[i].text = self.character.defaultSpell
                        self.spellGrid6.add_widget(self.tSL6[i])

                        self.DeltSL6.append(Button(text = "[color=ffffff]Delete Spell 6 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL6[i].bind(on_press = self.updateSR)
                        self.spellGrid6.add_widget(self.DeltSL6[i])
                
                self.addtSL6 = Button(text = "[color=ffffff]Add Level 6 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL6.bind(on_press = lambda x:self.updateSN(self, 6))
                self.spellGrid6.add_widget(self.addtSL6)

                self.SL7 = Label(text = "[color=ffffff]Spell Level 7",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT7.add_widget(self.SL7)

#~~~~~~~~~~~~~~~~~~~~~~~~spell slots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL7TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid7.add_widget(self.SL7TS)

                self.tSL7TS = TextInput(size_hint_y=None, height=30)
                self.tSL7TS.text = self.character.spellSlots[7]
                self.spellGrid7.add_widget(self.tSL7TS)

                self.SL7RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid7.add_widget(self.SL7RS)

                self.tSL7RS = TextInput(size_hint_y=None, height=30)
                self.tSL7RS.text = self.character.remainingSpells[7]
                self.spellGrid7.add_widget(self.tSL7RS)

#~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL7 = [TextInput(size_hint_y=None, height=150)]
                self.tSL7[0].text = self.character.spells[7][0]
                self.spellGrid7.add_widget(self.tSL7[0])

                self.DeltSL7 = [Button(text = "[color=ffffff]Delete Spell 7 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL7[0].bind(on_press = self.updateSR)
                self.spellGrid7.add_widget(self.DeltSL7[0])
                
                for i in range(1 , int(self.character.numOfSpells[7])):
                        self.tSL7.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL7[i].text = self.character.spells[7][i]
                        except IndexError:
                                self.tSL7[i].text = self.character.defaultSpell
                        self.spellGrid7.add_widget(self.tSL7[i])

                        self.DeltSL7.append(Button(text = "[color=ffffff]Delete Spell 7 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL7[i].bind(on_press = self.updateSR)
                        self.spellGrid7.add_widget(self.DeltSL7[i])
                
                self.addtSL7 = Button(text = "[color=ffffff]Add Level 7 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL7.bind(on_press = lambda x:self.updateSN(self, 7))
                self.spellGrid7.add_widget(self.addtSL7)

                self.SL8 = Label(text = "[color=ffffff]Spell Level 8",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT8.add_widget(self.SL8)

#~~~~~~~~~~~~~~~~~~~~~~~~spell slots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL8TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid8.add_widget(self.SL8TS)

                self.tSL8TS = TextInput(size_hint_y=None, height=30)
                self.tSL8TS.text = self.character.spellSlots[8]
                self.spellGrid8.add_widget(self.tSL8TS)

                self.SL8RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid8.add_widget(self.SL8RS)

                self.tSL8RS = TextInput(size_hint_y=None, height=30)
                self.tSL8RS.text = self.character.remainingSpells[8]
                self.spellGrid8.add_widget(self.tSL8RS)

#~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL8 = [TextInput(size_hint_y=None, height=150)]
                self.tSL8[0].text = self.character.spells[8][0]
                self.spellGrid8.add_widget(self.tSL8[0])

                self.DeltSL8 = [Button(text = "[color=ffffff]Delete Spell 8 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL8[0].bind(on_press = self.updateSR)
                self.spellGrid8.add_widget(self.DeltSL8[0])
                
                for i in range(1 , int(self.character.numOfSpells[8])):
                        self.tSL8.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL8[i].text = self.character.spells[8][i]
                        except IndexError:
                                self.tSL8[i].text = self.character.defaultSpell
                        self.spellGrid8.add_widget(self.tSL8[i])

                        self.DeltSL8.append(Button(text = "[color=ffffff]Delete Spell 8 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL8[i].bind(on_press = self.updateSR)
                        self.spellGrid8.add_widget(self.DeltSL8[i])
                
                self.addtSL8 = Button(text = "[color=ffffff]Add Level 8 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL8.bind(on_press = lambda x:self.updateSN(self, 8))
                self.spellGrid8.add_widget(self.addtSL8)

                self.SL9 = Label(text = "[color=ffffff]Spell Level 9",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGridT9.add_widget(self.SL9)

#~~~~~~~~~~~~~~~~~~~~~~~~spell slots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.SL9TS = Label(text = "[color=ffffff]Total Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid9.add_widget(self.SL9TS)

                self.tSL9TS = TextInput(size_hint_y=None, height=30)
                self.tSL9TS.text = self.character.spellSlots[9]
                self.spellGrid9.add_widget(self.tSL9TS)

                self.SL9RS = Label(text = "[color=ffffff]Remaining Slots",
                                           markup = True, size_hint_y=None, height=30)
                self.spellGrid9.add_widget(self.SL9RS)

                self.tSL9RS = TextInput(size_hint_y=None, height=30)
                self.tSL9RS.text = self.character.remainingSpells[9]
                self.spellGrid9.add_widget(self.tSL9RS)

#~~~~~~~~~~~~~~~~~~~~~~~spells~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                self.tSL9 = [TextInput(size_hint_y=None, height=150)]
                self.tSL9[0].text = self.character.spells[9][0]
                self.spellGrid9.add_widget(self.tSL9[0])

                self.DeltSL9 = [Button(text = "[color=ffffff]Delete Spell 9 0",
                                       markup = True,size_hint_y = None, height = 50)]
                self.DeltSL9[0].bind(on_press = self.updateSR)
                self.spellGrid9.add_widget(self.DeltSL9[0])
                
                for i in range(1 , int(self.character.numOfSpells[9])):
                        self.tSL9.append(TextInput(size_hint_y=None, height=150))
                        try:
                                self.tSL9[i].text = self.character.spells[9][i]
                        except IndexError:
                                self.tSL9[i].text = self.character.defaultSpell
                        self.spellGrid9.add_widget(self.tSL9[i])

                        self.DeltSL9.append(Button(text = "[color=ffffff]Delete Spell 9 " + str(i),
                                       markup = True,size_hint_y = None, height = 50))
                        self.DeltSL9[i].bind(on_press = self.updateSR)
                        self.spellGrid9.add_widget(self.DeltSL9[i])
                
                self.addtSL9 = Button(text = "[color=ffffff]Add Level 9 Spell",
                                       markup = True,size_hint_y = None, height = 50)
                self.addtSL9.bind(on_press = lambda x:self.updateSN(self, 9))
                self.spellGrid9.add_widget(self.addtSL9)

                print(self.character.spells)
                print(self.character.numOfSpells)

#***********************Updaters************************************************

        def updateSN(self, instance, lvl):
                self.character.numOfSpells[lvl] = int(self.character.numOfSpells[lvl])
                self.character.numOfSpells[lvl] += 1
                self.character.spells[lvl].append("Spells")
                print(self.character.spells[lvl])
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene4(name = 'scene4'))

        def updateSR(self, instance):
                t = instance.text.split()
                print(t)
                lvl = int(t[2])
                sn = int(t[3])
                print(str(sn))
                temp = self.character.spells[lvl].pop(sn)
                print(self.character.spells[lvl])
                self.character.numOfSpells[lvl] = int(self.character.numOfSpells[lvl])
                self.character.numOfSpells[lvl] -= 1

                if(lvl == 0):
                        self.tCan.pop(sn)
                elif(lvl == 1):
                        self.tSL1.pop(sn)
                elif(lvl == 2):
                        self.tSL2.pop(sn)
                elif(lvl == 3):
                        self.tSL3.pop(sn)
                elif(lvl == 4):
                        self.tSL4.pop(sn)
                elif(lvl == 5):
                        self.tSL5.pop(sn)
                elif(lvl == 6):
                        self.tSL6.pop(sn)
                elif(lvl == 7):
                        self.tSL7.pop(sn)
                elif(lvl == 8):
                        self.tSL8.pop(sn)
                elif(lvl == 9):
                        self.tSL9.pop(sn)
                
                self.saveExisting()
                self.root.clear_widgets()
                sm.switch_to(Scene4(name = 'scene4'))

        def updateExp(self, instance):
                self.character.exp += int(self.amountExp.text)
                self.expPopup.dismiss()
                tempLvl = self.character.level
                self.character.setLevel()
                self.saveExisting()

                self.charLevele.text = "[color=ffffff]Level: " + str(self.character.level)

                self.charExpe.text = "[color=ffffff]Exp: " + str(self.character.exp)
                
                self.charExp.text = "[color=ffffff]Exp: " + str(self.character.exp)
                if(tempLvl < self.character.level):
                        self.updateHp(instance, self.character.level - tempLvl)

        def updateHp(self, instance, difference):
                self.addRoll = Button(text = "[color=ffffff]Roll: " + str(self.character.healthVals[self.character.clss][1]),
                                     markup = True, size_hint_y = None, height = 20)
                self.addRoll.bind(on_press = lambda x:self.rollHp(instance, difference))
                self.addBase = Button(text = "[color=ffffff]Base Value: " + str(self.character.healthVals[self.character.clss][0]),
                                     markup = True, size_hint_y = None, height = 20)
                self.addBase.bind(on_press = lambda x:self.baseHp(instance, difference))

                self.levelUp = Popup(title='Roll HP or add base HP?', size_hint=(None, None),
                                      size=(400, 400))

                try:
                        self.levelUp.add_widget(self.popupGrid2)
                except kivy.uix.widget.WidgetException:
                        self.popupGrid2.add_widget(self.addRoll)
                        self.popupGrid2.add_widget(self.addBase)
                        
                self.popupGrid2.add_widget(self.addRoll)
                self.popupGrid2.add_widget(self.addBase)

                self.levelUp.open()

        def baseHp(self, instance, difference):
                self.levelUp.dismiss()
                self.character.hpChange(instance, "base")
                self.saveExisting()
                difference -= 1
                if(difference != 0):
                        self.hpAddBasic(instance, difference)

        def rollHp(self, instance, difference):
                self.levelUp.dismiss()
                self.character.hpChange(instance, "roll")
                self.saveExisting()
                difference -= 1
                if(difference != 0):
                        self.hpAddRoll(instance, difference)

        def saveExisting(self):
                self.character.alignment = self.tAlignment.text
                self.character.SA = self.tSA.text
                self.character.SDC = self.tSDC.text
                self.character.SAB = self.tSAB.text
                
                self.character.spellSlots[1] = int(self.tSL1TS.text)
                self.character.remainingSpells[1] = int(self.tSL1RS.text)
                self.character.spellSlots[2] = int(self.tSL2TS.text)
                self.character.remainingSpells[2] = int(self.tSL2RS.text)
                self.character.spellSlots[3] = int(self.tSL3TS.text)
                self.character.remainingSpells[3] = int(self.tSL3RS.text)
                self.character.spellSlots[4] = int(self.tSL4TS.text)
                self.character.remainingSpells[4] = int(self.tSL4RS.text)
                self.character.spellSlots[5] = int(self.tSL5TS.text)
                self.character.remainingSpells[5] = int(self.tSL5RS.text)
                self.character.spellSlots[6] = int(self.tSL6TS.text)
                self.character.remainingSpells[6] = int(self.tSL6RS.text)
                self.character.spellSlots[7] = int(self.tSL7TS.text)
                self.character.remainingSpells[7] = int(self.tSL7RS.text)
                self.character.spellSlots[8] = int(self.tSL8TS.text)
                self.character.remainingSpells[8] = int(self.tSL8RS.text)
                self.character.spellSlots[9] = int(self.tSL9TS.text)
                self.character.remainingSpells[9] = int(self.tSL9RS.text)
                
                for i in range(len(self.tCan)):
                        try:
                                self.character.spells[0][i] = self.tCan[i].text
                        except IndexError:
                                self.character.spells[0].append(self.tCan[i].text)

                for i in range(len(self.tSL1)):
                        try:
                                self.character.spells[1][i] = self.tSL1[i].text
                        except IndexError:
                                self.character.spells[1].append(self.tSL1[i].text)

                for i in range(len(self.tSL2)):
                        try:
                                self.character.spells[2][i] = self.tSL2[i].text
                        except IndexError:
                                self.character.spells[2].append(self.tSL2[i].text)

                for i in range(len(self.tSL3)):
                        try:
                                self.character.spells[3][i] = self.tSL3[i].text
                        except IndexError:
                                self.character.spells[3].append(self.tSL3[i].text)

                for i in range(len(self.tSL4)):
                        try:
                                self.character.spells[4][i] = self.tSL4[i].text
                        except IndexError:
                                self.character.spells[4].append(self.tSL4[i].text)

                for i in range(len(self.tSL5)):
                        try:
                                self.character.spells[5][i] = self.tSL5[i].text
                        except IndexError:
                                self.character.spells[5].append(self.tSL5[i].text)

                for i in range(len(self.tSL6)):
                        try:
                                self.character.spells[6][i] = self.tSL6[i].text
                        except IndexError:
                                self.character.spells[6].append(self.tSL6[i].text)

                for i in range(len(self.tSL7)):
                        try:
                                self.character.spells[7][i] = self.tSL7[i].text
                        except IndexError:
                                self.character.spells[7].append(self.tSL7[i].text)

                for i in range(len(self.tSL8)):
                        try:
                                self.character.spells[8][i] = self.tSL8[i].text
                        except IndexError:
                                self.character.spells[8].append(self.tSL8[i].text)

                for i in range(len(self.tSL9)):
                        try:
                                self.character.spells[9][i] = self.tSL9[i].text
                        except IndexError:
                                self.character.spells[9].append(self.tSL9[i].text)

                self.character.storeExisting()
