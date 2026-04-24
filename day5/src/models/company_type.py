#create company type enum
from enum import Enum
class CompanyType(Enum):
    PRIVATE = "Private"
    PUBLIC = "Public"
    NON_PROFIT = "Non-Profit"