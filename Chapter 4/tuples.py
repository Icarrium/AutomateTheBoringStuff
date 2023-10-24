dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# cannot overwrite the tuple item
#dimensions[0] = 400

print("Original dimensions tuple:")
for dimension in dimensions:
	print(dimension)

# you can overwrite tuple item, but you can overwrite the tuple itself
dimensions = (400, 100)
print("Modified dimensions tuple:")
for dimension in dimensions:
	print(dimension)

