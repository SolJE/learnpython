import math 
R = map(lambda x: (int( (math.sqrt( 8 * x + 1 ) + 1) / 2), x),range(0,45)) 
RC = map(lambda x: (x[0], x[1] + 1 - (x[0] - 1) * x[0] / 2), R) 
T = map(lambda x: ("%d*%d=%d"%(x[1],x[0],x[0]*x[1]) + ("\n" if(x[0]==x[1]) else " ")), RC) 
print ("".join(T))