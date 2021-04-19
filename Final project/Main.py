import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Evaluate_teams import Ui_Evaluate
abc=sqlite3.connect('match.db')
cur=abc.cursor()


class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 3, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setReadOnly(True)
        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setReadOnly(True)
        self.gridLayout_4.addWidget(self.lineEdit_2, 0, 4, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)
        self.gridLayout_4.addWidget(self.lineEdit_4, 1, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_6, 1, 3, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_3.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_3.addWidget(self.radioButton_4, 0, 3, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_3.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_3.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 1, 0, 1, 4)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_2.addWidget(self.listWidget_2, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.frame_3, 2, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(MainWindow)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionEvaluate_Team.triggered.connect(self.evaluate_teams)
        self.menuManage_Teams.addAction(self.actionNew_Team)
        self.menuManage_Teams.addAction(self.actionOpen_Team)
        self.menuManage_Teams.addAction(self.actionSave_Team)
        self.menuManage_Teams.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.radioButton.toggled.connect(self.checkstate)
        self.radioButton_2.toggled.connect(self.checkstate)
        self.radioButton_3.toggled.connect(self.checkstate)
        self.radioButton_4.toggled.connect(self.checkstate)
        self.listWidget.itemDoubleClicked.connect(self.removelist1)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)

        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.label_4.setText(_translate("MainWindow", "Wicket-Keeper (WK)"))
        self.label_3.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label_2.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label_5.setText(_translate("MainWindow", "Points Available"))
        self.label_6.setText(_translate("MainWindow", "Points Used"))
        self.radioButton_2.setText(_translate("MainWindow", "BOW"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.label_7.setText(_translate("MainWindow", "Team Name"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionSave_Team.setText(_translate("MainWindow", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))


    def menu(self,action):
        txt=action.text()
        if txt=='New Team':
            
            self.bat_count=0
            self.ball_count=0
            self.ar_count=0
            self.wicket_count=0

            self.avl=1000
            self.used=0
            self.listWidget.clear()
            self.listWidget_2.clear()


            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "New Team", "Enter name of team:")
            if ok:
                self.lineEdit_7.setText(str(text))

            self.show()
        if txt=='Save Team':
           if self.bat_count+self.ball_count+self.ar_count+self.wicket_count==11:              
               count=self.listWidget_2.count()
               selected=""

               for i in range(count):
                   selected+=self.listWidget_2.item(i).text()
                   if i<count-1:
                       selected+=","
               sql="insert into Teams (Name,Players,Value) VALUES ('"+self.lineEdit_7.text()+"','"+selected+"','"+self.lineEdit_6.text()+"');"
               try:  
                   cur.execute(sql)
                   abc.commit()
                   self.showdlg("Team saved succesfully")
               except:
                   self.showdlg("Error! Please try again")
           else:
               self.showdlg("Players should be 11")
        if txt=='Open Team':
            self.bat_count=0
            self.ball_count=0
            self.ar_count=0
            self.wicket_count=0

            self.avl=1000
            self.used=0
            self.listWidget.clear()
            self.listWidget_2.clear()

            self.show()
            self.open_team()


    def evaluate_teams(self):
        self.evaluate=QtWidgets.QMainWindow()
        self.score=Ui_Evaluate()
        self.score.setupUi(self.evaluate)
        self.evaluate.show()
        


    def open_team(self):        
        cur.execute("SELECT Name from Teams")
        teams=[]
        for row in cur:
            teams.append(row[0])
        team, ok = QtWidgets.QInputDialog.getItem(MainWindow, "Open Team","Choose a team", teams, 0, False)
        if ok and team:
            self.lineEdit_7.setText(team)
        
        cur2=cur.execute("select Players, Value from Teams where Name='"+team+"'")
        row=cur2.fetchone()
        
        Split=row[0].split(',')
        
        self.listWidget_2.addItems(Split)
        self.used=1000-row[1]
        self.avl=row[1]
        for i in range(self.listWidget_2.count()):
            player=self.listWidget_2.item(i).text()        
            cur3=cur.execute( "select ctg from Stats where Player='"+player+"'")
            row=cur3.fetchone()
            category=row[0]
            if category=="BAT":
                self.bat_count+=1
            if category=="BWL":
                self.ball_count+=1
            if category=="AR":
                self.ar_count+=1
            if category=="WK":
                self.wicket_count+=1            
            
        self.show()
        

        

    def show(self):
        self.lineEdit.setText(str(self.bat_count))
        self.lineEdit_2.setText(str(self.ball_count))
        self.lineEdit_3.setText(str(self.ar_count))
        self.lineEdit_4.setText(str(self.wicket_count))
        self.lineEdit_5.setText(str(self.avl))
        self.lineEdit_6.setText(str(self.used))



    def checkstate(self):
        if self.radioButton.isChecked()==True:
            cur.execute("SELECT Player FROM Stats WHERE ctg=='BAT'")
            rows=cur.fetchall()
            self.listWidget.clear()
            player=list(set(rows))
            for row in player:
               self.listWidget.addItem("{}".format(row[0]))
              
        elif self.radioButton_2.isChecked()==True:
            cur.execute("SELECT Player FROM stats WHERE ctg=='BWL'")
            rows=cur.fetchall()
            self.listWidget.clear()
            player=list(set(rows))
            for row in player:
                self.listWidget.addItem("{}".format(row[0]))
                
        elif self.radioButton_3.isChecked()==True:
            cur.execute("SELECT Player FROM stats WHERE ctg=='AR'")
            rows=cur.fetchall()
            self.listWidget.clear()
            player=list(set(rows))
            for row in player:
                self.listWidget.addItem("{}".format(row[0]))
                
        elif self.radioButton_4.isChecked()==True:
            cur.execute("SELECT Player FROM stats WHERE ctg=='WK'")
            rows=cur.fetchall()
            self.listWidget.clear()
            player=list(set(rows))
            for row in player:
                self.listWidget.addItem("{}".format(row[0]))
               

    
    def removelist1(self,item):
        self.listWidget.row(item)
        sql="SELECT Value FROM Stats WHERE Player='"+item.text()+"' "
        a=cur.execute(sql)
        point=a.fetchone()
        self.avl=self.avl-(point[0])
        self.used=self.used+(point[0])
        if self.radioButton.isChecked()==True:
            self.bat_count+=1
            if self.bat_count>4:
                msg=QMessageBox()
                msg.setWindowTitle(" ")
                msg.setText("You can select four Batsmen")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                self.bat_count-=1
                self.avl=self.avl+(point[0])
                self.used=self.used-(point[0])
                return
            
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            
            self.lineEdit.setText(str(self.bat_count))
           

        elif self.radioButton_2.isChecked()==True:           
            self.ball_count+=1
            if self.ball_count>3:
                msg=QMessageBox()
                msg.setWindowTitle(" ")
                msg.setText("You can select three Bowlers")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                self.ball_count-=1
                self.avl=self.avl+(point[0])
                self.used=self.used-(point[0])
                return
                
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            
            self.lineEdit_2.setText(str(self.ball_count))
        elif self.radioButton_3.isChecked()==True:
            self.ar_count+=1
            if self.ar_count>3:
                msg=QMessageBox()
                msg.setWindowTitle(" ")
                msg.setText("You can select three All-Rounders")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                self.ar_count-=1
                self.avl=self.avl+(point[0])
                self.used=self.used-(point[0])
                return
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.lineEdit_3.setText(str(self.ar_count))
        elif self.radioButton_4.isChecked()==True:
            self.wicket_count+=1
            if self.wicket_count>1:
                msg=QMessageBox()
                msg.setWindowTitle(" ")
                msg.setText("You can select only one wicket keeper")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                self.wicket_count-=1
                self.avl=self.avl+(point[0])
                self.used=self.used-(point[0])                
                return
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.lineEdit_4.setText(str(self.wicket_count))
        
        self.lineEdit_5.setText(str(self.avl))
        self.lineEdit_6.setText(str(self.used))




    def removelist2(self,item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        sql="SELECT Value FROM Stats WHERE Player='"+item.text()+"' "
        a=cur.execute(sql)
        point=a.fetchone()
        self.avl=self.avl+(point[0])
        self.used=self.used-(point[0])
        self.lineEdit_5.setText(str(self.avl))
        self.lineEdit_6.setText(str(self.used))
        cursor = cur.execute("SELECT ctg from Stats where Player='"+item.text()+"'")
        rows=cursor.fetchone()
        ctgr=rows[0]
        if ctgr=="BAT":
            self.bat_count-=1
            if self.radioButton.isChecked()==True:
                self.listWidget_2.takeItem(self.listWidget_2.row(item))
                self.listWidget.addItem(item.text())
            self.lineEdit.setText(str(self.bat_count))
        if ctgr=="BWL":
            self.ball_count-=1
            if self.radioButton_2.isChecked()==True:
                self.listWidget_2.takeItem(self.listWidget_2.row(item))
                self.listWidget.addItem(item.text())
            self.lineEdit_2.setText(str(self.ball_count))
        if ctgr=="AR":
            self.ar_count-=1
            if self.radioButton_3.isChecked()==True:
                self.listWidget_2.takeItem(self.listWidget_2.row(item))
                self.listWidget.addItem(item.text())            
            self.lineEdit_3.setText(str(self.ar_count))
        if ctgr=="WK":
            self.wicket_count-=1
            if self.radioButton_4.isChecked()==True:
                self.listWidget_2.takeItem(self.listWidget_2.row(item))
                self.listWidget.addItem(item.text())               
            self.lineEdit_4.setText(str(self.wicket_count))
               
        



    def showdlg(self,msg):
        
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Team selector")
        ret=Dialog.exec()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
