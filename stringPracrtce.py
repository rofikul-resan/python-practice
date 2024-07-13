# practice string methode

name = "resan"

sub_name= name[-4 : -1]
print(len(name))
print(sub_name)

# try skiping value by   index
full_name = "rofikul islam resan"

print(full_name[2:9:2])
print(full_name[2::2])

# print(full_name[2:9:1]) #[start index : end index : numder of skiping value ] 
print(full_name[2::3])


# ------------------------
# string function practice 
# -------------------------
print(len(full_name))

print(full_name.endswith('an')) # return boolean value
print(full_name.startswith('re')) # return boolean value


print(full_name.capitalize()) # capitalize the first letter
print(full_name.upper()) # convert into upper case
print(full_name.lower()) # convert into lower case
print(full_name.title())  # convert into title case

print(full_name.find('is')) # find the index of the letter
print(full_name.replace("r" , "f")) #return a new value , replace all the match
print(full_name)
print(full_name.count('a')) # count the letter
print(full_name.isdigit()) # return a boolean value

# write all string function  with a comment what that function work 
print('''
   string function practice
   -------------------------
   len() - return the length of the string
   endswith() - return a boolean value if the string end with the given letter
   startswith() - return a boolean value if the string start with the given letter
   capitalize() - capitalize the first letter of the string
   upper() - convert the string into upper case
   lower() - convert the string into lower case
   title() - convert the string into title case
   find() - find the index of the given letter
   replace() - replace all the match letter with the given letter
   count() - count the number of the given letter
   isdigit() - return a boolean value if the string is digit
   ''')

# more string function practice

print(full_name.isalnum()) # return a boolean value if the string is alphanumeric
print(full_name.isalpha()) # return a boolean value if the string is alphabetic
print(full_name.isascii()) # return a boolean value if the string is ascii
print(full_name.isdecimal()) # return a boolean value if the string is decimal
print(full_name.isdigit()) # return a boolean value if the string is digit
print(full_name.isidentifier()) # return a boolean value if the string is identifier
print(full_name.islower()) # return a boolean value if the string is lower case
print(full_name.isnumeric()) # return a boolean value if the string is numeric
print(full_name.isprintable()) # return a boolean value if the string is printable
print(full_name.isspace()) # return a boolean value if the string is space
print(full_name.istitle()) # return a boolean value if the string is title case
print(full_name.isupper()) # return a boolean value if the string is upper case

# '''
# practice string function
# '''
print('''
   string function practice
   -------------------------
   isalnum() - return a boolean value if the string is alphanumeric
   isalpha() - return a boolean value if the string is alphabetic
   isascii() - return a boolean value if the string is ascii
   isdecimal() - return a boolean value if the string is decimal
   isdigit() - return a boolean value if the string is digit
   isidentifier() - return a boolean value if the string is identifier
   islower() - return a boolean value if the string is lower case
   isnumeric() - return a boolean value if the string is numeric
   isprintable() - return a boolean value if the string is printable
   isspace() - return a boolean value if the string is space
   istitle() - return a boolean value if the string is title case
   isupper() - return a boolean value if the string is upper case
   ''')

# all escape sequence practice

print("hello \t resan") # tab
print("hello \n resan") # new line
print("hello \\ resan") # back slash
print("hello \' resan") # single quote
print("hello \" resan") # double quote
print("hello \a resan alert") # alert
print("hello \b resan") # back space
print("hello \r resan") # carriage return
print("hello \v resan") # vertical tab
print("hello \f resan") # form feed
print("hello \x1b resan") # hex escape sequence

# --------------------------------
# f string practice
# --------------------------------
name = input("Enter your name: ")
print(f"Hello {name}") # f string practice