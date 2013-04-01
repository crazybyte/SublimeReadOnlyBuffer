# Sublime Read Only Buffer

SublimeReadOnlyBuffer is small plugin for setting Sublime Text 2 editor buffer(s) read-only and maintaning
the read-only/read-write state of an edited file between editing sessions using a filename cache.

# Install

Install with [Package Control](http://wbond.net/sublime_packages/package_control).

`Command Palette` > `Package Control: Install Package` > `Read Only Buffer`

Or clone this reporitory from GitHub into Sublime's Packages folder:

```bash
$ git clone https://github.com/crazybyte/SublimeReadOnlyBuffer.git
```

# Config

You can edit the configuration/filename cache list via the menu entry.

`Preferences` -> `Package Settings` -> `Read Only Buffer` -> `Settings - User`

Or  

`Command Palette` > `Preferences: Read Only Buffer Settings - User`

```json
{
    "cache" : {
    	"filename": True
	}
}
```

# Usage

For setting a buffer read-only use `Buffer: Set read-only buffer` option, from command palette or on OS X
key binding `super + shift + r` or key binding `ctrl + alt + r` on Linux.  
For setting a buffer read-write use `Buffer: Set read-write buffer` option, from command palette or on OS X
key binding `super + shift + u` or key binding `ctrl + alt + u` on Linux.  


# Contributors

[Jeffrey Sadeli] (https://github.com/jsadeli)

# License

This plugin is licensed under the MIT license.