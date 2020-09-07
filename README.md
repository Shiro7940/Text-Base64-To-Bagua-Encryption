# Text-Base64-To-Bagua-Encryption
A very simple Python program to convert text and base64 strings to Chinese bagua characters.
* You can enable the auto copy by install pyperclip (pip install pyperclip) and remove the # in the code. 
## An example of running the script:
Notice that the converted Bagua string's appearance will not correspond to the base64 characters' binary representation, since the conversion is performed according to the Unicode order.
* (Might have a update about that.)
```
[evaluate bagua_app.py]
-----ENCODE INPUT-----
Text to Bagua: test
-----ENCODE OUTPUT-----
䷝䷆䷕䷳䷝䷀☯☯
Info: The lenth of the output string is 8.
-----ENCODE END-----
-----DECODE INPUT-----
Bagua to Text: ䷝䷆䷕䷳䷝䷀☯☯
-----DECODE OUTPUT-----
test
-----DECODE END-----
```
