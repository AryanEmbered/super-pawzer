import keyboard as k
import time
import psutil as p
import win32gui
import win32process


def suspend():
    global suspended
    if suspended == 0:
        processid = pid()
        print(f"suspended {processid}")
        suspended = processid
        p.Process(processid).suspend()
    else:
        pass


def resume():
    global suspended
    if suspended == 0:
        p.Process(pid()).resume()
    else:
        processid = suspended
        suspended = 0
        print(f"resume {processid}")
        p.Process(processid).resume()


def pid():
    process_id = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())[1]
    return process_id


suspended = 0
k.add_hotkey("ctrl+alt+p", lambda: suspend())
k.add_hotkey("ctrl+alt+r", lambda: resume())

if __name__ == '__main__':
    while True:
        time.sleep(0.1)
