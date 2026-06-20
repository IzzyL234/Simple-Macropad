# Macro-Tin 

I was inspired to make this as a way to get practice with some basic hardware and make somethng that is useful everyday! I wanted to be creative with the design, and after some looking online, found my way back to a sardine tin design that I had seen several times pop up on my feed. I thought that it was a fun and summery design and would be a cute desk decoration as well, when i'm not using it. Thus, the macro tin came to be! 

## What it is: 
The macro-tin is a four key macro pad that runs on a Raspberry Pi Pico microcontroller. The keys are programmable and customizable based on the user's needs. As I plan to use it, right now the keys are: 1) Copy 2) Paste 3) Screenshot 4) Screen Record
<br/><br/>
Note: a macro pad is a small keyboard with each key being a shortcut. When pressed, it executes the longer command and is meant to increase productivity. 
<br/><br/>
Zine:
<br/><br/>
<img width="1410" height="2000" alt="image" src="https://github.com/user-attachments/assets/b0c7c6a0-8ad9-4a82-8bcc-6324e4970b0b" />

## How it Works:

The Macro-Tin works by using a Raspberry Pi Pico as the main controller. Each of the four keys is connected to the Pico through the PCB. When a key is pressed, the switch closes the circuit and sends a signal to one of the Pico’s input pins.

The Pico runs firmware that reads which key was pressed and translates that button press into a keyboard shortcut. 


Current Functionality: 
<br/><br/>
<img width="823" height="190" alt="image" src="https://github.com/user-attachments/assets/6ef528c3-ccce-4547-92c4-6c66322adcf3" />

<br/><br/>
The case is designed to look like a sardine tin, to add some fun! The PCB and Raspberry Pi Pico are housed inside the case, while the keycaps are accessible from the top.l 

### Schematic
<img width="238" height="223" alt="image" src="https://github.com/user-attachments/assets/600acf50-d4ba-4e5a-9bb7-99ad3be6c42c" />
<br/><br/>
- All keys are connected to GND (ground)
- Each key is also connected to a GPIO# pin on the microcontroller
  
### PCB

**Gerber and Drill files available in Gerber Files folder**

<img width="301" height="200" alt="image" src="https://github.com/user-attachments/assets/a8946e56-8303-4404-9189-a366a3300d99" />

<img width="361" height="243" alt="image" src="https://github.com/user-attachments/assets/f58b9e52-8ca2-46bd-a1b8-0e1565ae96cc" />
<img width="392" height="255" alt="image" src="https://github.com/user-attachments/assets/6ccad750-d75d-4abb-8e9b-dce9c5495d84" />


<br/><br/>
- The Raspberry Pi Pico is on the bottom of the board to make it easier to organize things underneath the keys in the casing
- The keys are in the Cherry Mx Profile
- There are mounting holes on the edges to secure the PCB into the container/casing
- Using footprints generated with KiCad (passed KiCad DRC)

### Outer casing

**Assembly and STEP Files available in Assembly and STEP Files folder**


<img width="511" height="182" alt="image" src="https://github.com/user-attachments/assets/89f62e90-a88d-494d-a23f-9fc6cf20def1" />
<br/><br/>
- The outer casing has three parts: The outside box, the decoration layer, and the lid (becasue a sardine box needs a lid!)

### Firmware
[Firmware](Firmware/code.py) is uploaded to the github but is untested as of now. 
The Macro-Tin is designed to run on KMK firmware with CircuitPython on a Raspberry Pi Pico. Each switch connects a GPIO pin to GND when pressed. The firmware reads the GPIO inputs and sends the assigned keyboard shortcut to the computer over USB.

Planned default keymap:
- Key 1: Copy
- Key 2: Paste
- Key 3: Screenshot
- Key 4: Screenrecord

As stated above, although the current settings on the keymap is for copy/paste/screenshot/screenrecord the keymap can be edited in `code.py`, making the macropad programmable for different shortcuts and workflows.
### To Assemble:
1. 3D print the outer casing and order the custom PCB
3. Solder the switches, Raspberry Pi Pico, and any other required components onto the PCB.
4. Snap the keycaps on top of each switch.
5. Screw the board into the standoffs.
         /n Note: The hole clearance is designed so the screw will bite into the standoff and stay secure.
6. Place the PCB inside the bottom casing, making sure the USB port lines up with the cutout.
7. Attach the top casing so only the keycaps are exposed. It should naturally rest on top. 
8. Plug the Macro-Tin into the computer using a USB cable and test that each key activates the correct shortcut.
9. Put the lid on. It should stay secure.
   
### To Use:

1. Plug the USB cable into the Macro-Tin and connect it to the computer.
2. Wait for the computer to recognize it as a keyboard input device.
3. Press one of the four keys to activate its assigned shortcut or macro.
4. To change what the keys do, edit the firmware keymap and reload it onto the Raspberry Pi Pico.
5. Unplug the Macro-Tin when finished, or leave it connected as a desk shortcut tool.


#### More Details:
- Voltage: 5V through USB-C/micro-USB to the Raspberry Pi Pico

### BOM
| Item                    |                      Cost | Link                                                                                     |
| ----------------------- | ------------------------: | ---------------------------------------------------------------------------------------- |
| Raspberry Pi Pico 1     |                     $7.00 | https://www.pishop.us/product/raspberry-pi-pico-wh-pre-soldered-headers/?src=raspberrypi |
| Mechanical Switches (4) |                     $0.99 | https://www.aliexpress.us/item/3256806066297936.html                                     |
| Key Caps (4)            |                     $4.31 | https://www.aliexpress.us/item/3256809198369912.html                                     |
| Custom PCB Board        | $20.07 including shipping | https://www.nextpcb.com/                                                                 |
| **Total**               |                **$32.37** |                                                                                          |

