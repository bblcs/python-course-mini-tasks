def singleton(cls):
    instances = {}

    def dummy(*args, **kwargs):
        pass

    class SingletonWrapper(cls):
        def __new__(cls, *args, **kwargs):
            if cls not in instances:
                instance = super().__new__(cls)
                instances[cls] = instance
            else:
                cls.__init__ = dummy
            return instances[cls]

    return SingletonWrapper


## test on classes woth prints in inits
