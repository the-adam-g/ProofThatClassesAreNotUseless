# ProofThatClassesAreNotUseless

When classes were first introduced to me in school, I had already been a developer for several years, working with languages such as PHP and having a lot of experience with SQL databases.

This is why classes were initially very difficult for me to understand. I was very used to interacting directly with data in a database: inserting data, selecting data, updating it, and generally just running queries whenever I needed something. If I needed to update some data, I would usually just run a query directly against the database, or assign the result to a variable and work with it.

Because of this, the idea of having a large local record containing data didn't make much sense to me.

However, this GitHub repository is my unequivocal proof that there are useful applications for classes outside of the general examples that teachers often use to explain them. Classes aren't just useful for changing a bunch of things inside a program; they can actually be useful for representing and managing collections of related data.

Let's imagine, for example, that we are creating a class for an insurance company. The class might contain a claim ID, a claim name, and a claim type.

Rather than relying on a database to store multiple claims, we could create an array and populate it with instances of our class. Each claim becomes its own object, and because each object occupies a specific position in the array, we can uniquely identify and access it using the array index.

This is the concept I demonstrate in my `proof.py` file.

```python
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

```
