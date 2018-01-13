# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'amcat_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
import matplotlib.pyplot as plt
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
    def proceed(self):
        def mConvert(values):
            # integer encode
            label_encoder = LabelEncoder()
            integer_encoded = label_encoder.fit_transform(values)
            return integer_encoded
        ten = self.ten_percentage.toPlainText()
        gen = self.gender.toPlainText()
        spec = self.specizlization.toPlainText()
        deg = self.degree.toPlainText()
        log = self.logical.toPlainText()
        con = self.conscientiosness.toPlainText()
        extra = self.extraversion.toPlainText()
        ote = self.openess_to_experience.toPlainText()
        twelve = self.twelth_percentage.toPlainText()
        desig = self.designation.toPlainText()
        gpa = self.collegeGpa.toPlainText()
        eng = self.english.toPlainText()
        quant = self.quantitative.toPlainText()
        agree = self.agreeableness.toPlainText()
        nuero = self.nueroticism.toPlainText()
        
        '''print(ten)
        print(gen)
        print(spec)'''
        
        ttt=[[desig],[gen],[ten],[twelve],[deg],[spec],[gpa],[eng],[log],[quant],[con],[agree],[extra],[nuero],[ote]]
        for i in range(15):
            ttt[i]=mConvert(ttt[i])
        input_x_test=ttt
        input_x_test = np.array(input_x_test).reshape(1,-1)        
        file = pd.read_csv("train.csv",usecols=["Designation","Gender","10percentage","12percentage",
           "Degree","Specialization","collegeGPA","English","Logical","Quant","conscientiousness","agreeableness","extraversion","nueroticism","openess_to_experience"])
        y_test = pd.read_csv("train.csv",usecols=["Salary"])
        
        
        y_test=y_test["Salary"]
        y_test=np.array(y_test)
        
        ybk=y_test
        de=(file["Designation"])
        ge=(file["Gender"])
        tper=(file["10percentage"])
        twper=(file["12percentage"])
        dg=(file["Degree"])
        sp=(file["Specialization"])
        co=(file["collegeGPA"])
        en=(file["English"])
        lo=(file["Logical"])
        qa=(file["Quant"])
        cs=(file["conscientiousness"])
        ag=(file["agreeableness"])
        ex=(file["extraversion"])
        nu=(file["nueroticism"])
        oe=(file["openess_to_experience"])
        de=mConvert(de)
        ge=mConvert(ge)
        tper=mConvert(tper)
        twper=mConvert(twper)
        dg=mConvert(dg)
        sp=mConvert(sp)
        co=mConvert(co)
        en=mConvert(en)
        lo=mConvert(lo)
        qa=mConvert(qa)
        cs=mConvert(cs)
        ag=mConvert(ag)
        ex=mConvert(ex)
        nu=mConvert(nu)
        oe=mConvert(oe)
        
        X=[[de[i],ge[i],tper[i],twper[i],dg[i],sp[i],co[i],en[i],lo[i],qa[i],cs[i],ag[i],ex[i],nu[i],oe[i] ] for i in range(len(de))]
        
        
        X_train, X_test, y_train, y_test = train_test_split(X, y_test, test_size=0.10)
        
        
        reg = linear_model.Lasso(alpha=.01,selection='random')
        reg.fit(X_train,y_train)
        #pp=reg.predict(X_test)
        pp=reg.predict(input_x_test)
        
        print(pp)
        
        
        fig = plt.figure(figsize=(18, 12))
        fig.subplots_adjust(wspace=0.75,hspace=0.75)
        sub1 = fig.add_subplot(351)
        sub1.scatter(de,ybk)
        sub1.set_xlabel('Designation')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(352)
        sub1.scatter(ge,ybk)
        sub1.set_xlabel('Gender')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(353)
        sub1.scatter(tper,ybk)
        sub1.set_xlabel('10percentage')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(354)
        sub1.scatter(twper,ybk)
        sub1.set_xlabel('12percentage')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(355)
        sub1.scatter(dg,ybk)
        sub1.set_xlabel('Degree')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(356)
        sub1.scatter(sp,ybk)
        sub1.set_xlabel('Specialization')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(357)
        sub1.scatter(co,ybk)
        sub1.set_xlabel('collegeGPA')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(358)
        sub1.scatter(en,ybk)
        sub1.set_xlabel('English')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(359)
        sub1.scatter(lo,ybk)
        sub1.set_xlabel('Logical')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(3,5,10)
        sub1.scatter(qa,ybk)
        sub1.set_xlabel('Quantitative')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(3,5,11)
        sub1.scatter(cs,ybk)
        sub1.set_xlabel('Conscientiousness')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(3,5,12)
        sub1.scatter(ag,ybk)
        sub1.set_xlabel('Agreeableness')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(3,5,13)
        sub1.scatter(ex,ybk)
        sub1.set_xlabel('Extraversion')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(3,5,14)
        sub1.scatter(nu,ybk)
        sub1.set_xlabel('Nueroticism')
        sub1.set_ylabel('Salary')
        sub1 = fig.add_subplot(3,5,15)
        sub1.scatter(oe,ybk)
        sub1.set_xlabel('Openess_to_experience')
        sub1.set_ylabel('Salary')
        
        
        def mtp(i):
            print(pp[i],y_test[i])
            print(y_test[i]-pp[i])
			
			
			
			
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(789, 504)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(:/temporary/3.jpg);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ten_percentage = QtGui.QTextEdit(self.centralwidget)
        self.ten_percentage.setGeometry(QtCore.QRect(160, 20, 171, 31))
        self.ten_percentage.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.ten_percentage.setObjectName(_fromUtf8("ten_percentage"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.predict_button = QtGui.QPushButton(self.centralwidget)
        self.predict_button.setGeometry(QtCore.QRect(500, 380, 171, 41))
        self.predict_button.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.predict_button.setObjectName(_fromUtf8("predict_button"))
        self.predict_button.clicked.connect(self.proceed)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 31))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gender = QtGui.QTextEdit(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(160, 60, 171, 31))
        self.gender.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.gender.setObjectName(_fromUtf8("gender"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.specizlization = QtGui.QTextEdit(self.centralwidget)
        self.specizlization.setGeometry(QtCore.QRect(160, 100, 171, 31))
        self.specizlization.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.specizlization.setObjectName(_fromUtf8("specizlization"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 131, 31))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.degree = QtGui.QTextEdit(self.centralwidget)
        self.degree.setGeometry(QtCore.QRect(160, 140, 171, 31))
        self.degree.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.degree.setObjectName(_fromUtf8("degree"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 131, 31))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.logical = QtGui.QTextEdit(self.centralwidget)
        self.logical.setGeometry(QtCore.QRect(160, 180, 171, 31))
        self.logical.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.logical.setObjectName(_fromUtf8("logical"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 220, 131, 31))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.conscientiosness = QtGui.QTextEdit(self.centralwidget)
        self.conscientiosness.setGeometry(QtCore.QRect(160, 220, 171, 31))
        self.conscientiosness.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.conscientiosness.setObjectName(_fromUtf8("conscientiosness"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 260, 131, 31))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.extraversion = QtGui.QTextEdit(self.centralwidget)
        self.extraversion.setGeometry(QtCore.QRect(160, 260, 171, 31))
        self.extraversion.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.extraversion.setObjectName(_fromUtf8("extraversion"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 161, 31))
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.openess_to_experience = QtGui.QTextEdit(self.centralwidget)
        self.openess_to_experience.setGeometry(QtCore.QRect(190, 300, 171, 31))
        self.openess_to_experience.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.openess_to_experience.setObjectName(_fromUtf8("openess_to_experience"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(420, 20, 131, 31))
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(420, 180, 131, 31))
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.designation = QtGui.QTextEdit(self.centralwidget)
        self.designation.setGeometry(QtCore.QRect(560, 60, 171, 31))
        self.designation.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.designation.setObjectName(_fromUtf8("designation"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(420, 140, 131, 31))
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.collegeGpa = QtGui.QTextEdit(self.centralwidget)
        self.collegeGpa.setGeometry(QtCore.QRect(560, 100, 171, 31))
        self.collegeGpa.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.collegeGpa.setObjectName(_fromUtf8("collegeGpa"))
        self.english = QtGui.QTextEdit(self.centralwidget)
        self.english.setGeometry(QtCore.QRect(560, 140, 171, 31))
        self.english.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.english.setObjectName(_fromUtf8("english"))
        self.quantitative = QtGui.QTextEdit(self.centralwidget)
        self.quantitative.setGeometry(QtCore.QRect(560, 180, 171, 31))
        self.quantitative.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.quantitative.setObjectName(_fromUtf8("quantitative"))
        self.agreeableness = QtGui.QTextEdit(self.centralwidget)
        self.agreeableness.setGeometry(QtCore.QRect(560, 220, 171, 31))
        self.agreeableness.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.agreeableness.setObjectName(_fromUtf8("agreeableness"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(420, 60, 131, 31))
        self.label_13.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(420, 100, 131, 31))
        self.label_14.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(420, 220, 131, 31))
        self.label_15.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.twelth_percentage = QtGui.QTextEdit(self.centralwidget)
        self.twelth_percentage.setGeometry(QtCore.QRect(560, 20, 171, 31))
        self.twelth_percentage.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.twelth_percentage.setObjectName(_fromUtf8("twelth_percentage"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(420, 260, 131, 31))
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.nueroticism = QtGui.QTextEdit(self.centralwidget)
        self.nueroticism.setGeometry(QtCore.QRect(560, 260, 171, 31))
        self.nueroticism.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);"))
        self.nueroticism.setObjectName(_fromUtf8("nueroticism"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ten_percentage.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "10 th Percentage", None))
        self.predict_button.setText(_translate("MainWindow", "Predict Salary", None))
        self.label_2.setText(_translate("MainWindow", "Gender", None))
        self.label_3.setText(_translate("MainWindow", "Specialization", None))
        self.label_4.setText(_translate("MainWindow", "Degree", None))
        self.label_5.setText(_translate("MainWindow", "Logical", None))
        self.label_6.setText(_translate("MainWindow", "Conscientiousness", None))
        self.label_7.setText(_translate("MainWindow", "Extraversion", None))
        self.label_8.setText(_translate("MainWindow", "Openess to Experience", None))
        self.label_9.setText(_translate("MainWindow", "12 th Percentage", None))
        self.label_10.setText(_translate("MainWindow", "Quantitative", None))
        self.label_12.setText(_translate("MainWindow", "English", None))
        self.label_13.setText(_translate("MainWindow", "Designation", None))
        self.label_14.setText(_translate("MainWindow", "College GPA", None))
        self.label_15.setText(_translate("MainWindow", "Agreeableness", None))
        self.label_16.setText(_translate("MainWindow", "Nueroticism", None))

import resource_file_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
