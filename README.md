# PyWinMonkey  
WinMonkey helps you to work randomly on a specified windows program. After lunching PyWinMonkey, it performs clicks on your mentioned window to simulate user activity.  

Lunching with command line:  
At first you should lunch your desired program manually and after that you should open command line and enter command as bellow:  
  
"python PyWinMonkey.py -w [Window Name] -c [Click Count=10] -s [Sleep Seconds Before Start=2]"  
  
Note #1: PyWinMonkey assumes you have already opened your specified program.  

Examples:  
Assume we want to do 100 random clicks on notepad window.  

"python PyWinMonkey.py -w notepad -c 100 -s 5"  

Note #2: PyWinMonkey starts its work after -s seconds, it is useful in cases you want to open your program and let it to be on top of other windows.  

PyWinMonkey is useful for:  
1) Lunching a program automatically and performing actions such as click, right click etc. on it,  
2) testing your software under click stress,  
3) we are working on many other capabilities!  

You will need these libraries in python:  
1) pyautogui,  
2) win32gui.  

Thank you,  
Sajad Homayoun & Ali Dehghantanha
