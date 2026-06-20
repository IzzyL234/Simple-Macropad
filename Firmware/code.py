
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# Change these pins to match your PCB connections
keyboard.matrix = KeysScanner(
    pins=[
        board.GP0,  #20
        board.GP1,  #19
        board.GP2,  #17
        board.GP3,  #16
    ],
    value_when_pressed=False,
    pull=True,
)

keyboard.keymap = [
    [
        KC.LCTRL(KC.C),             # Copy
        KC.LCTRL(KC.V),             # Paste
        KC.LGUI(KC.LSHIFT(KC.S)),   # Screenshot
        KC.LCTRL(KC.P),             # Print
    ]
]

if __name__ == "__main__":
    keyboard.go()
