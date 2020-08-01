import sys, os
import fcntl, termios, struct
import tty, termios
def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def start_buff():
	print("\033[?1049h\033[H", end='');
def end_buff():
	print("\033[?1049l", end='');

def gotoxy(x, y):
	print("\033[" + str(y) + ";" + str(x) + "H", end='', flush=True);

def terminal_size():
	h, w, hp, wp = struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH',0,0,0,0)))
	return w, h
	
def clear():
	print("\033[H\033[J", end='');

	


text_str = ""

script_name = os.path.basename(__file__)

filename = "untitled"

for i in range(len(sys.argv)):
	if len(sys.argv) != i+1:
		if script_name in sys.argv[i]:
			i+=1;
			filename = sys.argv[i]
if filename != "untitled":
	try:
		f = open(filename)
		text_str = f.read()
		f.close()
	except Exception:
		pass
text = text_str.split('\n')
if text == []:
	text.append("");

class Coord:
	def __init__(self, x, y):
		self.x = x
		self.y = y

cursor = Coord(0, 0)

w, h = (0, 0)
start_buff()

starting_line = 0

ending_line = h

try:
	while True:
		clear()
		gotoxy(1,2);
		
		w, h = terminal_size()
		ending_line = starting_line+h-3
		
		for i in range(w):
			print('\033[31;47m-\033[0m', end='')
		
		for s in range(starting_line, min(len(text), ending_line)):
			print(text[s])
		
		gotoxy(cursor.x+1, cursor.y+3)
		
		c = getch()
		if ord(c) == 27:
			c = getch()
			c = getch()
			print(c)
			if c == 'C':
				cursor.x+=1
			elif c == 'B':
				if cursor.y < len(text)-1:		
					cursor.y+=1
				else:
					cursor.x = len(text[cursor.y])-1
			elif c == 'D':
				cursor.x-=1
			elif c == 'A':
				if cursor.y > 0:		
					cursor.y-=1
				else:
					cursor.x = 0
			else:
				break
		elif c == '\n' or c == '\r':
			nl_text = text[cursor.y][:cursor.x]
			text[cursor.y] = text[cursor.y][cursor.x:]
			text.insert(cursor.y, nl_text)
			cursor.y+=1
			cursor.x=0 
		elif ord(c) == 127:
			if cursor.x == 0 and cursor.y != 0:
				line_text = text[cursor.y][:]
				text = text[:cursor.y] + text[cursor.y+1:]
				cursor.y -= 1
				cursor.x = len(text[cursor.y])
				text[cursor.y] += line_text
			else:
				text[cursor.y] = text[cursor.y][:cursor.x-1] + text[cursor.y][cursor.x:]
				cursor.x-=1
		else:
			text[cursor.y] = text[cursor.y][:cursor.x]+c+text[cursor.y][cursor.x:]
			cursor.x+=1
		
		if cursor.x > len(text[cursor.y]):
			if cursor.y != len(text)-1:
				cursor.x=0
				cursor.y+=1
			else:
				cursor.x = len(text[cursor.y])-1
			
		if cursor.x < 0:
			if cursor.y > 0:
				cursor.y-=1
				cursor.x=len(text[cursor.y])-1
			else:
				cursor.x = 0
			
				
except KeyboardInterrupt:
	pass

end_buff()

