from pynput import keyboard
import sys


class Keyboardstuff:
    
    def __init__(self) -> None:
           
           pass
        
    def on_press(key):
    
        try:
       
            print('{0}'.format(
            key),end="")
            
            
            sys.stdout.flush()
        

        except AttributeError:
            print('special key {0} pressed'.format(
                key))
            sys.stdout.flush()

    def on_release(key):
        
            


        #print('{0} released'.format(
        #   key))
        if key==keyboard.Key.backspace:
            pass
            #remove last letter.
       
        if key == keyboard.Key.esc:
            # Stop listener
            return False #And show the word! 
    #Utilize this for gathering data - 

 # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start() #Start the listener - a thread.





