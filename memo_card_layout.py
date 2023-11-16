from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)
sleep_text = QLabel("хвилин")

text_question = QLabel("Яблуко")

question_group_box = QGroupBox("Варіанти відповідей")
btn_group = QButtonGroup()

rbt1 = QRadioButton()
rbt2 = QRadioButton()
rbt3 = QRadioButton()
rbt4 = QRadioButton()

buttons_group.addButton(rbt1)
buttons_group.addButton(rbt2)
buttons_group.addButton(rbt3)
buttons_group.addButton(rbt4)

answer_group_box = QGroupBox("Результати тесту")
text_res = QLabel()
text_correct = QLabel()

layout_question_h1 = QHBoxLayout()
layout_question_v1 = QVBoxLayout()
layout_question_v2 = QVBoxLayout()

layout_question_v1.addWidget(rbt1)
layout_question_v1.addWidget(rbt2)
layout_question_v2.addWidget(rbt3)
layout_question_v2.addWidget(rbt4)

layout_question_h1.addLayout(layout_question_v1)
layout_question_h1.addLayout(layout_question_v2)