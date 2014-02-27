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

	char_to_morse = {
		' ':' ',
		'a':'.-',
		'b':'-...',
		'c':'-.-.',
		'd':'-..',
		'e':'.',
		'f':'..-.',
		'g':'--.',
		'h':'....',
		'i':'..',
		'j':'.---',
		'k':'-.-',
		'l':'.-..',
		'm':'--',
		'n':'-.',
		'o':'---',
		'p':'.--.',
		'q':'--.-',
		'r':'.-.',
		's':'...',
		't':'-',
		'u':'..-',
		'v':'...-',
		'w':'.--',
		'x':'-..-',
		'y':'-.--',
		'z':'--..'
	}

	morse_list = []
	for char in string:
		morse_list.append(char_to_morse[char.lower()])

	return morse_list

def main(string):
	play_morse(string_to_morse(string))


if __name__ == '__main__':
	string = "SOS         SOS"
	#string = "Hello my name is Tyler nice to meet you"
	main(string)
	