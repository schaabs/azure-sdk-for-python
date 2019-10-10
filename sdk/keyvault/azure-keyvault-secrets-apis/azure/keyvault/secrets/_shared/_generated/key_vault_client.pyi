# Stubs for azure.keyvault.secrets._shared._generated.key_vault_client (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from azure.profiles.multiapiclient import MultiApiClientMixin
from typing import Any, Optional

class KeyVaultClient(MultiApiClientMixin):
    DEFAULT_API_VERSION: str = ...
    LATEST_PROFILE: Any = ...
    def __init__(self, credentials: Any, pipeline: Optional[Any] = ..., api_version: Optional[Any] = ..., aio: bool = ..., profile: Any = ...) -> None: ...
    @staticmethod
    def get_configuration_class(api_version: Any, aio: bool = ...): ...
    @property
    def models(self): ...
    def __aenter__(self, *args: Any, **kwargs: Any): ...
    def __enter__(self, *args: Any, **kwargs: Any): ...
    def __aexit__(self, *args: Any, **kwargs: Any): ...
    def __exit__(self, *args: Any, **kwargs: Any): ...
    def __getattr__(self, name: Any): ...
    def __setattr__(self, name: Any, attr: Any) -> None: ...