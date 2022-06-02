#Add these methods to class student - full_name, year_of_birth, initials.
# Create two instances and verify the work as expected

class Student:
    school = "Jkuat"
    def __init__(self, first_name, last_name, country,age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.age = age
        def full_name (self):
            
            return f"Hello {self.first_name} {self.second_name} How is your {country}"
        def year_of_birth (self):
            year = 2022 - self.age
            return f"Hello {self.first_name} {self.second_name} How is your {self.country} and when were you born in {year}"
        def initials (self):
            return f"Hello {self.first_name} {self.second_name} what are your {self.country} initials  {year}"

            
        
    
        
    
