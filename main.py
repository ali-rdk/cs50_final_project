#developed by Seyyed Mohammad Hossein Tabatabaeifard , Ali Roodaki , Seyyed Mohammad Sepehr Zekavat
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
from PIL.ImageQt import ImageQt
import sys
import filters


openFile = QtGui.QAction("&Open File",self)
openFile.setShortcut("Ctrl+O")
openFile.setStatusTip('Open File')
openFile.triggered.connect(self.file_open)
#file open pyqt
saveFile = QtGui.QAction("&Save File",self)
saveFile.setShortcut("Ctrl+S")
saveFile.setStatusTip('Save File')
saveFile.triggered.connect(self.file_save)
#file save pyqt
fileMenu.addAction(openFile)
fileMenu.addAction(openFile)
#adds action to menu

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
def file_open(self):
    name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
    file = open(name, 'r')
    #function that opens all files
def file_save(self):
    name = QtGui.QFileDialog.getSaveFileName(self)
    file = open(name, 'w')
    file.write(image)
    file.close()
    #function that saves file

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 610)
        #
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # blur button properties
        self.blur = QtWidgets.QPushButton(self.centralwidget)
        self.blur.setGeometry(QtCore.QRect(10, 10, 211, 28))
        self.blur.setObjectName("blur")
        # sepia button properties
        self.sepia = QtWidgets.QPushButton(self.centralwidget)
        self.sepia.setGeometry(QtCore.QRect(10, 50, 211, 28))
        self.sepia.setObjectName("sepia")
        # gray scale button properties
        self.gray = QtWidgets.QPushButton(self.centralwidget)
        self.gray.setGeometry(QtCore.QRect(10, 90, 211, 28))
        self.gray.setObjectName("gray")
        # sharpen button properties
        self.sharpen = QtWidgets.QPushButton(self.centralwidget)
        self.sharpen.setGeometry(QtCore.QRect(10, 130, 211, 28))
        self.sharpen.setObjectName("sharpen")
        # unsharpen button properties
        self.unsharpen = QtWidgets.QPushButton(self.centralwidget)
        self.unsharpen.setGeometry(QtCore.QRect(10, 170, 211, 28))
        self.unsharpen.setObjectName("unsharpen")
        # smooth button properties
        self.smooth = QtWidgets.QPushButton(self.centralwidget)
        self.smooth.setGeometry(QtCore.QRect(10, 210, 211, 28))
        self.smooth.setObjectName("smooth")
        # median button properties
        self.median = QtWidgets.QPushButton(self.centralwidget)
        self.median.setGeometry(QtCore.QRect(10, 250, 211, 28))
        self.median.setObjectName("media")
        # emboss button properties
        self.emboss = QtWidgets.QPushButton(self.centralwidget)
        self.emboss.setGeometry(QtCore.QRect(10, 290, 211, 28))
        self.emboss.setObjectName("emboss")
        # contour button properties
        self.contour = QtWidgets.QPushButton(self.centralwidget)
        self.contour.setGeometry(QtCore.QRect(10, 330, 211, 28))
        self.contour.setObjectName("contour")
        # find edge button properties
        self.find_egde = QtWidgets.QPushButton(self.centralwidget)
        self.find_egde.setGeometry(QtCore.QRect(10, 370, 211, 28))
        self.find_egde.setObjectName("find_egde")
        # enhance edge button properties
        self.enhance_edge = QtWidgets.QPushButton(self.centralwidget)
        self.enhance_edge.setGeometry(QtCore.QRect(10, 410, 211, 28))
        self.enhance_edge.setObjectName("enhance_edge")
        # histogram button properties
        self.invert = QtWidgets.QPushButton(self.centralwidget)
        self.invert.setGeometry(QtCore.QRect(10, 530, 211, 28))
        self.invert.setObjectName("histogram")
        # normalization button properties
        self.normalization = QtWidgets.QPushButton(self.centralwidget)
        self.normalization.setGeometry(QtCore.QRect(10, 490, 211, 28))
        self.normalization.setObjectName("normalization")
        # crop scale button properties
        self.crop = QtWidgets.QPushButton(self.centralwidget)
        self.crop.setGeometry(QtCore.QRect(10, 450, 211, 28))
        self.crop.setObjectName("crop")
        # image lable properties
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(240, 10, 821, 541))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.image.setFont(font)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("duck.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        #
        MainWindow.setCentralWidget(self.centralwidget)
        #menu bar properties
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 26))
        self.menubar.setObjectName("menubar")
        # file menu properties
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        # help menu properties
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # setting actions for open butyon
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        # setting actions for save button
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        # setting actions for credit button
        self.actioncredits = QtWidgets.QAction(MainWindow)
        self.actioncredits.setObjectName("actioncredits")
        # attaching them to menu bar
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionsave)
        self.menuhelp.addAction(self.actioncredits)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # connecting button with functions

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
        self.actionopen.triggered.connect(self.open_image)



        # set texts in each object
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.blur.setText(_translate("MainWindow", "blur"))
        self.sepia.setText(_translate("MainWindow", "sepia"))
        self.gray.setText(_translate("MainWindow", "gray scale"))
        self.sharpen.setText(_translate("MainWindow", "sharpen"))
        self.unsharpen.setText(_translate("MainWindow", "unsharpen"))
        self.smooth.setText(_translate("MainWindow", "smooth"))
        self.median.setText(_translate("MainWindow", "median"))
        self.emboss.setText(_translate("MainWindow", "emboss"))
        self.contour.setText(_translate("MainWindow", "contour"))
        self.find_egde.setText(_translate("MainWindow", "find edegs"))
        self.enhance_edge.setText(_translate("MainWindow", "enhance edges"))
        self.invert.setText(_translate("MainWindow", "invert color"))
        self.normalization.setText(_translate("MainWindow", "image normalization"))
        self.crop.setText(_translate("MainWindow", "crop"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionopen.setText(_translate("MainWindow", "open.."))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actioncredits.setText(_translate("MainWindow", "credits"))

    def filter(self, mode):

        image = Image.open("duck.jpg")

        #result = image

        if mode == "gray_scale":
            result = image.convert("L")

        if mode == "blur":
            result = image.filter(ImageFilter.BLUR)

        if mode == "sharpen":
            result = image.filter(ImageFilter.SHARPEN)

        if mode == "unsharpen":
            result = image.filter(ImageFilter.unsharpenMask)

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

    def open_image(self):
        image_path = QFileDialog.getOpenFileName()
        pixmap = Qpixmap(image_path)
        self.image.setPixmap(pixmap)
        self.resize(pixmap.size())
        self.adjustSize()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())