```
   __      __    ______      __________      _______      _____
  | ||    | ||  |  __  ||   /  _    _ \\    |  ____||    /  __ \\
  \ \\    / //  | || | ||  / // \ // \ \\   | ||____    / //  \_\\
   \ \\  / //   | || | ||  | || | || | ||   | _____||   | ||
    \ \\/ //    | |__| ||  | || | || | ||   | ||___     | ||
     \___//     |______||  |_|| |_|| |_||   |______||   |_||
```

# vomer text editor
A text editor in python. Based on nano  

## installation
```
./install.sh
```
  
this makes a symlink in /usr/local/bin  

## usage
```
vomer [<filename>]
```
edit `filename`.  
if `filename` doesn't exist, it makes a new file.  

#### keys
- esc 3 times: exit editor
- ctrl-S: save file
- ctrl-F: find next text, go to that line
