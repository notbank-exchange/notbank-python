

from concurrent.futures import ThreadPoolExecutor
from time import sleep
import unittest
from notbank_python_sdk.websocket.synched_var import SynchedValue

from notbank_python_sdk.websocket.websocket_restarter.pinger import Pinger


class Counter:
    _count: SynchedValue[int]

    def __init__(self):
        self._count = SynchedValue.create(0)

    def count_up(self) -> None:
        current_count = self._count.get()
        self._count.set(current_count+1)

    def get_count(self) -> int:
        return self._count.get()

    def reset(self) -> None:
        self._count.set(0)


def force_timeout(ping_timeout: int) -> None:
    sleep(ping_timeout*2)


class TestAddWhiteListedAddresses(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @unittest.skip("slow")
    def test_pings_until_stop(self):
        ping_interval_seconds = 2
        counter = Counter()
        pinger = Pinger(
            executor=ThreadPoolExecutor(1, "pinger"),
            stop_requested=SynchedValue.create(False),
            ping_interval_seconds=ping_interval_seconds,
            ping_timeout=1
        )
        pinger.restart(
            ping_fn=counter.count_up,
            reconnect_fn=counter.reset
        )
        sleep(ping_interval_seconds*2+1)
        pinger.stop()
        sleep(ping_interval_seconds*2+1)
        self.assertEqual(counter.get_count(), 2)

    @unittest.skip("slow")
    def test_reconnect_on_ping_timeout(self):
        counter = Counter()
        ping_timeout = 1
        ping_interval_seconds = 2
        pinger = Pinger(
            executor=ThreadPoolExecutor(1, "pinger"),
            stop_requested=SynchedValue.create(False),
            ping_interval_seconds=ping_interval_seconds,
            ping_timeout=ping_timeout
        )
        def timeout_on_third_call() -> None:
            counter.count_up()
            if counter.get_count() >= 3:
                force_timeout(ping_timeout)
                return
        pinger.restart(
            ping_fn=timeout_on_third_call,
            reconnect_fn=counter.reset
        )
        sleep(ping_interval_seconds*3+2)
        pinger.stop()
        self.assertEqual(counter.get_count(), 0)


if __name__ == "__main__":
    unittest.main()
