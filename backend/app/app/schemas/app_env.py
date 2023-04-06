from enum import Enum


class Environment(str, Enum):
    LOCAL: str = "LOCAL"
    DEVELOPMENT: str = "DEVELOPMENT"
    STAGING: str = "STAGING"
    TESTING: str = "TESTING"
    PRODUCTION: str = "PRODUCTION"


class Module(str, Enum):
    AUTHENTICATION: str = "Authentication"
    SUBSCRIPTION: str = "Subscription"
    SYSTEM: str = "System"
    USER: str = "User"
