import bagua_func
import base64
#import pyperclip

'''
This is a beginner's work; sorry if the code is not that regulated.
You can enable the auto copy by install pyperclip
(pip install pyperclip) and remove the # in the code. 
---This part of code below is for testing.---
'''
'''
str_text = input("Text to base64: ")
bytes_str_text = str_text.encode("utf-8")
str_text = base64.b64encode(bytes_str_text)  
print(str_text.decode("utf-8"))

input_str_e = input("Base64 to bagua: ")
testi = bagua_func.encode_bagua(input_str_e)
print(testi)

input_str_d = input("Bagua to base64: ")
testo = bagua_func.decode_bagua(input_str_d)
print(testo)

str_64 = input("Base64 to text: ")
str_64 = base64.b64decode(str_64).decode("utf-8")
print(str_64)
'''

print("-----ENCODE INPUT-----")
str_to_bagua = input("Text to Bagua: ")
try:
    bytes_str_to_bagua = str_to_bagua.encode("utf-8")
    str_to_bagua = base64.b64encode(bytes_str_to_bagua)
    print("-----ENCODE OUTPUT-----")
    output = bagua_func.encode_bagua(str_to_bagua.decode("utf-8"))
    print(output)
    print("Info: The lenth of the output string is "+str(len(output))+".")
#    pyperclip.copy(output)
#    print("Output string copied to clipboard")
except Exception as error:
    print("Error: "+ str(error))    
print("-----ENCODE END-----")    

print("-----DECODE INPUT-----")    
bagua_to_str = input("Bagua to Text: ")
try:
    str_64 = bagua_func.decode_bagua(bagua_to_str)
    string = base64.b64decode(str_64)
    string = string.decode("utf-8")
    print("-----DECODE OUTPUT-----")
    print(string)
    print("-----DECODE END-----") 
except Exception as error:
    print("Error: "+ str(error))    
    
