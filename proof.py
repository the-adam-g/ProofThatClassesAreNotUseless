#This example is using a scenario of an insurance claim. No particular reason why in relation to the proof, it just works

class Claim:
    def __init__(self, claimid, name, claimtype):
        self.claimid = claimid
        self.name = name
        self.claimtype = claimtype
        
array = []

for i in range(5):
    newclaim = Claim(i, ("name" + str(i)), "car")
    array.append(newclaim)
    
print(array)
print(array[3].name)
