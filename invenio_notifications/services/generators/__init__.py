# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-FileCopyrightText: 2026 TU Wien.
# SPDX-License-Identifier: MIT

"""Generators for notification context."""

from .backends import EmailBackendGenerator, RecipientBackendGenerator, UserEmailBackend
from .context import ContextGenerator, EntityResolve, EntityResolverContextGenerator
from .recipients import ConditionalRecipientGenerator, RecipientGenerator

__all__ = (
    "ConditionalRecipientGenerator",
    "ContextGenerator",
    "EmailBackendGenerator",
    "EntityResolve",
    "EntityResolverContextGenerator",
    "RecipientBackendGenerator",
    "RecipientGenerator",
    "UserEmailBackend",
)
