class Solution(object):
    def minimumOperations(self, parcels):
        # length of parcels
        n = len(parcels)
        # count number of days
        days = 0
        # to know whether any parcel is left
        parcelsRemaining = True
        # loop until parcels to deliver exist
        while parcelsRemaining:
            minParcel = float('inf')
            parcelsRemaining=False
            # calculate the minimum parcel to be delivered
            for i in range(n):
                if parcels[i] == 0:
                    continue
                minParcel=min(minParcel,parcels[i])
                # even if one parcel is non zero then parcels to deliver will be True
                parcelsRemaining=True
            # subtract the minimum parcel from all non-zero parcels
            for i in range(n):
                if parcels[i]==0:
                    continue
                parcels[i]-=minParcel
            # increment days
            days+=1
        # return days(-1 because in last iteration an extra day will be counted)
        return days-1