from turtle import *
import math
def ngon(w):
    w=w.lower()
    if w=="triangle":
        return 3
    if w=="quadrilateral" or w=="square" or w=="rectangle" or w=="parallelogram" or w=="trapezoid" or w=="kite":
        return 4
    if "gon"!=w[-3:]:
        print(w[-1:-4:-1])
        return -1
    else:
        w=w[:-3]
    if w=="hecto":
        return 100
    names={
        "kis":1,
        "cos":10,
        "do":2,
        "hen":1,
        "hena":1,
        "di":2,
        "tri":3,
        "tetra":4,
        "penta":5,
        "hexa":6,
        "hepta":7,
        "octa":8,
        "ennea":9,
        "deca":10,
        "icosa":20,
        "icosi":20,
        "triaconta":30,
        "tetraconta":40,
        "pentaconta":50,
        "hexaconta":60,
        "heptaconta":70,
        "octaconta":80,
        "enneaconta":90,
        "hecta":100,
        "hecto":100,
        "chilia":1000,
        "myria":10000
    }
    tw=[]
    for i in names.keys():
        if i in w:
            tw.append(i)
    summ=0
    if tw[-1]=='deca':
        if names[tw[-2]]<10:
            summ+=10+names[tw[-2]]
            tw=tw[:-2]
        else:
            sum+=10
            tw=tw[:-1]
    
print(ngon("dodecagon"))