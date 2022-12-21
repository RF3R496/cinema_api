class AdminUser():
    def __init__(self , id , name=None, last_name=None, user=None, password=None, created_at=None):
        self.id = id
        self.name = name 
        self.last_name = last_name
        self.user = user 
        self.password = password
        self.created_at = created_at
        

    def to_json(self):
        return {
            'id': self.id,
            'name' : self.name,
            'last_name': self.last_name,
            'user': self.user,
            'password':self.password,
            'created_at':self.created_at,
        }