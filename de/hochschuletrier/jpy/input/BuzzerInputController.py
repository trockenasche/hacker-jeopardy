__author__ = 'miko'
import sys
from de.hochschuletrier.jpy.console.JPYLogger import JPYLogger
from de.hochschuletrier.jpy.input.InputController import InputController


#


class BuzzerInputController(InputController):
	def __init__(self, root):
		if not (root.debug):
			import RPIO
		self.root = root
		self.logger = JPYLogger(self)
		self.logger.log("BuzzerInputController initialisiert")
		self.blockBuzzer = False
		mainWindow = root.mainWindow

		if (root.debug):
			return
		RPIO.add_interrupt_callback(25, lambda x, y: self.pressedBuzzer(trigger=0), edge='rising',
									pull_up_down=RPIO.PUD_UP)
		RPIO.add_interrupt_callback(8, lambda x, y: self.pressedBuzzer(trigger=1), edge='rising',
									pull_up_down=RPIO.PUD_UP)
		RPIO.add_interrupt_callback(7, lambda x, y: self.pressedBuzzer(trigger=2), edge='rising',
									pull_up_down=RPIO.PUD_UP)

		RPIO.wait_for_interrupts(threaded=True)