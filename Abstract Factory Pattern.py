from abc import ABC,abstractmethod

class ComputerFactory(ABC):
    def get_computer(self,kargs):
        pass

class  Laptop:
    def __init__(self,hdd,ram,cpu,bluet):
        self.HardDisk = hdd
        self.MainMemory = ram
        self.Processing = cpu
        self.Bluetooth =bluet

    def __str__(self):
        return f"""
        Laptop Hard Disk : {self.HardDisk}
        Laptop Ram : {self.MainMemory}
        Laptop CPU : {self.Processing}
        Laptop Bluetooth : {self.Bluetooth}
        """

    def __repr__(self):
        return str(self)

class LaptopFactory(ComputerFactory):
    def get_computer(self,kargs):
        if kargs.get('bluet'):
            return Sever(kargs.get('hdd'), kargs.get('cpu'), kargs.get('ram'), kargs.get('bluet'))
        else:
            print('Bluetooth property missing')


class Desktop:

    def __init__(self, hdd, ram, cpu, crt):
        self.HardDisk = hdd
        self.MainMemory = ram
        self.Processing = cpu
        self.Monitor =crt

    def __str__(self):
        return f"""
        Desktop Hard Disk : {self.HardDisk}
        Desktop Ram : {self.MainMemory}
        Desktop CPU : {self.Processing}
        Desktop Monitor : {self.Monitor}
        """

    def __repr__(self):
        return str(self)


class DesktopFactory(ComputerFactory):
    def get_computer(self, kargs):
        if kargs.get('crt'):
            return Sever(kargs.get('hdd'), kargs.get('cpu'), kargs.get('ram'), kargs.get('crt'))
        else:
            print('CRT property missing')


class Sever:

    def __init__(self, hdd, ram, cpu, space):
        self.HardDisk = hdd
        self.MainMemory = ram
        self.Processing = cpu
        self.StorageSpace = space

    def __str__(self):
        return f"""
        Server Hard Disk : {self.HardDisk}
        Server Ram : {self.MainMemory}
        Server CPU : {self.Processing}
        Server Space : {self.StorageSpace}
        """


    def __repr__(self):
        return str(self)


class ServerFactory(ComputerFactory):
    def get_computer(self, kargs):
        if kargs.get('space'):
            return Sever(kargs.get('hdd'),kargs.get('cpu'),kargs.get('ram'),kargs.get('space'))
        else:
            print('Server Space property missing')


class MainFactory:
    @staticmethod
    def get_computer(factory,kargs):
        if factory and kargs.get('hdd') and kargs.get('ram') and kargs.get('cpu'):
            return factory.get_computer(kargs)
        else:
            print('Invalid Factory type')

factory =DesktopFactory()
c1 =MainFactory.get_computer(factory,{'ram': '8gb','hdd':'2tb','cpu':'i7','space':'100*100','bluet':'2.4'})
print(c1)