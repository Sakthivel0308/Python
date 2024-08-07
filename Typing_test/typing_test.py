import curses
from curses import wrapper
import time

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        color = curses.color_pair(1) if char == target[i] else curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

def wpm_test(stdscr):
    target_text = "Hello World Welcome to the Typing Test to Get wpm"
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getch()
            if key != -1:
                if key == 27:  # Escape key
                    return False
                elif key in (8, 127, curses.KEY_BACKSPACE):
                    if current_text:
                        current_text.pop()
                elif 0 <= key <= 0x10FFFF and len(current_text) < len(target_text):
                    current_text.append(chr(key))
        except Exception as e:
            continue
    return True

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        test_completed = wpm_test(stdscr)
        if not test_completed:
            break
        stdscr.addstr(2, 0, "You completed the test! Press any key to continue or ESC to exit.")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)
