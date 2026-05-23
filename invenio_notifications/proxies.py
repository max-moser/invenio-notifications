# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Proxies for accessing the currently instantiated notifications extension."""

from flask import current_app
from werkzeug.local import LocalProxy

current_notifications = LocalProxy(
    lambda: current_app.extensions["invenio-notifications"]
)
"""Proxy for the instantiated notifications extension."""

current_notifications_manager = LocalProxy(lambda: current_notifications.manager)
"""Proxy for the instantiated notifications manager."""
