# tetrahedroninsphere
Imagine four points randomly selected on a surface of a sphere. 
These points form the vertices of an imaginary tetrahedron. 
What is the probability that the tetrahedron contains the center of the sphere? 

Some run results:
redmond$ ./prob.py 
numPointsOnSphere =  10
NumTests =  10000
NumInside =  1104
Probabiliy= 0.1104

redmond$ ./prob.py 
numPointsOnSphere =  20
NumTests =  160000
NumInside =  19152
Probabiliy= 0.1197

redmond$ ./prob.py 
numPointsOnSphere =  30
NumTests =  810000
NumInside =  99216
Probabiliy= 0.122488888889

redmond$ ./prob.py 
numPointsOnSphere =  40
NumTests =  2560000
NumInside =  315912
Probabiliy= 0.123403125

redmond$ ./prob.py 
numPointsOnSphere =  50
NumTests =  6250000
NumInside =  774072
Probabiliy= 0.12385152
