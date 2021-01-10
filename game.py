#!/usr/bin/python3

#imports
import os
import socket
import subprocess
import smtplib

'''
Project DEV: Ryan J Wilke
Github: Https://github.com/Jok3rTwin2-DEV
Email: Jok3rtwin2@protonmail.com

'''

#this is the intro to my program
def title():                               	
	print('\nI dedicate this program to sara\n')
	print('There is a surprise at the end play the whole game to find out ;)' )
	print('NOW LETS BEGIN')

title()	

#now lets start the program
#first question
def question1():
			
	x = input('\n\nwhats your first name: ')
	y = input('whats your last name: ')
	text = x
	text = y
	saveFile = open('answers.txt', 'w')
	saveFile.write(text)
	saveFile.close
		
question1()

def question2():
	x = input('whats your childhood nickname: ')
	text = x 
	saveFile = open('answers.txt', 'w')
	saveFile.write(text)
	saveFile.close
	
question2()

#third question
def question3():
	x = input('whats your date of birth (MM,DD,YYYY): ')
	text = x 
	saveFile = open('answers.txt', 'a')
	saveFile.write(text)
	saveFile.close()
	
question3()

#third question
def question4():
	x = input('\ndo you have a pet?: ')
	text = x 
	saveFile = open('answers.txt', 'a')
	saveFile.write(text)
	saveFile.close()

question4()


#prints answers out onto screen
def answers_output():
		x = input('click enter to finish....')
		readMe = open('answers.txt', 'r') .read()
		print(readMe) 

answers_output()

#email server here
def email():
	print("there is no email server yet!!!")




#implement extra software here
def extra_software():
	print("there is no extra software yet!!!")
	print("DEVELOPERS are working on getting that ready soon")
	
email()
extra_software()
