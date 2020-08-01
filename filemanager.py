import termfuncs as tf

def save(filename, text_list, original_text, defaultname="untitled"):
	text_str = ""
	for s in text_list:
		text_str += s + '\n'
	if text_str != original_text+'\n':
		w, h = tf.terminal_size()
		tf.gotoxy(1,h-2);
		for i in range(w):
			print('\033[30;47m \033[0m', end='')
		
		tf.gotoxy(1,h-2);
		command = input("\033[30;47mSave file?[Y/n] ")
		if command == '' or command.lower()[0] == 'y':
			if filename == defaultname:
				for i in range(w):
					print('\033[30;47m \033[0m', end='')
				
				tf.gotoxy(1,h-2);
				filename = input("\033[30;47mSave as: ")
				
			with open(filename, 'w') as f: 
				f.write(text_str[:-1])
				original_text = text_str[:-1]
		print("\033[0m")
	return original_text

def open_file_formatted(filename, defaultname="untitled"):
	text_str = ""
	if filename != defaultname:
		try:
			f = open(filename)
			text_str = f.read()
			f.close()
		except Exception:
			pass
	text = text_str.split('\n')
	if text == []:
		text.append("");
		
	for i in range(len(text)):
		text[i] = text[i].replace('\t',  '        ')
	return text_str, text

