# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Notifications base backend module."""

from .builders import NotificationBuilder
from .filters import KeyRecipientFilter, RecipientFilter
from .generators import (
    ConditionalRecipientGenerator,
    ContextGenerator,
    EmailBackendGenerator,
    EntityResolverContextGenerator,
    RecipientBackendGenerator,
    RecipientGenerator,
)

__all__ = (
    "ConditionalRecipientGenerator",
    "ContextGenerator",
    "EmailBackendGenerator",
    "EntityResolverContextGenerator",
    "KeyRecipientFilter",
    "NotificationBuilder",
    "RecipientBackendGenerator",
    "RecipientFilter",
    "RecipientGenerator",
)
