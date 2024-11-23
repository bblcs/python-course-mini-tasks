def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instance = cls(*args, **kwargs)
            instances[cls] = instance
        return instances[cls]

    return get_instance
