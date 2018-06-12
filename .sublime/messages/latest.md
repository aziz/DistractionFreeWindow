## DistractionFreeWindow v1.0.0

* created separate branches for ST2 and ST3
  * future releases will be tagged with prefixes
  * removed redundant code where applicable
  * fixed aziz/DistractionFreeWindow#22

### Breaking changes for SublimeText 3

DistractionFreeWindow now inherits `distraction free mode` settings from the core application.
You can set these via `Preferences > Settings - Distraction Free`, compare the official docs:

<https://www.sublimetext.com/docs/3/distraction_free.html>

This implicitly means that the `Data/Packages/User/distraction_free_window.sublime-settings` file
is now redundant / useless and can safely be removed them.
