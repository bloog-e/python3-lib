import colors_print as colors
reset = "\033[0m"
# Black
fgBlack = "\033[30m"
fgBrightBlack = "\033[30;1m"
bgBlack = "\033[40m"
bgBrightBlack = "\033[40;1m"

# Red
fgRed = "\033[31m"
fgBrightRed = "\033[31;1m"
bgRed = "\033[41m"
bgBrightRed = "\033[41;1m"

# Green
fgGreen = "\033[32m"
fgBrightGreen = "\033[32;1m"
bgGreen = "\033[42m"
bgBrightGreen = "\033[42;1m"

# Yellow
fgYellow = "\033[33m"
fgBrightYellow = "\033[33;1m"
bgYellow = "\033[43m"
bgBrightYellow = "\033[43;1m"

# Blue
fgBlue = "\033[34m"
fgBrightBlue = "\033[34;1m"
bgBlue = "\033[44m"
bgBrightBlue = "\033[44;1m"

# Magenta
fgMagenta = "\033[35m"
fgBrightMagenta = "\033[35;1m"
bgMagenta = "\033[45m"
bgBrightMagenta = "\033[45;1m"
# Cyan
fgCyan = "\033[36m"
fgBrightCyan = "\033[36;1m"
bgCyan = "\033[46m"
bgBrightCyan = "\033[46;1m"

# White
fgWhite = "\033[37m"
fgBrightWhite = "\033[37;1m"
bgWhite = "\033[47m"
bgBrightWhite = "\033[47;1m"

#specific
BOLD="\033[1m"
FAINT="\033[2m"
ITALIC="\033[3m"
UNDERLINE="\033[4m"
BLINK="\033[5m"
NEGATIVE="\033[7m"
CROSSED="\033[9m"
def color_test(message='colors test !'):
    for i in dir(colors):
        if not i.startswith('__'):
            if i not in ["color_test","put","parse_color","bases","colors_names","l","all_colors"]:
                print(getattr(colors,i)+message+'\033[0m')
def colors_names():
    l=[]
    for i in dir(colors):
        if not i.startswith('__'):
            if i not in ["color_test","put","parse_color","bases","colors_names","l","all_colors"]:
                l.append(i)
    
    return l
def all_colors():
    l=[]
    for i in dir(colors):
        if not i.startswith('__'):
            if i not in ["color_test","put","parse_color","bases","colors_names","l","all_colors"]:
                l.append(getattr(colors,i))
    
    return l

def put(color=fgBlack, text="hello"):
    return color+text+reset
def parse_color(color_str):
    """parse a color name in a string to the real color"""
    return getattr(colors,color_str)
