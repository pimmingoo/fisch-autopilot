import keyboard
import threading
import time

loop_running = False

hotkey1 = str(input('Insert hotkey for starting the autopilot: '))
hotkey3 = str(input('Insert hotkey for stopping the autopilot: '))
hotkey2 = str(input('Insert hotkey for quitting the program: '))

def loop_keys():
    global loop_running
    while loop_running:
        keyboard.press_and_release('s') 
        time.sleep(0.1)
        keyboard.press_and_release('enter')
        time.sleep(0.1)

def start_autopilot():
    """Starts the autopilot loop."""
    global loop_running
    if not loop_running:
        keyboard.press_and_release('\\') 
        time.sleep(0.1)
        loop_running = True
        threading.Thread(target=loop_keys, daemon=True).start()

def stop_autopilot():
    """Stops the autopilot loop."""
    global loop_running
    loop_running = False

keyboard.add_hotkey(hotkey1, start_autopilot)
keyboard.add_hotkey(hotkey3, stop_autopilot)

print(f"Press {hotkey1} to start the autopilot, {hotkey3} to stop it, and {hotkey2} to exit.")
keyboard.wait(hotkey2)

 