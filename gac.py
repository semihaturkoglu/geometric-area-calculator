def clockwise(L):
    total_x = 0
    total_y = 0
    
    for i in range(len(L)):
        L[i] = list(L[i])

    for i in range(len(L)):
        total_x += L[i][0]
        total_y += L[i][1]
    mean_x = total_x/len(L)
    mean_y = total_y/len(L)

    mean_point = [mean_x,mean_y]

    for i in range(len(L)):
        L[i][0] = L[i][0] - mean_point[0]
        L[i][1] = L[i][1] - mean_point[1]

    def find_angle(L):
        from math import atan2
        from math import pi
        for i in range(len(L)):
            tan = atan2(L[i][1],L[i][0])
            if tan < 0:
                tan = tan + 2*pi
            L[i].append(tan)
        return L

    def sort_points(L):
        for i in range(len(L)):
            for j in range(len(L)-1):
                if L[j][2] > L[j+1][2]:
                    L[j], L[j+1] = L[j+1], L[j]
                if L[j][2] == L[j+1][2]:
                    from math import sqrt
                    d1 = sqrt((L[j][0]-mean_x)**2 + (L[j][1]-mean_y)**2)
                    d2 =sqrt((L[j+1][0]-mean_x)**2 + (L[j+1][1]-mean_y)**2)
                    if d1 > d2:
                        L[j], L[j+1] = L[j+1], L[j]
                    else:
                        continue

        return L

    def sorted_points_without_angle(L):
        for i in range(len(L)):
            L[i].pop(2)

        return L

    L_withangle = find_angle(L)
    sorted_L_with_angle = sort_points(L_withangle)
    sorted_L = sorted_points_without_angle(sorted_L_with_angle)


    for i in range(len(sorted_L)):
        sorted_L[i][0] += mean_x
        sorted_L[i][1] += mean_y

    return sorted_L




def area_(L):
    L = clockwise(L)
    L.append(L[0])
    sum1 = 0
    for i in range(0,len(L)-1):
            sum1 += L[i][0] * L[i+1][1]
    sum2 = 0
    for i in range(0,len(L)-1):
        sum2 += L[i][1] * L[i+1][0]   
    area_of_poly = (abs(sum1-sum2))/2
    
    return area_of_poly


def inside_points_of_triangle_inquad(Q,T):
    
    x1,y1 = Q[0]
    x2,y2 = Q[1]
    x3,y3 = Q[2]
    x4,y4 = Q[3]
    
    inside_points = []
    
    for i in range(3):
        count = 0
        xt,yt = T[i]
        
        if (yt<y1) != (yt<y2) and xt < (x1 + ((yt-y1)/(y2-y1)) * (x2-x1)):
            count +=1
        if (yt<y2) != (yt<y3) and xt < (x2 + ((yt-y2)/(y3-y2)) * (x3-x2)):
            count +=1
        if (yt<y3) != (yt<y4) and xt < (x3 + ((yt-y3)/(y4-y3)) * (x4-x3)):
            count += 1
        if (yt<y1) != (yt<y4) and xt < x1 + ((yt-y1)/(y4-y1) * (x4-x1)):
            count +=1
        
        if count % 2 != 0:
            inside_points.append((xt,yt))
            
    if len(inside_points) != 0:
        return inside_points
    
    else:
        return False



    
    
def inside_points_of_quad_intri(Q,T):
    
    x1,y1 = T[0]
    x2,y2 = T[1]
    x3,y3 = T[2]
    
    inside_points = []
    
    for i in range(4):
        count = 0
        xq,yq = Q[i]
        
        if (yq<y1) != (yq<y2) and xq < x1 + ((yq-y1)/(y2-y1)) * (x2-x1):
            count +=1
        if (yq<y2) != (yq<y3) and xq < x2 + ((yq-y2)/(y3-y2)) * (x3-x2):
            count +=1
        if (yq<y1) != (yq<y3) and xq < x1 + ((yq-y1)/(y3-y1)) * (x3-x1):
            count += 1
            
        if count %2 != 0:
            inside_points.append((xq,yq))
            
    if len(inside_points) != 0:
        return inside_points
    else:
        return False

    
    
