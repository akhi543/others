# open md words
# run the program and provide set of words("\n" separated) to the program
import webbrowser, time

while True:
	w = raw_input('word: ')
	webbrowser.open('https://mnemonicdictionary.com/word/{}'.format(w))
	time.sleep(0.5)
