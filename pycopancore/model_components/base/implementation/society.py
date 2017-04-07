"""Base component's Society entity type mixin implementation class."""

# This file is part of pycopancore.
#
# Copyright (C) 2017 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

# only used in this component, not in others:
from ... import abstract
from .... import master_data_model as D
from ....private import unknown

from .. import interface as I


class Society (I.Society, abstract.Society):
    """Society entity type mixin implementation class.

    Base component's Society mixin that every model must use in composing
    their Society class. Inherits from I.Society as the interface with all
    necessary variables and parameters.
    """

    # standard methods:

    def __init__(self,
                 *,
                 world,
                 next_higher_society=None,
                 population = 0 * D.people,
                 **kwargs
                 ):
        """Initialize an instance of Society."""
        super().__init__(**kwargs)  # must be the first line

        self._next_lower_societies = set()
        self._direct_cells = set()

        self._world = None
        self._next_higher_society = None

        self.world = world
        self.next_higher_society = next_higher_society
        self.population = population

    # getters and setters for references:

    @property
    def world(self):
        """Return world."""
        return self._world

    @world.setter
    def world(self, w):
        """Set world."""
        if self._world is not None:
            self._world._societies.remove(self)
        assert isinstance(w, I.World), "world must be of entity type World"
        w._societies.add(self)
        self._world = w

    @property
    def next_higher_society(self):
        """Return next higher society."""
        return self._next_higher_society

    @next_higher_society.setter
    def next_higher_society(self, s):
        """Set next higher society."""
        if self._next_higher_society is not None:
            self._next_higher_society._next_lower_societies.remove(self)
            # reset dependent cache:
            self._next_higher_society.cells = unknown
        if s is not None:
            assert isinstance(s, I.Society), \
                "next_higher_society must be of entity type Society"
            s._next_lower_societies.add(self)
            # reset dependent cache:
            s.cells = unknown
        self._next_higher_society = s
        # reset dependent caches:
        self.higher_societies = unknown

    # getters for backwards references and convenience variables:

    @property  # read-only
    def nature(self):
        """Return nature."""
        return self._world.nature

    @property  # read-only
    def metabolism(self):
        """Return metabolism."""
        return self._world.metabolism

    @property  # read-only
    def culture(self):
        """Return culture."""
        return self._world.culture

    _higher_societies = unknown
    """cache, depends on self.next_higher_society 
    and self.next_higher_society.higher_societies"""
    @property  # read-only
    def higher_societies(self):
        """Return higher societies."""
        if self._higher_societies is unknown:
            # find recursively:
            self._higher_societies = [] if self.next_higher_society is None \
                else [self.next_higher_society] \
                        + self.next_higher_society.higher_societies
        return self._higher_societies

    @higher_societies.setter
    def higher_societies(self, u):
        assert u == unknown, "setter can only be used to reset cache"
        self._higher_societies = unknown
        # reset dependent caches:
        for s in self._next_lower_societies:
            s.higher_societies = unknown
        for c in self._direct_cells:
            c.societies = unknown

    @property  # read-only
    def next_lower_societies(self):
        """Read next lower societies."""
        return self._next_lower_societies

    @property  # read-only
    def lower_societies(self):
        """Return lower societies."""
        # aggregate recursively:
        l = self._next_lower_societies
        for s in self._next_lower_societies:
            l.update(s.lower_societies)
        return l

    @property  # read-only
    def direct_cells(self):
        """Return direct cells."""
        return self._direct_cells

    _cells = unknown
    """cache, depends on self.direct_cells, self._next_lower_societies,
    and lowersociety.cells"""
    @property  # read-only
    def cells(self):
        """Return cells."""
        if self._cells is unknown:
            # aggregate recursively:
            self._cells = self.direct_cells
            for s in self._next_lower_societies:
                self._cells.update(s.cells)
        return self._cells

    @cells.setter
    def cells(self, u):
        assert u == unknown, "setter can only be used to reset cache"
        self._cells = unknown
        # reset dependent caches:
        if self.next_higher_society is not None:
            self.next_higher_society.cells = unknown

    _direct_individuals = unknown
    """cache, depends on _direct_cells, directcell.individuals"""
    @property  # read-only
    def direct_individuals(self):
        """Return direct individuals."""
        if self._direct_individuals is unknown:
            # aggregate from direct_cells:
            self._direct_individuals = set()
            for c in self._direct_cells:
                self._direct_individuals.update(c.individuals)
        return self._direct_individuals

    @direct_individuals.setter
    def direct_individuals(self, u):
        assert u == unknown, "setter can only be used to reset cache"
        self._direct_individuals = unknown
        # reset dependent caches:
        pass

    _individuals = unknown
    """cache, depends on self.cells, cell.individuals"""
    @property  # read-only
    def individuals(self):
        """Return individuals."""
        if self._individuals is unknown:
            # aggregate from cells:
            self._individuals = set()
            for c in self.cells:
                self._individuals.update(c.individuals)
        return self._individuals

    @individuals.setter
    def individuals(self, u):
        assert u == unknown, "setter can only be used to reset cache"
        self._individuals = unknown
        # reset dependent caches:
        pass

    # TODO: helper methods for mergers, splits, etc.

    # no process-related methods

    processes = []
