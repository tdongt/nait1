from PySide6.QtWidgets import QWidget,QApplication
from chg_ui import Ui_Form
class chgwin(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lengthvar={'毫米/mm':0.001,'米/m':1,'千米/km':1000}
        self.weightvar={'毫克/mg':0.001,'克/g':1,'千克/kg':1000}
        #定义换算标准选择框
        self.type={'长度':self.lengthvar,'质量':self.weightvar}
        #为各下拉框添加元素
        self.comboBox_select.addItems(self.type.keys())
        self.comboBox1.addItems(self.lengthvar.keys())
        self.comboBox2.addItems(self.lengthvar.keys())
        self.bind()
    def bind(self):
        #点击换算标准选择框发生改变
        self.comboBox_select.currentTextChanged.connect(self.typechg)
        #点击换算输出结果
        self.pushButton_chg.clicked.connect(self.chgnow)
    def chgnow(self):
        #获取换算标准
        alltype=self.comboBox_select.currentText()
        #获取需要换算的值
        value=self.lineEdit1.text()
        if value=='':
            return
        #当前单位和换算后单位
        nowtype=self.comboBox1.currentText()
        transtype=self.comboBox2.currentText()
        #标准化
        strand=float(value)*self.type[alltype][nowtype]
        #换算
        result=strand/self.type[alltype][transtype]
        #在标签中显示换算结果
        self.textBrowser_qian.setText(f"{value} {nowtype}=")
        self.textBrowser_hou.setText(f"{result} {transtype}")
        self.lineEdit2.setText(str(result))

    def typechg(self,text):
        self.comboBox1.clear()
        self.comboBox2.clear()
        self.comboBox1.addItems(self.type[text].keys())
        self.comboBox2.addItems(self.type[text].keys())


if __name__ == '__main__':
    app=QApplication()
    window=chgwin()
    window.show()
    app.exec()