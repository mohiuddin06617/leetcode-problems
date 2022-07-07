class AUsefulThing(object):
    def __init__(self, aStrategicAlternative):
        super(AUsefulThing, self).__init__()
        self.howToDoX = aStrategicAlternative

    def doX(self, someArg):
        self. howToDoX.theAPImethod(someArg, self)


class StrategicAlternative(object):
    pass


class AlternativeOne(StrategicAlternative):
    def __init__(self):
        super(AlternativeOne, self).__init__()

    def theAPImethod(self, someArg, theUsefulThing):
        print("an implementation through ", theUsefulThing.__class__.__name__)
        pass  # an implementation


class AlternativeTwo(StrategicAlternative):
    def theAPImethod(self, someArg, theUsefulThing):
        print("another implementation",theUsefulThing)
        pass  # another implementation


if __name__ == '__main__':
    val = AlternativeTwo
    t = AUsefulThing(val())
    t.doX('arg')
    val = AlternativeOne
    one = AUsefulThing(val())
    one.doX('arg_one')