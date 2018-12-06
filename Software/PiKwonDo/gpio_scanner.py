#! /bin/env/python3
# David Wright
# Copyright 2017
# Written for Python 3.5.6
"""Scan hardware status for buttons and emit correct signal."""
import os
import time
import threading
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Not running on Pi")


class ButtonHandler(threading.Thread):
    """Detect desired signal from GPIO pin and emits signal after debounce."""

    def __init__(self, pin, func, edge='both'):
        """Initialize timing thread and input assignments."""
        super().__init__(daemon=True)

        self.edge = edge
        self.func = func
        self.pin = pin
        self.glitchtime = 0.00005  # 50 us
        self.lastpinval = GPIO.input(self.pin)
        self.glitch_lock = threading.Lock()
        if self.edge == 'rising':
            gpio_edge = GPIO.RISING
        elif self.edge == 'falling':
            gpio_edge = GPIO.FALLING

        GPIO.add_event_detect(pin, gpio_edge, callback=self)

    def __call__(self, *args):
        """Lock thread and start new timer."""
        if not self.glitch_lock.acquire(blocking=False):
            return

        glitch_timer = threading.Timer(
            self.glitchtime, self.glitch_done, args=args)
        glitch_timer.start()

    def glitch_done(self, *args):
        """Emit assigned signal when valid signal detected."""
        pinval = GPIO.input(self.pin)
        rising = (pinval == 0 and self.lastpinval == 1)
        falling = (pinval == 1 and self.lastpinval == 0)
        if ((rising and (self.edge in ['falling', 'both'])) or
                (falling and (self.edge in ['rising', 'both']))):
            self.func(*args)

        self.lastpinval = pinval
        self.glitch_lock.release()


class PeriodicActionThread(threading.Thread):
    """Perform an action on a regular repeating schedule."""

    def __init__(self, function, period):
        """Start thread and setup settings."""
        super().__init__()
        self.function = function
        self.lock = threading.Lock()
        self.period = period/1000
        self.step()

    def step(self):
        """Perform desired action in thread-safe way."""
        if self.lock.acquire(blocking=False):
            self.function()
            self.lock.release()
        self.timer = threading.Timer(self.period, self.step)
        self.timer.start()


class HardwareConfiguration():
    """Configure pins for each generation of hardware."""

    def __init__(self):
        """Set class variables."""
        self.load_pins = False
        self.clock_pins = False
        self.data_pins = False
        # cluster clock, step, and data pins
        self.set_pinout()
        self.setup_gpio()

    def set_pinout(self):
        """Assign pins to circuit expectations."""
        j0_clk_pin = 2
        j0_load_pin = 3
        j0_dat_pin = 4

        j1_clk_pin = 17
        j1_load_pin = 27
        j1_dat_pin = 22

        j2_clk_pin = 10
        j2_load_pin = 9
        j2_dat_pin = 11

        # timer
        t_load_pin = 19
        t_clk_pin = 6
        t_dat_pin = 26

        self.load_pins = [j0_load_pin, j1_load_pin, j2_load_pin, t_load_pin]
        self.clock_pins = [j0_clk_pin, j1_clk_pin, j2_clk_pin, t_clk_pin]
        self.data_pins = [j0_dat_pin, j1_dat_pin, j2_dat_pin, t_dat_pin]

    def setup_gpio(self):
        """Set GPIO pin numbering scheme and pin initialization."""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        initialize_pins(self.load_pins)
        initialize_pins(self.clock_pins)
        initialize_pins(self.data_pins)


