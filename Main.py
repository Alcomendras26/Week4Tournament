#############################################
# Name: Vincent Alcomendras
# Class: ICS3C
# Date: Friday Sept. 25
# Project Name: Week4Tournament
#
# Project Description: See the README file
#############################################
from asyncio import FrameCallGraphEntry

# THIS IS WHERE YOU CODE

print("Welcome to the tournament score program!")


print("Input the name of the first team")
team1=input()
print("answer the following")
wins1=int(input(f"How many wins for {team1}?"))
ties1=int(input(f"How many ties for {team1}?"))
los1=int(input(f"How many loses for {team1}?"))

var1=wins1 * 2 + ties1
print(f"The total is {var1}")


print("Input the name of the second team")
team2=input()
print("answer the following")
wins2=int(input(f"How many wins for {team2}?"))
ties2=int(input(f"How many ties for {team2}?"))
los2=int(input(f"How many loses for {team2}?"))

var2=wins2 * 2 + ties2
print(f"The total is {var2}")


print("Input the name of the third team")
team3=input()
print("answer the following")
wins3=int(input(f"How many wins for {team3}?"))
ties3=int(input(f"How many ties for {team3}?"))
los3=int(input(f"How many loses for {team3}?"))

var3=wins3 * 2 + ties3
print(f"The total is {var3}")


print("Input the name of the fourth team")
team4=input()
print("answer the following")
wins4=int(input(f"How many wins for {team4}?"))
ties4=int(input(f"How many ties for {team4}?"))
los4=int(input(f"How many loses for {team4}?"))

var4=wins4 * 2 + ties4
print(f"The total is {var4}")


print("Input the name of the fifth team")
team5=input()
print("answer the following")
wins5=int(input(f"How many wins for {team5}?"))
ties5=int(input(f"How many ties for {team5}?"))
los5=int(input(f"How many loses for {team5}?"))

var5=wins5 * 2 + ties5
print(f"The total is {var5}")


print("Input the name of the sixth team")
team6=input()
print("answer the following")
wins6=int(input(f"How many wins for {team6}?"))
ties6=int(input(f"How many ties for {team6}?"))
los6=int(input(f"How many loses for {team6}?"))

var6=wins6 * 2 + ties6
print(f"The total is {var6}")



if var1>var2 and var1>var3 and var1>var4 and var1>var5 and var1>var6:
    print(team1 , "was first place with" , var1 , "points")


if var2>var1 and var2>var3 and var2>var4 and var2>var5 and var2>var6:
    print(team2 , "was first place with" , var2 , "points")


if var3>var1 and var3>var2 and var3>var4 and var3>var5 and var3>var6:
    print(team3 , "was first place with" , var3 , "points")


if var4>var1 and var4>var2 and var4>var3 and var4>var5 and var4>var6:
    print(team4 , "was first place with" , var4 , "points")


if var5>var1 and var5>var2 and var5>var3 and var5>var4 and var3>var6:
    print(team5 , "was first place with" , var5 , "points")


if var6>var1 and var6>var2 and var6>var3 and var6>var4 and var6>var5:
    print(team6 , "was first place with" , var6 , "points")

print("also")

if var1==var2:
    print("Both" , team1 , "and" , team2 , "the same")
if var1==var3:
    print("Both" , team1 , "and" , team3 , "the same")
if var1==var4:
    print("Both" , team1 , "and" , team4 , "the same")
if var1==var5:
    print("Both" , team1 , "and" , team5 , "the same")
if var1==var6:
    print("Both" , team1 , "and" , team6 , "the same")

if var2==var1:
    print("Both" , team2 , "and" , team1 , "the same")
if var2==var3:
    print("Both" , team2 , "and" , team3 , "the same")
if var2==var4:
    print("Both" , team2 , "and" , team4 , "the same")
if var2==var5:
    print("Both" , team2 , "and" , team5 , "the same")
if var2==var6:
    print("Both" , team2 , "and" , team6 , "the same")

if var3==var1:
    print("Both" , team3 , "and" , team1 , "the same")
if var3==var2:
    print("Both" , team3 , "and" , team2 , "the same")
if var3==var4:
    print("Both" , team3 , "and" , team4 , "the same")
if var3==var5:
    print("Both" , team3 , "and" , team5 , "the same")
if var3==var6:
    print("Both" , team3 , "and" , team6 , "the same")

if var4==var1:
    print("Both", team4, "and", team1, "the same")
elif var4==var2:
    print("Both", team4, "and", team2, "the same")
elif var4==var3:
    print("Both", team4, "and", team3, "the same")
elif var4==var5:
    print("Both", team4, "and", team4, "the same")
elif var4==var6:
    print("Both", team4, "and", team6, "the same")


if var5==var1:
    print("Both" , team5 , "and" , team1 , "the same")
elif var5==var2:
    print("Both" , team5 , "and" , team2 , "the same")
elif var5==var3:
    print("Both" , team5 , "and" , team3 , "the same")
elif var5==var4:
    print("Both" , team5 , "and" , team4 , "the same")
elif var5==var6:
    print("Both" , team5 , "and" , team6 , "the same")


if var6==var1:
    print("Both" , team6 , "and" , team1 , "the same")
elif var6==var2:
    print("Both" , team6 , "and" , team2 , "the same")
elif var6==var3:
    print("Both" , team6 , "and" , team3 , "the same")
elif var6==var4:
    print("Both" , team6 , "and" , team4 , "the same")
elif var6==var5:
    print("Both" , team6 , "and" , team5 , "the same")



























