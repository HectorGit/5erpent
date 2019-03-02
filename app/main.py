import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#00FF00"

    return start_response(color)


@bottle.post('/move')
def move():
    data = bottle.request.json

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))

    #directions = ['up', 'down', 'left', 'right']

    #direction = random.choice(directions)

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
    distance_x = abs(myCoord['x']-closestFood['x'])

    print("distance x: %d",distance_x)

    distance_y = abs(myCoord['y']-closestFood['y'])

    print("distance y: %d",distance_y)


    #how to determine whether moving up or down?
    #use the coordinates of the food we are chasing.

    #careful here
    #just initiating it as the same coordinates
    hypotheticalEndPosition = myCoord


    #direction ='right'

    if distance_x > distance_y:
        
        if myCoord['x'] - closestFood['x'] >= 0 :

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
        else:#if myCoord['x'] - closestFood['x'] < 0:

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


    elif distance_y > distance_x:

        if myCoord['y'] - closestFood['y'] >= 0 :
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

        else:#if myCoord['x'] - closestFood['x'] < 0 :
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

            
    

    return move_response(direction)


@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
