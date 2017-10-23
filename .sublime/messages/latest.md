## DistractionFreeWindow v0.6.7

This will be one of the last updates to DistractionFreeWindow for Sublime Text 2
as Sublime Text 3 has left beta. Currently it is planned to split the releases
for Sublime Text 2 into a ST2 branch with "st2-"-prefixed tags. This enables
a significantly reduced package size and complexity for Sublime Text 3 users.
Also planned:

* dropping support for "distraction_free_window.sublime-settings" and only
  using:
  * Preferences.sublime-settings
  * Distraction Free.sublime-settings

Feedback is encouraged BEFORE these steps are taken:

    https://github.com/aziz/DistractionFreeWindow/issues/22

### Changes

* Python:
  * added missing double-checks in python script
  * make pycodestyle happy
* Package:
  * added missing command palette entry to open user keybindings
* Package Control:
  * added .gitattributes file to reduce package size by not shipping the
    screencast gif
* Package Dev:
  * added comments to all settings to support PackageDev's tooltips when
    completing settings
* Docs:
  * fixed screencast link in README due to addition of .gitattributes file
  * updated issue template
