from abc import ABC, abstractmethod


class Developer(ABC):
    @abstractmethod
    def work(self) -> str:
        pass

    @abstractmethod
    def get_salary(self) -> int:
        pass


class BackEndDeveloper(Developer):
    pass  # implement me!


class FrontEndDeveloper(Developer):
    pass  # implement me!


class TeamLead(Developer):
    pass  # implement me!


class DevelopmentTeam:
    def __init__(self):
        raise NotImplementedError('Implement me!')

    def add_member(self, member):
        raise NotImplementedError('Implement me!')

    def work(self):
        raise NotImplementedError('Implement me!')


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
