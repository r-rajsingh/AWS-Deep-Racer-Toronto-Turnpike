def reward_function(params):
    import math

    def angle(y2,y1,x2,x1):
        degrees = math.degrees(math.atan2(y2 - y1, x2 - x1))
        degrees = (degrees + 360) % 360
        return degrees

    
   
    width = params['track_width']
    distance_from_center = abs(params['distance_from_center'])
    flag = params['is_left_of_center']
    all_wheels_on_track = params['all_wheels_on_track']
    steering = abs(params['steering_angle']) 
    heading = params['heading']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    if heading<0:
        heading = 360 + heading

    reward = 1.0
  
    next_point   = waypoints[closest_waypoints[1]]
    prev_point   = waypoints[closest_waypoints[0]]
    target = closest_waypoints[1]
   
    track_direction = angle(next_point[1],prev_point[1],next_point[0],prev_point[0])
    heading_diff = abs(track_direction - heading)


    # 1st
    if target >= 185 and target < 15:
        if distance_from_center <= width/2:
            if distance_from_center <= width/6:
                reward =1
            else:
                reward -= 0.4 * (distance_from_center/(width/2))
        else:
            reward -= 0.999

        if reward > 0.002:
            if steering < 15:
                if steering < 10:
                    reward = reward * 1.25
                else:
                    reward = reward * 1.3 * (1.00 - (steering/100))
            else:
                reward = reward *0.98 * (1.00 - steering/100)
            
            if reward >=0.3:
                if heading_diff < 14:
                    if heading_diff < 9:
                        reward = reward * 1.3
                    else:
                        reward = reward * 1.2 * (1.00 - (heading_diff/100))
                else:
                    reward = reward * 0.90


    # 2nd
    elif target >= 15 and target < 46:                                                                                                                     
        if flag == True:
            reward -= 0.9
        elif flag == False:
            if distance_from_center >= width/3 and distance_from_center <= width/2:
                reward = reward * 1.25
            else:
                reward = reward * (1-  (0.30  * (1 - distance_from_center/(width/2)))) 

            if heading_diff <= 15:
                reward = reward + 0.1
            elif heading_diff < 25:
                reward = reward * 1.28 * (1.00 - (heading_diff/100))
            elif heading_diff < 35:
                reward = reward - 0.08
            else:
                reward =reward - 0.2
        else:
            reward -= 0.999


    ### 3rd
    elif target >= 46 and target < 63:

        if distance_from_center <= width/8:
            reward = 1.2
        elif distance_from_center <= width/2:
            reward -= 0.4 * (distance_from_center/(width/2))
        else:
            reward -= 0.999
        if reward > 0.002:    
            if steering < 10:
                reward = reward * 1.25
            elif steering < 14:
                reward = reward * 1.25 * (1.00 - (steering/100))
            else:
                reward = reward *0.98 * (1.00 - steering/100)

            if heading_diff < 10:
                reward = reward + 0.2
            elif heading_diff < 15:
                reward = reward * 1.2 * (1.00 - (heading_diff/100))
            else:
                reward = reward * 0.90

    # 4th
    elif target >= 63 and target < 95:
        if distance_from_center < width/3:
            reward = reward + 0.2
        elif distance_from_center < width/2:
            reward -= 0.30 * (distance_from_center/(width/2))
        else:
            reward -= 0.999

        if reward > 0.002:
            if steering < 10:
                reward = reward + 0.25
            elif steering < 20:
                reward = reward * 1.35 * (1.00 - (steering/100))
            else:
                reward = reward * (1.00 - steering/100)

            if heading_diff < 10:
                reward = reward + 0.10
            elif heading_diff < 20:
                reward = reward * 1.23 * (1.00 - (heading_diff/100))
            else:
                reward = reward * 0.95


    # 5th
    elif target >= 95 and target < 118:
        if all_wheels_on_track == True:
            reward = 1.0
            if steering < 13:
                reward = reward + 0.3
            elif steering < 18:
                reward = reward + 0.18
            else:
                reward = reward *0.95 * (1.00 - steering/100)

            reward = reward + (0.15 * (width/2 - distance_from_center)/(width/2))
        else:
            reward -= 0.999
        
            
            

    # 6th
    elif target >= 118 and target < 158:                                                                                                                     
        if flag == True:
            reward -= 0.9
        elif flag == False:
            if distance_from_center >= width/3 and distance_from_center <= width/2:
                reward = reward * 1.30
            else:
                reward = reward * (1-  (0.30  * (1 - distance_from_center/(width/2)))) 


            if heading_diff <= 15:
                reward = reward + 0.1
            elif heading_diff < 25:
                reward = reward * 1.28 * (1.00 - (heading_diff/100))
            elif heading_diff < 35:
                reward = reward - 0.08
            else:
                reward =reward - 0.2

            
        else:
            reward -= 0.999

    # 7th
    elif target >= 158 and target < 185:    
        if distance_from_center < width/3:
            reward = reward + 0.2
        elif distance_from_center < width/2:
            reward -= 0.30 * (distance_from_center/(width/2))
        else:
            reward -= 0.999

        if reward > 0.002:
            if steering < 10:
                reward = reward + 0.2
            elif steering < 15:
                reward = reward * 1.3 * (1.00 - (steering/100))
            else:
                reward = reward * (1.00 - steering/100)

            if heading_diff < 20:
                reward = reward + 0.15
            elif heading_diff < 25:
                reward = reward + 0.05
            else:
                reward = reward * 0.95

    return float(reward)