#!/usr/bin/env python3
"""Defines mixins and a Dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Make the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Make the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon with swimming and flying abilities."""

    def roar(self):
        """Make the dragon roar."""
        print("The dragon roars!")
