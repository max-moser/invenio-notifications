# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-FileCopyrightText: 2026 TU Wien.
# SPDX-License-Identifier: MIT

"""Backend generators for notifications."""

from abc import ABC, abstractmethod

from ...backends.email import EmailNotificationBackend


class RecipientBackendGenerator(ABC):
    """Backend generator for a notification."""

    @abstractmethod
    def __call__(self, notification, recipient, backends):
        """Update required recipient information and add backend ID."""
        raise NotImplementedError()


class EmailBackendGenerator(RecipientBackendGenerator):
    """Backend generator for adding the email backend."""

    def __call__(self, notification, recipient, backends):
        """Add email backend ID to backends."""
        backend_id = EmailNotificationBackend.id
        backends.append(backend_id)
        return backend_id


UserEmailBackend = EmailBackendGenerator
"""Alias for backwards-compatibility."""
