import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import json
import csv

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Convert from .json to .csv'
        self.left = 0
        self.top = 0
        self.width = 320
        self.height = 120
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Select a file', self)
        button.setToolTip('This is an example button')
        button.move(100,70)
        button.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('button click')
        self.openFileNameDialog()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select a file", "","JSON Files (*.json);;", options=options)
        
        #check if there is a file
        if fileName:
            #print(fileName)
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
                    titles.append(info)

                index = 0
                for info in data[file_name]:
                    rows.append([])
                    for key in titles:
                        rows[index].append(info[key])
                    index += 1 # index defines at what row we find ourselves

                with open(str(file_name) + ".csv", "w") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(titles)
                    csvwriter.writerows(rows)

            else: #the json doesn't start with a section
                for info in data[0]:
                    print(info)
                    titles.append(info)

                index = 0
                for info in data:
                    rows.append([])
                    for key in titles:
                        rows[index].append(info[key])
                    index += 1

                for list in rows:
                    print(list)

                with open(str(file_name) + ".csv", "w") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(titles)
                    csvwriter.writerows(rows)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())