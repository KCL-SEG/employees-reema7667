"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, flexible = True):
        self.name = name
        self.contract_flexible = flexible

    def set_hours(self, hr):
        self.hours = 0
        if self.contract_flexible:
            self.hours = hr

    def get_hours(self):
        if self.contract_flexible:
            return self.hours
        return "contract not flexible"
        ## should I use try except or raise Error? ## what type of Error?

    def setContract(self, is_contract_flexible,  fixed_pay = 0, max_hr = 0, hr_wage = 0):
        self.contract_flexible = is_contract_flexible
        ##if self.contract_flexible:
        self.max_hr = max_hr
        self.hr_wage = hr_wage
        self.fixed_pay = fixed_pay
    
    def getContractStr(self):
        return f"works on a contract of {self.max_hr} hours at {self.hr_wage}/hour"

    def setCommision(self, fixed_bonus = 0, contract_based =0, n_contract =0):
        #self.type = 
        self.n_contracts = n_contract
        self.contract_based = contract_based
        self.fixed_bonus = fixed_bonus
        self.commision = fixed_bonus + contract_based*self.n_contracts

    def getCommisionStr(self):
        if self.n_contracts ==0:
            commision_str = "receives a bonus commision of " + self.fixed_bonus
        else:
            commision_str = f"receives a bonus commision for {self.n_contracts} contract(s) at {self.contract_based}/contract"
        return commision_str

    def get_pay(self):
        return self.commision + self.max_hr*self.hr_wage + self.fixed_pay 

    def __str__(self):
        _str = f"{self.name} {self.getContractStr()} and {self.getCommisionStr}. Their total pay is {self.get_pay()}"
        return _str


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.setContract(False, 4000)
billie.setCommision()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.setContract(True, 0,100, 25)
charlie.setCommision()
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.setContract(False, 3000, 0,0)
renee.setCommision(0,200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.setContract(True,0,150, 25)
jan.setCommision(0,220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.setContract(False, 2000)
robbie.setCommision(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.setContract(True, 0,120, 30)
ariel.setCommision(600)
