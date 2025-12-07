import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QAction, qApp, QFileDialog, QTextEdit
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

        

    def initUI(self):
        self.setWindowTitle('HxD Editor')
        self.setWindowIcon(QIcon('My_logo.png')) ## 어플리케이션 아이콘 설정
        self.resize(1000, 700)
        self.center()
        self.statusBar().showMessage('HxD Editor Ready') ## 상태바 설정

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        ## menubar 생성
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        ## File 메뉴 추가 
        filemenu = menubar.addMenu('&File')

        ## File -> Open 액션 추가
        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        openAction.triggered.connect(self.showDialog)
        filemenu.addAction(openAction)

        filemenu.addSeparator()

        ## File -> Exit 액션 추가
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        filemenu.addAction(exitAction)

        self.show()

    ## 프로그램 동적으로 가운데 위치 고정
    def center(self): 
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
