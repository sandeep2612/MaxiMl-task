#counts the maximum number of distinct character in the string(str_name)
def distict_elements_in_string(str_name,n):
	Number_chara=[0]*256
	for i in range(n):
		Number_chara[ord(str_name[i])]+=1

	maximum_distinct=0
	for i in range(256):
		if Number_chara[i]!=0:
			maximum_distinct+=1
	return maximum_distinct


# Function that return the length of smallest Substring with maximum distinct character 

def SubstringMaximumDistictElements(str_name):
	LengthOfString=len(str_name)

	Max_distinct=distict_elements_in_string(str_name,LengthOfString)
	# print(Max_distinct)
	val=LengthOfString

	for i in range(LengthOfString):
		for j in range(LengthOfString):
			substr=str_name[i:j]
			#print(substr)
			length_substr=len(substr)
			# print(length_substr)
			substr_distinct=distict_elements_in_string(substr,length_substr)
			# print(substr_distinct)

			if length_substr<val and Max_distinct==substr_distinct:
				val=length_substr

	return val


if __name__ == "__main__":
    #Input the string using prompt
    string_name=input("Enter a string:  ")

    Length=SubstringMaximumDistictElements(string_name)
    print(Length)