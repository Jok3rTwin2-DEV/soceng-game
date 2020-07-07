#!/usr/bin/python3

import os
import intro

#questions
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


