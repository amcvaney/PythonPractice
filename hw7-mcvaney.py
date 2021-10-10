#Hw 7 Abi McVaney
#Implementation of a simple polygon


"""
  Problem 1, SCP Part I:
  ----------------------------------------------
Suppose the vertices of the polygon A are:
(1,0), (2,-1), (3,0), (2,1)
This polygon has 4 edges:
  edge 0: (1,0) to (2,-1)
  edge 1: (2,-1) to (3,0)
  edge 2: (3,0) to (2,1)
  edge 3: (2,1) to (1,0)
  
Perimeter = length(edge 0) + length(edge 1) + length(edge 2) + length(edge 3)   length(edge 0) = sqrt((2-1)**2 + (-1-0)**2)=> sqrt(2)
    length(edge 1) = sqrt((3-2)**2 + (0-(-1))**2) => sqrt(2)
    length(edge 2) = sqrt((2-3)**2 + (1-0)**2) => sqrt(2)
    length(edge 3) = sqrt((1-2)**2 + (0-1)**2) =>sqrt(2)
    
    perimeter is 4*sqrt(2)

  
  Problem 1, SCP Part II:
  ----------------------------------------------
Suppose that the polygon has vertices
(x[0], y[0]), (x[1], y[1]), ..., (x[n-1],y[n-1]).
Then the perimeter is given by:
perimeter = length(edge 0) + length(edge 1) + ...+ length(edge n-1)
  where  the length of edge i is 
  length(edge i) = sqrt((x[i+1] - x[i])**2 + (y[i+1]-y[i])**2)
    for i = 0,1,...,n-2
  and
  length(edge n-1) = sqrt((x[n-1] - x[0])**2 + (y[n-1] - y[0])**2)
  

  Problem 1, SCP Part III:
  ----------------------------------------------
Consider the polygon with vertices (0,0), (2,0), (2,2), (0,2)
  x[0]= 0, y[0]= 0
  x[1]= 2, y[1]= 0
  x[2]= 2, y[2]= 2
  x[3]= 0, y[3]= 2

using the process above, 
  length(edge 0)= sqrt((x[1] - x[0])**2 + (y[1] -y[0])**2)
                = sqrt(4 +0) = 2 

"""

class Polygon:
    ###########################################################
    def __init__(self):
        # Initialize a Polygon object.
        self.x = [] # self.x[i] is the x-coordinate of vertex 'i'.
        self.y = [] # self.y[i] is the y-coordinate of vertex 'i'.

    ###########################################################
    def set_vertices(self, coordinates):
        # Set the vertices for this Polygon object.
        # 'coordinates' is a list of floats, interpretted as follows:
        # coordinates[0] is the x-coordinate of vertex 1,
        # coordinates[1] is the y-coordinate of vertex 1,
        # coordinates[2] is the x-coordinate of vertex 2,
        # coordinates[3] is the y-coordinate of vertex 2,
        # and so on.
        # The polygon has sides connecting:
        # vertex 0 and vertex 1,
        # vertex 1 and vertex 2,
        # ...
        # vertex (n-2) and vertex (n-1)
        # vertex (n-1) and vertex 0.
        n = len(coordinates)
        if n%2 != 0:
            print("set_vertices(): Error! 'coordinates' must"+
                  "contain an even number of elements!")
            return False
        self.x = [coordinates[2*i] for i in range(n//2)]
        self.y = [coordinates[2*i+1] for i in range(n//2)]
        return True

    ##########################################################
    def num_vertices(self):
        # Return the number of vertices in this Polygon object.
        return len(self.x)

    ###########################################################
    def get_string(self):
        # Return a string representation of this Polygon object.
        # It will be a list of of the vertices, in order.
        n = self.num_vertices()
        result = "" # Start with empty string, and append each vertex to it.
        for i in range(n):
            result += "({0}, {1})".format(self.x[i], self.y[i])
            if i<n-1:
                result += ", "
        return result

    ############################################################
    def perimeter(self):
      p = 0   #initialize perimeter to zero
     
      n = self.num_vertices()
  
      for i in range(0,n):
         p+= ((self.x[(i+1)%n] - self.x[i])**2  + (self.y[(i+1)%n] - self.y[i])**2 )**(1/2)
      return p  
  
    

    ############################################################
    def area(self):
      a=0
  #iterate over the coordinates of vertices and apply the formula given in question
  #we find the area of polygon
      for i in range(len(self.x)-1):
          a+=self.x[i]*self.y[i+1] - self.x[i+1]*self.y[i]
      return abs(a/2)   #according to formula



############################################
# Do NOT change anything below here!!!!!!! #
############################################

P = Polygon() # Create a Polygon object, P.

# This next line sets 'P' to be the polygon
# whose vertices are (1,0),(2,-1),(3,0),(2,1).
# You should be able to work out by hand what the perimeter
# and area of this polygon are, so I suggest using this as
# one of your examples.
P.set_vertices([1,0, 2,-1, 3,0, 2,1])

# Print out some information about the Polygon P.
print("P has vertices : "+P.get_string())
p = P.perimeter()
print("Its perimeter is {0}".format(p))
a = P.area()
print("Its area is {0}".format(a))
