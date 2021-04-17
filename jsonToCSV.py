import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import json
import csv

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        self.openFileNameDialog()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","JSON Files (*.json);;", options=options)
        
        #check if there is a file
        if fileName:
            print(fileName)
            # extract the data from the JSON file
            with open(fileName, "r") as jayson:
                data = json.load(jayson)

            file_name = "data"
            titles = []
            rows = []

            entries = 0
            for info in data:
                entries += 1

            if entries == 1:
                file_name = info

                for info in data[file_name][0]:
                    #print(info)
                    titles.append(info)

                #print(titles)

                index = 0

                for key in titles:
                    rows.append([])
                    for info in data[file_name]:
                        #print(info)
                        rows[index].append(info[key])
                    index +=1

                #print(f"the rows are: {rows}")
                with open(str(file_name) + ".csv", "w") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(titles)
                    csvwriter.writerows(rows)

            else:
                for info in data[0]:
                    print(info)
                    titles.appendd(info)

                index = 0

                for key in titles:
                    rows.append([])
                    for info in data:
                        rows[index].append(info[key])
                    index += 1
                    
                with open(str(file_name) + ".csv", "w") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(titles)
                    csvwriter.writerows(rows)

            # TODO extract the data and write it with commas!


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())