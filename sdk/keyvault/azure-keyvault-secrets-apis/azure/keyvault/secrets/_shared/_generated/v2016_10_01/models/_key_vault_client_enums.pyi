# Stubs for azure.keyvault.secrets._shared._generated.v2016_10_01.models._key_vault_client_enums (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from enum import Enum

class JsonWebKeyType(str, Enum):
    ec: str = ...
    ec_hsm: str = ...
    rsa: str = ...
    rsa_hsm: str = ...
    oct: str = ...

class JsonWebKeyCurveName(str, Enum):
    p_256: str = ...
    p_384: str = ...
    p_521: str = ...
    secp256_k1: str = ...

class DeletionRecoveryLevel(str, Enum):
    purgeable: str = ...
    recoverable_purgeable: str = ...
    recoverable: str = ...
    recoverable_protected_subscription: str = ...

class KeyUsageType(str, Enum):
    digital_signature: str = ...
    non_repudiation: str = ...
    key_encipherment: str = ...
    data_encipherment: str = ...
    key_agreement: str = ...
    key_cert_sign: str = ...
    c_rl_sign: str = ...
    encipher_only: str = ...
    decipher_only: str = ...

class ActionType(str, Enum):
    email_contacts: str = ...
    auto_renew: str = ...

class JsonWebKeyOperation(str, Enum):
    encrypt: str = ...
    decrypt: str = ...
    sign: str = ...
    verify: str = ...
    wrap_key: str = ...
    unwrap_key: str = ...

class JsonWebKeyEncryptionAlgorithm(str, Enum):
    rsa_oaep: str = ...
    rsa_oaep_256: str = ...
    rsa1_5: str = ...

class JsonWebKeySignatureAlgorithm(str, Enum):
    ps256: str = ...
    ps384: str = ...
    ps512: str = ...
    rs256: str = ...
    rs384: str = ...
    rs512: str = ...
    rsnull: str = ...
    es256: str = ...
    es384: str = ...
    es512: str = ...
    ecdsa256: str = ...