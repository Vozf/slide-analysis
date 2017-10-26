# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slide_analysis/UI/view/settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.settings_tab_widget = QtWidgets.QTabWidget(Dialog)
        self.settings_tab_widget.setObjectName("settings_tab_widget")
        self.descriptor_settings_tab = QtWidgets.QWidget()
        self.descriptor_settings_tab.setObjectName("descriptor_settings_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.descriptor_settings_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.choose_descriptors_combo_box = QtWidgets.QComboBox(self.descriptor_settings_tab)
        self.choose_descriptors_combo_box.setObjectName("choose_descriptors_combo_box")
        self.gridLayout_2.addWidget(self.choose_descriptors_combo_box, 2, 0, 1, 1)
        self.extra_descriptor_settings_layout = QtWidgets.QGridLayout()
        self.extra_descriptor_settings_layout.setObjectName("extra_descriptor_settings_layout")
        self.gridLayout_2.addLayout(self.extra_descriptor_settings_layout, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.choose_descriptors_label = QtWidgets.QLabel(self.descriptor_settings_tab)
        self.choose_descriptors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_descriptors_label.setObjectName("choose_descriptors_label")
        self.gridLayout_2.addWidget(self.choose_descriptors_label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.settings_tab_widget.addTab(self.descriptor_settings_tab, "")
        self.similar_images_settings_tab = QtWidgets.QWidget()
        self.similar_images_settings_tab.setObjectName("similar_images_settings_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.similar_images_settings_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.search_settings_label = QtWidgets.QLabel(self.similar_images_settings_tab)
        self.search_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.search_settings_label.setObjectName("search_settings_label")
        self.verticalLayout.addWidget(self.search_settings_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.similar_images_count_slider = QtWidgets.QSlider(self.similar_images_settings_tab)
        self.similar_images_count_slider.setMaximum(20)
        self.similar_images_count_slider.setOrientation(QtCore.Qt.Horizontal)
        self.similar_images_count_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.similar_images_count_slider.setTickInterval(1)
        self.similar_images_count_slider.setObjectName("similar_images_count_slider")
        self.horizontalLayout.addWidget(self.similar_images_count_slider)
        self.similar_images_count_label = QtWidgets.QLabel(self.similar_images_settings_tab)
        self.similar_images_count_label.setObjectName("similar_images_count_label")
        self.horizontalLayout.addWidget(self.similar_images_count_label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.settings_tab_widget.addTab(self.similar_images_settings_tab, "")
        self.metrics_settings = QtWidgets.QWidget()
        self.metrics_settings.setObjectName("metrics_settings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.metrics_settings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.choose_descriptors_label_2 = QtWidgets.QLabel(self.metrics_settings)
        self.choose_descriptors_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_descriptors_label_2.setObjectName("choose_descriptors_label_2")
        self.verticalLayout_2.addWidget(self.choose_descriptors_label_2)
        self.choose_metrics_combo_box = QtWidgets.QComboBox(self.metrics_settings)
        self.choose_metrics_combo_box.setObjectName("choose_metrics_combo_box")
        self.verticalLayout_2.addWidget(self.choose_metrics_combo_box)
        self.extra_metrics_settings_layout = QtWidgets.QGridLayout()
        self.extra_metrics_settings_layout.setObjectName("extra_metrics_settings_layout")
        self.verticalLayout_2.addLayout(self.extra_metrics_settings_layout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.settings_tab_widget.addTab(self.metrics_settings, "")
        self.gridLayout.addWidget(self.settings_tab_widget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.settings_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choose_descriptors_label.setText(_translate("Dialog", "Choose method for calculating descroptors"))
        self.settings_tab_widget.setTabText(self.settings_tab_widget.indexOf(self.descriptor_settings_tab), _translate("Dialog", "Descriptors"))
        self.search_settings_label.setText(_translate("Dialog", "How many similar images to display"))
        self.similar_images_count_label.setText(_translate("Dialog", "0"))
        self.settings_tab_widget.setTabText(self.settings_tab_widget.indexOf(self.similar_images_settings_tab), _translate("Dialog", "Similar images"))
        self.choose_descriptors_label_2.setText(_translate("Dialog", "Choose metrics"))
        self.settings_tab_widget.setTabText(self.settings_tab_widget.indexOf(self.metrics_settings), _translate("Dialog", "Metrics"))

