from typing import Dict 

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):  
    """Convert text to initials.""" 

    def operate(self, text: str = None, params: Dict = None) -> str:
        """Convert text to initials.""" 
        if not text:
            return ""
        
        words = text.split()
        initials = '.'.join(word[0].upper() for word in words if word)
        return initials + '.' if initials else "" 

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"  

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize