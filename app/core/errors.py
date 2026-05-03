class AppError(Exception):
    """Base class for domain-level errors."""


class ConflictError(AppError):
    """Entity state conflicts with requested operation."""


class UnauthorizedError(AppError):
    """Authentication failed."""


class ForbiddenError(AppError):
    """User has no permission for operation."""


class NotFoundError(AppError):
    """Requested entity is missing."""


class ExternalServiceError(AppError):
    """External provider request failed."""
