from abc import ABC, abstractmethod

class Developer(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

class BackEndDeveloper(Developer):
    def work(self):
        print("Developing server-side of the application")

    def get_salary(self):
        return 5000  # Replace with the actual salary calculation for a backend developer

class FrontEndDeveloper(Developer):
    def work(self):
        print("Developing client-side of the application")

    def get_salary(self):
        return 4500  # Replace with the actual salary calculation for a frontend developer

class TeamLead(Developer):
    def __init__(self, team):
        self.team = team

    def work(self):
        print("Coordinating the work of the team")

    def get_salary(self):
        total_salary = sum(member.get_salary() for member in self.team.members)
        return total_salary + 2000  # Additional bonus for the team lead

class DevelopmentTeam:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def work(self):
        for member in self.members:
            member.work()

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
