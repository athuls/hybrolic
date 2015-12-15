import math, random

# Function which calculates the euclidean distance between two points
def euclideanDistance(v1, v2):
    # use Zip to iterate over the two vectors
    sum =0.0
    for coord1,coord2 in zip(v1,v2):
        sum += pow((coord1-coord2), 2)
    
    return math.sqrt(sum)

# Function that evaluates the total length of a path
def tourCost(perm):
    # Here tour cost refers to the sum of the euclidean distance between consecutive points starting from first element
    totalDistance =0.0
    size = len(perm)
    for index in range(size):
        # select the consecutive point for calculating the segment length
        if index == size-1 : 
            # This is because in order to complete the 'tour' we need to reach the starting point
            point2 = perm[0] 
        else: # select the next point
            point2 = perm[index+1]
            
        totalDistance +=  euclideanDistance(perm[index], point2)
    
    return totalDistance    

'''We could just return n+1 and n-1 for the input n, which is perm here'''
def stochasticTwoOptWithEdges(perm):
    result = perm[:] # make a copy
    size = len(result)
    # select indices of two random points in the tour
    p1, p2 = random.randrange(0,size), random.randrange(0,size)
    # do this so as not to overshoot tour boundaries
    exclude = set([p1])
    if p1 == 0:
        exclude.add(size-1)
    else:
        exclude.add(p1-1)
    
    if p1 == size-1:
        exclude.add(0)
    else:
        exclude.add(p1+1) 
                       
    while p2 in exclude:
        p2 = random.randrange(0,size)

    # to ensure we always have p1<p2        
    if p2<p1:
        p1, p2 = p2, p1
     
    # now reverse the tour segment between p1 and p2   
    result[p1:p2] = reversed(result[p1:p2])
    
    return result, [[perm[p1-1],perm[p1]],[perm[p2-1],perm[p2]]]

# Function that generates initial solution by picking random value of n
def constructInitialSolution(initPerm):
    initSolution = random.randrange(initPerm[0],initPerm[1])
    return initSolution