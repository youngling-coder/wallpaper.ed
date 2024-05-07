# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/icon_128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(128, 128))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageQueryEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageQueryEdit.sizePolicy().hasHeightForWidth())
        self.imageQueryEdit.setSizePolicy(sizePolicy)
        self.imageQueryEdit.setText("")
        self.imageQueryEdit.setObjectName("imageQueryEdit")
        self.horizontalLayout.addWidget(self.imageQueryEdit)
        self.getWallpaperButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getWallpaperButton.sizePolicy().hasHeightForWidth())
        self.getWallpaperButton.setSizePolicy(sizePolicy)
        self.getWallpaperButton.setMinimumSize(QtCore.QSize(0, 36))
        self.getWallpaperButton.setObjectName("getWallpaperButton")
        self.horizontalLayout.addWidget(self.getWallpaperButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imageArea = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageArea.sizePolicy().hasHeightForWidth())
        self.imageArea.setSizePolicy(sizePolicy)
        self.imageArea.setTextFormat(QtCore.Qt.RichText)
        self.imageArea.setScaledContents(False)
        self.imageArea.setAlignment(QtCore.Qt.AlignCenter)
        self.imageArea.setObjectName("imageArea")
        self.verticalLayout.addWidget(self.imageArea)
        self.creditsLabel = QtWidgets.QLabel(self.tab)
        self.creditsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.creditsLabel.setOpenExternalLinks(True)
        self.creditsLabel.setObjectName("creditsLabel")
        self.verticalLayout.addWidget(self.creditsLabel)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 867, 516))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.downloadDirectoryEdit = QtWidgets.QLineEdit(self.groupBox)
        self.downloadDirectoryEdit.setObjectName("downloadDirectoryEdit")
        self.verticalLayout_3.addWidget(self.downloadDirectoryEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.apiTokenEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apiTokenEdit.sizePolicy().hasHeightForWidth())
        self.apiTokenEdit.setSizePolicy(sizePolicy)
        self.apiTokenEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apiTokenEdit.setObjectName("apiTokenEdit")
        self.horizontalLayout_3.addWidget(self.apiTokenEdit)
        self.showAPITokenButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showAPITokenButton.sizePolicy().hasHeightForWidth())
        self.showAPITokenButton.setSizePolicy(sizePolicy)
        self.showAPITokenButton.setObjectName("showAPITokenButton")
        self.horizontalLayout_3.addWidget(self.showAPITokenButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.wallpaperCommandEdit = QtWidgets.QTextEdit(self.groupBox)
        self.wallpaperCommandEdit.setObjectName("wallpaperCommandEdit")
        self.verticalLayout_3.addWidget(self.wallpaperCommandEdit)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.imageOrientationEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.imageOrientationEdit.setText("")
        self.imageOrientationEdit.setObjectName("imageOrientationEdit")
        self.verticalLayout_5.addWidget(self.imageOrientationEdit)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.isUpdateAutostartEnabledCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.isUpdateAutostartEnabledCheckBox.setObjectName("isUpdateAutostartEnabledCheckBox")
        self.verticalLayout_7.addWidget(self.isUpdateAutostartEnabledCheckBox)
        self.autostartSearchQueryEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.autostartSearchQueryEdit.setText("")
        self.autostartSearchQueryEdit.setReadOnly(False)
        self.autostartSearchQueryEdit.setObjectName("autostartSearchQueryEdit")
        self.verticalLayout_7.addWidget(self.autostartSearchQueryEdit)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.resetSettingsButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetSettingsButton.sizePolicy().hasHeightForWidth())
        self.resetSettingsButton.setSizePolicy(sizePolicy)
        self.resetSettingsButton.setObjectName("resetSettingsButton")
        self.horizontalLayout_2.addWidget(self.resetSettingsButton)
        self.applySettingsButton = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applySettingsButton.sizePolicy().hasHeightForWidth())
        self.applySettingsButton.setSizePolicy(sizePolicy)
        self.applySettingsButton.setObjectName("applySettingsButton")
        self.horizontalLayout_2.addWidget(self.applySettingsButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.setWallpaperButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setWallpaperButton.sizePolicy().hasHeightForWidth())
        self.setWallpaperButton.setSizePolicy(sizePolicy)
        self.setWallpaperButton.setMinimumSize(QtCore.QSize(0, 36))
        self.setWallpaperButton.setObjectName("setWallpaperButton")
        self.verticalLayout_2.addWidget(self.setWallpaperButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WallpaperED"))
        self.imageQueryEdit.setPlaceholderText(_translate("MainWindow", "flowers, people, color, etc.."))
        self.getWallpaperButton.setToolTip(_translate("MainWindow", "Enter"))
        self.getWallpaperButton.setText(_translate("MainWindow", "Get Wallpaper!"))
        self.getWallpaperButton.setShortcut(_translate("MainWindow", "Return"))
        self.imageArea.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/icon/icons/icon_128.png\"/></p><p>Wallpaper image will be shown here!</p></body></html>"))
        self.creditsLabel.setText(_translate("MainWindow", "Captured by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main"))
        self.groupBox.setTitle(_translate("MainWindow", "Application Settings"))
        self.label_3.setText(_translate("MainWindow", "Download directory"))
        self.downloadDirectoryEdit.setPlaceholderText(_translate("MainWindow", "~/path/to/dowbload/direcory"))
        self.label_4.setText(_translate("MainWindow", "Unsplash API Access Token"))
        self.apiTokenEdit.setPlaceholderText(_translate("MainWindow", "API-TOKEN"))
        self.showAPITokenButton.setText(_translate("MainWindow", "Show"))
        self.showAPITokenButton.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.label_5.setText(_translate("MainWindow", "Commands to update wallpaper"))
        self.wallpaperCommandEdit.setPlaceholderText(_translate("MainWindow", "Use %PATH% to specify your download directory..."))
        self.label.setText(_translate("MainWindow", "*commands separated by new line"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image Settings"))
        self.label_6.setText(_translate("MainWindow", "Image orientation"))
        self.imageOrientationEdit.setPlaceholderText(_translate("MainWindow", "landscape, portrait, squarish"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Autostart"))
        self.isUpdateAutostartEnabledCheckBox.setText(_translate("MainWindow", "Update wallpaper with a new session"))
        self.autostartSearchQueryEdit.setPlaceholderText(_translate("MainWindow", "Which category of wallpaper would you like to see? (cars, building, abstract, etc...)"))
        self.resetSettingsButton.setText(_translate("MainWindow", "Reset"))
        self.resetSettingsButton.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.applySettingsButton.setText(_translate("MainWindow", "Apply"))
        self.applySettingsButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings"))
        self.setWallpaperButton.setToolTip(_translate("MainWindow", "Ctrl+Alt+Enter"))
        self.setWallpaperButton.setText(_translate("MainWindow", "Set Wallpaper!"))
        self.setWallpaperButton.setShortcut(_translate("MainWindow", "Ctrl+Alt+Return"))
import src_rc
