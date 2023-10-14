from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout)

menu = QWidget()

lb_question = QLabel('Введіть запитання')
lb_right_ans = QLabel('Введіть вірну відповідь')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

btn_ad_question = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")
btn_qbushButton = QPushButton("Назад")

lb_status = QLabel("Статистика")
lb_status.setStyleSheet("font-size: 20px; font-weight: bold")

lb_statistic = QLabel('Статистика')

line_horizon1 = QHBoxLayout()
line_horizon2 = QHBoxLayout()
line_horizon3 = QHBoxLayout()
line_horizon4 = QHBoxLayout()
line_horizon5 = QHBoxLayout()
line_horizon6 = QHBoxLayout()
line_horizon7 = QHBoxLayout()
line_horizon8 = QHBoxLayout()
line_horizon9 = QHBoxLayout()

line_horizon1.addWidget(lb_question)
line_horizon1.addWidget(le_question)

line_horizon2.addWidget(lb_right_ans)
line_horizon2.addWidget(le_right_ans)

line_horizon3.addWidget(lb_wrong_ans1)
line_horizon3.addWidget(le_wrong_ans1)

line_horizon4.addWidget(lb_wrong_ans2)
line_horizon4.addWidget(le_wrong_ans2)

line_horizon5.addWidget(lb_wrong_ans3)
line_horizon5.addWidget(le_wrong_ans3)

line_horizon6.addWidget(btn_ad_question)
line_horizon6.addWidget(btn_clear)

line_horizon9.addWidget(btn_qbushButton)

line_horizon7.addWidget(lb_status)

line_horizon8.addWidget(lb_statistic)

line = QVBoxLayout()

line.addLayout(line_horizon1)
line.addLayout(line_horizon2)
line.addLayout(line_horizon3)
line.addLayout(line_horizon4)
line.addLayout(line_horizon5)
line.addLayout(line_horizon6)
line.addLayout(line_horizon7)
line.addLayout(line_horizon8)
line.addLayout(line_horizon9)


menu.setLayout(line)
menu.resize(400, 300)

