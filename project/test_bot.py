import pytest
from . import DatabaseMock, AddTaskState, AddDeveloperState, StartState, BackEndDeveloper
from .commands import Commands
from .bot import Bot

TEST_TASK = 'Test task'


@pytest.fixture
def bot():
    bot = Bot()
    bot.reply('Hi')
    return bot


def test_add_and_show_tasks(bot: Bot) -> Bot:
    _ = bot.reply(Commands.add_task.value)
    _ = bot.reply(TEST_TASK)
    reply = bot.reply(Commands.show_tasks.value)
    assert TEST_TASK in reply
    return bot


def test_add_and_show_team(bot: Bot) -> Bot:
    _ = bot.reply(Commands.add_developer.value)
    _ = bot.reply(Commands.backend.value)
    reply = bot.reply(Commands.show_team.value)
    assert Commands.backend.value in reply
    return bot


def test_pay_salary(bot: Bot):
    bot = test_add_and_show_team(bot)
    reply = bot.reply(Commands.show_team.value)
    assert '0' in reply
    
    _ = bot.reply(Commands.pay_salary.value)
    reply = bot.reply(Commands.show_team.value)
    assert str(BackEndDeveloper().get_salary()) in reply
