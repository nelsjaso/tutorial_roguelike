# Following tutorial on youtube by 'Barry Peddycord III'

import curses
import sys
import traceback

stdscr = None

# Single instance of a game.  Maps, data, etc.
class Game(object):
	def __init__(self):
		pass

	def step(self):

		running = True
		x,y = 0,0

		while running:
			c = stdscr.getch()

			if c == curses.KEY_UP:
				y -= 1
			elif c == curses.KEY_DOWN:
				y += 1
			elif c == curses.KEY_LEFT:
				x -= 1
			elif c == curses.KEY_RIGHT:
				x += 1
			elif c == ord('q'):
				running = False

			if c != -1:	
				stdscr.clear()
				stdscr.addch(y,x,'@')


	# runs an interactive seesion of our game with the player.
	def play(self):

		#init
		global stdscr
		stdscr = curses.initscr()
		curses.noecho()
		curses.cbreak()
		curses.curs_set(0)
		stdscr.keypad(1)
		stdscr.timeout(0)

		try:
			self.step()
			
		except:
			curses.nocbreak()
			stdscr.timeout(0)
			stdscr.keypad(0)
			curses.echo()
			curses.endwin()

			print(traceback.format_exc())
			sys.exit(-1)
		
		#cleanup
		curses.nocbreak()
		curses.curs_set(1)
		stdscr.timeout(0)
		stdscr.keypad(0)
		curses.echo()
		curses.endwin()
			

	
