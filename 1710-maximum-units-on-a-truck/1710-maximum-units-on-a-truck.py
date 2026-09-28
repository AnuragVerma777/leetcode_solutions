class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0
        for boxes, units in boxTypes:
            take = min(boxes, truckSize)
            total += take * units
            truckSize -= take
            if truckSize == 0:
                break
        return total