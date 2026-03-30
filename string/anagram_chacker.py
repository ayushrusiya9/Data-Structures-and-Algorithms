# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
	# Remove spaces and convert to lowercase
	str1 = str1.replace(' ', '').lower()
	str2 = str2.replace(' ', '').lower()
    
	# If lengths differ, they can't be anagrams
	if len(str1) != len(str2):
		return False
    
	# Sort both strings and compare
	return sorted(str1) == sorted(str2)

# Example usage
if __name__ == "__main__":
	s1 = input("Enter first string: ")
	s2 = input("Enter second string: ")
	if are_anagrams(s1, s2):
		print("Anagrams!")
	else:
		print("Not anagrams.")
