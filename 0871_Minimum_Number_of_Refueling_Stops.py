class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        nstations = len(stations)
        refuel, position = 0, startFuel
        available = []
        for i in range(nstations):
            if position >= target:
                break
            elif position > stations[i][0]:
                heappush(available, -stations[i][1])
            elif position == stations[i][0]:
                heappush(available, -stations[i][1])
                fuel = -heappop(available)
                position += fuel
                refuel += 1
            else:
                while available and position < stations[i][0]:
                    fuel = -heappop(available)
                    position += fuel
                    refuel += 1
                if position >= stations[i][0]:
                    heappush(available, -stations[i][1])
                else:
                    break
        return refuel if position >= target else -1
