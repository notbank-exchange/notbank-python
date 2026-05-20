from dataclasses import dataclass
from typing import Optional

from notbank_python_sdk.constants import (
    ArProvince,
    BrState,
    ChileanCommune,
    CivilStatus,
    Gender,
    IdentityType,
    Profession,
)


@dataclass
class RegisterAdvancedUserRequest:
    first_name: str
    last_name: str
    phone_number: str
    profession: Profession
    gender: Gender
    birthdate: str
    citizenship: str
    identity_type: IdentityType
    identity_number: str
    identity_country: str
    address_country: str
    address_city: str
    address_street: str
    address_postal_code: str
    pep: bool
    subject_comply: bool
    is_public_servant: bool
    # AR-only
    address_province: Optional[ArProvince] = None
    # BR-only
    address_district: Optional[str] = None
    address_number: Optional[str] = None
    address_state: Optional[BrState] = None
    address_complement: Optional[str] = None
    # CL-only
    address_comune: Optional[ChileanCommune] = None
    # PE-only
    civil_status: Optional[CivilStatus] = None
    spouse_name: Optional[str] = None
    pep_position: Optional[str] = None
    pep_institution: Optional[str] = None
    pep_links_description: Optional[str] = None
    is_pep_family_member: Optional[bool] = None
    pep_family_member_name: Optional[str] = None
    pep_family_member_relation: Optional[str] = None
