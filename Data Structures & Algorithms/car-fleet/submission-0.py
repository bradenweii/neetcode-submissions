class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        pos, spd = cars[0]
        fleet_time = (target - pos) / spd
        count = 1
        for i in range(1,len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if time<=fleet_time:
                continue
            else:
                fleet_time = time
                count+=1

      

        return count



        