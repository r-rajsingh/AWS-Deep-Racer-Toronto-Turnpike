def reward_function(params):
    import math

    def angle(y2,y1,x2,x1):
        degrees = math.degrees(math.atan2(y2 - y1, x2 - x1))
        degrees = (degrees + 360) % 360
        return degrees

    width = params['track_width']
    distance_from_center = abs(params['distance_from_center'])
    steering = abs(params['steering_angle']) 
    heading = params['heading']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    flag = params['is_left_of_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    if heading<0:
        heading = 360 + heading
    reward = 1.0
  
    next_point   = waypoints[closest_waypoints[1]]
    prev_point   = waypoints[closest_waypoints[0]]
    target = closest_waypoints[1]
    track_direction = angle(next_point[1],prev_point[1],next_point[0],prev_point[0])
    heading_diff = abs(track_direction - heading)


    # 1st
    if target >= 180 and target < 13:
        if distance_from_center <= width/2:
            if distance_from_center <= width/5:
                reward =1.0
            else:
                reward -= 0.4 * (distance_from_center/(width/2))
        else:
            reward -= 0.999

        if speed < 2.2:
            reward = reward * 0.6
        elif speed < 2.7:
            reward = reward * 0.80
        elif speed < 3.7:
            reward = reward * 1.40
        else :
            reward = reward * 1.60
        
        if reward > 0.002:
            if steering < 15:
                if steering < 7:
                    reward = reward * 1.30
                elif steering < 11:
                    reward = reward * 1.20
                else:
                    reward = reward * 1.25 * (1.00 - (steering/100))
            else:
                reward = reward *0.90 * (1.00 - steering/100)
            
            if reward >=0.3:
                if heading_diff < 20:
                    if heading_diff < 9:
                        reward = reward * 1.22
                    else:
                        reward = reward * 1.15 * (1.00 - (heading_diff/100))
                else:
                    reward = reward * 0.75

    # 2nd
    elif target >= 13 and target < 65:                                                                                                                     
        if flag == True:
            reward -= 0.75
        elif flag == False:
            if distance_from_center >= (width/2)*(13/16) and distance_from_center <= width/2:
                reward = reward * 1.50

            elif distance_from_center >= (width/2)*(7/12) and distance_from_center < (width/2)*(13/16):
                reward = reward * 1.28
            else:
                reward = reward * (1-  (0.30  * (1 - distance_from_center/(width/2)))) 

            if speed < 1.2:
                reward = reward * 0.6
            elif speed < 1.75:
                reward = reward * 0.8
            elif speed < 2.3:
                reward = reward * 1.25
            else :
                reward = reward * 1.40

            if heading_diff <= 15:
                reward = reward + 0.20
            elif heading_diff < 25:
                reward = reward * 1.25 * (1.00 - (heading_diff/100))
            elif heading_diff < 35:
                reward = reward - 0.1
            else:
                reward =reward - 0.2
        else:
            reward -= 0.999
    '''
    ### 3rd
    elif target >= 65 and target < 63:

        if distance_from_center <= width/6:
            reward = 1.2
        elif distance_from_center <= width/2:
            reward -= 0.4 * (distance_from_center/(width/2))
        else:
            reward -= 0.999

        
        if speed < 2:
            reward = reward * 0.6
        elif speed < 3.5:
            reward = reward * 0.8
        else :
            reward = reward * 1.35
            
        if reward > 0.002:    
            if steering < 10:
                reward = reward * 1.25
            elif steering < 14:
                reward = reward * 1.25 * (1.00 - (steering/100))
            else:
                reward = reward *0.98 * (1.00 - steering/100)

            if heading_diff < 14:
                reward = reward + 0.2
            elif heading_diff < 18:
                reward = reward * 1.2 * (1.00 - (heading_diff/100))
            else:
                reward = reward * 0.90
    '''

    # 4th
    elif target >= 65 and target < 93:
        if distance_from_center <= width/3:
            reward = reward * 1.4
        elif distance_from_center <= width/2:
            reward = reward * 1.2
        else:
            reward -= 0.999
       
    
        if speed < 2.0:
            reward = reward * 0.6
        elif speed < 2.8:
            reward = reward * 0.8
        elif speed < 3.40:
            reward = reward * 1.20
        else :
            reward = reward * 1.40

        if reward > 0.002:
            if steering < 10:
                reward = reward + 0.40
            elif steering < 13:
                reward = reward + 0.25
            elif steering < 18:
                reward = reward * 1.20 * (1.00 - (steering/100))
            else:
                reward = reward * (1.00 - steering/100)

            if heading_diff < 15:
                reward = reward + 0.20
            elif heading_diff < 20:
                reward = reward * 1.23 * (1.00 - (heading_diff/100))
            else:
                reward = reward * 0.95
            

    # 5th
    elif target >= 93 and target < 113:
        if all_wheels_on_track == True:
            if steering < 10:
                reward = reward + 0.40
            elif steering < 17:
                reward = reward + 0.25
            elif steering < 23:
                reward = reward + 0.10
            else:
                reward = reward *0.95 * (1.00 - steering/100)
        else:
            reward -= 0.999
        
        if speed < 2.0:
            reward = reward * 0.6
        elif speed < 2.5:
            reward = reward * 0.8
        elif speed < 3.2:
            reward = reward * 1.20
        else :
            reward = reward * 1.35
            
    # 6th
    elif target >= 113 and target < 155:                                                                                                                     
        if flag == True:
            reward -= 0.9
        elif flag == False:
            if distance_from_center >= (width/2)*(13/16) and distance_from_center <= width/2:
                reward = reward * 1.50
            elif distance_from_center >= (width/2)*(7/12) and distance_from_center < (width/2)*(13/16):
                reward = reward * 1.25
            else:
                reward = reward * (1-  (0.30  * (1 - distance_from_center/(width/2)))) 

            if speed < 1.0:
                reward = reward * 0.6
            elif speed < 1.80:
                reward = reward * 0.8
            elif speed < 2.5:
                reward = reward * 1.20
            else :
                reward = reward * 1.40

            if heading_diff <= 12:
                reward = reward + 0.2
            elif heading_diff < 23:
                reward = reward * 1.28 * (1.00 - (heading_diff/100))
            elif heading_diff < 30:
                reward = reward - 0.1
            else:
                reward =reward - 0.2

        else:
            reward -= 0.999

    # 7th
    elif target >= 155 and target < 180:    
       
        if distance_from_center <= width/2:
            if flag == False:
                if distance_from_center > (width/2)*(13/16):
                    reward =reward * 1.5
                elif distance_from_center >= width/4:
                    reward =reward * 1.25
                else:
                    reward = reward *1.1
            else:
                if distance_from_center < width/4:
                    reward = reward - 0.2
                elif distance_from_center <= width/2:
                    reward = reward - 0.35
        else:
            reward -= 0.999

        if speed < 2:
            reward = reward * 0.6
        elif speed < 2.5:
            reward = reward * 0.8
        elif speed < 3.0:
            reward = reward * 1.20
        else :
            reward = reward * 1.40

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