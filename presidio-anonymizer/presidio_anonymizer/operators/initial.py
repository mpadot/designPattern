from typing import Dict 

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):  
    """Convert text to initials.""" 

    def operate(self, text: str = None, params: Dict = None) -> str:
        """Convert text to initials (e.g., 'John Smith' -> 'J. S.', '@abc' -> '@A.')."""
        if not text:
            return ""
        
        words = text.split()
        initials_list = []
        
        for word in words:
          
            prefix = ""
            initial = ""
            
            for char in word:
                if char.isalnum():
                    initial = char.upper()
                    break
                else:
                    prefix += char
            
            if initial:
                initials_list.append(prefix + initial)
        
        return '. '.join(initials_list) + '.' if initials_list else ""

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"  

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize