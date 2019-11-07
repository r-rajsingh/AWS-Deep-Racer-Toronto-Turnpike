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

    print('Position - ',closest_waypoints[1])
    print('Distance from center - ',distance_from_center)
    print('Speed - ',speed)
    print('Width - ',width)
    print('All wheels on track - ',all_wheels_on_track)
    print('Is left of center - ',flag)
    print('Steering - ',steering)
    print('Heading - ',heading)
    print('Heading difference - ',heading_diff)
    

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
            reward = reward - 0.40
        elif speed <= 3.0:
            reward = reward - ((3.0 - speed)/2)
        elif speed < 3.70:
            reward = reward + 0.40
        else:
            reward = reward + 0.55
        

        if reward > 0.002:
            if steering <= 9.10:
                reward = reward + 0.35
            elif steering <= 16.10:
                reward = reward + 0.10
            else:
                reward = reward - (steering/43)
            
            if reward >=0.3:
                if heading_diff < 20:
                    if heading_diff < 9:
                        reward = reward + 0.27
                    else:
                        reward = reward * 1.15 * (1.00 - (heading_diff/100))
                else:
                    reward = reward - 0.35

    # 2nd
    elif target >= 13 and target < 60:                                                                                                                     
        if flag == True:
            reward -= 0.80
        elif flag == False:
            if distance_from_center >= (width/2)*(13/16) and distance_from_center <= width/2:
                reward = reward * 1.50

            elif distance_from_center >= (width/2)*(7/12) and distance_from_center < (width/2)*(13/16):
                reward = reward * 1.30
            else:
                reward = reward * (1-  (0.20  * (1 - distance_from_center/(width/2)))) 

            if target >= 13 and target < 33: 
                if speed < 1.3:
                    reward = reward - 0.50
                elif speed <= 1.90:
                     reward = reward - ((1.90 - speed)/2)
                elif speed < 2.30:
                    reward = reward + 0.45
                else:
                    reward = reward + 0.65

            else:
                if speed < 1.0:
                    reward = reward - 0.50
                elif speed <= 1.70:
                    reward = reward - ((1.70 - speed)/2)
                elif speed < 2.10:
                    reward = reward + 0.50
                else :
                    reward = reward + 0.65


            if heading_diff <= 13:
                reward = reward + 0.30
            elif heading_diff < 25:
                reward = reward * 1.30 * (1.00 - (heading_diff/100))
            elif heading_diff < 35:
                reward = reward - 0.35
            else:
                reward =reward - 0.50
        else:
            reward -= 0.999
    
    # 4th first
    elif target >= 60 and target < 83:
        if distance_from_center <= width/3:
            reward = reward * 1.35
        elif distance_from_center <= width/2:
            reward = reward * 1.25
        else:
            reward -= 0.999
       
        if speed < 1.50:
            reward = reward - 0.50
        elif speed <= 2.30:
            reward = reward - ((2.30 - speed)/2)
        elif speed < 3.00:
            reward = reward + 0.45
        else :
            reward = reward + 0.70

        if reward > 0.002:
            if steering <= 8.10:
                reward = reward + 0.50
            elif steering <= 16.10:
                reward = reward + 0.30
            elif steering < 21:
                reward = reward * 1.10 * (1.00 - (steering/80))
            else:
                reward = reward * (1.00 - steering/70)

            if heading_diff < 18:
                reward = reward + 0.15
            elif heading_diff < 22:
                reward = reward * 1.23 * (1.00 - (heading_diff/100))
            else:
                reward = reward * 0.90

    # 4th second
    elif target >= 83 and target < 93:
        if all_wheels_on_track == True:
            if distance_from_center <= width/6:
                reward = reward * 1.40
            elif distance_from_center <= width/4:
                reward = reward * 1.30
            else:
                reward = reward - 0.20

            if steering <= 8.10:
                reward = reward + 0.40
            elif steering <= 16.10:
                reward = reward + 0.25
            elif steering <= 20:
                reward = reward + 0.10
            else:
                reward = reward * (1.00 - steering/80)
        else:
            reward -= 0.999

        if speed < 2.0:
            reward = reward - 0.50
        elif speed <= 2.6:
            reward = reward - ((2.60 - speed)/2)
        elif speed < 3.00:
            reward = reward + 0.50
        else:
            reward = reward + 0.80

        if reward > 0.002:
            if heading_diff < 20:
                reward = reward + 0.15
            elif heading_diff < 25:
                reward = reward * 1.23 * (1.00 - (heading_diff/100))
            else:
                reward = reward * 0.95
            
    # 5th
    elif target >= 93 and target < 117:
        
        if all_wheels_on_track == True:
            if steering <= 8.10:
                reward = reward + 0.60
            elif steering <= 16.10:
                reward = reward + 0.30
            elif steering < 21:
                reward = reward * 1.10 * (1.00 - (steering/80))
            else:
                reward = reward * (1.00 - steering/70)
        else:
            reward -= 0.999
        
        if speed < 2.0:
            reward = reward - 0.50
        elif speed <= 2.8:
            reward = reward - ((2.80 - speed)/2)
        elif speed < 3.4:
            reward = reward + 0.50
        else :
            reward = reward + 0.80
            
    # 6th
    elif target >= 117 and target < 152:                                                                                                                     
        if flag == True:
            reward -= 0.6
        elif flag == False:
            if distance_from_center >= (width/2)*(13/16) and distance_from_center <= width/2:
                reward = reward * 1.70
            elif distance_from_center >= (width/2)*(7/12) and distance_from_center < (width/2)*(13/16):
                reward = reward * 1.45
            else:
                reward = reward * (1-  (0.30  * (1 - distance_from_center/(width/2)))) 

            if target >= 117 and target < 140: 
                if speed < 1.2:
                    reward = reward - 0.5
                elif speed <= 1.80:
                    reward = reward - ((1.80 - speed)/2)
                elif speed < 2.3:
                    reward = reward + 0.50
                else :
                    reward = reward + 0.80
            else:
                if speed < 0.8:
                    reward = reward - 0.4
                elif speed < 1.50:
                    reward = reward - ((1.50 - speed)/2)
                elif speed < 2.0:
                    reward = reward + 0.50
                else :
                    reward = reward + 0.70

            if heading_diff <= 12:
                reward = reward + 0.15
            elif heading_diff < 23:
                reward = reward * 1.28 * (1.00 - (heading_diff/100))
            elif heading_diff < 30:
                reward = reward - 0.1
            else:
                reward =reward - 0.2
        else:
            reward -= 0.999

    # 7th
    elif target >= 152 and target < 180:    
       
        if distance_from_center <= width/2:
            if flag == False:
                if distance_from_center > (width/2)*(13/16):
                    reward =reward * 1.5
                elif distance_from_center >= width/4:
                    reward =reward * 1.30
                else:
                    reward = reward *1.1
            else:
                if distance_from_center < width/4:
                    reward = reward - 0.2
                elif distance_from_center <= width/2:
                    reward = reward - 0.35
        else:
            reward -= 0.999

        if speed < 1.80:
            reward = reward - 0.6
        elif speed <= 2.30:
            reward = reward - ((2.30 - speed)/2)
        elif speed < 3.10:
            reward = reward + 0.40  
        else :
            reward = reward + 0.70

        if reward > 0.002:
            if steering <= 8.10:
                reward = reward + 0.40
            elif steering <= 16.10:
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