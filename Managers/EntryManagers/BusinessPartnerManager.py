from Entries.BusinessPartner import BusinessPartner
from Utils.Singleton import Singleton


class BusinessPartnerManager(metaclass=Singleton):
    """
    Singleton class that holds data for all BusinessPartners
    """
    def __init__(self, data: list[BusinessPartner|object]=None):
        """
        Constructor for BusinessPartnerManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    def names(self) -> list[str]:
        names = []
        for business_partner in self.data:
            names.append(business_partner.company)
        return names



def create(data: list[BusinessPartner|object]) -> BusinessPartnerManager:
    """
    Constructor for BusinessPartnerManager, do not use this to access existing singleton, use __init__ method instead
    :param data: list of BusinessPartner objects
    :return: returns created singleton instance for BusinessPartnerManager
    """
    return BusinessPartnerManager(data)