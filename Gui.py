from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import Drawer as DrCls
from PyQt5.QtGui import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.qlabel = QLabel(self)
        self.resline = QLineEdit(self)
        self.resline.setFixedWidth(50)
        self.result_text = QLabel()
        self.res = 100
        self.ascii_img = ""
        self.name = ""
        self.filename = ""
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.res_layout = QHBoxLayout()
        self.image_layout = QVBoxLayout()
        self.image = QTextEdit()
        self.addimgbtn = QPushButton("Add Image", self)
        self.toasciibtn = QPushButton("To ASCII", self)
        self.toansibtn = QPushButton("To ANSI", self)
        self.saveasimgbtn = QPushButton("Save as image", self)
        self.res_text = QLabel()

        self.res_text.setText('Enter resolution:')

        self.initUI()

    def initUI(self):

        """
        this method shows an interface
        """

        self.setGeometry(300, 300, 100, 50)
        self.setWindowTitle("ASCIIArt")
        self.move_center()

        self.hbox.addWidget(self.addimgbtn)
        self.res_layout.addWidget(self.res_text)
        self.res_layout.addWidget(self.resline)
        self.res_layout.addStretch(1)

        self.hbox.addLayout(self.res_layout)
        self.hbox.addWidget(self.toasciibtn)
        self.hbox.addWidget(self.toansibtn)

        self.image_layout.addWidget(self.qlabel)

        self.vbox.addStretch(2)
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.image_layout)
        self.vbox.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.saveasimgbtn)

        self.setLayout(self.vbox)

        self.show()

        self.addimgbtn.clicked.connect(lambda: self.add_image_button())
        self.toasciibtn.clicked.connect(lambda: self.to_ascii())
        self.toansibtn.clicked.connect(lambda: self.to_ansi())
        self.saveasimgbtn.clicked.connect(lambda: self.save_as_img())

        self.resline.textChanged[str].connect(self.on_changed)

    def move_center(self):

        """
        this method moves a window to the center of the screen
        """

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def add_image_button(self):

        """
        this method allow to get an image by clicking the button
        """

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "QFileDialog.getOpenFileName"
                                                  "()",
                                                  "",
                                                  "Image (*.png *jpg *bmp)",
                                                  options=options)

        self.filename = filename
        self.pixmap = QPixmap(self.filename)
        self.qlabel.setPixmap(self.pixmap)

    def on_changed(self, text):
        self.resline.setText(text)
        self.resline.adjustSize()
        self.res = int(text)

    def to_ascii(self):

        """
        this method starts the drawer class with ascii
        """

        try:
            drawer = DrCls.Drawer(self.filename)
            _tuple = self.get_ascii_img()
            self.ascii_img = drawer.to_ascii_art(_tuple[0], _tuple[1][0])

            with open("%s.txt" % self.name, "w") as f:
                f.write(self.ascii_img)

            self.result_window = Result(ascii_img=self.ascii_img)
            self.result_window.show()
            msg = QMessageBox()
            msg.setText("Now you can find your image on %s.txt \n" % self.name)
            msg.exec_()
            print("Now you can find your image on %s.txt \n" % self.name)
            print(self.ascii_img)

        except Exception as e:
            print(e)
            if self.name == "":
                msg = QMessageBox()
                msg.setText("Empty name \n")
                msg.exec_()
                print("Empty name")
                print(e)
            else:
                msg = QMessageBox()
                msg.setText("Choose file at first \n")
                msg.exec_()
                print("Choose file at first")

    def to_ansi(self):

        """
        this method starts the drawer class with ansi
        """

        try:
            _tuple = self.get_ascii_img()

            drawer = DrCls.Drawer(self.filename)
            ansi_image = drawer.to_ansi_art(_tuple)

            with open("%s.txt" % self.name, "w") as f:
                f.write(ansi_image)

            msg = QMessageBox()
            msg.setText("Now you can find your image on %s.txt \n" % self.name)
            msg.exec_()
            print("Now you can find your image on %s.txt \n" % self.name)

        except Exception as e:
            if self.name == "":
                msg = QMessageBox()
                msg.setText("Empty name \n")
                msg.exec_()
                print("Empty name")
                print(e)
            else:
                msg = QMessageBox()
                msg.setText("Choose file at first \n")
                msg.exec_()
                print("Choose file at first")

    def get_ascii_img(self):

        """
        this method gets an ascii string with picture
        """

        while self.name == '':
            self.name, ok = QInputDialog.getText(self, "Name",
                                                 "Enter your filename")
            if self.name == '':
                msg = QMessageBox()
                msg.setText("Please type filename!!!")
                msg.exec_()

        drawer = DrCls.Drawer(self.filename)
        res = drawer.resize_image(self.res)
        pixels = drawer.get_image_data()
        arr = drawer.draw_picture(pixels)

        return arr, res

    def save_as_img(self, name=None):

        """
        this method saves an image
        """

        image = DrCls.Drawer(self.filename).get_img(self.name)

        while name is None or name == '':
            name, ok = QInputDialog.getText(self, "Name",
                                            "Enter your filename")
            if name == '':
                msg = QMessageBox()
                msg.setText("Please type filename!!!")
                msg.exec_()

        image.save("%s.png" % name)
        msg = QMessageBox()
        msg.setText("Done!")
        msg.exec_()


class Result(QWidget):
    def __init__(self, ascii_img):
        super().__init__()
        self.setWindowTitle('Result')
        self.hbox = QHBoxLayout()
        self.ascii = QLabel(self)
        self.ascii.setText(ascii_img)
        self.ascii.setFont(QFont('Courier New', 10))
        self.ascii.setStyleSheet("color:#f00000")

        self.initUI()

    def initUI(self):
        """
        this method sets layout
        """

        self.setWindowTitle("test")
        self.hbox.addWidget(self.ascii)
        self.setLayout(self.hbox)
