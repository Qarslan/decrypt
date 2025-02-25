import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(0)
    stdscr.timeout(100)

    menu = ["ENCODE - MD5", "ENCODE - SHA1", "ENCODE - SHA224", "ENCODE - SHA256",
            "ENCODE - SHA384", "ENCODE - SHA512", "ENCODE/DECODE - BASE64", "EXIT"]

    idx = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        for i, text in enumerate(menu):
            x = w//2 - len(text)//2
            y = h//2 - len(menu)//2 + i
            if i == idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, text)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, text)

        key = stdscr.getch()
        
        if key == curses.KEY_UP and idx > 0:
            idx -= 1
        elif key == curses.KEY_DOWN and idx < len(menu) - 1:
            idx += 1
        elif key == ord("\n"):
            if menu[idx] == "EXIT":
                break
            stdscr.addstr(h-2, 0, f"You selected: {menu[idx]}")
            stdscr.refresh()
            stdscr.getch()

curses.wrapper(main)
