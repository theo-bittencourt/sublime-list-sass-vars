List SASS variables
======================

## Please note
This fork does work, but only for `.scss` files and you **need** to have all files containing variables opened because it cannot search imported files yet. If you think you can help, please help try to improve this

Simple Sublime 2/3 plugin for listing SASS variables used in a file.

The default hotkey is <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>L</kbd> (or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>
+<kbd>L</kbd> on Linux to avoid conflicts with the lock screen hotkey).

It displays a list of SASS variables used in your current file allowing you to insert a selected one
directly into your code. It also supports `@imported SASS files so you can use variables defined in
external files. This can be disabled in settings.

Note that the plugin automatically ignores anything which looks like a vendor prefixed statement (e.g.
`@-webkit-keyframes`) and reserved words (e.g. `@media`, `@import` etc.)

![Screenshot](http://cl.ly/PIca)

Please note that the plugin currently does not understand variable scope and therefore will display all
the occurances of a variable.

Installation
------------
You can use the Sublime Package Manager to install this plugin. Alternatively, clone the repo into your
Packages folder.

Configuration
-------------
The settings file has currently two options:

 - `readImported` (default: `true`) - decides whether the plugin should attempt to read imported files
 - `readAllViews` (default: `false`) - decides whether the plugin should attempt to read all opened SASS files

Currently if the plugin checks all opened SASS files, it will only check for imported files in the currently selected file.
