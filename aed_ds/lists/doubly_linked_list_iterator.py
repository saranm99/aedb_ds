from .tad_iterator import Iterator
from .singly_linked_list_iterator import SinglyLinkedListIterator
from ..exceptions import NoSuchElementException  

class DoublyLinkedListIterator(SinglyLinkedListIterator):
    def __init__(self, position):
        pass

    # Returns true iff the iteration has more elements in the reverse direction.
    # In other words, returns true if previous would return an element rather than throwing an exception.
    def has_previous(self): 
        pass
    
    # Returns the previous element in the iteration.
    # Throws NoSuchElementException
    def previous(self): 
        pass

    # Restarts the iteration in the reverse direction. After fullForward, if the iteration is not empty, previous will return the last element in the iteration.
    def full_forward(self): 
        pass