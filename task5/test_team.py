import pytest
from team import BackEndDeveloper, FrontEndDeveloper, TeamLead, DevelopmentTeam


def test_back_end_developer_work():
    back_end_dev = BackEndDeveloper()
    back_end_dev.work()


def test_back_end_developer_get_salary():
    back_end_dev = BackEndDeveloper()
    back_end_dev.get_salary()


def test_front_end_developer_work():
    front_end_dev = FrontEndDeveloper()
    front_end_dev.work()


def test_front_end_developer_get_salary():
    front_end_dev = FrontEndDeveloper()
    front_end_dev.get_salary()


def test_team_lead_work():
    back_end_dev = BackEndDeveloper()
    front_end_dev1 = FrontEndDeveloper()
    front_end_dev2 = FrontEndDeveloper()
    team_lead = TeamLead([back_end_dev, front_end_dev1, front_end_dev2])

    team_lead.work()


def test_team_lead_get_salary():
    back_end_dev = BackEndDeveloper()
    front_end_dev1 = FrontEndDeveloper()
    front_end_dev2 = FrontEndDeveloper()
    team_lead = TeamLead([back_end_dev, front_end_dev1, front_end_dev2])

    team_lead.get_salary()


def test_development_team_work():
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


def test_development_team_add_member():
    development_team = DevelopmentTeam()
    back_end_dev = BackEndDeveloper()
    development_team.add_member(back_end_dev)

    front_end_dev = FrontEndDeveloper()
    development_team.add_member(front_end_dev)
