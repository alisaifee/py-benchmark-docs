import hashlib
import mmh3

import pytest


@pytest.mark.parametrize(
    "function",
    [mmh3.hash, hashlib.md5, hashlib.blake2s, hashlib.blake2b, hashlib.sha512, hashlib.shake_256],
)
@pytest.mark.benchmark
def test_hash(benchmark, function):
    benchmark(function, b"data")
