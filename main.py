import delete
import sys
import install
import update
import search
import helppage
import os
import urllib.request
import ntgcfg
from colorama import Fore


# Check for arguments that will disable POST
full_cmd_arguments = sys.argv
DebugArgs = full_cmd_arguments[3:]
if not DebugArgs:
    print(Fore.GREEN + "Post Enabled" + Fore.WHITE)
    # P O S T, do all checks to be sure Elements can go ahead
    def post():
        if os.geteuid() != 0:
            print(Fore.RED + "Fatal Error: You must run Elements as root.")
            sys.exit()
        else:
            pkgs = open('/usr/share/elements/pkgs', 'r')
        packages = pkgs.read()
        print(Fore.GREEN + "Pkgs Loaded")
    post()
else:
    print("")

# Check for Configuration File
cfg_load = os.system("ls /usr/share/elements | grep cfg.py > /dev/null")
# In case config file isnt found(command returns an answer other an 0), throw an error
if cfg_load != 0:
    print(Fore.RED + "Fatal Error: Config File Not Found.")
    if DebugArgs:
        print(Fore.RED + "Continuing with Errors" + Fore.WHITE)
    else:
        sys.exit()
else:
    # If successful run the config file
    os.system("python3 /usr/share/elements/cfg.py")
    print(Fore.GREEN + "Success: Config File Loaded" + Fore.WHITE)

# Read first argument, mostly used for --add/--del etc
full_cmd_arguments = sys.argv
args1 = full_cmd_arguments[1:]
# Read second argument, used for packages
full_cmd_arguments = sys.argv
args2 = full_cmd_arguments[2:]

# If first args arent found, tell the user how to use Elements
if not args1:
    print(Fore.RED + "Usage: 'lmt --option package'")
    helppage.helppage()
    sys.exit()
else:
    args = args1[0]


# Check for internet, since --update could do massive damage without internet
def connect():
    try:
        # Try find internet
        urllib.request.urlopen('https://google.com')
        return True
    except:
        return False


if connect():
    # Several CLI Arguments
    if args in ['--up', '-U', '--update']:
        update.update()
    elif args in ['--ref', '-R', '--refresh']:
        update.refresh()
    elif args in ['--cfg-regen']:
        update.cfgregen()
    elif args in ['--help', '-h', '?']:
        helppage.helppage()
    elif args in ['--ver', '-v']:
        helppage.version()
    elif args in ['--list', '-l']:
        print("Packages: " + packages)
    elif args in ['--configure', '--cfg']:
        ntgcfg.tui_interface()
    else:
        # Check for second argument
        if not args2:
            print(Fore.RED + "Error: you must specify what package to add/remove." + Fore.WHITE)
        else:
            # Make pkg str in install.py to be the second argument taken before
            install.pkg = args2[0]
    if args in ['--add', '-a']:
        install.install_pkg()
    elif args in ['--del', '-d', '--delete']:
        delete.delete_pkg()
    elif args in ['--sr', '--search', '-s']:
        search.search_pkg()


else:
    # Average Internet Error
    print(Fore.RED + "No internet. Cannot do " + args + " at the moment." + Fore.WHITE)
