user = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi'
	}

favorite_languages = {
	'jen': "python",
	'sarah': "c",
	'edward': "rust",
	'phil': "python"
	}

for key, value in user.items():
	print(f"Keys: {key}")
	print(f"Values: {value}")
	
for k, v in favorite_languages.items():
	print(f"{k.title()}'s favorite language is {v.title()}'")

# looping through just the keys using the .key() method
print("The software developers on the team are:")
for name in favorite_languages.keys():
	print(name)

