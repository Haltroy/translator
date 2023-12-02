# translator
 Automate translation of XML files using Google Translate.

 Originally designed to read .NET's `.resx` files.

 This script reads an XML file, gets every `<data>` nodes and the values inside these from `<value>` node
 and translates them to all available languages. The original file's language is auto-detected.

 This script is designed to not write the failed transltions and ignores the pre-made ones meaning if it fails on multiple
 languages you can start the script again and it will try those failed languages again.

 Requires `googletrans` python library to be installed.

 USAGE: `python translate-item.py <original> <template> [before] [after]`
 - `<>` - Required Arguments
 - `[]` - Optional arguments
 - Use `$name$` for translation name and `$value$` for the translations in template file.

