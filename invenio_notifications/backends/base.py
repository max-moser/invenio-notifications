# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Notification backend base class."""

from abc import ABC, abstractmethod


class NotificationBackend(ABC):
    """Base class for notification backends."""

    id = None
    """Unique ID of the backend."""

    @abstractmethod
    def send(self, notification, recipient):
        """Send the notification message."""
        raise NotImplementedError()
