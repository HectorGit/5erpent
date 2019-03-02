import random
import math
#kinsol research... 

def main():

	#data = {}
	data = {"game": {"id": "game-id-string"},"turn": 1,"board": {"height": 11,"width": 11, "food": [{"x": 7,"y": 0},{"x": 8,"y": 2},{"x": 4,"y": 4}],"snakes": [{"id": "snake-id-string","name": "Sneky Snek","health": 100,"body": [{"x": 5,"y": 5}]}]},"you": {"id": "snake-id-string","name": "Sneky Snek","health": 100,"body": [{"x": 1,"y": 3}]}}

	move(data)

	#print("Hello World!")


def move(data):

	#print(data)

	directions = ['up', 'down', 'left', 'right']    

	foodList = data['board']['food']
	print(foodList)

	#my start position

	myCoord = data['you']['body'][0]

	#storing the distances
	distances = []

	for food in foodList:
		print("calculating distance for:")
		print(food)
		#calculate the distance.
		distance = math.sqrt(math.pow(myCoord['x'] - food['x'], 2) + math.pow(myCoord['y'] - food['y'], 2) * 1.0)

		distances.append(distance)

	# find the one with the min distance	
	minpos = foodList.index(min(foodList)) 
	print("this food has the least distance")
	print(minpos)

	closestFood = foodList[minpos]


    #find whether x or y is larger in distance. move in that direction.
	distance_x = abs(myCoord['x']-foodList[minpos]['x'])

	print("distance x: %d",distance_x)

	distance_y = abs(myCoord['y']-closestFood['y'])

	print("distance y: %d",distance_y)


	#how to determine whether moving up or down?
	#use the coordinates of the food we are chasing.

	if distance_x > distance_y:
		if myCoord['x'] - closestFood['x'] >0 :
			print "food is on my left"
			direction = 'left'
		else:
		#myCoord['x'] - closestFood['x'] <0
			print "food is on my right"
			direction = 'right'

	else:
	#distance_y > distance_x
		if myCoord['y'] - closestFood['y'] >0 :
			print "food is down"
			direction = 'down'
		else:
		#myCoord['x'] - closestFood['x'] <0
			print "food is up"
			direction = 'up'
    
	print(direction)

"""	direction = random.choice(directions)"""



if __name__== "__main__":

  main()

