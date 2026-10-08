"""Reproducible parameter audit of OpenAI's explicit exact DFT recurrence.

No third-party dependencies. This evaluates/proves bounds; it does not execute
the astronomically large Fourier network or validate the whole upstream proof.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import comb
import json
from pathlib import Path


@dataclass(frozen=True)
class Network:
    h: int
    v: int
    neighbors: int
    m: int
    wires: int
    saving: int

    @classmethod
    def make(cls, h):
        if h < 7:
            raise ValueError("h >= 7 ensures coordinates outside two triple supports")
        v = comb(h, 3)
        neighbors = comb(h - 3, 3) + 3 * (h - 3)
        wires = 2 * v**3 + 3 * v**2 * (v * neighbors + h + 1)
        saving = 2 * v**2 * (v - 3 * h * (h + 1))
        return cls(h, v, neighbors, h**3, wires, saving)

    def roles(self, padded=True):
        return 1 << (self.wires - 1).bit_length() if padded else self.wires

    def epsilon(self, padded=True):
        return F(self.saving, self.roles(padded) * self.m)


def log_unit_interval(x, terms=40):
    """Exact rational enclosure for ln(x), 1 <= x <= 2."""
    assert 1 <= x <= 2
    z = (x - 1) / (x + 1)
    lo = 2 * sum((z ** (2*j + 1) / (2*j + 1) for j in range(terms)), F(0))
    tail = 2 * z ** (2*terms + 1) / ((2*terms + 1) * (1-z*z))
    return lo, lo + tail


def log_integer(x):
    k = x.bit_length() - 1
    a, b = log_unit_interval(F(x, 1 << k))
    c, d = log_unit_interval(F(2))
    return a + k*c, b + k*d


def saving_interval(network, padded=True):
    """Certified interval for 1-theta = -ln(1-epsilon)/ln(m)."""
    e = network.epsilon(padded)
    assert 0 < e < 1
    lo = sum((e**j / j for j in range(1, 5)), F(0))
    hi = lo + e**5 / (5 * (1-e))
    log_lo, log_hi = log_integer(network.m)
    return lo / log_hi, hi / log_lo


def decimal(x):
    with localcontext() as ctx:
        ctx.prec = 65
        return str(Decimal(x.numerator) / Decimal(x.denominator))

