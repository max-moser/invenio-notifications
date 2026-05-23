# SPDX-FileCopyrightText: 2023 Graz University of Technology.
# SPDX-FileCopyrightText: 2026 TU Wien.
# SPDX-License-Identifier: MIT

"""Context generators for notifications."""

from abc import ABC, abstractmethod

from invenio_records.dictutils import dict_lookup, dict_set

from ...registry import EntityResolverRegistry


class ContextGenerator(ABC):
    """Payload generator for a notification."""

    @abstractmethod
    def __call__(self, notification):
        """Update notification context in-place."""
        raise NotImplementedError()


class EntityResolverContextGenerator(ContextGenerator):
    """Payload generator for a notification using the entity resolvers."""

    def __init__(self, key):
        """Constructor."""
        self.key = key

    def __call__(self, notification):
        """Update required recipient information and add backend ID."""
        entity_ref = dict_lookup(notification.context, self.key)
        entity = EntityResolverRegistry.resolve_entity(entity_ref)
        dict_set(notification.context, self.key, entity)
        return notification


EntityResolve = EntityResolverContextGenerator
"""Alias for backwards-compatibility."""
