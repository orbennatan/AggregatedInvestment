from BaseClass import BaseClass

"""
A broker class attempting to encapsulate all brokers in a single API. We only know about IBKR when writing
this class so it is probably heavily biased towared IBKR.
"""


class AggregatorBase(BaseClass):
    BrokerProvider = 'BrokerProvider'
    Accounts = 'Accounts'
    Owners = 'Owners'