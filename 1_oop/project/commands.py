from enum import Enum


class Commands(Enum):
    add_task = 'Добавь задачу'
    show_tasks = 'Покажи задачи'
    add_developer = 'Добавь разработчика'
    show_team = 'Покажи команду'
    pay_salary = 'Начисли зарплату'
    backend = 'Backend'
    frontend = 'Frontend'
    teamlead = 'TeamLead'
