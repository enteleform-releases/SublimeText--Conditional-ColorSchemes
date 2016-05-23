# Conditional ColorSchemes

Define color schemes for specific paths, extensions, & filenames.

## FEATURES

### Color Schemes For Specific Directories

![Path](https://raw.githubusercontent.com/Enteleform/-RES-/master/%5B%20%40README%20%5D/ST_ConditionalColorSchemes/Path.gif)

You can define `RegEx` patterns to match:

* parent directories
* sequences of subdirectories
* sequences of subdirectories within a particular parent directory

Additionally, there is an `include_FileName_In_FilePath` setting which allows you to match:

* specific files with an exact path
* specific files with a particular extension within one of the previously mentioned directory patterns

### Color Schemes For Specific Files

![FileName](https://raw.githubusercontent.com/Enteleform/-RES-/master/%5B%20%40README%20%5D/ST_ConditionalColorSchemes/FileName.gif)

You can define `RegEx` patterns to match:

* file extensions
* complete file names
* partial file names

## USAGE

Copy the contents of the [**example settings**](https://github.com/Enteleform/ST_ConditionalColorSchemes/blob/master/Example.sublime-settings):  
`Preferences > Package Settings > Conditional ColorSchemes > Settings ─ Example`  
to your user settings file:  
`Preferences > Package Settings > Conditional ColorSchemes > Settings ─ User`  
and edit them as necessary.

User settings can also be accessed via the command palette with the `Conditional ColorSchemes: Edit Settings` command.

**Note:**  
When adding new conditions, files that were already open must be reloaded in order for the color schemes to be affected.

## KNOWN BUGS

When SublimeText is first opened, files are loaded before plugins.

Because of this, only files which are opened *after* SublimeText is fully loaded will be affected by this plugin.
