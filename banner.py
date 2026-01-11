try:
   from colorama import Fore, init
   init(autoreset=False)
except Exception:
   class _Fore:
      RED = ""
      GREEN = ""
      YELLOW = ""
      RESET = ""
   Fore = _Fore()


def show_banner():
   print(
      Fore.RED
      + """
 ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗     ██╗  ██╗
 ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     ██║  ██║
 ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     ███████║
 ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║     ██╔══██║
 ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗██║  ██║
 ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝
 """
      + Fore.GREEN
      + "          SentinelX – Quick Pentesting Toolkit\n"
   )
   print(Fore.YELLOW + "                Author: Arunaditya Ghosh | Version: 1.0.0\n" + Fore.RESET)