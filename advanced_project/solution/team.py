from abc import ABC, abstractmethod
from .bank_account import BankAccount


class Developer(ABC):
    def __init__(self):
        self._bank_account = BankAccount('Ivan', 'Ivanov', '1234', 0, 'USD')
    
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass
    
    def pay_salary(self):
        self._bank_account.deposit(self.get_salary())
        
    def get_balance(self):
        return self._bank_account.get_balance()
        

class BackEndDeveloper(Developer):
    def work(self):
        print("Developing server-side of the application")

    def get_salary(self):
        return 5000  # Replace with the actual salary calculation for a backend developer
    
    def __repr__(self):
        return f'BackendDeveloper: {self.get_balance()}'


class FrontEndDeveloper(Developer):
    def work(self):
        print("Developing client-side of the application")

    def get_salary(self):
        return 4500  # Replace with the actual salary calculation for a frontend developer
    
    def __repr__(self) -> str:
        return f'FrontendDeveloper: {self.get_balance()}'


class TeamLead(Developer):
    def __init__(self, team):
        self.team = team

    def work(self):
        print("Coordinating the work of the team")

    def get_salary(self):
        total_salary = sum(member.get_salary() for member in self.team.members)
        return total_salary + 2000  # Additional bonus for the team lead
    
    def __repr__(self) -> str:
        return f'TeamLead: {self.get_balance()}'


class DevelopmentTeam:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def work(self):
        for member in self.members:
            member.work()
            
    def pay_salary(self):
        for member in self.members:
            member.pay_salary()
            
    def __repr__(self) -> str:
        return '\n'.join([str(member) for member in self.members])
        

if __name__ == "__main__":
    back_end_dev = BackEndDeveloper()
    front_end_dev1 = FrontEndDeveloper()
    front_end_dev2 = FrontEndDeveloper()
    team_lead = TeamLead([back_end_dev, front_end_dev1, front_end_dev2])

    development_team = DevelopmentTeam()
    development_team.add_member(back_end_dev)
    development_team.add_member(front_end_dev1)
    development_team.add_member(front_end_dev2)
    development_team.add_member(team_lead)

    development_team.work()
    total_salary = team_lead.get_salary()

    print("\nTotal salary for the team lead and the team:", total_salary)
