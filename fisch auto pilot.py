import keyboard
import threading
import time

loop_running = False

hotkey1 = str(input('Insert hotkey for starting the autopilot:'))
hotkey2 = str(input('Insert hotkey for quitting the program:'))

def loop_keys():
    global loop_running
    while loop_running:
        keyboard.press_and_release('s') 
        time.sleep(0.1)
        keyboard.press_and_release('enter')
        time.sleep(0.1)

def on_r_press():
    """Handles f2 key press to start the sequence."""
    global loop_running
    if not loop_running:
        keyboard.press_and_release('\\') 
        time.sleep(0.1)
        loop_running = True
        threading.Thread(target=loop_keys, daemon=True).start()
    else:
        loop_running = False  

keyboard.add_hotkey(hotkey1, on_r_press)

print(f"Press {hotkey1} to start or stop the key sequence. Press {hotkey2} to exit.")
keyboard.wait(hotkey2)
 