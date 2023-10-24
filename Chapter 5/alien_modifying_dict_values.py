alien = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien)
print(f"Original postion: {alien['x_position']}, {alien['y_position']}")

# move the alien to the right
# Determine how far to move the alien based on it's current speed

if alien['speed'] == 'slow':
	x_increment = 1
elif alien['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

# The new position of the alien is old + increment
alien['x_position'] = alien['x_position'] + x_increment

print(f"New position: {alien['x_position']}, {alien['y_position']}")

# removing a key-value pair
del alien['y_position']
print(alien)