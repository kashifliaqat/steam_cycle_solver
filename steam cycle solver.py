# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 16:09:47 2021

@author: SARFRAZ AHMED
"""
import random as r
from tkinter import*
from sympy import symbols, solve
from CoolProp.CoolProp import PropsSI
def carnot():
    def Calculation():
         P0 = int(PRESURE1ENTRY.get())
         P1 = P0*1000
         P = int(PRESURE2ENTRY.get())
         P2 = P*1000
         QINUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
         QINUNIT.place(relx = 0.76,rely =0.45)
         QcompUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
         QcompUNIT.place(relx = 0.76,rely =0.53)
         WturbUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
         WturbUNIT.place(relx = 0.76,rely =0.61)
         WpumpUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
         WpumpUNIT.place(relx = 0.76,rely =0.70)
         TefiUNIT = Label(window,font = ('arial',15,'bold'),text = "% ",fg ="black")
         TefiUNIT.place(relx = 0.76,rely =0.78)
         BWRUNIT = Label(window,font = ('arial',15,'bold'),text = "% ",fg ="black")
         BWRUNIT.place(relx = 0.76,rely =0.85)
         H2 = PropsSI('H','P',P2,'Q',0,'Water')
         S2 = PropsSI('S','P',P2,'Q',0,'Water')
         S1f = PropsSI('S','P',P1,'Q',0,'Water')
         S1g = PropsSI('S','P',P1,'Q',1,'Water')
         S1fg = S1g-S1f
         s2s1f =S2-S1f
         x1 =s2s1f/S1fg
         H1f = PropsSI('H','P',P1,'Q',0,'Water')
         H1g = PropsSI('H','P',P1,'Q',1,'Water')
         H1fg =H1g-H1f
         H1fgx =H1fg*x1
         H1 = H1f + H1fgx
         H3 = PropsSI('H','P',P2,'Q',1,'Water')
         S3 = PropsSI('S','P',P2,'Q',1,'Water')
         T4 = PropsSI('T','P',P1,'Q',0,'Water')
         S4f = PropsSI('S','P',P1,'Q',0,'Water')
         S4g = PropsSI('S','P',P1,'Q',1,'Water')
         S4fg = S4g-S4f
         S32f =S3-S4f
         x4 =S32f/S4fg
         H4f = PropsSI('H','P',P1,'Q',0,'Water')
         H4g = PropsSI('H','P',P1,'Q',1,'Water')
         H4fg =H4g-H4f
         H4fgx =H4fg*x4
         H4 = H4f + H4fgx
         qsg =H3-H2
         qsg =qsg/1000
         qcomp =H4-H1
         qcomp =qcomp/1000
         Wturbine =H3-H4
         Wturbine =Wturbine/1000
         Wpump =H2-H1
         Wpump =Wpump/1000
         Wnet = Wturbine -Wpump
         Tefi = Wnet/qsg
         Tefi =Tefi*100
         BWR = Wpump/Wturbine
         BWR =BWR*100
         Qinresult.delete(0.0,END)
         Qinresult.insert(END,qsg)
         Qcompresult.delete(0.0,END)
         Qcompresult.insert(END,qcomp)
         Wturbresult.delete(0.0,END)
         Wturbresult.insert(END,Wturbine)
         Wpumpresult.delete(0.0,END)
         Wpumpresult.insert(END, Wpump)
         Tefiresult.delete(0.0,END)
         Tefiresult.insert(END,Tefi)
         BWRresult.delete(0.0,END)
         BWRresult.insert(END,BWR)
    window = Tk()
    window.geometry("300x400")
    window.title("CARNOT CYCLE SOLVER")
    progname = Label(window,font = ('arial',16,'bold'),text = "CARNOT CYCLE SOLVER",fg ="blue")
    progname.place(relx=0.06,rely=0.01)
    commant = Label(window,font = ('arial',12,'bold'),text = "PUT PRESSURE IN *KP*",fg ="black")
    commant.place(relx=0.025,rely=0.13)
    PRESSURE1 = Label(window,font = ('arial',15,'bold'),text="P1")
    PRESSURE1.place(relx=0.025,rely=0.2)
    sign1 = Label(window,font = ('arial',15,'bold'),text="=")
    sign1.place(relx=0.2,rely=0.2)
    pressure1vlaue=StringVar()
    PRESURE1ENTRY = Entry(window,textvariable=pressure1vlaue,font = ('arial',12,'bold'))
    PRESURE1ENTRY.place(relx=0.35,rely=0.2)
    PRESSURE2 = Label(window,font = ('arial',15,'bold'),text="P2")
    PRESSURE2.place(relx=0.025,rely=0.28)
    sign2 = Label(window,font = ('arial',15,'bold'),text="=")
    sign2.place(relx=0.2,rely=0.28)
    pressure2vlaue=StringVar()
    PRESURE2ENTRY = Entry(window,textvariable=pressure2vlaue,font = ('arial',12,'bold'))
    PRESURE2ENTRY.place(relx=0.35,rely=0.28)
    QIN = Label(window,font = ('arial',12,'bold'),text = "Qin ",fg ="black")
    QIN.place(relx = 0.1,rely =0.45)
    Qinresult =Text(window,font = ('arial',10,'bold'), height =1 ,width = 18)
    Qinresult.place(relx=0.32,rely=0.45)
    Qcomp = Label(window,font = ('arial',12,'bold'),text = "Qcomp ",fg ="black")
    Qcomp.place(relx = 0.1,rely =0.53)
    Qcompresult =Text(window,font = ('arial',10,'bold'), height =1 ,width = 18)
    Qcompresult.place(relx=0.32,rely=0.53)
    Wturb = Label(window,font = ('arial',12,'bold'),text = "Wturb ",fg ="black")
    Wturb.place(relx = 0.1,rely =0.61)
    Wturbresult =Text(window,font = ('arial',10,'bold'), height =1 ,width = 18)
    Wturbresult.place(relx=0.32,rely=0.61)
    Wpump = Label(window,font = ('arial',12,'bold'),text = "Wpump ",fg ="black")
    Wpump.place(relx = 0.1,rely =0.70)
    Wpumpresult =Text(window, font = ('arial',10,'bold'),height =1 ,width = 18)
    Wpumpresult.place(relx=0.32,rely=0.70)
    Tefi  = Label(window,font = ('arial',12,'bold'),text = "Tefi ",fg ="black")
    Tefi.place(relx = 0.1,rely =0.78)
    Tefiresult =Text(window,font = ('arial',10,'bold'), height =1 ,width = 18)
    Tefiresult.place(relx=0.32,rely=0.78)
    BWR  = Label(window,font = ('arial',12,'bold'),text = "BWR ",fg ="black")
    BWR.place(relx = 0.1,rely =0.85)
    BWRresult =Text(window, font = ('arial',10,'bold'),height =1 ,width = 18)
    BWRresult.place(relx=0.32,rely=0.85)
    Genbutton = Button(window,font = ('arial',10,'bold'),text="CALCULATE",command=Calculation)
    Genbutton.place(relx = 0.3,rely =0.35)
    window.mainloop()
def rankine():
    def Calculatio():
        P0 = int(PRESURE1ENTRY.get())
        P1 = P0*1000
        P = int(PRESURE2ENTRY.get())
        P2 =P*1000
        POWE = int(POWERENTRY.get())
        POWER = POWE*1000
        QINUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        QINUNIT.place(relx = 0.76,rely =0.45)
        QcompUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        QcompUNIT.place(relx = 0.76,rely =0.53)
        WturbUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        WturbUNIT.place(relx = 0.76,rely =0.61)
        WpumpUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        WpumpUNIT.place(relx = 0.76,rely =0.70)
        TefiUNIT = Label(window,font = ('arial',15,'bold'),text = "% ",fg ="black")
        TefiUNIT.place(relx = 0.76,rely =0.78)
        BWRUNIT = Label(window,font = ('arial',15,'bold'),text = "% ",fg ="black")
        BWRUNIT.place(relx = 0.76,rely =0.85)
        MASSUNIT = Label(window,font = ('arial',12,'bold'),text = "Kg/s ",fg ="black")
        MASSUNIT.place(relx = 0.76,rely =0.93)
        H1 = PropsSI('H','P',P1,'Q',0,'Water')
        S1 = PropsSI('S','P',P1,'Q',0,'Water')
        H2 = PropsSI('H','P',P2,'S',S1,'Water')
        H3 = PropsSI('H','P',P2,'Q',1,'Water')
        S3 = PropsSI('S','P',P2,'Q',1,'Water')
        S4f = PropsSI('S','P',P1,'Q',0,'Water')
        S4g = PropsSI('S','P',P1,'Q',1,'Water')
        S4fg = S4g-S4f
        S32f =S3-S4f
        x4 =S32f/S4fg
        H4f = PropsSI('H','P',P1,'Q',0,'Water')
        H4g = PropsSI('H','P',P1,'Q',1,'Water')
        H4fg =H4g-H4f
        H4fgx =H4fg*x4
        H4 = H4f + H4fgx
        qsg =H3-H2
        qsg =qsg/1000
        qcomp =H4-H1
        qcomp =qcomp/1000
        Wturbine =H3-H4
        Wturbine =Wturbine/1000
        Wpump =H2-H1
        Wpump =Wpump/1000
        Wnet = Wturbine -Wpump
        Tefi = Wnet/qsg
        Tefi =Tefi*100
        BWR = Wpump/Wturbine
        BWR =BWR*100
        C=Wturbine-Wpump
        M = POWER/C
        Qinresult.delete(0.0,END)
        Qinresult.insert(END,qsg)
        Qcompresult.delete(0.0,END)
        Qcompresult.insert(END,qcomp)
        Wturbresult.delete(0.0,END)
        Wturbresult.insert(END,Wturbine)
        Wpumpresult.delete(0.0,END)
        Wpumpresult.insert(END, Wpump)
        Tefiresult.delete(0.0,END)
        Tefiresult.insert(END,Tefi)
        BWRresult.delete(0.0,END)
        BWRresult.insert(END,BWR)
        massresult.delete(0.0,END)
        massresult.insert(END,M)
    window = Tk()
    window.geometry("300x450")
    window.title("RANKINE CYCLE CALCULATER")
    progname = Label(window,font = ('arial',16,'bold'),text = "RANKINE CYCLE SOLVER",fg ="blue")
    progname.place(relx=0.07,rely=0.01)
    commant = Label(window,font = ('arial',12,'bold'),text = "PUT VALUES IN *PASCAL*,*KW*",fg ="black")
    commant.place(relx=0.025,rely=0.10)
    PRESSURE1 = Label(window,font = ('arial',12,'bold'),text="P1")
    PRESSURE1.place(relx=0.025,rely=0.18)
    sign1 = Label(window,font = ('arial',12,'bold'),text="=")
    sign1.place(relx=0.2,rely=0.18)
    pressure1vlaue=StringVar()
    PRESURE1ENTRY = Entry(window,textvariable=pressure1vlaue,font = ('arial',12,'bold'))
    PRESURE1ENTRY.place(relx=0.35,rely=0.18)
    PRESSURE2 = Label(window,font = ('arial',12,'bold'),text="P2")
    PRESSURE2.place(relx=0.025,rely=0.24)
    sign2 = Label(window,font = ('arial',12,'bold'),text="=")
    sign2.place(relx=0.2,rely=0.24)
    pressure2vlaue=StringVar()
    PRESURE2ENTRY = Entry(window,textvariable=pressure2vlaue,font = ('arial',12,'bold'))
    PRESURE2ENTRY.place(relx=0.35,rely=0.24)
    POWER = Label(window,font = ('arial',12,'bold'),text="Wnet")
    POWER.place(relx=0.025,rely=0.30)
    POWERsign = Label(window,font = ('arial',12,'bold'),text="=")
    POWERsign.place(relx=0.2,rely=0.30)
    POWERvlaue=StringVar()
    POWERENTRY = Entry(window,textvariable=POWERvlaue,font = ('arial',12,'bold'))
    POWERENTRY.place(relx=0.35,rely=0.30)
    QIN = Label(window,font = ('arial',12,'bold'),text = "Qin ",fg ="black")
    QIN.place(relx = 0.1,rely =0.45)
    Qinresult =Text(window,font = ('arial',10,'bold'), height =1 ,width = 18)
    Qinresult.place(relx=0.32,rely=0.45)
    Qcomp = Label(window,font = ('arial',12,'bold'),text = "Qcomp ",fg ="black")
    Qcomp.place(relx = 0.1,rely =0.53)
    Qcompresult =Text(window,font = ('arial',10,'bold'), height =1 ,width = 18)
    Qcompresult.place(relx=0.32,rely=0.53)
    Wturb = Label(window,font = ('arial',12,'bold'),text = "Wturb ",fg ="black")
    Wturb.place(relx = 0.1,rely =0.61)
    Wturbresult =Text(window,font = ('arial',10,'bold'), height =1 ,width = 18)
    Wturbresult.place(relx=0.32,rely=0.61)
    Wpump = Label(window,font = ('arial',12,'bold'),text = "Wpump ",fg ="black")
    Wpump.place(relx = 0.1,rely =0.69)
    Wpumpresult =Text(window, font = ('arial',10,'bold'),height =1 ,width = 18)
    Wpumpresult.place(relx=0.32,rely=0.69)
    Tefi  = Label(window,font = ('arial',12,'bold'),text = "Tefi ",fg ="black")
    Tefi.place(relx = 0.1,rely =0.77)
    Tefiresult =Text(window,font = ('arial',10,'bold'), height =1 ,width = 18)
    Tefiresult.place(relx=0.32,rely=0.77)
    BWR  = Label(window,font = ('arial',12,'bold'),text = "BWR ",fg ="black")
    BWR.place(relx = 0.1,rely =0.85)
    BWRresult =Text(window, font = ('arial',10,'bold'),height =1 ,width = 18)
    BWRresult.place(relx=0.32,rely=0.85)
    mass  = Label(window,font = ('arial',12,'bold'),text = "mfr",fg ="black")
    mass.place(relx = 0.1,rely =0.93)
    massresult =Text(window, font = ('arial',10,'bold'),height =1 ,width = 18)
    massresult.place(relx=0.32,rely=0.93)
    Genbutton = Button(window,font = ('arial',10,'bold'),text="CALCULATE",command=Calculatio)
    Genbutton.place(relx = 0.3,rely =0.37)
    window.mainloop()
def srankine():
    def Calculati():
        P0 = int(PRESURE1ENTRY.get())
        P1 =P0*1000
        P = int(PRESURE2ENTRY.get())
        P2 =P*1000
        t = int(TENTRY.get())
        t1 =t+273
        POWE = int(POWERENTRY.get())
        POWER =POWE*1000
        TeP = int(TeffPENTRY.get())
        TefP = TeP/100
        TeT = int(TeffTENTRY.get())
        TefT = TeT/100
        QINUNIT = Label(window,font = ('arial',10,'bold'),text = "KJ/Kg ",fg ="black")
        QINUNIT.place(relx = 0.8,rely =0.52)
        QcompUNIT = Label(window,font = ('arial',10,'bold'),text = "KJ/Kg ",fg ="black")
        QcompUNIT.place(relx = 0.8,rely =0.59)
        WturbUNIT = Label(window,font = ('arial',10,'bold'),text = "KJ/Kg ",fg ="black")
        WturbUNIT.place(relx = 0.8,rely =0.66)
        WpumpUNIT = Label(window,font = ('arial',10,'bold'),text = "KJ/Kg ",fg ="black")
        WpumpUNIT.place(relx = 0.8,rely =0.73)
        TefiUNIT = Label(window,font = ('arial',12,'bold'),text = "% ",fg ="black")
        TefiUNIT.place(relx = 0.8,rely =0.8)
        BWRUNIT = Label(window,font = ('arial',12,'bold'),text = "% ",fg ="black")
        BWRUNIT.place(relx = 0.8,rely =0.87)
        MASSUNIT = Label(window,font = ('arial',10,'bold'),text = "Kg/s ",fg ="black")
        MASSUNIT.place(relx = 0.8,rely =0.94)
        H1 = PropsSI('H','P',P1,'Q',0,'Water')
        S1 = PropsSI('S','P',P1,'Q',0,'Water')
        H2s = PropsSI('H','P',P2,'S',S1,'Water')
        H3 = PropsSI('H','P',P2,'T',t1,'Water')
        S3 = PropsSI('S','P',P2,'T',t1,'Water')
        S4f = PropsSI('S','P',P1,'Q',0,'Water')
        S4g = PropsSI('S','P',P1,'Q',1,'Water')
        S4fg = S4g-S4f
        S32f =S3-S4f
        x4 =S32f/S4fg
        H4f = PropsSI('H','P',P1,'Q',0,'Water')
        H4g = PropsSI('H','P',P1,'Q',1,'Water')
        H4fg =H4g-H4f
        H4fgx =H4fg*x4
        H4s = H4f + H4fgx
        hhs = 1/TefP
        hhs1 =  H2s-H1
        hhs2 = hhs*hhs1
        H2 = hhs2+H1
        hhhs1 =  H3-H4s
        hhhs2 = hhhs1*TefT
        H4 = H3-hhhs2
        qsg =H3-H2
        qsg =qsg/1000
        qcomp =H4-H1
        qcomp =qcomp/1000
        Wturbine =H3-H4
        Wturbine =Wturbine/1000
        Wpump =H2-H1
        Wpump =Wpump/1000
        Wnet = Wturbine -Wpump
        Tefi = Wnet/qsg
        Tefi =Tefi*100
        BWR = Wpump/Wturbine
        BWR = BWR*100
        C=Wturbine-Wpump
        M = POWER/C
        Qinresult.delete(0.0,END)
        Qinresult.insert(END,qsg)
        Qcompresult.delete(0.0,END)
        Qcompresult.insert(END,qcomp)
        Wturbresult.delete(0.0,END)
        Wturbresult.insert(END,Wturbine)
        Wpumpresult.delete(0.0,END)
        Wpumpresult.insert(END, Wpump)
        Tefiresult.delete(0.0,END)
        Tefiresult.insert(END,Tefi)
        BWRresult.delete(0.0,END)
        BWRresult.insert(END,BWR)
        massresult.delete(0.0,END)
        massresult.insert(END,M)
    window = Tk()
    window.geometry("320x600")
    window.title("RANKINE CYCLE CALCULATER ")
    progname = Label(window,font = ('arial',16,'bold'),text = "RANKINE CYCLE SOLVER",fg ="blue")
    progname.place(relx=0.07,rely=0.01)
    commant = Label(window,font = ('arial',12,'bold'),text = "PUT VALUES IN *KP*,  *C*,  *MW* ,*% *",fg ="black")
    commant.place(relx=0.025,rely=0.08)
    PRESSURE1 = Label(window,font = ('arial',12,'bold'),text="P1")
    PRESSURE1.place(relx=0.025,rely=0.15)
    sign1 = Label(window,font = ('arial',12,'bold'),text="=")
    sign1.place(relx=0.2,rely=0.15)
    pressure1vlaue=StringVar()
    PRESURE1ENTRY = Entry(window,textvariable=pressure1vlaue,font = ('arial',12,'bold'))
    PRESURE1ENTRY.place(relx=0.35,rely=0.15)
    PRESSURE2 = Label(window,font = ('arial',12,'bold'),text="P2")
    PRESSURE2.place(relx=0.025,rely=0.20)
    sign2 = Label(window,font = ('arial',12,'bold'),text="=")
    sign2.place(relx=0.2,rely=0.20)
    pressure2vlaue=StringVar()
    PRESURE2ENTRY = Entry(window,textvariable=pressure2vlaue,font = ('arial',12,'bold'))
    PRESURE2ENTRY.place(relx=0.35,rely=0.20)
    T = Label(window,font = ('arial',12,'bold'),text="Tstat")
    T.place(relx=0.025,rely=0.25)
    Tsign = Label(window,font = ('arial',12,'bold'),text="=")
    Tsign.place(relx=0.2,rely=0.25)
    Tvlaue=StringVar()
    TENTRY = Entry(window,textvariable=Tvlaue,font = ('arial',12,'bold'))
    TENTRY.place(relx=0.35,rely=0.25)
    POWER = Label(window,font = ('arial',12,'bold'),text="Wnet")
    POWER.place(relx=0.025,rely=0.30)
    POWERsign = Label(window,font = ('arial',12,'bold'),text="=")
    POWERsign.place(relx=0.2,rely=0.30)
    POWERvlaue=StringVar()
    POWERENTRY = Entry(window,textvariable=POWERvlaue,font = ('arial',12,'bold'))
    POWERENTRY.place(relx=0.35,rely=0.30)
    TeffP = Label(window,font = ('arial',12,'bold'),text="Te_P")
    TeffP.place(relx=0.025,rely=0.35)
    TeffPsign = Label(window,font = ('arial',12,'bold'),text="=")
    TeffPsign.place(relx=0.2,rely=0.35)
    TeffPvlaue=StringVar()
    TeffPENTRY = Entry(window,textvariable=TeffPvlaue,font = ('arial',12,'bold'))
    TeffPENTRY.place(relx=0.35,rely=0.35)
    TeffT = Label(window,font = ('arial',12,'bold'),text="Te_T")
    TeffT.place(relx=0.025,rely=0.4)
    TeffTsign = Label(window,font = ('arial',12,'bold'),text="=")
    TeffTsign.place(relx=0.2,rely=0.4)
    TeffTvlaue=StringVar()
    TeffTENTRY = Entry(window,textvariable=TeffTvlaue,font = ('arial',12,'bold'))
    TeffTENTRY.place(relx=0.35,rely=0.4)
    QIN = Label(window,font = ('arial',12,'bold'),text = "Qboil ",fg ="black")
    QIN.place(relx = 0.025,rely =0.52)
    Qinresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Qinresult.place(relx=0.27,rely=0.52)
    Qcomp = Label(window,font = ('arial',12,'bold'),text = "Qcond ",fg ="black")
    Qcomp.place(relx = 0.025,rely =0.59)
    Qcompresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Qcompresult.place(relx=0.27,rely=0.59)
    Wturb = Label(window,font = ('arial',12,'bold'),text = "Wturb ",fg ="black")
    Wturb.place(relx = 0.025,rely =0.66)
    Wturbresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Wturbresult.place(relx=0.27,rely=0.66)
    Wpump = Label(window,font = ('arial',12,'bold'),text = "Wpump ",fg ="black")
    Wpump.place(relx =0.025,rely =0.73)
    Wpumpresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    Wpumpresult.place(relx=0.27,rely=0.73)
    Tefi  = Label(window,font = ('arial',12,'bold'),text = "Tefi ",fg ="black")
    Tefi.place(relx = 0.025,rely =0.8)
    Tefiresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Tefiresult.place(relx=0.27,rely=0.8)
    BWR  = Label(window,font = ('arial',12,'bold'),text = "BWR ",fg ="black")
    BWR.place(relx = 0.025,rely =0.87)
    BWRresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    BWRresult.place(relx=0.27,rely=0.87)
    mass  = Label(window,font = ('arial',12,'bold'),text = "mfr",fg ="black")
    mass.place(relx = 0.025,rely =0.94)
    massresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    massresult.place(relx=0.27,rely=0.94)
    Genbutton = Button(window,font = ('arial',10,'bold'),text="CALCULATE",command=Calculati)
    Genbutton.place(relx = 0.35,rely =0.455)
    window.mainloop()
def Rrankine():
    def Calculation():
        P0 = int(PRESURE1ENTRY.get())
        P1 =P0*1000
        P = int(PRESURE2ENTRY.get())
        P2 =P*1000
        Pp = int(PRESURE3ENTRY.get())
        P3 =Pp*1000
        t = int(TENTRY.get())
        t1 =t+273
        POWE = int(POWERENTRY.get())
        POWER =POWE*1000
        QINUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        QINUNIT.place(relx = 0.8,rely =0.54)
        QcompUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        QcompUNIT.place(relx = 0.8,rely =0.6)
        WturbUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        WturbUNIT.place(relx = 0.8,rely =0.66)
        WpumpUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        WpumpUNIT.place(relx = 0.8,rely =0.72)
        TefiUNIT = Label(window,font = ('arial',15,'bold'),text = "% ",fg ="black")
        TefiUNIT.place(relx = 0.8,rely =0.89)
        BWRUNIT = Label(window,font = ('arial',15,'bold'),text = "% ",fg ="black")
        BWRUNIT.place(relx = 0.8,rely =0.85)
        MASSUNIT = Label(window,font = ('arial',12,'bold'),text = "Kg/s ",fg ="black")
        MASSUNIT.place(relx = 0.8,rely =0.91)
        H1 = PropsSI('H','P',P1,'Q',0,'Water')
        S1 = PropsSI('S','P',P1,'Q',0,'Water')
        H2 = PropsSI('H','P',P2,'S',S1,'Water')
        H3 = PropsSI('H','P',P2,'T',t1,'Water')
        S3 = PropsSI('S','P',P2,'T',t1,'Water')
        H4 = PropsSI('H','P',P3,'S',S3,'Water')
        H5 = PropsSI('H','P',P3,'T',t1,'Water')
        S5 = PropsSI('S','P',P3,'T',t1,'Water')
        T6 = PropsSI('T','P',P1,'Q',0,'Water')
        T6 = T6-273
        S6f = PropsSI('S','P',P1,'Q',0,'Water')
        S6g = PropsSI('S','P',P1,'Q',1,'Water')
        S6fg = S6g-S6f
        S62f =S5-S6f
        x6 =S62f/S6fg
        H6f = PropsSI('H','P',P1,'Q',0,'Water')
        H6g = PropsSI('H','P',P1,'Q',1,'Water')
        H6fg =H6g-H6f
        H6fgx =H6fg*x6
        H6 = H6f + H6fgx
        qsg =(H3-H2)+(H5-H4)
        qsg =qsg/1000
        qcomp =H6-H1
        qcomp =qcomp/1000
        Wturbine =(H3-H4)+(H5-H6)
        Wturbine =Wturbine/1000
        Wpump =H2-H1
        Wpump =Wpump/1000
        Wnet = Wturbine -Wpump
        Tefi = Wnet/qsg
        Tefi =Tefi*100
        BWR = Wpump/Wturbine
        BWR =BWR*100
        C=Wturbine-Wpump
        M = POWER/C
        Qinresult.delete(0.0,END)
        Qinresult.insert(END,qsg)
        Qcompresult.delete(0.0,END)
        Qcompresult.insert(END,qcomp)
        Wturbresult.delete(0.0,END)
        Wturbresult.insert(END,Wturbine)
        Wpumpresult.delete(0.0,END)
        Wpumpresult.insert(END, Wpump)
        Tefiresult.delete(0.0,END)
        Tefiresult.insert(END,Tefi)
        BWRresult.delete(0.0,END)
        BWRresult.insert(END,BWR)
        massresult.delete(0.0,END)
        massresult.insert(END,M)
    window = Tk()
    window.geometry("300x550")
    window.title("RANKINE CYCLE CALCULATER ")
    progname = Label(window,font = ('arial',16,'bold'),text = "RANKINE CYCLE SOLVER",fg ="blue")
    progname.place(relx=0.07,rely=0.01)
    commant = Label(window,font = ('arial',12,'bold'),text = "PUT VALUES IN *KP*,  *C*,  *MW* ",fg ="black")
    commant.place(relx=0.025,rely=0.08)
    PRESSURE1 = Label(window,font = ('arial',12,'bold'),text="P1")
    PRESSURE1.place(relx=0.025,rely=0.14)
    pressure1vlaue=StringVar()
    sign1 = Label(window,font = ('arial',12,'bold'),text="=")
    sign1.place(relx=0.2,rely=0.14)
    pressure1vlaue=StringVar()
    PRESURE1ENTRY = Entry(window,textvariable=pressure1vlaue,font = ('arial',12,'bold'))
    PRESURE1ENTRY.place(relx=0.35,rely=0.14)
    PRESSURE2 = Label(window,font = ('arial',12,'bold'),text="P2")
    PRESSURE2.place(relx=0.025,rely=0.2)
    sign2 = Label(window,font = ('arial',12,'bold'),text="=")
    sign2.place(relx=0.2,rely=0.2)
    pressure2vlaue=StringVar()
    PRESURE2ENTRY = Entry(window,textvariable=pressure2vlaue,font = ('arial',12,'bold'))
    PRESURE2ENTRY.place(relx=0.35,rely=0.2)
    PRESSURE3 = Label(window,font = ('arial',12,'bold'),text="P3")
    PRESSURE3.place(relx=0.025,rely=0.26)
    sign2 = Label(window,font = ('arial',12,'bold'),text="=")
    sign2.place(relx=0.2,rely=0.26)
    pressure2vlaue=StringVar()
    PRESURE3ENTRY = Entry(window,textvariable=pressure2vlaue,font = ('arial',12,'bold'))
    PRESURE3ENTRY.place(relx=0.35,rely=0.26)
    T = Label(window,font = ('arial',12,'bold'),text="T3 =T5")
    T.place(relx=0.021,rely=0.32)
    Tsign = Label(window,font = ('arial',12,'bold'),text="=")
    Tsign.place(relx=0.2,rely=0.32)
    Tvlaue=StringVar()
    TENTRY = Entry(window,textvariable=Tvlaue,font = ('arial',12,'bold'))
    TENTRY.place(relx=0.35,rely=0.32)
    POWER = Label(window,font = ('arial',12,'bold'),text="Wnet")
    POWER.place(relx=0.025,rely=0.39)
    POWERsign = Label(window,font = ('arial',12,'bold'),text="=")
    POWERsign.place(relx=0.2,rely=0.39)
    POWERvlaue=StringVar()
    POWERENTRY = Entry(window,textvariable=POWERvlaue,font = ('arial',12,'bold'))
    POWERENTRY.place(relx=0.35,rely=0.39)
    QIN = Label(window,font = ('arial',12,'bold'),text = "Qboil ",fg ="black")
    QIN.place(relx = 0.025,rely =0.54)
    Qinresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Qinresult.place(relx=0.27,rely=0.54)
    Qcomp = Label(window,font = ('arial',12,'bold'),text = "Qcond ",fg ="black")
    Qcomp.place(relx = 0.025,rely =0.6)
    Qcompresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Qcompresult.place(relx=0.27,rely=0.6)
    Wturb = Label(window,font = ('arial',12,'bold'),text = "Wturb ",fg ="black")
    Wturb.place(relx = 0.025,rely =0.66)
    Wturbresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Wturbresult.place(relx=0.27,rely=0.66)
    Wpump = Label(window,font = ('arial',12,'bold'),text = "Wpump ",fg ="black")
    Wpump.place(relx =0.025,rely =0.72)
    Wpumpresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    Wpumpresult.place(relx=0.27,rely=0.72)
    Tefi  = Label(window,font = ('arial',12,'bold'),text = "Tefi ",fg ="black")
    Tefi.place(relx = 0.025,rely =0.79)
    Tefiresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Tefiresult.place(relx=0.27,rely=0.79)
    BWR  = Label(window,font = ('arial',12,'bold'),text = "BWR ",fg ="black")
    BWR.place(relx = 0.025,rely =0.85)
    BWRresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    BWRresult.place(relx=0.27,rely=0.85)
    mass  = Label(window,font = ('arial',12,'bold'),text = "mfr",fg ="black")
    mass.place(relx = 0.025,rely =0.91)
    massresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    massresult.place(relx=0.27,rely=0.91)
    Genbutton = Button(window,font = ('arial',10,'bold'),text="CALCULATE",command=Calculation)
    Genbutton.place(relx = 0.35,rely =0.46)
    window.mainloop()
def RRrankine():
    def Calculation():
        P0 = int(PRESURE1ENTRY.get())
        P1 =P0*1000
        P = int(PRESURE2ENTRY.get())
        P2 =P*1000
        Pp = int(PRESURE3ENTRY.get())
        P3 =Pp*1000
        t = int(TENTRY.get())
        t1 =t+273
        POWE = int(POWERENTRY.get())
        POWER =POWE*1000
        QINUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        QINUNIT.place(relx = 0.8,rely =0.54)
        QcompUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        QcompUNIT.place(relx = 0.8,rely =0.6)
        WturbUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        WturbUNIT.place(relx = 0.8,rely =0.66)
        WpumpUNIT = Label(window,font = ('arial',12,'bold'),text = "KJ/Kg ",fg ="black")
        WpumpUNIT.place(relx = 0.8,rely =0.72)
        TefiUNIT = Label(window,font = ('arial',15,'bold'),text = "% ",fg ="black")
        TefiUNIT.place(relx = 0.8,rely =0.89)
        BWRUNIT = Label(window,font = ('arial',15,'bold'),text = "% ",fg ="black")
        BWRUNIT.place(relx = 0.8,rely =0.85)
        MASSUNIT = Label(window,font = ('arial',12,'bold'),text = "Kg/s ",fg ="black")
        MASSUNIT.place(relx = 0.8,rely =0.91)
        T1 = PropsSI('T','P',P1,'Q',0,'Water')
        H1 = PropsSI('H','P',P1,'Q',0,'Water')
        S1 = PropsSI('S','P',P1,'Q',0,'Water')
        T2 = PropsSI('T','P',P3,'S',S1,'Water')
        H2 = PropsSI('H','P',P3,'S',S1,'Water')
        H3 = PropsSI('H','P',P3,'Q',0,'Water')
        S3 = PropsSI('S','P',P3,'Q',0,'Water')
        H4 = PropsSI('H','P',P2,'S',S3,'Water')
        H5 = PropsSI('H','P',P2,'T',t1,'Water')
        S5 = PropsSI('S','P',P2,'T',t1,'Water')
        H6 = PropsSI('H','P',P3,'S',S5,'Water')
        S7f = PropsSI('S','P',P1,'Q',0,'Water')
        S7g = PropsSI('S','P',P1,'Q',1,'Water')
        S7fg = S7g-S7f
        S72f =S5-S7f
        x7 =S72f/S7fg
        H7f = PropsSI('H','P',P1,'Q',0,'Water')
        H7g = PropsSI('H','P',P1,'Q',1,'Water')
        H7fg =H7g-H7f
        H7fgx =H7fg*x7
        H7 = H7f + H7fgx
        ld = (H3-H2)/(H6-H2)
        qsg =H5-H4
        qsg =qsg/1000
        qcomp =(H7-H1)*(1-ld)
        qcomp =qcomp/1000
        Wturbine =(H5-H6)+(H6-H7)*(1-ld)
        Wturbine =Wturbine/1000
        Wpump =(H4-H3)+(1-ld)*(H2-H1)
        Wpump =Wpump/1000
        Wnet = Wturbine -Wpump
        Tefi = Wnet/qsg
        Tefi =Tefi*100
        BWR = Wpump/Wturbine
        BWR =BWR*100
        C=Wturbine-Wpump
        M = POWER/C
        Qinresult.delete(0.0,END)
        Qinresult.insert(END,qsg)
        Qcompresult.delete(0.0,END)
        Qcompresult.insert(END,qcomp)
        Wturbresult.delete(0.0,END)
        Wturbresult.insert(END,Wturbine)
        Wpumpresult.delete(0.0,END)
        Wpumpresult.insert(END, Wpump)
        Tefiresult.delete(0.0,END)
        Tefiresult.insert(END,Tefi)
        BWRresult.delete(0.0,END)
        BWRresult.insert(END,BWR)
        massresult.delete(0.0,END)
        massresult.insert(END,M)
    window = Tk()
    window.geometry("300x570")
    window.title("R RANKINE CYCLE CALCULATER ")
    progname = Label(window,font = ('arial',16,'bold'),text = "R RANKINE CYCLE SOLVER",fg ="blue")
    progname.place(relx=0.04,rely=0.01)
    commant = Label(window,font = ('arial',12,'bold'),text = "PUT VALUES IN *KP*,  *C*,  *MW* ",fg ="black")
    commant.place(relx=0.025,rely=0.08)
    PRESSURE1 = Label(window,font = ('arial',12,'bold'),text="P1")
    PRESSURE1.place(relx=0.025,rely=0.14)
    pressure1vlaue=StringVar()
    sign1 = Label(window,font = ('arial',12,'bold'),text="=")
    sign1.place(relx=0.2,rely=0.14)
    pressure1vlaue=StringVar()
    PRESURE1ENTRY = Entry(window,textvariable=pressure1vlaue,font = ('arial',12,'bold'))
    PRESURE1ENTRY.place(relx=0.35,rely=0.14)
    PRESSURE2 = Label(window,font = ('arial',12,'bold'),text="P2")
    PRESSURE2.place(relx=0.025,rely=0.2)
    sign2 = Label(window,font = ('arial',12,'bold'),text="=")
    sign2.place(relx=0.2,rely=0.2)
    pressure2vlaue=StringVar()
    PRESURE2ENTRY = Entry(window,textvariable=pressure2vlaue,font = ('arial',12,'bold'))
    PRESURE2ENTRY.place(relx=0.35,rely=0.2)
    PRESSURE3 = Label(window,font = ('arial',12,'bold'),text="P3")
    PRESSURE3.place(relx=0.025,rely=0.26)
    sign2 = Label(window,font = ('arial',12,'bold'),text="=")
    sign2.place(relx=0.2,rely=0.26)
    pressure2vlaue=StringVar()
    PRESURE3ENTRY = Entry(window,textvariable=pressure2vlaue,font = ('arial',12,'bold'))
    PRESURE3ENTRY.place(relx=0.35,rely=0.26)
    T = Label(window,font = ('arial',12,'bold'),text="TS")
    T.place(relx=0.021,rely=0.32)
    Tsign = Label(window,font = ('arial',12,'bold'),text="=")
    Tsign.place(relx=0.2,rely=0.32)
    Tvlaue=StringVar()
    TENTRY = Entry(window,textvariable=Tvlaue,font = ('arial',12,'bold'))
    TENTRY.place(relx=0.35,rely=0.32)
    POWER = Label(window,font = ('arial',12,'bold'),text="Wnet")
    POWER.place(relx=0.025,rely=0.39)
    POWERsign = Label(window,font = ('arial',12,'bold'),text="=")
    POWERsign.place(relx=0.2,rely=0.39)
    POWERvlaue=StringVar()
    POWERENTRY = Entry(window,textvariable=POWERvlaue,font = ('arial',12,'bold'))
    POWERENTRY.place(relx=0.35,rely=0.39)
    QIN = Label(window,font = ('arial',12,'bold'),text = "Qboil ",fg ="black")
    QIN.place(relx = 0.025,rely =0.54)
    Qinresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Qinresult.place(relx=0.27,rely=0.54)
    Qcomp = Label(window,font = ('arial',12,'bold'),text = "Qcond ",fg ="black")
    Qcomp.place(relx = 0.025,rely =0.6)
    Qcompresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Qcompresult.place(relx=0.27,rely=0.6)
    Wturb = Label(window,font = ('arial',12,'bold'),text = "Wturb ",fg ="black")
    Wturb.place(relx = 0.025,rely =0.66)
    Wturbresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Wturbresult.place(relx=0.27,rely=0.66)
    Wpump = Label(window,font = ('arial',12,'bold'),text = "Wpump ",fg ="black")
    Wpump.place(relx =0.025,rely =0.72)
    Wpumpresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    Wpumpresult.place(relx=0.27,rely=0.72)
    Tefi  = Label(window,font = ('arial',12,'bold'),text = "Tefi ",fg ="black")
    Tefi.place(relx = 0.025,rely =0.79)
    Tefiresult =Text(window,font = ('arial',12,'bold'), height =1 ,width = 18)
    Tefiresult.place(relx=0.27,rely=0.79)
    BWR  = Label(window,font = ('arial',12,'bold'),text = "BWR ",fg ="black")
    BWR.place(relx = 0.025,rely =0.85)
    BWRresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    BWRresult.place(relx=0.27,rely=0.85)
    mass  = Label(window,font = ('arial',12,'bold'),text = "mfr",fg ="black")
    mass.place(relx = 0.025,rely =0.91)
    massresult =Text(window, font = ('arial',12,'bold'),height =1 ,width = 18)
    massresult.place(relx=0.27,rely=0.91)
    Genbutton = Button(window,font = ('arial',10,'bold'),text="CALCULATE",command=Calculation)
    Genbutton.place(relx = 0.35,rely =0.46)
    window.mainloop()
window = Tk()
window.geometry("300x400")
window.title("STEAM CYCLE SOLVER")
progname = Label(window,font = ('arial',18,'bold'),text = "STEAM CYCLE SOLVER",fg ="blue")
progname.place(relx=0.05,rely=0.01)
choosetype = Label(window,font = ('Kristen ITC',15,'bold'),text = "CHOSE YOUR CYCLE",fg ="red")
choosetype.place(relx=0.05,rely=0.11)
Tchoice = StringVar()
carnotcycle = Radiobutton(window,font = ('corbel',13,'bold'),text = "CARNOT CYCLE",variable =Tchoice,value = carnot,command = carnot ,fg ="black")
carnotcycle.place(relx=0.03,rely=0.25)
rankinecycle = Radiobutton(window,font = ('corbel',13,'bold'),text = "RANKINE CYCLE",variable =Tchoice,value = rankine,command = rankine,fg ="green")
rankinecycle.place(relx=0.03,rely=0.4)
srankinecycle = Radiobutton(window,font = ('corbel',13,'bold'),text = "SUPER HEATED RANKINE CYCLE",variable =Tchoice,value = srankine,command = srankine,fg ="blue")
srankinecycle.place(relx=0.03,rely=0.55)
Rrankinecycle = Radiobutton(window,font = ('corbel',13,'bold'),text = "REHEATED RANKINE CYCLE",variable =Tchoice,value = Rrankine,command = Rrankine,fg ="red")
Rrankinecycle.place(relx=0.03,rely=0.7)
Rrankinecycle = Radiobutton(window,font = ('corbel',13,'bold'),text = "RGENRATED RANKINE CYCLE",variable =Tchoice,value = RRrankine,command = RRrankine,fg ="blue")
Rrankinecycle.place(relx=0.03,rely=0.85)
window.mainloop()
