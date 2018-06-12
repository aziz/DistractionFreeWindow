# [DistractionFreeWindow](https://github.com/aziz/DistractionFreeWindow) for [Sublime Text](https://www.sublimetext.com)

[![License](https://img.shields.io/github/license/aziz/DistractionFreeWindow.svg?style=flat-square)](https://github.com/aziz/DistractionFreeWindow/blob/master/LICENSE)
[![Downloads via Package Control](https://img.shields.io/packagecontrol/dt/DistractionFreeWindow.svg?style=flat-square)](https://packagecontrol.io/packages/DistractionFreeWindow)
[![Latest release](https://img.shields.io/github/release/aziz/DistractionFreeWindow.svg?style=flat-square)](https://github.com/aziz/DistractionFreeWindow/releases/latest)

<br>

<p align="center">
  <img width="750" src="https://raw.githubusercontent.com/aziz/DistractionFreeWindow/master/docs/screencast.gif" alt="Screencast">
</p>

<br>

> Screencast shows [gruvbox](https://github.com/Briles/gruvbox) Theme & Color Scheme, [Operator Mono](http://www.typography.com/fonts/operator/overview) Medium as font.

---

## Description

[Sublime Text](https://www.sublimetext.com)'s [`distraction free mode`](https://www.sublimetext.com/docs/3/distraction_free.html) but not full-screen!
A windowed UI is more manageable and accessible, yet it can be simple and sublime!

DistractionFreeWindow was inspired by [this forum post](https://forum.sublimetext.com/t/non-fullscreen-distraction-free-mode/12343).

## Installation

### Installation via Package Control

1. Install [Package Control](https://packagecontrol.io/installation) for [Sublime Text](https://www.sublimetext.com).
  * Close and reopen Sublime Text when done.
2. Open the [Command Palette](http://docs.sublimetext.info/en/latest/extensibility/command_palette.html) via `Tools > Command Palette` from the main menu and select `Package Control: Install Package`.
3. Select [`DistractionFreeWindow`](https://packagecontrol.io/packages/DistractionFreeWindow).

### Manual installation

* Select `Preferences > Browse Packages` from the main menu. Use the command line to `cd .../Packages` into that exact same folder, then `git clone git://github.com/aziz/DistractionFreeWindow.git`.
* Or select `Preferences > Browse Packages` from the main menu, then create a subfolder named `DistractionFreeWindow` and unzip the contents of [a current snapshot of `master` as `*.zip`](https://github.com/aziz/DistractionFreeWindow/archive/master.zip) into it.

## Usage

Use the keybinding `Super+F11` to toggle DistractionFreeWindow mode.

### Changing Layout

Users of the [`MaxPane`](https://packagecontrol.io/packages/MaxPane) plug-in will appreciate that [`DistractionFreeWindow`](https://packagecontrol.io/packages/DistractionFreeWindow) directly integrates with it and simplifies the layout when you go into **DistractionFreeWindow mode** and restores the layout after comming back out of it.

## Customization

### Settings

DistractionFreeWindow inherits `distraction free mode` settings from the core application.
You can set these via `Preferences > Settings - Distraction Free`, compare the official docs:

<https://www.sublimetext.com/docs/3/distraction_free.html>

### Key Bindings

You can adjust the default key binding <kbd>Super</kbd><kbd>F11</kbd> via `Preferences > Package Settings > DistractionFreeWindow > Key Bindings` from the main menu.

## License

See the [`LICENSE`](LICENSE) for details.
