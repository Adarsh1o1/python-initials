class database_connect():
    def __init__(self,x) -> None:
        self.x =x

    def get_data(self):
        print("getting data from database")
    
    def status(self):
        self.get_data()

data_obj = database_connect(200)
data_obj.status()

def new_data(self):
    print("fetching new data")

database_connect.get_data = new_data

data_obj.status()
