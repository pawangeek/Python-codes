# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

# Important : (i) How to sort tuples/dictionary in our own way(for example inc. key dec. value or any other)
#             (ii) Getting values from list of tuples is same as for lists of lists

restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 1 
maxPrice = 50
maxDistance = 10

dct = {}
if veganFriendly==1:            
    for i in restaurants:
        if i[2]==1 and i[4]<=maxDistance and i[3]<=maxPrice:
            dct.update({i[0]:i[1]})
                           
else:            
    for i in restaurants:
        if i[4]<=maxDistance and i[3]<=maxPrice:
            dct.update({i[0]:i[1]})
                            
d = sorted(dct.items(), key=lambda x: (-x[1], -x[0]))   # (i)
print ([i[0] for i in d])