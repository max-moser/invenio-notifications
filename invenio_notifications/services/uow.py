# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Unit of work for notifications."""

from invenio_records_resources.services.uow import Operation

from ..tasks import broadcast_notification


class NotificationOp(Operation):
    """A notification operation that sends notifications after transaction commit."""

    def __init__(self, notification):
        """Initialize operation."""
        self._notification = notification

    def on_post_commit(self, uow):
        """Start task to send notification."""
        broadcast_notification.delay(self._notification.dumps())
