import sys

terminal_arguments = sys.argv

if len(terminal_arguments) < 2:
    print("erreur.")
    exit()
else:
    print("\n".join(terminal_arguments[:0:-1]))