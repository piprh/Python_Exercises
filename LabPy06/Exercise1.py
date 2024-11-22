#!/usr/bin/python3
import os

def quiz(q1 = "Pip", q2 = "24", q3 = "Green", q4 = "Eh", q5 = "Fake news"):
    import string
    quiz_ans = {}
    As=[q1, q2, q3, q4, q5]
    Qs=['Name', 'Age', 'Colour', 'Python', 'Flat Earther']
    for Q in Qs:
        quiz_ans[Q]=As[Qs.index(Q)]
    return quiz_ans

ans={}
ans["a1"] = input("Name: ")
ans["a2"] = int(input("Age: ")) #wrapped with int because input defaults to string
ans["a3"] = input("Colour: ")
ans["a4"] = input("Python: ")
ans["a5"] = input("Flat earth: ")

print(quiz(*list(ans.values()))) #* passes multiple variables to the function
    
