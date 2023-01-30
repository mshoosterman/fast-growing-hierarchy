from __future__ import annotations
from typing import List, Tuple
from ordinal_exceptions import NonSuccessorException, NonLimitException


class Ordinal:
    """ A Class defining ordinal numbers.
    === Public Attributes ===
    None. Don't touch my Attributes.

    === Private Attributes ===
    _normal_form: a list of tuples representing the ordinal in cantor normal
    form.
    _is_epsilon_0
    """

    def __init__(self, normal_form: List[Tuple[Ordinal, int]]) -> None:
        """ Initializes a new Ordinal

        normal_form must be a list where the Ordinals in each tuple are in a
        strictly decreasing order, and each integer in each tuple must be
        positive. An Attempt will be made to fix an out of order list, and
        an attempt will be made to fix some issues, but any negative integers
        will throw an error."""
        self._normal_form = normal_form
        self._is_epsilon_0 = False

    def is_epsilon_0(self) -> bool:
        return self._is_epsilon_0

    def normal_form(self) -> List[Tuple[Ordinal, int]]:
        return self._normal_form

    # Automatically gives a recursive definition of equality.
    def __eq__(self, other: Ordinal) -> bool:
        return self.normal_form() == other.normal_form()

    def __contains__(self, item) -> bool:
        # Returns false whenever self is the ordinal 0, as 0 is empty.
        if not self.normal_form():
            return False
        for index, term in enumerate(self.normal_form()):
            return True #Not complete code.

    def is_lim(self) -> bool:
        """ Returns true if self is a limit ordinal."""
        normal = self.normal_form()
        # If the normal form is empty then self is 0 which isn't a limit ordinal
        if not normal:
            return False
        # If the ordinal part of the last element of normal, has an empty normal
        # form, then it represents 0, which means the last element of normal is
        # an integer, which means that self is a limit ordinal plus an integer,
        # and is therefore a successor ordinal.
        if not normal[-1][0].normal_form():
            return False
        return True

    def is_successor(self) -> bool:
        """ Returns true if self is a limit successor ordinal."""
        normal = self.normal_form()
        # If the normal form is empty then self is 0 which isn't a successor
        # ordinal
        if not normal:
            return False
        # If the ordinal part of the last element of normal, has an empty normal
        # form, then it represents 0, which means the last element of normal is
        # an integer, which means that self is a limit ordinal plus an integer,
        # and is therefore a successor ordinal.
        if not normal[-1][0].normal_form():
            return True
        return False

    def is_zero(self) -> bool:
        """ Returns true if self is zero. """
        # If and only if the normal form is empty then self is 0.
        if not self.normal_form():
            return True
        return False

    def predecessor(self) -> Ordinal:
        """ If Self is a successor Ordinal, then returns an ordinal who's
        successor is self. This is a helper function for the fundemetal sequence
        method.
        If Self is not a successor ordinal, then returns error.
        """
        if not self.is_successor():
            raise NonSuccessorException("This is not a Successor Ordinal.")
        normal = self.normal_form()
        l = len(normal)
        new_normal = []
        for index, term in enumerate(normal):
            if index < l-1:
                new_normal.append(term)
            # If the last term in the normal form is greater than 1, then
            # subtract 1 from it. If it is equal to 1, then subtract 1 by not
            # including that term in the normal form.
            if index == l-1:
                if term[1] > 1:
                    new_normal.append((term[0], term[1]-1))
        return Ordinal(new_normal)

    def fun_seq(self, n: int) -> Ordinal:
        """ For a non negative integer n, returns the nth element of the
        fundamental sequence for the ordinal <self>.

        <self> must be a limit ordinal.
        """
        #   Note the choice for how to define the fundamental sequence of each
        #   ordinal is the main factor which determines the particular
        #   fast-growing that is being used. This code is meant to implement the
        #   Wainer hierarchy which uses fundamental sequences defined as
        #   follows.
        if not self.is_lim():
            raise NonLimitException("This is not a Limit Ordinal")
        normal = self.normal_form()
        last = normal[-1]
        ord = last[0]
        coefficient = last[1]
        if last[0].is_successor():
            if coefficient > 1:
                normal[-1] = (ord, coefficient-1)
                pred = ord.predecessor()
                normal.append((pred, n))
            else:
                pred = ord.predecessor()
                normal[-1] = (pred, n)
        if last[0].is_lim():
            if coefficient > 1:
                normal[-1] = (ord, coefficient-1)
                new_ord = ord.fun_seq(n)
                # It is weird that there is a hard coded 1 here as a coefficient
                # Please just trust that its supposed to work that way.
                # There is a good reason for it, but there's no way im writing
                # an explanation of that as a comment. Sorry.
                normal.append((new_ord, 1))
            else:
                new_ord = ord.fun_seq(n)
                # See previous comment.
                normal[-1] = (new_ord, 1)
        else:
            # I am pretty sure this exception should never happen. If it does
            # then there is a big problem.
            raise Exception("Something went terribly terribly wrong, "
                            "and I have no Idea why")
        return Ordinal(normal)


