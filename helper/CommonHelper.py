class CommonHelper:
    
    @staticmethod
    def objlist_to_dict(objlist):
        return [ i.__dict__ for i in objlist ]

