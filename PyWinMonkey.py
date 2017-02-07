import pyautogui,sys,win32gui,random,time,getopt


def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    extra.push([x,y,w,h,win32gui.GetWindowText(hwnd)])


def main(argv):
    windowName=""
    clickCount=10
    sleepSec=2
    try:
        opts, args = getopt.getopt(argv, "hw:c:s:", ["window=", "clickcount=","sleep="])
    except getopt.GetoptError:
        print 'PyWinMonkey.py -w <Window Name> -c <Click Count=10> -s <Sleep Seconds Before Start=2>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'PyWinMonkey.py -w <Window Name> -c <Click Count=10> -s <Sleep Seconds Before Start>'
            sys.exit()
        elif opt in ("-w", "--window"):
            windowName = arg
        elif opt in ("-c", "--clickcount"):
            clickCount = int(arg)
        elif opt in ("-s", "--sleep"):
            sleepSec = int(arg)
    print(windowName+", "+str(clickCount)+", "+str(sleepSec))
    if windowName=="":
        print ("Error: Window name not found...")
    time.sleep(sleepSec)
    from pythonds.basic.stack import Stack
    s = Stack()
    win32gui.EnumWindows(callback, s)

    win_x = -1
    win_y = -1
    win_width=-1
    win_height=-1

    while s.size() > 0:
        win = s.pop()
        if win[4] == windowName:
            win_x=win[0]
            win_y=win[1]
            win_width=win[2]
            win_height=win[3]
            # print ("window status: "+str(win))
            break

    if win_x>-1 and win_y>-1:
        for i in xrange(int(clickCount)):
            print(str(i))
            xposition=random.randint(win_x+10,win_x+win_width-10)
            yposition = random.randint(win_y + 10, win_y + win_height - 10)
            print(str(xposition)+","+str(yposition))
            pyautogui.click(xposition,yposition)


if __name__ == "__main__":
    main(sys.argv[1:])
