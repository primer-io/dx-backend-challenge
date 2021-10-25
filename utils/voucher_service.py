"""
This is an example of how interactions with a real voucher service could work.

Please use this for the purposes of this challenge.
"""

VOUCHER_CODES_DB = {
    "primer-voucher-1": 200,
    "primer-voucher-2": 450,
    "primer-voucher-3": 0,
    "primer-voucher-4": 100
}


def validate_voucher_code(voucher_code: str) -> bool:
    return voucher_code in VOUCHER_CODES_DB


def apply_voucher_code(voucher_code: str) -> int:
    if not validate_voucher_code(voucher_code):
        raise ValueError("The voucher code you provided is invalid")

    return VOUCHER_CODES_DB[voucher_code]
