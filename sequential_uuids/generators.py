import os
import sys
from uuid import UUID
import datetime as dt


def uuid_time_nextval(interval_length=60, interval_count=65536):
    """Generates sequential UUIDs using current time.

    The timestamp-based sequential UUID generator defines the group size
    and group count based on data extracted from current timestamp.

    Args:
        interval_length (int): Number of seconds where UUIDs share
            the same prefix (60 seconds by default).
        interval_count (int): Prefix length. Determined by the number of
            intervals (65536 by default, i.e. 2B).

    Note:
        With default parameters the generator wraps around every ~45 days.

    Returns:
        UUID: Generated UUID object.
    """

    # Some basic sanity checks
    if interval_length < 1:
        raise ValueError('Length of interval must be a positive integer')

    if interval_count < 1:
        raise ValueError('Number of intervals must be a positive integer')

    uuid_len = 16
    uuid_bytes = bytearray()

    epoch_seconds = int(
        (dt.datetime.utcnow() - dt.datetime(1970, 1, 1)).total_seconds())
    block_id = int(epoch_seconds / interval_length).to_bytes(4, sys.byteorder)

    # Count the number of bytes to keep from the timestamp
    prefix_bytes = 0
    while interval_count > 1:
        interval_count /= 256
        prefix_bytes += 1

    # Copy the desired number of (least significant) bytes as prefix
    for idx in range(0, prefix_bytes):
        uuid_bytes.insert(idx, block_id[prefix_bytes - idx - 1])

    # Generate the remaining bytes as random
    rand_bytes = bytearray()
    rand_bytes += os.urandom(uuid_len - prefix_bytes)

    for idx in range(prefix_bytes, uuid_len):
        uuid_bytes.insert(idx, rand_bytes[idx - prefix_bytes])

    # Set the UUID version flags according to "version 4" (pseudorandom)
    # UUID, see http://tools.ietf.org/html/rfc4122#section-4.4

    # This does reduce the randomness a bit, because it determines the
    # value of certain bits, but that should be negligible (certainly
    # compared to the reduction due to prefix).

    # UUID v4 is probably the safest choice here. There is v1 which is
    # time-based, but it includes MAC address (which we don't use) and
    # works with very special timestamp (starting at 1582 etc.). So we
    # just use v4 and claim this is pseudorandom.
    uuid_bytes[6] = (uuid_bytes[6] & 0x0f) | 0x40  # time_hi_and_version
    uuid_bytes[8] = (uuid_bytes[8] & 0x3f) | 0x80  # clock_seq_hi_and_reserved

    return UUID(bytes=bytes(uuid_bytes))
