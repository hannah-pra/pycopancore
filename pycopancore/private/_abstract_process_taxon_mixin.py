"""_abstract_dynamics_mixin class.

It sets the basic structure of dynamic mixins (culture, metabolism, nature).
"""
# This file is part of pycopancore.
#
# Copyright (C) 2016 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

from ..data_model import variable
from ..data_model import OrderedSet
# TODO: why don't we need a _AbstractProcessTaxonMixinType as for entities?

class _AbstractProcessTaxonMixin(object):
    """Define Entity-unspecific abstract class.

    From this class all entity-specific abstract mixin classes are derived.
    """

    variables = OrderedSet()
    """All variables occurring in this taxon"""
    processes = []
    """All processes of this taxon"""
    model = None
    """Model containing this taxon"""
    instances = None
    """List containing the unique instance of this taxon"""

    def __init__(self):
        """Initialize an _AbstractProcessTaxonMixin instance."""
        if self.__class__.instances:
            self.__class__.instances.append(self)
            print('This Process Taxon is already initialized!')
        else:
            self.__class__.instances = [self]

    # the repr and the str methods were removed in the master/prototype_jobst1
    # Do we really don't want them anymore?
    def __repr__(self):
        return ('Process taxon object')

    def __str__(self):
        return repr(self)

    def set_value(self, variable, value):
        assert isinstance(variable, variable.Variable), \
            "variable must be a Variable object"
        variable.set_value(self, value)

    def assert_valid(self):
        """Make sure all variable values are valid.

        By calling assert_valid for all Variables

        """
        for v in self.variables:
            v.assert_valid(v.get_value(self))
