from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
from PIL.ImageQt import ImageQt
import sys
import numpy
from numpy.lib.npyio import save
import os


def normalizeRed(intensity):
    iI = intensity
    minI = 86
    maxI = 230
    minO = 0
    maxO = 255
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO

def normalizeGreen(intensity):
    iI = intensity
    minI = 90
    maxI = 225
    minO = 0
    maxO = 255
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO

def normalizeBlue(intensity):
    iI = intensity
    minI = 100
    maxI = 210
    minO = 0
    maxO = 255
    iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return iO


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 594)
        MainWindow.setMinimumSize(QtCore.QSize(776, 510))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("duck.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("    overflow: hidden;\n"
"    display: flex;\n"
"    flex-direction: column;\n"
"    align-items: center;\n"
"    justify-content: center;\n"
"    background: grey;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("    overflow: hidden;\n"
"    display: flex;\n"
"    flex-direction: column;\n"
"    align-items: center;\n"
"    justify-content: center;\n"
"    background: grey;")
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(160, 10, 891, 501))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.image.setFont(font)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("preview.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.gray = QtWidgets.QPushButton(self.centralwidget)
        self.gray.setGeometry(QtCore.QRect(20, 290, 123, 31))
        self.gray.setMinimumSize(QtCore.QSize(123, 31))
        self.gray.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.gray.setFont(font)
        #self.gray.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gray.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.gray.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.gray.setObjectName("gray")
        self.sharpen = QtWidgets.QPushButton(self.centralwidget)
        self.sharpen.setGeometry(QtCore.QRect(20, 210, 123, 31))
        self.sharpen.setMinimumSize(QtCore.QSize(123, 31))
        self.sharpen.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.sharpen.setFont(font)
        #self.sharpen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sharpen.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.sharpen.setObjectName("sharpen")
        self.unsharpen = QtWidgets.QPushButton(self.centralwidget)
        self.unsharpen.setGeometry(QtCore.QRect(20, 250, 123, 31))
        self.unsharpen.setMinimumSize(QtCore.QSize(123, 31))
        self.unsharpen.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.unsharpen.setFont(font)
        #self.unsharpen.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.unsharpen.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.unsharpen.setObjectName("unsharpen")
        self.smooth = QtWidgets.QPushButton(self.centralwidget)
        self.smooth.setGeometry(QtCore.QRect(20, 330, 123, 31))
        self.smooth.setMinimumSize(QtCore.QSize(123, 31))
        self.smooth.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.smooth.setFont(font)
        #self.smooth.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.smooth.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.smooth.setObjectName("smooth")
        self.median = QtWidgets.QPushButton(self.centralwidget)
        self.median.setGeometry(QtCore.QRect(20, 90, 123, 31))
        self.median.setMinimumSize(QtCore.QSize(123, 31))
        self.median.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.median.setFont(font)
        #self.median.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.median.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.median.setObjectName("median")
        self.emboss = QtWidgets.QPushButton(self.centralwidget)
        self.emboss.setGeometry(QtCore.QRect(20, 50, 123, 31))
        self.emboss.setMinimumSize(QtCore.QSize(123, 31))
        self.emboss.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.emboss.setFont(font)
        #self.emboss.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.emboss.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.emboss.setObjectName("emboss")
        self.contour = QtWidgets.QPushButton(self.centralwidget)
        self.contour.setGeometry(QtCore.QRect(20, 370, 123, 31))
        self.contour.setMinimumSize(QtCore.QSize(123, 31))
        self.contour.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.contour.setFont(font)
       # self.contour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.contour.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.contour.setObjectName("contour")
        self.find_egde = QtWidgets.QPushButton(self.centralwidget)
        self.find_egde.setGeometry(QtCore.QRect(20, 410, 123, 31))
        self.find_egde.setMinimumSize(QtCore.QSize(123, 31))
        self.find_egde.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.find_egde.setFont(font)
        #self.find_egde.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.find_egde.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.find_egde.setObjectName("find_egde")
        self.enhance_edge = QtWidgets.QPushButton(self.centralwidget)
        self.enhance_edge.setGeometry(QtCore.QRect(20, 170, 123, 31))
        self.enhance_edge.setMinimumSize(QtCore.QSize(123, 31))
        self.enhance_edge.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.enhance_edge.setFont(font)
        #self.enhance_edge.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enhance_edge.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.enhance_edge.setObjectName("enhance_edge")
        self.normalization = QtWidgets.QPushButton(self.centralwidget)
        self.normalization.setGeometry(QtCore.QRect(20, 130, 123, 31))
        self.normalization.setMinimumSize(QtCore.QSize(123, 31))
        self.normalization.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.normalization.setFont(font)
        #self.normalization.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.normalization.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.normalization.setObjectName("normalization")
        self.blur = QtWidgets.QPushButton(self.centralwidget)
        self.blur.setGeometry(QtCore.QRect(20, 10, 123, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blur.sizePolicy().hasHeightForWidth())
        self.blur.setSizePolicy(sizePolicy)
        self.blur.setMinimumSize(QtCore.QSize(123, 31))
        self.blur.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.blur.setFont(font)
        #self.blur.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.blur.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"

"  padding:100px;\n"
"  border-radius:5px;")
        self.blur.setObjectName("blur")
        self.cpright = QtWidgets.QLabel(self.centralwidget)
        self.cpright.setGeometry(QtCore.QRect(770, 510, 271, 20))
        self.cpright.setObjectName("cpright")
        self.coomingsoon = QtWidgets.QPushButton(self.centralwidget)
        self.coomingsoon.setGeometry(QtCore.QRect(20, 490, 123, 31))
        self.coomingsoon.setMinimumSize(QtCore.QSize(123, 31))
        self.coomingsoon.setMaximumSize(QtCore.QSize(123, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.coomingsoon.setFont(font)
        #self.coomingsoon.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.coomingsoon.setStyleSheet("  background-color: #87C98A; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"
"  padding:100px;\n"
"  border-radius:5px;")
        self.coomingsoon.setObjectName("coomingsoon")
        self.invert = QtWidgets.QPushButton(self.centralwidget)
        self.invert.setGeometry(QtCore.QRect(20, 450, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.invert.setFont(font)
        self.invert.setStyleSheet("  background-color: #4CAF50; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 20px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  margin: 4px 2px;\n"
"  padding:100px;\n"
"  border-radius:5px;\n"
"")
        self.invert.setObjectName("invert")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 26))
        self.menubar.setStyleSheet("  background-color: #555555; /* Green */\n"
"  border: none;\n"
"  color: white;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"")
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setStyleSheet("")
        self.menufile.setObjectName("menufile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuCredits = QtWidgets.QMenu(self.menuhelp)
        self.menuCredits.setObjectName("menuCredits")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionsave)
        self.menuhelp.addAction(self.menuCredits.menuAction())
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.gray.clicked.connect(lambda : self.filter("gray_scale"))
        self.blur.clicked.connect(lambda : self.filter("blur"))
        self.sharpen.clicked.connect(lambda : self.filter("sharpen"))
        self.unsharpen.clicked.connect(lambda : self.filter("unsharpen"))
        self.smooth.clicked.connect(lambda : self.filter("smooth"))
        self.median.clicked.connect(lambda : self.filter("median"))
        self.emboss.clicked.connect(lambda : self.filter("emboss"))
        self.find_egde.clicked.connect(lambda : self.filter("find_egde"))
        self.enhance_edge.clicked.connect(lambda : self.filter("enhance_edge"))
        self.contour.clicked.connect(lambda : self.filter("contour"))
        self.invert.clicked.connect(lambda : self.filter("invert_color"))
        self.normalization.clicked.connect(lambda : self.filter("contrast_streching"))
        self.actionopen.triggered.connect(self.file_open)
        self.actionsave.triggered.connect(self.file_save)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CS50 image filter"))
        #self.gray.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Adds Grayscale Effect to Image</span></p></body></html>"))
        self.gray.setText(_translate("MainWindow", "GrayScale"))
        #self.sharpen.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Sharpens Render of Edges</span></p></body></html>"))
        self.sharpen.setText(_translate("MainWindow", "Sharpen"))
        #self.unsharpen.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Unsharpens Render of Edges</span></p></body></html>"))
        self.unsharpen.setText(_translate("MainWindow", "Unsharpen"))
        #self.smooth.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">adds Emboss effect to image</span></p></body></html>"))
        self.smooth.setText(_translate("MainWindow", "Smooth"))
        #self.median.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Adds Median effect to image</span></p></body></html>"))
        self.median.setText(_translate("MainWindow", "Median"))
        #self.emboss.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">adds Emboss effect to image</span></p></body></html>"))
        self.emboss.setText(_translate("MainWindow", "Emboss"))
        #self.contour.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Contour</span></p></body></html>"))
        self.contour.setText(_translate("MainWindow", "contour"))
        #self.find_egde.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Finds Edges</span></p></body></html>"))
        self.find_egde.setText(_translate("MainWindow", "Find edges"))
        #self.enhance_edge.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Enhances Edges</span></p></body></html>"))
        self.enhance_edge.setText(_translate("MainWindow", "Enhance"))
        #self.normalization.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Image Normalization</span></p></body></html>"))
        self.normalization.setText(_translate("MainWindow", "Normalize"))
        #self.blur.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">Blurs the image</span></p></body></html>"))
        self.blur.setText(_translate("MainWindow", "Blur"))
        self.cpright.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; vertical-align:sub;\">By Ali Roodaki ,Seyed MohmmadHossein Tabatabaei and Seyed sepehr zekavat</span></p></body></html>"))
        #self.coomingsoon.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400; font-style:italic; color:aqua;\">More Effects may be added</span></p></body></html>"))
        self.coomingsoon.setText(_translate("MainWindow", "Coming Soon"))
        self.invert.setText(_translate("MainWindow", "invert color"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuhelp.setTitle(_translate("MainWindow", "More"))
        self.menuCredits.setTitle(_translate("MainWindow", "credits"))
        self.actionopen.setText(_translate("MainWindow", "open.."))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def filter(self, mode):

        image = Image.open(path)

        global result

        result = image

        if mode == "gray_scale":
            result = image.convert("L")

        if mode == "blur":
            result = image.filter(ImageFilter.BLUR)

        if mode == "sharpen":
            result = image.filter(ImageFilter.SHARPEN)

        if mode == "unsharpen":
            result = image.filter(ImageFilter.UnsharpMask)

        if mode == "smooth":
            result = image.filter(ImageFilter.SMOOTH)

        if mode == "median":
            result = image.filter(ImageFilter.MedianFilter)

        if mode == "emboss":
            result = image.filter(ImageFilter.EMBOSS)

        if mode == "find_egde":
            result = image.filter(ImageFilter.FIND_EDGES)

        if mode == "enhance_edge":
            result = image.filter(ImageFilter.EDGE_ENHANCE)

        if mode == "contour":
            result = image.filter(ImageFilter.CONTOUR)

        if mode == "invert_color":
            image_array = numpy.array(image)
            image_array = 255 - image_array
            result = Image.fromarray(image_array)

        if mode == "contrast_streching":
            multiBands = image.split()
            redband = multiBands[0].point(normalizeRed)
            greenband = multiBands[1].point(normalizeGreen)
            blueband = multiBands[2].point(normalizeBlue)
            result = Image.merge("RGB", (redband, greenband, blueband))

            

        #if mode == "sepia":

        temp = ImageQt(result)
        pixmap = QtGui.QPixmap.fromImage(temp)
        self.image.setPixmap(pixmap)

    def file_open(self):
        #options = QtWidgets.QFileDialog.Options()
        global path
        path, _ = QtWidgets.QFileDialog.getOpenFileName()
        image_file = Image.open(path)
        temp = ImageQt(image_file)
        pixmap = QtGui.QPixmap.fromImage(temp)
        self.image.setPixmap(QPixmap(pixmap))

    def file_save(self):
        #global save_path
        save_path, _ = QtWidgets.QFileDialog.getSaveFileName()
        
        save_image_array =numpy.array(result)
        bin = Image.new("RGB", result.size)
        bin = Image.fromarray(save_image_array)
        bin.save("result.jpg")
            #save_path = save_path[::-1]
            
            #for i in range(len(save_path)):
            #   if save_path[i] != 92:
            #        save_file_name = save_path[0:i-4]
            #   elif save_path[i] == 92:
            #        break
            #bin.save(save_file_name, format="png")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
