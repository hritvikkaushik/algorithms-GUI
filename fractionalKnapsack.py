class Item:
    def __init__(self,wt,val,index):
        self.wt = wt
        self.val = val
        self.index = index
        self.cost = val//wt
    
def getMaxValue(wt,val,capacity):
    iVal = []
    for i in range(len(wt)):
        iVal.append(Item(wt[i],val[i],i))
    iVal.sort(key = lambda x: x.val/x.wt, reverse = True)
    totalValue = 0
    for i in iVal:
        curWt = int(i.wt)
        curVal = int(i.val)
        if(capacity - curWt >=0):
            capacity -= curWt
            totalValue += curVal
        else:
            fraction = capacity/curWt
            totalValue += curVal*fraction
            capacity -= curWt*fraction
            break
    return totalValue