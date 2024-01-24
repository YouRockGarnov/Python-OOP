import pytest
from devices import Device, Router, Switch, Firewall


@pytest.fixture
def device():
    return Device("Device1", "192.168.1.1")


@pytest.fixture
def router():
    return Router("Router1", "192.168.1.1", ["eth0", "eth1", "eth2"])


@pytest.fixture
def switch():
    return Switch("Switch1", "192.168.1.2", [1, 2, 3, 4, 5])


@pytest.fixture
def firewall():
    return Firewall("Firewall1", "192.168.1.3", ["Allow HTTP", "Deny FTP"])


def test_device_configure(device):
    config = device.configure()
    assert device.name in config and device.ip_address in config


def test_router_configure(router):
    config = device.configure()
    assert router.name in config and router.ip_address in config and router.interfaces in config


def test_switch_configure(switch):
    config = device.configure()
    assert switch.name in config and switch.ip_address in config and switch.ports in config


def test_firewall_configure(firewall):
    config = device.configure()
    assert firewall.name in config and firewall.ip_address in config and firewall.rules in config
