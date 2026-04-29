#create enum for account type
from enum import Enum
class AccountType(str, Enum):
    SAVINGS = "SAVINGS"
    CURRENT = "CURRENT"
    DEMAT = "DEMAT"
    