class Device:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address

    def configure(self):
        return f"Configuring {self.name} with IP address {self.ip_address}"


class Router(Device):
    def __init__(self, name, ip_address, interfaces):
        super().__init__(name, ip_address)
        self.interfaces = interfaces

    def configure(self):
        base_configuration = super().configure()
        interface_configuration = f"Configuring interfaces: {', '.join(self.interfaces)}"
        return f"{base_configuration}\n{interface_configuration}"


class Switch(Device):
    def __init__(self, name, ip_address, ports):
        super().__init__(name, ip_address)
        self.ports = ports

    def configure(self):
        base_configuration = super().configure()
        port_configuration = f"Configuring ports: {', '.join(map(str, self.ports))}"
        return f"{base_configuration}\n{port_configuration}"


class Firewall(Device):
    def __init__(self, name, ip_address, rules):
        super().__init__(name, ip_address)
        self.rules = rules

    def configure(self):
        base_configuration = super().configure()
        rules_configuration = f"Configuring firewall rules: {', '.join(self.rules)}"
        return f"{base_configuration}\n{rules_configuration}"


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
