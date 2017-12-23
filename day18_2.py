#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import threading
import queue
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
                except queue.Empty:
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


class Day(day18.Day):
    def __init__(self, *args, **kwargs):
        super(Day, self).__init__(*args, **kwargs)
        self.count = 0
        
    def on_send(self):
        self.count += 1

    def on_send_nop(self):
        pass

    def parse(self, input):
        input_lists = day18.to_lists(input)

        prog0_to_prog1_queue = queue.Queue()
        prog1_to_prog0_queue = queue.Queue()

        prog0_hang_event = threading.Event()
        prog1_hang_event = threading.Event()

        program0 = ConcurrentProgram(input_lists, 0, prog0_to_prog1_queue, prog1_to_prog0_queue, prog0_hang_event, prog1_hang_event, self.on_send_nop)
        program1 = ConcurrentProgram(input_lists, 1, prog1_to_prog0_queue, prog0_to_prog1_queue, prog1_hang_event, prog0_hang_event, self.on_send)
        
        return program0,program1

    def run(self, programs):
        program0,program1 = programs

        program0.run_thread()
        program1.run_thread()

        program0.join()
        program1.join()

        return self.count

if __name__ == '__main__':
    Day(18).main()
