import pyautogui,win32gui,random,time,win32api,pywinauto


def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    extra.push([x,y,w,h,win32gui.GetWindowText(hwnd)])

MAIN_HWND = 0
win_x = -1
win_y = -1

def is_win_ok(hwnd, starttext):
    s = win32gui.GetWindowText(hwnd)
    if s.startswith(starttext):
            # print (s)
            global MAIN_HWND
            MAIN_HWND = hwnd
            return None
    return 1


def find_main_window(starttxt):
    global MAIN_HWND
    win32gui.EnumChildWindows(0, is_win_ok, starttxt)
    return MAIN_HWND

def winfun(hwnd,lparm):
    win_text = win32gui.GetWindowText(hwnd)
    win_pos = win32gui.GetWindowPlacement(hwnd)
    if len(win_text) > 3:
        print("winfun, child_hwnd: %d   txt: %s    pos: %s" % (hwnd, win_text ,win_pos[4]))

    pos = win_pos[4]
    if len(win_text) > 3:
        sleepBetween = random.randint(0, 2)
        time.sleep(sleepBetween)
        # print(win_text)
        pyautogui.click(win_x+10+pos[0], win_y+10+pos[1])
        # time.sleep(3)
    return 1

def GoSimulate(windowName,clickCount,sleepBefore):

    print(windowName+", "+str(clickCount)+", "+str(sleepBefore))
    if windowName == "":
        print("Error: Window name not found...")
    time.sleep(sleepBefore)
    from pythonds.basic.stack import Stack
    s = Stack()
    win32gui.EnumWindows(callback, s)

    global win_x
    global win_y
    win_width=-1
    win_height=-1

    while s.size() > 0:
        win = s.pop()
        if win[4] == windowName:
            win_x = win[0]
            win_y = win[1]
            print("x: %s   y:%s"  %(win_x,win_y))
            win_width=win[2]
            win_height=win[3]
            # print ("window status: "+str(win))
            break

    if win_x>-1 and win_y>-1:
        hwnd = win32gui.FindWindow(None, windowName)
        if hwnd < 1:
            hwnd = find_main_window(windowName)
        if hwnd:
            win32gui.EnumChildWindows(hwnd, winfun, None)

        for i in range(int(clickCount)):
            #print(str(i))
            xposition=random.randint(win_x+20,win_x+win_width-20)
            yposition = random.randint(win_y + 20, win_y + win_height - 20)
            #print(str(xposition)+","+str(yposition))
            if yposition>=win32api.GetSystemMetrics(1):
                yposition-=50
            click_or_rightClick=random.randint(0,9)

            sleepBetween=random.randint(0,2)
            time.sleep(sleepBetween)
            if click_or_rightClick<=4:
                pyautogui.click(xposition,yposition)
            elif click_or_rightClick>=5 and click_or_rightClick<=7:
                pyautogui.rightClick(xposition, yposition)
                right_prob=random.randint(1,10)
                if right_prob<=4:
                    y_top=random.randint(1,200)
                    pyautogui.click(xposition+50, yposition-y_top)
            else:
                pyautogui.scroll(10)
