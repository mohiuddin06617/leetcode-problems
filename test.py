from abc import ABC, abstractmethod


class M(ABC):
    @abstractmethod
    def spd(self):
        self.pdb()
        print('spd')

    @abstractmethod
    def pdb(self):
        print('pdb')


class Chi(M):
    def pdb(self):
        print('chi')
        return super().pdb()

    def spd(self):
        print('chi')
        return super().spd()

if __name__ == '__main__':
    c = Chi()
    c.spd()
