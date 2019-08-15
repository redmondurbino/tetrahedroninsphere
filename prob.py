#!/usr/bin/env python
import os
import sys
import argparse
import string
import warnings
import shutil

import math, random
import numpy as np

#from jodl gayatin
#Imagine four points randomly selected on a surface of a sphere. These points form the vertices of an imaginary tetrahedron. What is the probability that the tetrahedron contains the center of the sphere? Imagine four points randomly selected on a surface of a sphere. These points form the vertices of an imaginary tetrahedron. What is the probability that the tetrahedron contains the center of the sphere? 

#from https://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere


def fibonacci_sphere(samples=1,randomize=True):
    rnd = 1.
    if randomize:
        rnd = random.random() * samples

    points = []
    offset = 2./samples
    increment = math.pi * (3. - math.sqrt(5.));

    for i in range(samples):
        y = ((i * offset) - 1) + (offset / 2);
        r = math.sqrt(1 - pow(y,2))

        phi = ((i + rnd) % samples) * increment

        x = math.cos(phi) * r
        z = math.sin(phi) * r

        points.append(np.array([x,y,z]))

    return points



#from https://stackoverflow.com/questions/25179693/how-to-check-whether-the-point-is-in-the-tetrahedron-or-not
def sameside(v1,v2,v3,v4,p):
    normal = np.cross(v2-v1, v3-v1)
    result =  np.dot(normal, v4-v1) * np.dot(normal, p-v1) > 0
    return result



def tetraCoord(A,B,C,D):
    v1 = B-A ; v2 = C-A ; v3 = D-A
    # mat defines an affine transform from the tetrahedron to the orthogonal system
    mat = np.concatenate((np.array((v1,v2,v3,A)).T, np.array([[0,0,0,1]])))
    # The inverse matrix does the opposite (from orthogonal to tetrahedron)
    M1 = np.linalg.inv(mat)
    return(M1)

def pointInsideT(v1,v2,v3,v4,p):
    # Find the transform matrix from orthogonal to tetrahedron system
    try:
        M1=tetraCoord(v1,v2,v3,v4)
        # apply the transform to P
        p1 = np.append(p,1)
        newp = M1.dot(p1)
        # perform test
        return(np.all(newp>=0) and np.all(newp <=1) and sameside(v2,v3,v4,v1,p))
    except np.linalg.linalg.LinAlgError:
        return False
    

def parseArgs():
    """ Simply parse the arguments """
    parser = argparse.ArgumentParser(description = 'Check if apk size is out of cellular download limit.')
    args = parser.parse_args()
    return args

def main():
    # parse arguments
    args = parseArgs()
    #checkAndroidApkSize(args)
    numPointsOnSphere = 50
    points = fibonacci_sphere(numPointsOnSphere, False)
    numInside = 0;
    numTests = 0;
    origin = np.array([0,0,0])
    for p1 in points:
        for p2 in points:
            for p3 in points:
                for p4 in points:
                    numTests += 1
                    if pointInsideT( p1, p2, p3, p4, origin):
                        numInside += 1;
                        
    print "numPointsOnSphere = ", numPointsOnSphere
    print "NumTests = ", numTests
    print "NumInside = ", numInside
    print "Probabiliy=", float(numInside) / float(numTests)

if __name__ == "__main__":
    main()