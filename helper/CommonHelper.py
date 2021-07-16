class CommonHelper:
    __instance = None
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance
    
    def objlist_to_dict(self,objlist):
        return [ i.__dict__ for i in objlist ]

