import requests
import os
import json
from typing import Optional

   

def normalize_zip_code(state: Optional[str], city: Optional[str], zip_code: Optional[str]) -> Optional[str]:
    if zip_code is not None:
        return zip_code
    
    if state is None or city is None:
        return None
    
    
    response = requests.get(
        url=f"https://api.sipcode.dev/state/{state}/city/{city}/zip_codes"
    )
    results = json.loads(response.content)
    if len(results.get("zip_codes")) == 0:
        return None
    
    return results.get("zip_codes")[0]
