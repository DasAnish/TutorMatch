import abc


class Level:
    KS2, KS3, GCSE, ALEVEL = 0, 1, 2, 3


class Person:

    def __init__(self):

        self.name = ''
        self.subject = []
        self.rateMin =0
        self.rateMax =0
        self.location = None
        self.phoneNum = 0
        self.level = -1

    def baseUpdateInfo(self, info):
        if 'name' in info:
            self.name = info['name']

        if 'subject' in info:
            self.subject = info['subject']

        if 'rateMin' in info:
            self.rateMin = info['rateMin']

        if 'rateMax' in info:
            self.rateMax = info['rateMax']

        if 'location' in info:
            self.location = info['location']

        if 'phoneNum' in info:
            self.phoneNum = info['phoneNum']

        if 'level' in info:
            self.level = info['level']

    def baseToDict(self):
        output = {
            "name": self.name,
            "subject": self.subject,
            'rateMin': self.rateMin,
            'rateMax': self.rateMax,
            'location': self.location,
            'phoneNum': self.phoneNum,
            'level': self.level
        }

        return output

    @abc.abstractmethod
    def updateInfo(self, info):
        pass

    @abc.abstractmethod
    def toDict(self):
        pass


class Parent(Person):

    def __init__(self, id):
        Person.__init__(self)
        self.id = id

    def updateInfo(self, info):
        self.baseUpdateInfo(info)

    def toDict(self):
        output = self.baseToDict()

        output['_id'] = self.id
        return output


class Tutor(Person):

    def __init__(self, id):
        Person.__init__(self)
        self.id = id

        self.picture = None
        self.qualification = []

    def updateInfo(self, info):
        self.baseUpdateInfo(info)

        if 'picture' in info:
            self.picture = info['picture']

        if 'qualification' in info:
            self.qualification = info['qualification']

    def toDict(self):

        output = self.baseToDict()
        output['picture'] = self.picture
        output['qualification'] = self.qualification

        output['_id'] = self.id
        return output


class Match:

    REQUESTED, ACCEPTED, REJECTED = 0, 1, 2

    def __init__(self, id, parent, tutor):
        self.id = id

        self.parent = parent
        self.tutor = tutor

        self.status = Match.REQUESTED

    def accept(self):
        self.status = Match.ACCEPTED

    def reject(self):
        self.status = Match.REJECTED
