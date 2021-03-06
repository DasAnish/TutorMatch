import pymongo
from gridfs import GridFS


class Mongo:

    __instance = None

    @staticmethod
    def getInstance():
        if Mongo.__instance is None:
            Mongo()

        return Mongo.__instance

    def __init__(self):
        if Mongo.__instance is not None:
            raise Exception("Singleton Exception: Mongo")

        Mongo.__instance = self

        uri = "mongodb+srv://cluster0.d7bvv.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(uri,
                        tls=True,
                        tlsCertificateKeyFile='X509-cert-6197396631610520216.pem')

        self.parentsData = self.client['HopHacks']['Parents']
        self.tutorsData  = self.client['HopHacks']['Tutors']
        self.matchesData = self.client['HopHacks']['Matches']
        self.imagesData  = GridFS(self.client['HopHacks'], 'Images')
