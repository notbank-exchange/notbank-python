from dataclasses import dataclass
from enum import Enum
from typing import Optional


class BankAccountKind(str, Enum):
    CORRIENTE = "corriente"
    VISTA = "vista"
    AHORRO = "ahorro"
    ELECTRONIC_CHECKBOOK = "electronic_checkbook"
    AR_CBU = "ar_cbu"
    AR_CVU = "ar_cvu"
    AR_ALIAS = "ar_alias "
    BR_CORRIENTE_FISICA = "br_corriente_fisica"
    BR_SIMPLE_FISICA = "br_simple_fisica"
    BR_CORRIENTE_JURIDICA = "br_corriente_juridica"
    BR_POUPANCA_FISICA = "br_poupanca_fisica"
    BR_POUPANCA_JURIDICA = "br_poupanca_juridica"
    BR_CAIXA_FACIL = "br_caixa_facil"
    BR_PIX = "br_pix"


class PixType(str, Enum):
    CPF = "CPF"
    CNPJ = "CNPJ"
    EMAIL = "Email"
    PHONE = "Phone"
    OTRO = "Otro"


@dataclass
class AddClientBankAccountRequest:
    country: str
    bank: str
    number: str
    kind: BankAccountKind
    pix_type: Optional[PixType] = None
    agency: Optional[str] = None
    dv: Optional[str] = None
    province: Optional[str] = None
