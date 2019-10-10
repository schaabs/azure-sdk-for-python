# Stubs for azure.keyvault.secrets._shared.http_challenge_cache (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .http_challenge import HttpChallenge
from typing import Any

def get_challenge_for_url(url: Any): ...
def remove_challenge_for_url(url: Any) -> None: ...
def set_challenge_for_url(url: Any, challenge: Any) -> None: ...
def clear() -> None: ...