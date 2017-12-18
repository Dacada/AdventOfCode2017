#!/usr/bin/python
# -*- encoding:utf-8 -*-

import threading
import Queue
import day18

class ConcurrentProgram(day18.Program):
    def __init__(self, instructions, id, producer_queue, consumer_queue, own_event, other_event, on_send):
        super(ConcurrentProgram, self).__init__(instructions)
        self._registers.set('p', id)
        self._queue_out = producer_queue
        self._queue_in = consumer_queue
        self._self_waiting = own_event
        self._other_waiting = other_event
        self._on_send = on_send
        self._thread = None

    def _snd(self, x):
        val = self._get_value(x)
        self._queue_out.put(val)
        self._on_send()

    def _rcv(self, x):
        if self._other_waiting.is_set():
            self._self_waiting.set()
            raise day18.EndProgram
        else:
            done = False
            while not done:
                try:
                    in_val = self._queue_in.get(timeout = 0.1)
                except Queue.Empty:
                    self._self_waiting.set()
                    if self._other_waiting.is_set():
                        raise day18.EndProgram
                else:
                    self._self_waiting.clear()
                    done = True
            self._registers.set(x, in_val)
            

    def run_thread(self):
        self._thread = threading.Thread(target=self.run)
        self._thread.start()

    def join(self):
        self._thread.join()

count = 0
def on_send():
    global count
    count += 1

def on_send_nop():
    pass

def run(input):
    input_lists = day18.to_lists(input)

    prog0_to_prog1_queue = Queue.Queue()
    prog1_to_prog0_queue = Queue.Queue()

    prog0_hang_event = threading.Event()
    prog1_hang_event = threading.Event()

    program0 = ConcurrentProgram(input_lists, 0, prog0_to_prog1_queue, prog1_to_prog0_queue, prog0_hang_event, prog1_hang_event, on_send_nop)
    program1 = ConcurrentProgram(input_lists, 1, prog1_to_prog0_queue, prog0_to_prog1_queue, prog1_hang_event, prog0_hang_event, on_send)

    program0.run_thread()
    program1.run_thread()

    program0.join()
    program1.join()

    return count
day18.run = run

if __name__ == '__main__':
    day18.main()
