from tkinter import Tk
from tkinter import Button
from tkinter import Scrollbar

t=Tk()
t.minsize(1500,700)
t.title("Calender 2020")

def january():
    January=Button(text="JANUARY",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")

    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

    #days
    
    jan1=Button(text="",font=("Times New Roman",30),background="white")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")
  
    jan4=Button(text="1",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="2",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="3",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="4",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="5",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="6",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="7",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="8",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="9",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="10",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="11",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="12",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="13",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="14",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="15",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="16",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="17",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="18",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="19",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="20",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="21",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="22",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="23",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="24",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="25",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="26",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="27",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="28",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="29",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="30",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="31",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")


def february():
    January=Button(text="FEBRUARY",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")
    
    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="",font=("Times New Roman",30),background="white")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="1",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="2",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="3",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="4",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="5",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="6",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="7",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="8",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="9",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="10",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="11",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="12",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="13",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="14",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="15",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="16",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="17",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="18",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="19",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="20",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="21",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="22",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="23",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="24",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="25",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="26",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="27",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="28",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="29",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")


     


def march():
    January=Button(text="MARCH",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")
    
    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="1",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")
    
    jan2=Button(text="2",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="3",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="4",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="5",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="6",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="7",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="8",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="9",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="10",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="11",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="12",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="13",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="14",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="15",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="16",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="17",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="18",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="19",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="20",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="21",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="22",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")
    
    jan23=Button(text="23",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="24",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="25",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="26",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="27",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="28",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="29",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="30",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="31",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")





def april():
    January=Button(text="APRIL",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")

    #Week 
    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="1",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="2",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="3",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="4",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="5",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="6",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="7",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="8",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="9",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="10",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="11",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="12",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="13",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="14",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="15",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="16",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="17",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="18",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="19",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="20",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="21",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="22",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="23",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="24",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="25",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="26",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="27",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="28",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")
    
    jan32=Button(text="29",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="30",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")






def may():
    January=Button(text="MAY",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")

    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="31",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")
    
    jan6=Button(text="1",font=("Times New Roman",30),background="white",foreground="red")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="2",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="3",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="4",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="5",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="6",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="7",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="8",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="9",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="10",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="11",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="12",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="13",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="14",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="15",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="16",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="17",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="18",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="19",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="20",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="21",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="22",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="23",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="24",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="25",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="26",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")
    
    jan32=Button(text="27",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="28",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="29",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="30",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")





def june():
    January=Button(text="JUNE",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")

    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="1",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="2",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="3",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="4",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="5",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="6",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="7",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="8",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="9",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="10",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="11",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="12",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="13",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="14",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="15",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="16",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="17",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="18",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="19",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="20",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="21",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="22",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="23",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="24",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="25",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")
    
    jan27=Button(text="26",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")
    
    jan28=Button(text="27",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="28",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="29",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")
    
    jan31=Button(text="30",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")

   





def july():
    January=Button(text="JULY",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")
    
    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="1",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="2",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="3",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="4",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="5",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="6",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="7",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="8",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="9",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="10",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="11",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="12",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="13",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="14",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="15",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="16",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="17",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="18",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="19",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")
    
    jan23=Button(text="20",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="21",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="22",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="23",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="24",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="25",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="26",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="27",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="28",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="29",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="30",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="31",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")
    
    jan35=Button(text="",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")







def august():
    January=Button(text="AUGUST",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")
    
    #Week 
    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="30",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="31",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="1",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="2",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="3",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="4",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="5",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="6",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="7",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="8",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="9",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="10",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="11",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="12",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="13",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="14",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="15",font=("Times New Roman",30),background="white",foreground="red")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="16",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="17",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="18",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="19",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="20",font=("Times New Roman",30),background="white",foreground="purple")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="21",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="22",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="23",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="24",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="25",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="26",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="27",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="28",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="29",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")




def september():
    January=Button(text="SEPTEMBER",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")

    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="1",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="2",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="3",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="4",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="5",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="6",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="7",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="8",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="9",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="10",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="11",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="12",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="13",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="14",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="15",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="16",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="17",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="18",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="19",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="20",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="21",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="22",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="23",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="24",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="25",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="26",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="27",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="28",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="29",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="30",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")




def october():
    January=Button(text="OCTOBER",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")
    
    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="1",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="2",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="3",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="4",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="5",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="6",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="7",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="8",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="9",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="10",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="11",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="12",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="13",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="14",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="15",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="16",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="17",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="18",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="19",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="20",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="21",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="22",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="23",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="24",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="25",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="26",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="27",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="28",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="29",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="30",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="31",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")







def november():
    January=Button(text="NOVEMBER",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")

    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="1",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")

    jan2=Button(text="2",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="3",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="4",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="5",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="6",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="7",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="8",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="9",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="10",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="11",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="12",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="13",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="14",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="15",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="16",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="17",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="18",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="19",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="20",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="21",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="22",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="23",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="24",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="25",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="26",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="27",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="28",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="29",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="30",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")
    
    jan32=Button(text="",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")

    jan35=Button(text="",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")





def december():
    January=Button(text="DECEMBER",font=("Algerian",25),background="Orange")
    January.place(x=500,y=0,width="200",height="70")

    sun=Button(text="SUN",font=("Algerian",25),background="red")
    sun.place(x=155,y=100,width="100",height="95")

    Mon=Button(text="MON",font=("Algerian",25),background="yellow")
    Mon.place(x=155,y=200,width="100",height="95")

    Tue=Button(text="TUE",font=("Algerian",25),background="blue")
    Tue.place(x=155,y=300,width="100",height="95")

    Wed=Button(text="WED",font=("Algerian",25),background="pink")
    Wed.place(x=155,y=400,width="100",height="95")

    Thur=Button(text="THUR",font=("Algerian",25),background="violet")
    Thur.place(x=155,y=500,width="100",height="95")

    Fri=Button(text="FRI",font=("Algerian",25),background="purple")
    Fri.place(x=155,y=600,width="100",height="95")

    Sat=Button(text="SAT",font=("Algerian",25),background="green")
    Sat.place(x=155,y=700,width="100",height="95")

#Days
    jan1=Button(text="",font=("Times New Roman",30),background="white",foreground="red")
    jan1.place(x=260,y=100,width="200",height="95")
    
    jan2=Button(text="",font=("Times New Roman",30),background="white")
    jan2.place(x=260,y=200,width="200",height="95")

    jan3=Button(text="1",font=("Times New Roman",30),background="white")
    jan3.place(x=260,y=300,width="200",height="95")

    jan4=Button(text="2",font=("Times New Roman",30),background="white")
    jan4.place(x=260,y=400,width="200",height="95")

    jan5=Button(text="3",font=("Times New Roman",30),background="white")
    jan5.place(x=260,y=500,width="200",height="95")

    jan6=Button(text="4",font=("Times New Roman",30),background="white")
    jan6.place(x=260,y=600,width="200",height="95")

    jan7=Button(text="5",font=("Times New Roman",30),background="white")
    jan7.place(x=260,y=700,width="200",height="95")


    jan8=Button(text="6",font=("Times New Roman",30),background="white",foreground="red")
    jan8.place(x=460,y=100,width="200",height="95")

    jan9=Button(text="7",font=("Times New Roman",30),background="white")
    jan9.place(x=460,y=200,width="200",height="95")

    jan10=Button(text="8",font=("Times New Roman",30),background="white")
    jan10.place(x=460,y=300,width="200",height="95")

    jan11=Button(text="9",font=("Times New Roman",30),background="white")
    jan11.place(x=460,y=400,width="200",height="95")

    jan12=Button(text="10",font=("Times New Roman",30),background="white")
    jan12.place(x=460,y=500,width="200",height="95")

    jan13=Button(text="11",font=("Times New Roman",30),background="white")
    jan13.place(x=460,y=600,width="200",height="95")

    jan14=Button(text="12",font=("Times New Roman",30),background="white")
    jan14.place(x=460,y=700,width="200",height="95")


    jan15=Button(text="13",font=("Times New Roman",30),background="white",foreground="red")
    jan15.place(x=660,y=100,width="200",height="95")

    jan16=Button(text="14",font=("Times New Roman",30),background="white")
    jan16.place(x=660,y=200,width="200",height="95")

    jan17=Button(text="15",font=("Times New Roman",30),background="white")
    jan17.place(x=660,y=300,width="200",height="95")

    jan18=Button(text="16",font=("Times New Roman",30),background="white")
    jan18.place(x=660,y=400,width="200",height="95")

    jan19=Button(text="17",font=("Times New Roman",30),background="white")
    jan19.place(x=660,y=500,width="200",height="95")

    jan20=Button(text="18",font=("Times New Roman",30),background="white")
    jan20.place(x=660,y=600,width="200",height="95")

    jan21=Button(text="19",font=("Times New Roman",30),background="white")
    jan21.place(x=660,y=700,width="200",height="95")


    jan22=Button(text="20",font=("Times New Roman",30),background="white",foreground="red")
    jan22.place(x=860,y=100,width="200",height="95")

    jan23=Button(text="21",font=("Times New Roman",30),background="white")
    jan23.place(x=860,y=200,width="200",height="95")

    jan24=Button(text="22",font=("Times New Roman",30),background="white")
    jan24.place(x=860,y=300,width="200",height="95")

    jan25=Button(text="23",font=("Times New Roman",30),background="white")
    jan25.place(x=860,y=400,width="200",height="95")

    jan26=Button(text="24",font=("Times New Roman",30),background="white")
    jan26.place(x=860,y=500,width="200",height="95")

    jan27=Button(text="25",font=("Times New Roman",30),background="white")
    jan27.place(x=860,y=600,width="200",height="95")

    jan28=Button(text="26",font=("Times New Roman",30),background="white")
    jan28.place(x=860,y=700,width="200",height="95")


    jan29=Button(text="27",font=("Times New Roman",30),background="white",foreground="red")
    jan29.place(x=1060,y=100,width="200",height="95")

    jan30=Button(text="28",font=("Times New Roman",30),background="white")
    jan30.place(x=1060,y=200,width="200",height="95")

    jan31=Button(text="29",font=("Times New Roman",30),background="white")
    jan31.place(x=1060,y=300,width="200",height="95")

    jan32=Button(text="30",font=("Times New Roman",30),background="white")
    jan32.place(x=1060,y=400,width="200",height="95")

    jan33=Button(text="31",font=("Times New Roman",30),background="white")
    jan33.place(x=1060,y=500,width="200",height="95")

    jan34=Button(text="",font=("Times New Roman",30),background="white")
    jan34.place(x=1060,y=600,width="200",height="95")
    
    jan35=Button(text="",font=("Times New Roman",30),background="white")
    jan35.place(x=1060,y=700,width="200",height="95")


    
    
#MONTH 
b0=Button(text="2020",font=("",25),background="Blue",foreground="white")
b0.place(x=700,y=0,width="150",height="70")

b1=Button(text="January",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=january)
b1.place(x=0,y=0,width="150",height="65")

b2=Button(text="February",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=february)
b2.place(x=0,y=65,width="150",height="65")

b3=Button(text="March",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=march)
b3.place(x=0,y=130,width="150",height="65")

b4=Button(text="April",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=april)
b4.place(x=0,y=195,width="150",height="65")

b5=Button(text="May",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=may)
b5.place(x=0,y=260,width="150",height="65")

b6=Button(text="June",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=june)
b6.place(x=0,y=325,width="150",height="65")

b7=Button(text="July",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=july)
b7.place(x=0,y=390,width="150",height="65")

b8=Button(text="August",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=august)
b8.place(x=0,y=455,width="150",height="65")

b9=Button(text="September",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=september)
b9.place(x=0,y=520,width="150",height="65")

b10=Button(text="October",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=october)
b10.place(x=0,y=585,width="150",height="65")

b11=Button(text="November",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=november)
b11.place(x=0,y=650,width="150",height="65")

b12=Button(text="December",font=("",25),background="grey",foreground="white",activebackground="pink",activeforeground="purple",command=december)
b12.place(x=0,y=715,width="150",height="65")





t.mainloop()
