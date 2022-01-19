from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None


class CIF(BaseModel):
    loan_status: int = None,
    loan_amount: int = None,
    loan_tenure: int = None,
    interest: int = None,
    cif: int = None,
    idno: str = None,
    fname: str = None,
    lname: str = None,
    # dob: str = None,
    gender: str = None,
    marital: str = None,
    income: int = None,
    phone: str = None,
    email: str = None,
    isphoneverified: int = None,
    isemailverified: int = None,
    # createdate: str = None,
    # updatedate: str = None,
    source: str = None,

class Loan_by_Cif(BaseModel):
    # loan_tenure: int = None,
    # interest: int = None,
    cif: int = None,
    idno: str = None,
    fname: str = None,
    lname: str = None,
    # dob: str = None,
    gender: str = None,
    # marital: str = None,
    income: int = None,
    loan_amount: int = None,
    phone: str = None,
    email: str = None,
    # isphoneverified: int = None,
    # isemailverified: int = None,
    # createdate: str = None,
    # updatedate: str = None,
    source: str = None,


class ResponseCIF(BaseModel):
    cif_list: List[CIF]

class ResponseCIF1(BaseModel):
    cif_list: List[Loan_by_Cif]