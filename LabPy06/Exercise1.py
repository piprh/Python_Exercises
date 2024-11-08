#!/usr/bin/python3
import os

def quiz(q1 = "Pip", q2 = "24", q3 = "Green", q4 = "Eh", q5 = "Fake news"):
    quiz_ans = {}
    As=[q1, q2, q3, q4, q5]
    Qs=['Name', 'Age', 'Colour', 'Python', 'Flat Earther']
    for Q in Qs:
        quiz_ans[Q]=As[Qs.index(Q)]
    return quiz_ans

a1 = input("Name: ")
a2 = input("Age: ")
a3 = input("Colour: ")
a4 = input("Python: ")
a5 = input("Flat earth: ")

print(quiz(a1, a2, a3, a4, a5))
    
