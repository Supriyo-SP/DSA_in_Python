
prices = [7, 1, 5, 3, 6, 4]
n=len(prices)
mini=float(('inf'))
maxi=0
for i in range(0,n):
    mini=min(mini,prices[i])
    maxi=max(maxi,prices[i]-mini)
print(maxi) 
    