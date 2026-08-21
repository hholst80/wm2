import errno
import unittest

import pytest

pytest.importorskip("pywayland")

from wm2 import _is_retryable_display_error


class DisplayErrorTests(unittest.TestCase):
    def test_eagain_is_retryable(self) -> None:
        error = RuntimeError(f"Failed with error: {errno.EAGAIN}")

        self.assertTrue(_is_retryable_display_error(error))

    def test_connection_errors_are_fatal(self) -> None:
        for error_number in (errno.EPIPE, errno.EPROTO):
            with self.subTest(error_number=error_number):
                error = RuntimeError(f"Failed with error: {error_number}")

                self.assertFalse(_is_retryable_display_error(error))


if __name__ == "__main__":
    unittest.main()
