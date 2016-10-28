# This file is part of pycopancore.
#
# Copyright (C) 2016 by COPAN team at Potsdam Institute for Climate
# Impact Research
#
# URL: <http://www.pik-potsdam.de/copan/software>
# License: MIT license

"""
Binary_Social_Learner is a subclass of 'Individual'. It defines a more specific
instance of Individual such that they can interact due to the ExploitLike
model.
"""

#
#  Imports
#
from .abstract_individual import Individual

#
#  Define class MicroAgents
#


class BinarySocialLearner(Individual):
    """
    Binary_Social_Learner is a subclass of 'Individual'. It defines a more
    specific instance of Individual such that they can interact due to
    the ExploitLike model.
    """

    #
    #  Definitions of internal methods
    #

    def __init__(self,
                 individual_identifier,
                 group_affilitation=None,
                 cell_affilitation=None,
                 individual_update_time=None,
                 individual_connection=[],
                 individual_strategy=None,
                 individual_rationality=None,
                 individual_harvest=None
                 ):

        """
        Initializes an instance of BinarySocialLearner:
        The objects of BinarySocialLearner define a more specific micro agent
        with parameters that are necessary to interact due to the ExploitLike
        model.

        Parameters
        ----------
        individual_identifier : integer
            This is a number which identifies each individual
        group_affiliation : integer
            This is a number which indicates to which group the individual is
            affiliated
        cell_affiliation : integer
            This is a number which indicates to which cell the individual is
            affiliated
        individual_update_time : float
            The individual_update_time assigns a time for each individual after
            that adaption and rewiring happens.
        individual_connection : list
             This list shows existing connections of the individual
        individual_strategy : integer
            Denotes the strategy of each individual (1: sus, 0: unsus)
        individual_rationality : float
            Parameter concerning the social imitation due to rational behaviour
        individual_harvest : float
            The harvest for each individual.
        """

        super(BinarySocialLearner, self).__init__(individual_identifier,
                                                  group_affilitation,
                                                  cell_affilitation,
                                                  individual_connection,
                                                  individual_update_time)

        self.individual_strategy = individual_strategy
        self.individual_rationality = individual_rationality
        self.individual_harvest = individual_harvest

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return (super(BinarySocialLearner, self).__str__() +
                ('individual_strategy % s, \
                 individual_rationality % s, \
                 individual_harvest % s'
                 ) % (
                self.individual_strategy,
                self.individual_rationality,
                self.individual_harvest)
                )

    def set_individual_strategy(self, individual_strategy):
        """
        A function to set the strategy of the SocialBinaryLeaner
        """
        self.individual_strategy = individual_strategy

    def set_individual_rationality(self, individual_rationality):
        """
        A function to set the rationality of the SocialBinaryLearner
        """
        self.individual_rationality = individual_rationality

    def set_individual_harvest(self, individual_harvest):
        """
        A function to set the harvest of each individual
        """

    #
    #  Definitions of further methods
    #

    def get_ingredients(self):
        """
        This function returns a list of tuples, each of the form (label, type,
        list of affected variables, specification). Entries of each tuple are
        specified in the following clarification

        Clarification
        -------------
        label : string
            The denotation of the dynamical system
        type : string
            The type of the dynamics. Can be either "explicit", "derived",
            "ODE", "step" or "event"
        list of affected variables: any dtype
            List of all variables that are affected from the specified dynamics
        specification : any dtype
            Further specifications that are necessary for the global
            integration (e.g. methods to solve the specified dynamics)
        """
        return []

