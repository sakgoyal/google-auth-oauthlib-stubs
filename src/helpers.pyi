from typing import Any, Mapping, Sequence, Tuple

from requests_oauthlib import OAuth2Session
from google.oauth2.credentials import Credentials

def session_from_client_config(
    client_config: Mapping[str, Any], scopes: Sequence[str], **kwargs: Any
) -> Tuple[OAuth2Session, Mapping[str, Any]]: ...
def session_from_client_secrets_file(
    client_secrets_file: str, scopes: Sequence[str], **kwargs: Any
) -> Tuple[OAuth2Session, Mapping[str, Any]]: ...
def credentials_from_session(
    session: OAuth2Session, client_config: Mapping[str, Any] | None = ...
) -> Credentials: ...
