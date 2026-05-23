# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Notifications base backend module."""

from .base import NotificationBackend
from .email import EmailNotificationBackend

__all__ = (
    "EmailNotificationBackend",
    "NotificationBackend",
)
