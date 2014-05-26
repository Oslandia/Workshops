#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui, QtWebKit

from ui_mainwindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    # Maintain the list of browser windows so that they do not get garbage
    # collected.
    _window_list = []

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        MainWindow._window_list.append(self)

        self.setupUi(self)

        # Qt Designer (at least to v4.2.1) can't handle arbitrary widgets in a
        # QToolBar - even though uic can, and they are in the original .ui
        # file.  Therefore we manually add the problematic widgets.
        self.lblAddress = QtGui.QLabel("Address", self.tbAddress)
        self.tbAddress.insertWidget(self.actionGo, self.lblAddress)
        self.addressEdit = QtGui.QLineEdit(self.tbAddress)
        self.tbAddress.insertWidget(self.actionGo, self.addressEdit)

        self.connect(self.addressEdit, QtCore.SIGNAL("returnPressed()"),
                     self.actionGo, QtCore.SLOT("trigger()"))
        
        self.connect(self.actionBack, QtCore.SIGNAL("triggered()"),
                     self.WebBrowser, QtCore.SLOT("back()"))
        
        self.connect(self.actionForward, QtCore.SIGNAL("triggered()"),
                     self.WebBrowser, QtCore.SLOT("forward()"))
        
        self.connect(self.actionStop, QtCore.SIGNAL("triggered()"),
                     self.WebBrowser, QtCore.SLOT("stop()"))
        
        self.connect(self.actionRefresh, QtCore.SIGNAL("triggered()"),
                     self.WebBrowser, QtCore.SLOT("reload()"))
        
        #self.connect(self.actionHome, QtCore.SIGNAL("triggered()"),
        #    self.WebBrowser, QtCore.SLOT("load(QtCore.QUrl("http://www.google.com"))"))
        
        self.connect(self.actionHome, QtCore.SIGNAL("triggered()"),
                     self.WebBrowser, QtCore.SLOT("trigger()"))

        self.pb = QtGui.QProgressBar(self.statusBar())
        self.pb.setTextVisible(False)
        self.pb.hide()
        self.statusBar().addPermanentWidget(self.pb)
        self.WebBrowser.load(QtCore.QUrl("http://www.google.com"))

    @QtCore.pyqtSignature("")
    def on_actionHome_triggered(self):
        print "on_actionHome_triggered"
        self.WebBrowser.load(QtCore.QUrl("http://www.google.com"))

    def closeEvent(self, e):
        MainWindow._window_list.remove(self)
        e.accept()

    def on_WebBrowser_TitleChange(self, title):
        self.setWindowTitle("Qt WebBrowser - " + title)

    def on_WebBrowser_ProgressChange(self, a, b):
        if a <= 0 or b <= 0:
            self.pb.hide()
            return

        self.pb.show()
        self.pb.setRange(0, b)
        self.pb.setValue(a)

    def on_WebBrowser_CommandStateChange(self, cmd, on):
        if cmd == 1:
            self.actionForward.setEnabled(on)
        elif cmd == 2:
            self.actionBack.setEnabled(on)

    def on_WebBrowser_BeforeNavigate(self):
        self.actionStop.setEnabled(True)

    def on_WebBrowser_NavigateComplete(self, _):
        self.actionStop.setEnabled(False)

    @QtCore.pyqtSignature("")
    def on_actionGo_triggered(self):
        print "on_actionGo_triggered", self.addressEdit.text()
        self.WebBrowser.load(QtCore.QUrl(self.addressEdit.text()))

    @QtCore.pyqtSignature("")
    def on_actionNewWindow_triggered(self):
        
        print "on_actionNewWindow_triggered"
        window = MainWindow()
        window.show()
        if self.addressEdit.text().isEmpty():
            return;

        window.addressEdit.setText(self.addressEdit.text())
        window.actionStop.setEnabled(True)
        window.on_actionGo_triggered()

    @QtCore.pyqtSignature("")
    def on_actionAbout_triggered(self):
        QtGui.QMessageBox.about(self, self.tr("About WebBrowser"),
                self.tr("This Example has been created using the ActiveQt integration into Qt Designer.\n"
                        "It demonstrates the use of QAxWidget to embed the Internet Explorer ActiveX\n"
                        "control into a Qt application."))

    @QtCore.pyqtSignature("")
    def on_actionAboutQt_triggered(self):
        QtGui.QMessageBox.aboutQt(self, self.tr("About Qt"))


if __name__ == "__main__":
    a = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(a.exec_())
