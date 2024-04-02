import os
import toml
import socket

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

logo = '''\n
\033[1;96m ||\||\|  |\||\|  ||\|  ||\|      |\|   \033[1;91m||\||\||\|  ||\||\||\||\|
\033[1;96m ||\||\|  |\||\|  ||\|    ||\|  |\|     \033[1;91m||\|        ||\|      |\|
\033[1;96m ||\|   |\|  |\|  ||\|       ||\|       \033[1;91m||\||\||\|  ||\||\||\||\|
\033[1;96m ||\|   |\|  |\|  ||\|    ||\|   |\|    \033[1;91m||\|        ||\|   |\|
\033[1;96m ||\|        |\|  ||\|  ||\|       |\|  \033[1;91m||\|        ||\|      |\|
\033[1;96m ||\|        |\|  ||\| ||\|         |\| \033[1;91m||\||\||\|  ||\|        |\|

\033[1;96m Version 1.0.0 Codded By \033[1;91m@jabfx
\n'''

print(logo)
