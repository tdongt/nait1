from PySide6.QtWidgets import QWidget,QApplication
import translators as ts
import deep_translator as more_ts
from trans_ui import Ui_Form
class transwindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.language={'中文':'zh','英语':'en','法语':'fr','日语':'ja','德语':'de','阿拉伯语':'ar','韩语':'ko','西班牙语':'es','葡萄牙语':'pt','意大利语':'it'}
        self.lanoutpit={'zh':'中文','en':'英语','fr':'法语','ja':'日语','de':'德语','ar':'阿拉伯语','ko':'韩语','es':'西班牙语','pt':'葡萄牙语','it':'意大利语'}
        self.yuanlan.addItems(self.language.keys())
        self.hou_lan.addItems(self.language.keys())
        self.auto_2.clicked.connect(self.bind)
    def bind(self):
        if self.auto_2.isChecked()==True:
            #print("true")
            self.trans.clicked.connect(self.auto_detect)
        else:
            #print("false")
            self.trans.clicked.connect(self.transf)

    def transf(self):
        #print("check")
        lgu=self.language[self.yuanlan.currentText()]
        old_text=str(self.yuan.toPlainText())
        to_lgu=self.language[self.hou_lan.currentText()]
        if lgu =='':
            return
        new_text=ts.translate_text(old_text,from_language=lgu,to_language=to_lgu)
        self.hou.setText(str(new_text))
    def auto_detect(self):
        #print("auto")
        old_text=str(self.yuan.toPlainText())
        typex=more_ts.single_detection(old_text,api_key='6088732405975e7ee85132697565984c')
        def change(a):
            if a == 'zh-Hant':
                #print(type(a))
                b=a.replace("-Hant","")
                #print(b)
                return b
            else:
                return a
        typey=change(typex)
        #print(typey)
        self.lanout.setText(self.lanoutpit[typey])
        to_lgu=self.language[self.hou_lan.currentText()]
        #print(to_lgu)
        new_text=ts.translate_text(old_text,from_language=typey,to_language=to_lgu)
        self.hou.setText(str(new_text))
        
if __name__ =='__main__':
    app=QApplication()
    window=transwindow()
    window.show()
    app.exec()