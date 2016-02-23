import os
import random
import urllib.request
import urllib.parse
#requires lxml (install python-lxml);
try:
	from lxml import html
	from lxml.etree import tostring
except:
	print ("ERROR: This program requires python-lxml. You may not use the wiki.");
import re

#This is the voice system
def getVoice(x):
	print ("Swipe: "+x);
	try:
		return (os.system("espeak -s 160 -v en+f4 '" + x + "'"));
	except:
		return (print("[Voice is offline]"));

#user says no to command;
def noCom():
	return (getVoice("OK! Let me know if you need anything!"));
	#return ("Swipe: OK Anon! Let me know if you need anything!");

#game sections
def guessGame():
	return (getVoice("My game is currently down for maintenance"));

	#print ("Swipe: Ok! I'll guess your number!");
	#num = (input("Think of a number between 1 and 10"));

	#numList = [1,2,3,4,5,6,7,8,9,10];
	#while (True):
		#numGuess = random.choice(numList);
		#numGuess = str(numGuess);
		#print ("Swipe: Is your number " +numGuess+ "?");

		#ans = (input(""));
		#ans = ans.lower();
		#if (ans == "yes"):
			#print ("Swipe: Yay! That was fun!");
			#break;
		#else:
			#print ("Swipe: Awe, let me guess again!");

#check questions
def reactAsk():
	getVoice("Sure! What is your question?");
	x = (input());
	#convert to lowercase
	x = x.lower();
	if ("how" in x) and ("you" in x):
		return (getVoice("I am good, thank you!"));
	elif ("what" in x) and ("you" in x):
		return (getVoice("I am Swipe, a basic AI, but I will be better soon!"));
	else:
		return (getVoice("My Owner has not programmed that type of question yet."));

def greet():
	return (getVoice("Hello!"));

#set wiki, calls getWiki.
def setWiki():
	#Set the wikipedia subject (cannot disambiguate yet).
	getVoice("Sure, what subject would you like to know about?");
	x = (input());
	getVoice("OK, I will take a look.");
	return (getWiki(x));

#get the wiki page using lxml
def getWiki(subject):
	try:
		with urllib.request.urlopen('https://en.wikipedia.org/wiki/' + subject) as response:
			tree = html.document_fromstring(response.read())

			par = tree.get_element_by_id("mw-content-text")[2]

			s = ""

			if par.text is not None:
				s += par.text

			for c in par.getchildren():
				if c.text is not None:
					s += c.text

				if c.tail is not None:
					s += c.tail

			return (print(s));
	except:
		return (getVoice("I am sorry, I can not find anything about that right now."));

#Doesn't know what user typed.
def unknown():
	return (getVoice("I am sorry, I do not understand."));

#main section, get user input and call response.
def main():
	#what is the user typing?
	while (True):
		x = input("What is your command?\n");
		#convert to lowercase
		x = x.lower();

		if ("game" in x):
			guessGame();
		elif ("none" in x) or ("nothing" in x) or ("null" in x):
			noCom();
		elif ("ask" in x) or ("question" in x):
			reactAsk();
		elif ("bye" in x) or ("goodbye" in x) or ("exit" in x) or ("quit" in x):
			return (getVoice("Goodbye, User!"));
			break;
		elif ("hello" in x) or ("hi" in x) or ("greetings" in x):
			greet();
		elif ("search" in x) or ("wiki" in x) or ("information" in x):
			setWiki();
		else:
			unknown();



getVoice("Hello user, my name is Swipe.");

main();








#print (NoCom(comm));
