"""
Flatland is a country with a number of cities, some of which have train stations. Cities are 
numbered consecutively and each has a road of 1km length connecting it to the next city. 
It is not a circular route, so the first city doesn't connect with the last city. Determine 
the maximum distance from any city to its nearest train station.

Notes:
- Cities are indexed from 0.
- Number of cities is between 1 and 10000.
- Number of cities with train station is between 1 and number of cities.
- No city has more than one train station.

Example:

number_of_cities == 3
cities_with_train_station == [1]

There are 3 cities and city #1 has a train station. They occur consecutively along a route. 
City #0 is 1km away, city #1 is 0km away and city #2 is 1km away from its nearest train station.
The maximum distance is 1.

"""

from typing import List
import random

class TrainStation:
    def __init__(self,cities):
        self.cities=cities
        self.times=1
        self.changer=5
        self.numbers=[]

    def gen_station(self):
        count=0
        for i in range(self.cities):
            if count>=self.changer:
                self.changer+=5
                self.times+=1

            if count<=self.changer :
                n=[]
                for t in range(self.times):
                    new_number=random.randint(0,i)
                    while new_number in n:
                        new_number=random.randint(0,i)
                    n.append(new_number)
            self.numbers.append(n)
            
            count+=1
            
    def print(self):
        for i in range(len(self.numbers)):
            print(i+1,self.numbers[i])

class Node:
    def __init__(self,data,station):
        self.data=data
        self.next=None
        self.prev=None
        self.station = station

class Route:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def append(self,data,station):
        new_node=Node(data,station)
        # check if the list is empty
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head= new_node
            self.__tail= new_node
        else:
            self.__tail.next=new_node
            new_node.prev=self.__tail
            self.__tail =new_node # new_node is our new tail node

        self.__size+=1


    def traverse_fw(self):
        current_node = self.__head
        count=0
        range=0
        result=0
        while current_node: # while the current node is not None
            if count>=0 :
                if current_node.station ==False:
                    result+=1
                else:
                    if result > range:
                        range=result
                    print('r',result)
                    result=0
                
            current_node=current_node.next
            count+=1
        return range

    def traverse_bw(self):
        current_node = self.__tail
        while current_node:
            current_node=current_node.prev


    def list_size(self):
        return self.__size

def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]) -> int:
    train_station = TrainStation(number_of_cities)
    train_station.gen_station()

    routeList = Route()

    for i in range(number_of_cities):
        if i in cities_with_train_station:
            routeList.append(i,True)
        else:
            routeList.append(i,False)

    fw_result=routeList.traverse_fw()
    return fw_result

if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    )
    print("ALL TESTS PASSED")