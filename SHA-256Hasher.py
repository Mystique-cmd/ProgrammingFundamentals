import hashlib
text = input( " Enter Your Text Here: " )
hashed_value = hashlib.sha256(text.encode()).hexdigest()
print( "The Hashed Value is :"+ hashed_value)
