from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None


class CIF(BaseModel):
    loanid: str = None
    cif: str  = None
    tenor: int  = None
    amount: int  = None
    # limit: int  = None
    loan_type : str = None
    loan_status : str = None
    cif: str  = None
    loan_tenure : int = None
    loan_amount: int  = None
    interest : int = None
    idno : str = None
    fname : str = None
    lname : str = None
    dob : str = None
    gender : str = None
    marital_status : str = None
    income : int = None
    phone : str = None
    email : str = None
    isphoneverified : str = None
    isemailverified : str = None
    createdate : str = None
    updatedate : str = None
    source : str = None

class ResponseCIF(BaseModel):
    cif_list: List[CIF]