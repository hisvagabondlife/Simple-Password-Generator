#!/usr/bin/env python3

import string
import random
if __name__ == "__main__":
	x1 = string.ascii_lowercase
	x2 = string.ascii_uppercase
	x3 = string.digits
	x4 = string.punctuation
	le = int(input("Enter password length: "))
	s = []
	s.extend(list(x1))
	s.extend(list(x2))
	s.extend(list(x3))
	s.extend(list(x4))
	print("Your password: ", end="")
	print("".join(random.sample(s, le)))
	