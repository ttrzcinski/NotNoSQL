from abc import ABCMeta, abstractmethod


class Manager(metaclass=ABCMeta):
    """ Skeleton of Manager class. """

    @abstractmethod
    def create(self, props):
        """ Creates new element with given props. """
        print('Not implemented yet')
        pass

    def update(self, id: int, props) -> bool:
        """ Updates within element pointed by id with given props. """
        print('Not implemented yet')
        pass

    def remove(self, id) -> bool:
        """ Removes all elements with pointed id. """
        print('Not implemented yet')
        return False

    def exists(self, id) -> bool:
        """ Checks, if element with pointed id exists in the pool. """
        print('Not implemented yet')
        return False

    def count(self) -> int:
        """ Counts all elements kept in a pool. """
        print('Not implemented yet')
        return 0