def finding_points(l1,l2):
    def slope(l):
        if l[1][0]-l[0][0] != 0:
            m = (l[1][1] - l[0][1])/(l[1][0]-l[0][0])
            return m
        else:
            return "boom"
    if slope(l1)== "boom" and slope(l2) == "boom":
        return False
    elif slope(l1)!= "boom" and slope(l2) != "boom":
        
        
        error= 1e-6
        if abs(slope(l1)- slope(l2)) < error:
            return False
    
    if slope(l1)== 0 and slope(l2) == 0:
        return False
#PARALELLİK 
    if slope(l1) != "boom" and slope(l2) != "boom":
        x = ((l2[0][1] - slope(l2)*l2[0][0]) + (-1)*(l1[0][1] - slope(l1)*l1[0][0]))/(-slope(l2) + slope(l1))
        y = (l1[0][1] - slope(l1)*l1[0][0]) + slope(l1)*x
    
        x_of_l1 = [l1[0][0],l1[1][0]]
        y_of_l1 = [l1[0][1],l1[1][1]]

        x_of_l2 = [l2[0][0],l2[1][0]]
        y_of_l2 = [l2[0][1],l2[1][1]]
        if min(x_of_l1) <= x <= max(x_of_l1) and min(x_of_l2) <= x <= max(x_of_l2):
            if min(y_of_l1) <= y <= max(y_of_l1) and min(y_of_l2) <= y <= max(y_of_l2):
                return (x,y)
            
    elif slope(l1) != "boom" and slope(l2) == "boom":
        x = l2[0][0]
        y = (l1[0][1] - slope(l1)*l1[0][0]) + slope(l1)*x
        
        x_of_l1 = [l1[0][0],l1[1][0]]
        y_of_l1 = [l1[0][1],l1[1][1]]

        x_of_l2 = [l2[0][0],l2[1][0]]
        y_of_l2 = [l2[0][1],l2[1][1]]
        if min(x_of_l1) <= x <= max(x_of_l1) and min(x_of_l2) <= x <= max(x_of_l2):
            if min(y_of_l1) <= y <= max(y_of_l1) and min(y_of_l2) <= y <= max(y_of_l2):
                return (x,y)
        
    elif slope(l1) == "boom" and slope(l2) != "boom":
        x = l1[0][0]
        y = (l2[0][1] - slope(l2)*l2[0][0]) + slope(l2)*x
        x_of_l1 = [l1[0][0],l1[1][0]]
        y_of_l1 = [l1[0][1],l1[1][1]]

        x_of_l2 = [l2[0][0],l2[1][0]]
        y_of_l2 = [l2[0][1],l2[1][1]]
        if min(x_of_l1) <= x <= max(x_of_l1) and min(x_of_l2) <= x <= max(x_of_l2):
            if min(y_of_l1) <= y <= max(y_of_l1) and min(y_of_l2) <= y <= max(y_of_l2):
                return (x,y)
    
    return False



def area(Q,T):
    
    
    if type(inside_points_of_quad_intri(Q,T)) != bool and len(inside_points_of_quad_intri(Q,T)) == 4:
        return area_(Q)
    if type(inside_points_of_triangle_inquad(Q,T)) != bool and len(inside_points_of_triangle_inquad(Q,T)) == 3:
        return area_(T)
    
 
    
    in_points = inside_points_of_quad_intri(Q,T)
    in_points2 = inside_points_of_triangle_inquad(Q,T)
    last_list = []
    
    intersection_points = []
    
    for i in range(3):
        for j in range(2):
            x = finding_points([Q[i],Q[i+1]], [T[j],T[j+1]])
            if x != False:
                intersection_points.append(x)
            
    for i in range(2):
        a = finding_points([Q[3],Q[0]], [T[i],T[i+1]])
        if a != False:
            intersection_points.append(a)
            
    for i in range(3):
        b = finding_points([Q[i],Q[i+1]], [T[2],T[0]])
        if b != False:
            intersection_points.append(b)
        
    c = finding_points([Q[0],Q[3]], [T[0],T[2]])
    if c!= False:
        intersection_points.append(c)
        
    if in_points != False and in_points2 == False:
        last_list = in_points+ intersection_points
    
    elif in_points == False and in_points2 != False:
        last_list = in_points2 + intersection_points
        
    elif in_points != False and in_points2 != False:
        last_list = in_points + in_points2 + intersection_points
        
    else:
        last_list = intersection_points
    if not (inside_points_of_triangle_inquad(Q,T)) and not (inside_points_of_quad_intri(Q,T)) and len(last_list)==0:
        return 0
    return area_(last_list)

