class PersistenceError(Exception):
    pass


class ItemNotFound(PersistenceError):
    pass


class MapperError(Exception):
    pass
