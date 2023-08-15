import os
from datetime import datetime
import platform
import shutil
from time import sleep as wait
import threading as thr
import sys
from typing import Tuple, List, Any, TYPE_CHECKING

platform = platform.platform().split("-")[0]


def columns():
    return os.get_terminal_size().columns


def lines():
    return int(round(os.get_terminal_size().lines/2, 0))


os.system('')

threads = []


class colors:
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'

    list_of_colors = ['\33[30m', '\33[32m', '\33[31m', '\33[33m', '\33[34m', '\33[35m', '\33[36m', '\33[37m', '\33[40m', '\33[41m', '\33[42m', '\33[43m', '\33[44m', '\33[45m', '\33[46m', '\33[47m',
                      '\33[90m', '\33[91m', '\33[92m', '\33[93m', '\33[94m', '\33[95m', '\33[96m', '\33[97m', '\33[100m', '\33[101m', '\33[102m', '\33[103m', '\33[104m', '\33[105m', '\33[106m', '\33[107m']

    def gradient(
        start: Tuple[int, int, int], end: Tuple[int, int, int], steps: int
    ) -> List[Tuple[int, int, int]]:
        """
        Generate a gradient, from the start color to the end color with `steps` amount.
        Args:
            start (tuple[int, int, int]): start color, this must be a tuple of 3 ints.
            end (tuple[int, int, int]): end color, this must be a tuple of 3 ints.
            steps (int): amount of steps.
        Returns:
            list[tuple[int, int, int]]: `steps` amount of colors in between the `start_color` and the `end_color`
        """
        rs: List[int] = [start[0]]
        gs: List[int] = [start[1]]
        bs: List[int] = [start[2]]

        for step in range(1, steps):
            rs.append(round(start[0] + (end[0] - start[0]) * step / steps))
            gs.append(round(start[1] + (end[1] - start[1]) * step / steps))
            bs.append(round(start[2] + (end[2] - start[2]) * step / steps))

        return list(
            zip(
                rs,  # [255, 127,   0]
                gs,  # [0,   127, 255]
                bs,  # [0,     0,   0]
            )
        )

    def rgb(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    def hex(hexCode):
        return colors.rgb(hexCode[:2], 16, hexCode[2:4], 16, hexCode[4:], 16)

    def gradientText(text, startColor, endColor, center=0):
        string = []
        grad = colors.gradient(startColor, endColor, len(text))
        for i, char in enumerate(text):
            string.append(str(colors.rgb(*grad[i])) + char)
        string.append(str(colors.CEND))
        return ''.join(string).center(center)


class projectDetails:
    owner = ''
    projectName = ''
    version = ''


class settings:
    printCap = True
    logo = ''
    logoColor = colors.CWHITE2
    logoOnClear = False
    centerLogo = False
    startanimadelay = .1
    startmsg = ''
    logoAnim = True
    logoAnimDelay = .01


def current_time():
    return f'{colors.CGREY}[{colors.CEND}{colors.gradientText(datetime.now().strftime("%H:%M:%S"), (144, 3, 252), (3, 223, 252))}{colors.CEND}{colors.CGREY}]{colors.CEND}'


def logo():
    if settings.logoAnim == True:
        if settings.centerLogo:
            for line in settings.logo.split('\n'):
                wait(settings.logoAnimDelay)
                print(settings.logoColor+line.center(columns())+colors.CEND)

        else:
            wait(settings.logoAnimDelay)
            print(settings.logoColor+settings.logo+colors.CEND)
    else:
        if settings.centerLogo:
            for line in settings.logo.split('\n'):
                print((round(columns()/4)+10)*' ' +
                      settings.logoColor+line+colors.CEND)
        else:
            print(settings.logoColor+settings.logo+colors.CEND)


def animLogo(delay: int):
    if settings.centerLogo:
        for line in settings.logo.split('\n'):
            wait(delay)
            print(settings.logoColor+line.center(columns())+colors.CEND)

    else:
        wait(delay)
        print(settings.logoColor+settings.logo+colors.CEND)


def startUp(waitForDone: bool):
    def main():
        for i in range(lines()):
            print()
            wait(settings.startanimadelay)

        print(colors.CWHITE2+settings.startmsg.center(columns())+colors.CEND+'\n')

        for line in settings.logo.split('\n'):
            wait(settings.startanimadelay)
            print((round(columns()/4)+10)*' ' +
                  settings.logoColor+line+colors.CEND)

        print(f'{colors.CWHITE2}{projectDetails.projectName} - Made by: {projectDetails.owner}'.center(columns()))
        wait(settings.startanimadelay)
        print(f'v{projectDetails.version}{colors.CEND}'.center(columns()))

        for i in range(lines()):
            print()
            wait(settings.startanimadelay)
        wait(1)
        clear()

    if waitForDone == True:
        startUpThr = thr.Thread(target=main)
        startUpThr.name = 'startup'
        threads.append(startUpThr)
        startUpThr.start()
        startUpThr.join()

    else:
        startUpThr = thr.Thread(target=main)
        startUpThr.name = 'startup'
        threads.append(startUpThr)
        startUpThr.start()


def waitForStartup():
    for i in threads:
        if i.name == 'startup':
            i.join()


def error(why):
    waitForStartup()
    print(f'{current_time()} {colors.CBOLD+colors.CREDBG2}ERROR{colors.CEND+colors.CWHITE}: {colors.CBOLD+colors.CRED2+str(why)}{colors.CEND}')


def warn(why, solve=None) -> None:
    waitForStartup()
    if not solve:
        print(f'{current_time()} {colors.CBOLD+colors.CYELLOWBG}WARNING{colors.CEND+colors.CWHITE}: {colors.CBOLD+colors.CYELLOW2+why+colors.CEND}')
    else:
        print(f'{current_time()} {colors.CBOLD+colors.CYELLOWBG}WARNING{colors.CEND+colors.CWHITE}: {colors.CBOLD+colors.CYELLOW2+str(why)+colors.CEND} - {colors.CITALIC+colors.CYELLOW+str(solve)+colors.CEND}')


def success(message):
    waitForStartup()
    print(f'{current_time()} {colors.CBOLD+colors.CGREENBG}SUCCESS{colors.CEND+colors.CWHITE}: {colors.CBOLD+colors.CGREEN+str(message)+colors.CEND}')


def fail(message):
    waitForStartup()
    print(f'{current_time()} {colors.CBOLD+colors.CREDBG}FAIL{colors.CEND+colors.CWHITE}: {colors.CBOLD+colors.CRED2+str(message)+colors.CEND}')


def binput(ask):
    waitForStartup()
    return input(f'{current_time()} {colors.CWHITE+ask+colors.CEND}')


def log(message=None) -> None:
    waitForStartup()
    if message:
        if settings.printCap:
            print(
                f'{current_time()} {colors.CBOLD+colors.CWHITE+str(message).capitalize()}')
        else:
            print(f'{current_time()} {colors.CBOLD+colors.CWHITE+message}')
    else:
        print()


def clear():
    if platform == "Windows":
        import os
        os.system("cls")
        if settings.logoOnClear:
            logo()
    elif platform == "Linux":
        try:
            import os
            os.system("clear")
            if settings.logoOnClear:
                logo()
        except:
            import replit
            replit.clear()
            if settings.logoOnClear:
                logo()


def print2(message=None) -> None:
    waitForStartup()
    if message:
        if settings.printCap:
            text = f'{colors.CBOLD+colors.CWHITE+str(message).capitalize()}'
            print(text+' '*(columns()-len(text)), end='\r')

        else:
            text = f'{colors.CBOLD+colors.CWHITE+message}'
            print(text+' '*(columns()-len(text)), end='\r')

    else:
        print(end='\r')


def YnQn(qn: str):
    while True:
        ask = input(qn+' [Y/n]: ').lower()
        if ask == 'y' or ask == '' or ask == ' ':
            return True
        elif ask == 'n':
            return False
        else:
            pass


# def makeMenu(**opts):
#     for opt,do in opts.items():
#         print(f'This {opt} has to do {do}')
