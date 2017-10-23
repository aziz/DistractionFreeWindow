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

By default this plugin hides **tabs**, **status bar**, **side bar**, **menu** and **minimap**.
You can also hide **line numbers**, **fold buttons**, **the whole gutter**.
You can **center the text** and configure the width.
See the [settings section](#settings) in case you want to customize DistractionFreeWindow.

### Changing Layout

Users of the [`MaxPane`](https://packagecontrol.io/packages/MaxPane) plug-in will appreciate that [`DistractionFreeWindow`](https://packagecontrol.io/packages/DistractionFreeWindow) directly integrates with it and simplifies the layout when you go into **DistractionFreeWindow mode** and restores the layout after comming back out of it.

## Customization

### Settings

You can adjust the default settings via `Preferences > Package Settings > DistractionFreeWindow > Settings - User` from the main menu.

### Key Bindings

You can adjust the default key binding <kbd>Super</kbd><kbd>F11</kbd> via `Preferences > Key Bindings` from the main menu.

## License

See the [`LICENSE`](LICENSE) for details.
