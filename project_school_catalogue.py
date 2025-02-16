class School:
    def __init__(self,name,level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_number_of_students(self):
        return self.numberOfStudents
    
    def set_number_of_students(self,numberOfStudents):
        self.numberOfStudents = numberOfStudents

    def __repr__(self):
        return "A {self.level} school named {self.name} with {self.numberOfStudents} students".format(self=self)
    
school = School("Anglo", "High", 1000)
print(school.get_name())
print(school.get_level())
print(school.get_number_of_students())
school.set_number_of_students(500)
print(school.get_number_of_students())

# Create the PrimarySchool class
class PrimarySchool(School):
    def __init__(self,name,level,numberOfStudents,pickupPolicy):
        super().__init__(name,level,numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickup_policy(self):
        return self.pickupPolicy
    
    def __repr__(self):
        return super().__repr__() + " " + "The pickup policy is: {self.pickupPolicy}".format(self=self)

primary_school = PrimarySchool("CEMEI", "primary", 2000, "Pickup at 1pm")
print(primary_school.get_name())
print(primary_school.get_level())
print(primary_school.get_number_of_students())
print(primary_school.get_pickup_policy())
#print repr form primary_school
print(school)
print(primary_school)

# Create the HighSchool class
class HighSchool(School):
    def __init__(self,name,level,numberOfStudents,sportsTeams):
        super().__init__(name,level,numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sports_teams(self):
        return self.sportsTeams
    
    def __repr__(self):
        return "The {self.level} school named {self.name} with {self.numberOfStudents} students. The sports teams are: {self.sportsTeams}".format(self=self)
    
high_school = HighSchool("Anglo", "High", 800, ["soccer","basketball"])
print(high_school)
print(high_school.get_name())
print(high_school.get_level())
print(high_school.get_number_of_students())
print(high_school.get_sports_teams())