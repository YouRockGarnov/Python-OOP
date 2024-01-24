class Device:
    def __init__(self, name, ip_address):
        raise NotImplementedError("Implement me")

    def configure(self) -> str:
        raise NotImplementedError("Implement me")


class Router(Device):
    def __init__(self, name, ip_address, interfaces):
        raise NotImplementedError("Implement me")

    def configure(self) -> str:
        raise NotImplementedError("Implement me")


class Switch(Device):
    def __init__(self, name, ip_address, ports):
        raise NotImplementedError("Implement me")

    def configure(self) -> str:
        raise NotImplementedError("Implement me")


class Firewall(Device):
    def __init__(self, name, ip_address, rules):
        raise NotImplementedError("Implement me")

    def configure(self) -> str:
        raise NotImplementedError("Implement me")


# Создание объектов для каждого типа устройства
router = Router("Router1", "192.168.1.1", ["eth0", "eth1", "eth2"])
switch = Switch("Switch1", "192.168.1.2", [1, 2, 3, 4, 5])
firewall = Firewall("Firewall1", "192.168.1.3", ["Allow HTTP", "Deny FTP"])

if __name__ == "__main__":
    # Вызов метода configure для каждого устройства и вывод результатов
    print(router.configure())
    print()
    print(switch.configure())
    print()
    print(firewall.configure())
