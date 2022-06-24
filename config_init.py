def config_item(func):
    func.__config_item__ = True
    return func

