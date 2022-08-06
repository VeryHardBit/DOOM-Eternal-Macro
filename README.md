# DOOM-Eternal-Macro
The script that helps you handle the horde of demons in DOOM Eternal. Makes "Rip & Tear" easier.

In this branch, the program will make mouse scroll weapon become quick switch.

Designed for no side buttons mouse.

## Usage
Once you download this repository.

run `weapon_cycle.py` script either by click on the file or run it from the command line.

Once the program is running, It will wait the input from your keyboard : 2,4,5

2 for Combo2, 4 for Combo4, 5 for Combo5.

These combo will affect the way mouse scroll works.

After this, these shorten form gonna be used :
- `PB` = Precision Bolt
- `RL` = Rocker Launcher
- `SS` = Super Shotgun
- `BL` = Ballista

### Combo2
To start this combo you just press `2` on your keyboard

This combo will make mouse scroll cycle becomes : `PB, RL, PB, BL, PB, SS`.

This combo is designed for most heavy demons. And conserve ammo resources very well.

### Combo4
To start this combo you just press `4` on your keyboard

This combo will make mouse scroll cycle becomes : `RL, PB, PB, BL, PB, SS, PB`.

This combo is just like Combo2 but started with Rocker Launcher

### Combo5
To start this combo you just press `5` on your keyboard

This combo will make mouse scroll cycle becomes : `SS, PB, BL, PB`

This combo is designed against Marauder.


## Dependencies
- Python is required
- Other python packages include:
    - keyboard
    - mouse
    - pynput

## Combo Customization
===

## Issues

As you can see, the program in this branch only make mouse scroll weapon swap faster and limiting the scroll cycle.

For Full Macro, It's currently developing.
The obstacle for full macro is the program needs to perfect the timing.

For example : Once you click the "shoot" button on Ballista. There will be a slight delay before you can swap the gun.

And this delay tend to be different for each guns.