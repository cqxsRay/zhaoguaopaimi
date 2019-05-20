import random
import string
# print(random.randrange(0, 10, 2))
ran_str = ''.join(random.sample(string.ascii_letters + string.digits))
print(ran_str)