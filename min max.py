month=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

profit=[1,2,3,4,5,6,7,8,9,10,11,12]

mp=max(profit)
mpi=profit.index(mp)

mpm=month[mpi]
print('max profit:'+str(mp)+' max profit month:'+str(mpm))

ip=min(profit)
ipi=profit.index(ip)

ipm=month[ipi]
print('min profit:'+str(ip)+' min profit month:'+str(ipm))