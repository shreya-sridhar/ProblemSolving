def merge(intervals):
    def helper_merge(intervals):
        i = 0
        while i <= len(intervals)-2 and len(intervals)>1:                
            if intervals[i][0]<=intervals[i+1][0]<=intervals[i][1]:
                intervals[i] = [min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]
                del intervals[i+1]
                i-=1
            i+=1
        return(intervals)
    return helper_merge(sorted(intervals, key=lambda x: x[0])) 

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(max(15,15))






