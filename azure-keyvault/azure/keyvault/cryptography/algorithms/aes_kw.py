from ..algorithm import EncryptionAlgorithm, Algorithm
from ..transform import CryptoTransform
from cryptography.hazmat.primitives.keywrap import aes_key_wrap, aes_key_unwrap
from cryptography.hazmat.backends import default_backend


class _AesKeyWrapTransform(CryptoTransform):
    def __init__(self, key):
        self._key = key

    def transform(self, data):
        aes_key_wrap(self._key, data, default_backend())


class _AesKeyUnwrapTransform(CryptoTransform):
    def __init__(self, key):
        self._key = key

    def transform(self, data):
        aes_key_unwrap(self._key, data, default_backend())


class _AesKeyWrap(EncryptionAlgorithm):
    _key_size = 256

    @property
    def key_size(self):
        return self._key_size

    @property
    def key_size_in_bytes(self):
        return self._key_size >> 3

    def create_encryptor(self, key):
        key = self._validate_input(key)
        return _AesKeyWrapTransform(key)

    def create_decryptor(self, key):
        key = self._validate_input(key)
        return _AesKeyUnwrapTransform(key)

    def _validate_input(self, key):
        if not key:
            raise ValueError('key')
        if len(key) < self.key_size_in_bytes:
            raise ValueError('key must be at least %d bits' % self.key_size)

        return key[:self.key_size_in_bytes]


class AesKw128(_AesKeyWrap):
    _key_size = 128
    _name = 'A128KW'


class AesKw192(_AesKeyWrap):
    _key_size = 192
    _name = 'A192KW'


class AesKw256(_AesKeyWrap):
    _key_size = 256
    _name = 'A256KW'


AesKw128.register()
AesKw192.register()
AesKw256.register()
