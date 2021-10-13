from colorama import Fore
ver = "Next"


def helppage():
    print(Fore.CYAN + "Elements " + ver + Fore.WHITE)
    print("--------------")
    print("Commands: ")
    print("--add/-a: " + "install packages")
    print("--del/-d: " + "remove packages")
    print("--ref/-r: " + "refresh the repository")
    print("--up/-U: " + "update")
    print("--sr/-s: " + "search a package")
    print("--cfg-regen: " + "regenerate cfg.py file")
    print("--list/-l: " + " list all installed packages")
    print("--configure/--cfg:" + " configure Elements & Nitrogen")
    print('--ver/-v: ' + 'show version')
    print("--help/-h: " + "show this menu")


def version():
    print("Elements " + ver)
