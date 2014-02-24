import pyaudio
import time
import wave

def play_sound(src):

	CHUNK = 1024
	wf = wave.open(src, 'rb')
	p = pyaudio.PyAudio()

	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True)

	data = wf.readframes(CHUNK)

	while data != '':
	    stream.write(data)
	    data = wf.readframes(CHUNK)

	stream.stop_stream()
	stream.close()
	p.terminate()

def play_short():
	play_sound('short.wav')

def play_long():
	play_sound('long.wav')

def pause():
	time.sleep(.05)

def play_morse(morse_list):
	""" morse_list is a list of each letter that needs to be played.
	Ex: ['...', '---', '...'] which came from input "SOS" """

	for letter in morse_list:
		for symbol in letter:
			if symbol == '.':
				play_short()
			elif symbol == '-':
				play_long()
			else:
				pause()

def string_to_morse(string):
	""" Converts an input string to morse code. 
	Ex: "SOS" becomes ['...', '---', '...'] """

	morse_list = []
	for char in string:
		if char == ' ':
			morse_list.append(char)
		elif char.lower() == 'a':
			morse_list.append('.-')
		elif char.lower() == 'b':
			morse_list.append('-...')
		elif char.lower() == 'c':
			morse_list.append('-.-.')
		elif char.lower() == 'd':
			morse_list.append('-..')
		elif char.lower() == 'e':
			morse_list.append('.')
		elif char.lower() == 'f':
			morse_list.append('..-.')
		elif char.lower() == 'g':
			morse_list.append('--.')
		elif char.lower() == 'h':
			morse_list.append('....')
		elif char.lower() == 'i':
			morse_list.append('..')
		elif char.lower() == 'j':
			morse_list.append('.---')
		elif char.lower() == 'k':
			morse_list.append('-.-')
		elif char.lower() == 'l':
			morse_list.append('.-..')
		elif char.lower() == 'm':
			morse_list.append('--')
		elif char.lower() == 'n':
			morse_list.append('-.')
		elif char.lower() == 'o':
			morse_list.append('---')
		elif char.lower() == 'p':
			morse_list.append('.--.')
		elif char.lower() == 'q':
			morse_list.append('--.-')
		elif char.lower() == 'r':
			morse_list.append('.-.')
		elif char.lower() == 's':
			morse_list.append('...')
		elif char.lower() == 't':
			morse_list.append('-')
		elif char.lower() == 'u':
			morse_list.append('..-')
		elif char.lower() == 'v':
			morse_list.append('...-')
		elif char.lower() == 'w':
			morse_list.append('.--')
		elif char.lower() == 'x':
			morse_list.append('-..-')
		elif char.lower() == 'y':
			morse_list.append('-.--')
		elif char.lower() == 'z':
			morse_list.append('--..')
		else:
			morse_list.append(' ')

	return morse_list

def main(string):
	play_morse(string_to_morse(string))


if __name__ == '__main__':
	string = "SOS         SOS"
	#main(string)
	string = "Hello my name is Tyler nice to meet you"
	main(string)