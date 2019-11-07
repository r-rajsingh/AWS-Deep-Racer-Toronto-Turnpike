def reward_function(params):
    import math

    def angle(y2,y1,x2,x1):
        degrees = math.degrees(math.atan2(y2 - y1, x2 - x1))
        degrees = (degrees + 360) % 360
        return degrees

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    width = params['track_width']
    distance_from_center = params['distance_from_center']
    flag = params['is_left_of_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steering = abs(params['steering_angle']) 
    if heading<0:
        heading = 360 + heading

    reward = 1.0
  
    next_point   = waypoints[closest_waypoints[1]]
    prev_point   = waypoints[closest_waypoints[0]]
    target = closest_waypoints[1]
   
    track_direction = angle(next_point[1],prev_point[1],next_point[0],prev_point[0])
    heading_diff = abs(track_direction - heading)


    # 1st
    if target >= 185 and target < 12:
        if distance_from_center <= width/2:
            reward -= 0.4 * (distance_from_center/(width/2))
        else:
            reward -= 0.999

        if steering < 15:
            reward = reward * 1.3 * (1.00 - (steering/100))
        else:
            reward = reward *0.95 * (1.00 - steering/100)
        
        if reward >=0.3:
            if heading_diff < 15:
                reward = reward * 1.2 * (1.00 - (heading_diff/100))
            else:
                reward = reward * 0.95

    # 2nd
    elif target >= 12 and target < 42:
        if flag == True:
            reward -= 0.7
        elif flag == False:
            reward -= 0.1
            if distance_from_center >= width/4 and distance_from_center < width/2:
                reward = reward * (1+  (0.25 * (distance_from_center/(width/2)))) 
            else:
                reward = reward * (1-  (0.20  * (1 - distance_from_center/(width/2)))) 
            if heading_diff < 18:
                reward = reward * 1.22 * (1.00 - (heading_diff/100))
            elif heading_diff < 25:
                reward = reward
            else:
                reward =reward * 0.8
        else:
            reward -= 0.999

    ### 3rd
    elif target >= 42 and target < 60:
        if distance_from_center < width/2:
            reward -= 0.4 * (distance_from_center/(width/2))
        else:
            reward -= 0.999
            
        if steering < 15:
            reward = reward * 1.3 * (1.00 - (steering/100))
        else:
            reward = reward *0.95 * (1.00 - steering/100)

        if reward >=0.3:
            if heading_diff < 15:
                reward = reward * 1.2 * (1.00 - (heading_diff/100))
            else:
                reward = reward * 0.95

    # 4th
    elif target >= 60 and target < 95:
        if distance_from_center < width/2:
            reward -= 0.35 * (distance_from_center/(width/2))
        else:
            reward -= 0.999

        if steering < 15:
            reward = reward * 1.3 * (1.00 - (steering/100))
        else:
            reward = reward * (1.00 - steering/100)

        if heading_diff < 15:
            reward = reward * 1.2 * (1.00 - (heading_diff/100))
        else:
            reward = reward * 0.95


    # 5th
    elif target >= 95 and target < 118:
        if all_wheels_on_track == True:
            reward -= 0.3
        else:
            reward -= 0.999
        
        if all_wheels_on_track == True:
            
            if steering < 12:
                reward = reward * 1.3 * (1.00 - (steering/100))
            elif steering < 18:
                reward = reward * 1.2 * (1.00 - (steering/100))
            else:
                reward = reward *0.95 * (1.00 - steering/100)

            reward = reward + (0.15 * (width/2 - distance_from_center)/(width/2))

    # 6th
    elif target >= 118 and target < 160:
       
        if flag == True:
            reward -= 0.7
        elif flag == False:
            reward -= 0.1
            if distance_from_center >= width/4 and distance_from_center < width/2:
                reward = reward * (1+  (0.30 *(distance_from_center/(width/2)))) 
            else:
                reward = reward * (1-  (0.25 *(1 - distance_from_center/(width/2))))

            if heading_diff < 18:
                reward = reward * 1.22 * (1.00 - (heading_diff/100))
            elif heading_diff < 25:
                reward = reward
            else:
                reward =reward * 0.8
        else:
            reward -= 0.999

    # 7th
    elif target >= 160 and target < 185:    
        if distance_from_center < width/2:
            reward -= 0.35 * (distance_from_center/(width/2))
        else:
            reward -= 0.999

        if steering < 15:
            reward = reward * 1.3 * (1.00 - (steering/100))
        else:
            reward = reward * (1.00 - steering/100)


        if heading_diff < 15:
            reward = reward * 1.2 * (1.00 - (heading_diff/100))
        else:
            reward = reward * 0.95

    return float(reward)