class HardwareControllerScanner():
    """Monitor hardware status by regular sweep scans."""

    try:
        import RPi.GPIO as GPIO
    except ImportError:
        print("Not running on raspberry Pi.")

    def __init__(self):
        """Set initial pin numbers and class values."""
        name = os.uname()
        self.running_raspi = name[1] == "raspberrypi"

        self.target_queue = None
        # last meaningful bit in the judge controller is the 13th
        self.bits_to_scan = 10
        self.scan_period = 5  # ms
        if self.running_raspi:
            self.pinout = HardwareConfiguration()
        self.pin_change_signal_array = None

        self.old_bits = False

        _ = PeriodicActionThread(self.step, self.scan_period)

    @property
    def pin_change_signals(self):
        """Return array of button_signal-signal matrix."""
        return self.pin_change_signal_array

    def read_bits(self):
        """Read one bit from each data input pin."""
        result = [GPIO.input(pin) for pin in self.pinout.data_pins]
        return result

    def load_data(self):
        """Load data into shift registers."""
        for pin in self.pinout.load_pins:
            pulse_gpio_pin(pin)

    def shift_data(self):
        """Cycle the clock pin on each controller."""
        for pin in self.pinout.clock_pins:
            pulse_gpio_pin(pin)

    def scan_bits(self):
        """Read all data from controllers."""
        result = []
        # send load signal
        self.load_data()
        # Read bits from all controllers
        for _ in range(0, self.bits_to_scan):
            milliseconds(0.1)  # Wait for signals to stabilize
            result.append(self.read_bits())
            # Read a single bit from each of controllers
            self.shift_data()
        return result

    def step(self):
        """Cycle bit scanning and detects changes."""
        if self.running_raspi is True:
            new_bits = self.scan_bits()
        if self.old_bits and self.running_raspi:
            changes = compare_bits(self.old_bits, new_bits)
            changed = is_nonzero(changes)
            if changed:
                print(new_bits)
                # time = -1
                # if self.target_queue is not None:
                # self.target_queue.put(newBits)
                # self.bit_changed.emit(time,changes)
        self.old_bits = new_bits

    def __del__(self):
        """Cleanup GPIO settings on close."""
        GPIO.cleanup()  # Clean up


class BitDecoder():
    """Correlate button press events to signals to emit."""

    def __init__(self, pikwondo):
        """Create matrix to lookup correct signal to emit."""
        self.main_process = pikwondo
        bits = 13
        controllers = 4
        for _ in range(0, bits):
            for _ in range(0, controllers):
                pass
        # [pin1,pin2,pin3...]
        # [bit1,bit1,bit1...]
        # [bit2,bit2,bit2...]
        # [bit3,bit3,bit3...]
        # where each element is a touple of rising and falling signals
        # or rising is 1, falling is -1, and
        self.pin_change_signal_array = [[1, 0, -1], [0, 0, 0]]

        # connect(lambda: self.main_process.redPoint(1))

    @property
    def pin_signal_array(self):
        """Return pin change signal array, or calculate it."""
        return self.pin_change_signal_array

    def __del__(self):
        """Cleanup gpio pin statuses on close."""
        # GPIO.cleanup() # Clean up
        # self.wait()


def initialize_pins(pins, pin_type='output'):
    """Set pinmode for list of GPIO pin numbers."""
    for pin in pins:
        if pin_type == 'output':
            GPIO.setup(pin, GPIO.OUT)
        elif pin_type == 'input':
            GPIO.setup(pin, GPIO.IN)


def pulse_gpio_pin(pin):
    """Set a gpio pin high and low, with appropriate delay."""
    GPIO.output(pin, GPIO.HIGH)
    milliseconds(0.2)
    GPIO.output(pin, GPIO.LOW)


def milliseconds(duration):
    """Delay for desired number of milliseconds."""
    time.sleep(0.001*duration)


def compare_bits(olds, news):
    """Subtract 2D list to determine changes to bit state."""
    rows = len(olds)
    cols = len(olds[0])
    delta = [[0] * cols for i in range(rows)]
    for i in range(0, rows):
        for j in range(0, cols):
            delta[i][j] = news[i][j] - olds[i][j]
    return delta


def is_nonzero(delta):
    """Return True if any element of 2D list is nonzero."""
    nonzero = False
    for row in delta:
        for element in row:
            if element != 0:
                nonzero = True
    return nonzero
