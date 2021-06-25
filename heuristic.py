import math 
import sys 
nodes = 20 
demand = 10 
totalTrucks =  3 
truckCapacity = 75
truckArr = {1:75,2:75,3:75}
totalTruckCapacity= truckCapacity * totalTrucks
depotLocation = [43.8741722,	-79.2587357];
distArr = [
[43.6518936,	-79.3817139],
[45.4204216	,-75.6924286],
[43.2565346,	-79.8744202],
[43.4497871,	-80.4890900],
[42.9842682,	-81.2475357],
[43.8960838	,-78.8651276],
[42.3140793	,-83.0368576],
[44.3893394	,-79.6855240],
[43.5448074	,-80.2481079],
[44.2304764	,-76.4812469],
[45.3303375,	-75.9007416],
[43.5134926	,-79.8828049],
[48.3825111	,-89.2454834],
[46.4590378,	-81.0567856],
[43.1394043	,-80.2636490],
[43.6840210	,-79.7590485],
[43.5912933	,-79.6502533],
[45.0182571	,-74.7285767],
[43.1303864	,-80.7546768],
[43.6471672	,-79.9109955],
]

#add variable to hold the route trucks takes
truckRoute = {1:[],2:[],3:[]}


# d=√((x_2-x_1)²+(y_2-y_1)²)
def calcDist(a,b):  
  return math.sqrt(((b[0] - a[0])** 2 )+ ((b[1] - a[1])** 2))

for truck in truckArr.keys():
  currLocation =depotLocation
  truckRoute[truck].append(-1)
  while truckArr[truck] >= 10 :
    currMin = sys.maxsize;
    minIndexOfCustomer = 0;
    for index, i in enumerate(distArr):
      print(index)
      print(i)
      if(i[0]!=0 and i[1] != 0):
        currDist = calcDist(currLocation, i)
        print(currDist)
        if(currDist<currMin):
          currMin = currDist
          minIndexOfCustomer = index #this not index         
          
          #assign 0,0 to one thats chosen

      # currMin = min(currMin,currDist)

    truckArr[truck] -= 10;
    currLocation= distArr[minIndexOfCustomer]
    distArr[minIndexOfCustomer] = [0,0]
    truckRoute[truck].append(minIndexOfCustomer)
  truckRoute[truck].append(-1)
print(truckRoute)

  
