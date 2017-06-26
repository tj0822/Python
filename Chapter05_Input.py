# print "Enter your name : "
# somebody = raw_input()
# print "Hi,", somebody+'.', "How are you today?"



# 5.3
# print "This program converts Fahrenheit to Celsius"
# print "Type in a temperature in Fahrenheit : "
# fahrenheit = float(raw_input())
# print "fahrenheit : ", fahrenheit
# celsius = (fahrenheit - 32) * 5.0 / 9
# print "That is", celsius, "degrees Celsius"



# 5.4
import urllib
file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
message = file.read()

print message