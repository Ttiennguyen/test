import string
import random

password_generation = string.ascii_letters +string.digits
min_size_pass = 8
max_size_pass = 16

password ="".join(random .choice(password_generation) for x in range(random.randint(min_size_pass,max_size_pass))) 
#vong lap for noi lai va trong khoang 8 den 16
print "this pass = %s" %password