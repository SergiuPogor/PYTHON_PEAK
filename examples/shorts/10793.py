from dataclasses import dataclass, field
from typing import List
import threading

# Using a frozen dataclass to enforce immutability
@dataclass(frozen=True)
class UserConfig:
    username: str
    permissions: List[str] = field(default_factory=lambda: ["read"])

# Instance that cannot be changed
config = UserConfig(username="admin", permissions=["read", "write", "execute"])

# Trying to modify will raise a FrozenInstanceError
try:
    config.username = "superadmin"  # Raises an error
except Exception as e:
    print(f"Error: {e}")

# Example: Multi-threaded read-only access to UserConfig
def read_config(config_obj: UserConfig):
    print(f"Reading config for user: {config_obj.username}")

# Creating threads for secure read access
threads = [threading.Thread(target=read_config, args=(config,)) for _ in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# Demonstrating safety in shared multi-threaded environments
@dataclass(frozen=True)
class APIConfig:
    base_url: str
    api_key: str

# Immutable API config for security-sensitive applications
api_config = APIConfig(base_url="https://api.example.com", api_key="abcdef123456")

# No risk of accidental API key modification
print(f"Base URL: {api_config.base_url}, API Key: {api_config.api_key[:5]}...")