from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, user_pass):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = user_pass
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30594
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        #print("The value of DB is ", DB)
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
                        
            is_inserted = self.database.animals.insert_one(data)  # data should be dictionary
            if is_inserted is not None:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        #print(data)
        if data is not None:
            is_read = self.database.animals.find(data)
                
            if is_read is not None:
                #print(data, "test1")
                return is_read
            else:
                #print(data, "test2")
                return None
        else:
            #return self.database.animals.find({})
            #print(data, "test3")
            raise Exception("Nothing to read, because data parameter is empty")
            
#create method to implement U in CRUD
    def update(self, data, new_data):
        if data is not None:
            old_data = self.database.animals.find(data)
            if new_data is not None:
                set_field = {"$set": new_data}
                result = self.database.animals.update_one(data, set_field)
                if(result.modified_count <= 1):
                    print(result.modified_count)
                else:
                    print("No documents updated")
            else:
                raise Exception("Nothing to update, because new_data parameter is empty")
        else:
            raise Exception("Nothing to update, because data parameter is empty")

#create method to implement D in CRUD            
    def delete(self, data):
        if data is not None:
            #deleted_data = self.database.animals.find(data)
            delete_data = self.database.animals.delete_many(data)
            #if (delete_data.deleted_count <= 1):
            print(delete_data.deleted_count)
            #else:
            #    print("No documents deleted")
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            
            
            