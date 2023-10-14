''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)

window = QWidget()

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
btn_menu = QPushButton("Меню")
# кнопка прибирає вікно і повертає його після закінчення таймера
btn_Sleep = QPushButton("Відпочити")
# введення кількості хвилин
box_time = QSpinBox()
box_time.setValue(30)
lb_Time = QLabel('секунд')
# кнопка відповіді "Ок" / "Наступний"
btn_ok = QPushButton("Відповісти")
# текст питання
ld_question = QLabel('1')

# Опиши групу перемикачів
radio_group_box = QGroupBox("Варіанти відповідей")
radio_group = QButtonGroup()
radiobutton1 = QRadioButton('1')
radiobutton2 = QRadioButton('1')
radiobutton3 = QRadioButton('1')
radiobutton4 = QRadioButton('1')

radio_group.addButton(radiobutton1)
radio_group.addButton(radiobutton2)
radio_group.addButton(radiobutton3)
radio_group.addButton(radiobutton4)


# Опиши панень з результатами
answer_group_box = QGroupBox('Результати тесту')
lb_Resultat = QLabel('') #правильно, неправильно
lb_Correct = QLabel('') #правильна відповідь

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
layont_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
layout_h3 = QHBoxLayout()
layout_v1 = QVBoxLayout()
layout_v2 = QVBoxLayout()
layout_v3 = QVBoxLayout()
layout_h4 = QHBoxLayout()

layont_h1.addWidget(btn_menu)
layont_h1.addStretch(1)
layont_h1.addWidget(btn_Sleep)
layont_h1.addWidget(box_time)
layont_h1.addWidget(lb_Time)


layout_h2.addWidget(ld_question)

layout_v1.addWidget(radiobutton1)
layout_v1.addWidget(radiobutton2)
layout_v2.addWidget(radiobutton3)
layout_v2.addWidget(radiobutton4)
layout_h3.addLayout(layout_v1)
layout_h3.addLayout(layout_v2)


layout_h4.addWidget(btn_ok)

line = QVBoxLayout()
line.addLayout(layont_h1, stretch=1)
line.addLayout(layout_h2, stretch=2)
line.addLayout(layout_h3, stretch=8)
line.addStretch(1)
line.addLayout(layout_h4)
line.addSpacing(1)
line.addSpacing(5)

window.setLayout(line)
window.resize(550, 450)