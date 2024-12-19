def singleton(cls):
    instances = {}

    class SingletonWrapper(cls):
        def __new__(cls, *args, **kwargs):
            if cls not in instances:
                instance = super().__new__(cls)
                cls.__init__(instance, *args, **kwargs)
                instances[cls] = instance
            return instances[cls]

    return SingletonWrapper
