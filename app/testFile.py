import random
import math
#kinsol research... 

def main():

	#data = {}
	data = {"game": {"id": "game-id-string"},"turn": 1,"board": {"height": 11,"width": 11, "food": [{"x":1,"y":4},{"x":3,"y":3},{"x": 7,"y": 0},{"x": 8,"y": 2},{"x": 4,"y": 4}],"snakes": [{"id": "snake-id-string","name": "Sneky Snek","health": 100,"body": [{"x": 5,"y": 5}]}]},"you": {"id": "snake-id-string","name": "Sneky Snek","health": 100,"body": [{"x": 1,"y": 3}]}}

	move(data)

	#print("Hello World!")


def move(data):

	#print(data)

	directions = ['up', 'down', 'left', 'right']    

	height = data['board']['height']
	width = data['board']['width']

	foodList = data['board']['food']
	print(foodList)

	#my myCoord position

	myCoord = data['you']['body'][0]
	print('mycoord %o', myCoord)

	#storing the distances
	distances = []

	for food in foodList:
		print("calculating distance for:")
		print(food)
		#calculate the distance.
		#do i need this to be a float???
		distance = math.sqrt(math.pow(myCoord['x'] - food['x'], 2) + math.pow(myCoord['y'] - food['y'], 2) * 1.0)

		distances.append(distance)

	# find the one with the min distance	
	minpos = foodList.index(min(foodList)) 
	print("this food has the least distance")
	print(minpos)

	closestFood = foodList[minpos]
	print("closestFood %o",closestFood)


    #find whether x or y is larger in distance. move in that direction.
	distance_x = abs(myCoord['x']-foodList[minpos]['x'])

	print("distance x: %d",distance_x)

	distance_y = abs(myCoord['y']-closestFood['y'])

	print("distance y: %d",distance_y)


	#how to determine whether moving up or down?
	#use the coordinates of the food we are chasing.

	#careful here
	#just initiating it as the same coordinates
	hypotheticalEndPosition = myCoord


	if distance_x > distance_y:
		
		if myCoord['x'] - closestFood['x'] > 0 :

			if myCoord['x'] == closestFood['x']:
				print "on the same row x coord"
				#need to fix this - 
				#maybe move up or down depending on 
				#the y coord compared to 
				#current position
				direction = random.choice(['up','down'])
			else:
				print "food is on my left"
				direction = 'left'
				hypotheticalEndPosition = {"x":myCoord['x']-1,"y":myCoord['y']}
		else:
		#myCoord['x'] - closestFood['x'] <0

			if myCoord['x'] == closestFood['x']:
				print "on the same row x coord"
				#need to fix this - 
				#maybe move up or down depending on 
				#the y coord  compared to
				#current position
				direction = random.choice(['up','down'])
			else:
				print "food is on my right"
				direction = 'right'
				hypotheticalEndPosition = {"x":myCoord['x']+1,"y":myCoord['y']}


	else:
	#distance_y > distance_x

		if myCoord['y'] - closestFood['y'] >0 :
			if myCoord['y'] == closestFood['y']:
				print "on the same column y coord"
				#need to fix this - 
				#maybe move right or left depending on 
				#the x coord  compared to
				#current position
				direction = random.choice(['left','right'])
			else:
				print "food is up"
				direction = 'up'
				hypotheticalEndPosition = {"x":myCoord['x'],"y":myCoord['y']+1}

		else:
		#myCoord['x'] - closestFood['x'] <0
			if myCoord['y'] == closestFood['y']:
				print "on the same column y coord"
				#need to fix this - 
				#maybe move right or left depending on 
				#the x coord  compared to
				#current position
				direction = random.choice(['left','right'])

			else: 
				print "food is down"
				direction = 'down'
				hypotheticalEndPosition = {"x":myCoord['x'],"y":myCoord['y']-1}



	# verify that moving in a direction doesn't kill us
	# if it does, choose another direction (fix this)

	# for now if the hypotheticalEndPosition == myCoord 
	# means that we made a random choice.

	#try to go another way if the direction chosen would kill us
	
	#too far right
	if hypotheticalEndPosition['x'] >= width-1:
		direction = random.choice(['left','up','down'])

	#too far left
	if hypotheticalEndPosition['x'] <= 0 :
		direction = random.choice(['right','up','down'])

	#too far up
	if hypotheticalEndPosition['y'] <= 0:#>= height-1:
		direction = random.choice(['down','left','right'])

	#too far down
	if hypotheticalEndPosition['y'] >= height-1:#<= 0:
		direction = random.choice(['up','left','right'])

			
    
	print(direction)

"""	direction = random.choice(directions)"""



if __name__== "__main__":

  main()

