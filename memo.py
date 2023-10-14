from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])

from main_window import *
from menu_window import *

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAcking = True
        self.count_ask = 0 #кількість відповодей
        self.count_right = 0 #кількість правильних відповідей
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question("Яблуко", "Apple", "Pineapple", "Straberry", 'Blueberry')
q2 = Question('Дім', "House", 'Horse', 'School', 'Dom')
q3 = Question('Кіт', "Cat", 'Dog', 'Cats', 'Hq')
q4 = Question('Миша', "Mouse", 'Module', 'Mose', 'MSI')

question = [q1, q2, q3, q4] #список 
radio_button = [radiobutton1, radiobutton2, radiobutton3, radiobutton4] #список радіо кнопок

def ne_question():
    global curent_question
    curent_question = choice(question)


    ld_question.setText(curent_question.question)

    shuffle(radio_button)
    radio_button[0].setText(curent_question.answer)
    radio_button[1].setText(curent_question.wrong_answer1)
    radio_button[2].setText(curent_question.wrong_answer2)
    radio_button[3].setText(curent_question.wrong_answer3)

ne_question()

def check():
    for answer in radio_button:
        if answer.isChecked():
            if answer.text() == lb_Correct.text():
                curent_question.got_right()
                lb_Resultat.setText('Вірно!')
                break
    else:
        lb_Resultat.setText('не вірно!')
        curent_question.got_wrong()

def click_ok():
    if btn_ok.text() == 'Відповісти':
        check()
        radiobutton1.hide()
        radiobutton2.hide()
        radiobutton3.hide()
        radiobutton4.hide()

        btn_ok.setText('Наступне запитання')
    else:
        ne_question()
        radiobutton1.show()
        radiobutton2.show()
        radiobutton3.show()
        radiobutton4.show()

        btn_ok.setText('Відповісти')

btn_ok.clicked.connect(click_ok)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)

def back_menu():
    menu.hide()
    window.show()

btn_qbushButton.clicked.connect(back_menu)


def menu_generasion():
    menu.show()
    window.hide()

btn_menu.clicked.connect(menu_generasion)



window.show()
app.exec_()