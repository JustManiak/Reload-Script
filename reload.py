import os
import sys
import keyboard

def restart_script():
    python_executable = sys.executable    
    os.execv(python_executable, [python_executable] + sys.argv)

#Example of usage
    
def reloadscript():
    while True:
        key = keyboard.read_event(suppress=True)
        if key.event_type == keyboard.KEY_DOWN:
            if key.name == 'r':
                print("Reloading the script...")
                restart_script()

            elif key.name == 'q':
                print("Quitting the script.")
                sys.exit()

if __name__ == "__main__":
    reloadscript()