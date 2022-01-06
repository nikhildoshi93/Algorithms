# Given a String containing only digits, restore it by returning all possible valid IP address combinations.
# (A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.) 

# Eg: 25525511135
# Ans: 2 ([“255.255.11.135”, “255.255.111.35”])

def segments(r, i, s, buf):
	if (r == 1):
		return [e + "." + s[i:] for e in buf]

	new = []
	if not (len(s) - i - 1 > (r-1)*3):
		if not (len(s) - i - 1 == (r-1)*3 and int(s[i+1] + s[i+2] + s[i+3]) > 255):
			ones = [e + "." + s[i] for e in buf]
			new += segments(r-1,i+1,s,ones)

	if not (len(s) - i - 2 > (r-1)*3) and s[i] != "0":
		if not (len(s) - i - 2 == (r-1)*3 and int(s[i+2] + s[i+3] + s[i+4]) > 255):
			twos = [e + "." + s[i] + s[i+1] for e in buf]
			new += segments(r-1,i+2,s,twos)

	three_digit = s[i] + s[i+1] + s[i+2]
	if not (len(s) - i - 3 > (r-1)*3) and s[i+1] != "0" and int(three_digit) < 256:
		threes = [e + "." + s[i] + s[i+1] + s[i+2] for e in buf]
		new += segments(r-1,i+3,s,threes)
	return new



print(segments(4, 0, "25525511135", [""]))

