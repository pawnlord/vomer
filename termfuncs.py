import fcntl, termios, struct, tty, sys

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

