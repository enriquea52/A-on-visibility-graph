import numpy as np
import math

def wrap_angle(angle):
    """ Wraps angle between -pi and pi 

    @type  angle: float or numpy array
    @param angle: angle in radinas

    @rtype:   float or numpy array
    @return:  angle in radinas between -Pi to Pi
    """
    if isinstance(angle, float) or isinstance(angle, int):
        return (angle + ( 2.0 * np.pi * np.floor( ( np.pi - angle ) / ( 2.0 * np.pi ) ) ) )
    elif isinstance(angle, np.ndarray):
        return (angle + np.pi) % (2 * np.pi ) - np.pi 
    elif isinstance(angle, list):
        ret = []
        for i in angle:
            ret.append(wrap_angle(i))
        return ret
    else:
        raise NameError('wrap_angle')

        
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.alph = 0

    def alpha(self, x):
        self.alph = x
    
    def dist(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    
    def numpy(self):
        return np.array([self.x, self.y])
        
    def dist_line(self, l):
        return np.linalg.norm(np.cross(l.p2.numpy() - l.p1.numpy(), l.p1.numpy() - self.numpy())) / np.linalg.norm(l.p2.numpy() - l.p1.numpy())

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y,self.alph)

    def dot(self, p):
        return self.x * p.x + self.y*p.y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def vector(self, p):
        return Point(p.x - self.x, p.y - self.y)

    def unit(self):
        mag = self.length()
        return Point(self.x/mag, self.y/mag)

    def scale(self, sc):
        return Point(self.x * sc, self.y * sc)

    def add(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __truediv__(self, s):
        return Point(self.x / s, self.y / s)
    
    def __floordiv__(self, s):
        return Point(int(self.x / s), int(self.y / s))
    
    def __mul__(self, s):
        return Point(self.x * s, self.y * s)
    
    def __rmul__(self, s):
        return self.__mul__(s)
        
    def dist_segment(self, s):
        line_vec = s.p1.vector(s.p2)
        pnt_vec = s.p1.vector(self)
        line_len = line_vec.length()
        line_unitvec = line_vec.unit()
        pnt_vec_scaled = pnt_vec.scale(1.0/line_len)
        t = line_unitvec.dot(pnt_vec_scaled)    
        if t < 0.0:
            t = 0.0
        elif t > 1.0:
            t = 1.0
        nearest = line_vec.scale(t)
        dist = nearest.dist(pnt_vec)
        nearest = nearest.add(s.p1)
        return dist
    
    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y,self.alph)

def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) >= (B.y - A.y) * (C.x - A.x)

def det(a, b):
    return a[0] * b[1] - a[1] * b[0]

class Segment:
    def __init__(self, p1=Point(), p2=Point()):
        self.p1 = p1
        self.p2 = p2
        self.distance = 0

    @classmethod
    def point_angle_length(cls, p1=Point(), angle=0, length=1):
        x2 = p1.x + math.cos(angle) * length
        y2 = p1.y + math.sin(angle) * length
        return cls(p1, Point(x2, y2))
        
    # Return true if line segments AB and CD intersect
    def intersect(self, s):
        if ccw(self.p1, s.p1, s.p2) != ccw(self.p2, s.p1, s.p2) and ccw(self.p1, self.p2, s.p1) != ccw(self.p1, self.p2, s.p2):
            return True, self.intersection_point(s)
        else:
            return False, None

    def intersection_point(self, line):
        xdiff = (self.p1.x - self.p2.x, line.p1.x - line.p2.x)
        ydiff = (self.p1.y - self.p2.y, line.p1.y - line.p2.y)

        div = det(xdiff, ydiff)
        if div == 0:
            #print("Something went wrong!")
            return None

        d = (det((self.p1.x, self.p1.y), (self.p2.x, self.p2.y)), det((line.p1.x, line.p1.y), (line.p2.x, line.p2.y)))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return Point(x, y)

    def dis(self, x):
        self.distance = x

    def magnitude(self):

        return math.sqrt(((self.p2.x-self.p1.x)**2)+(self.p2.y-self.p1.y)**2)

    def angle(self):

        return abs(math.atan2((self.p2.x-self.p1.x),(self.p2.y-self.p1.y)))

    
    def __str__(self):
        return "[{}, {}]".format(self.p1, self.p2)
