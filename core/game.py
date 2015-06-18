# Following tutorial on youtube by 'Barry Peddycord III'

from . import gfx
import curses
import sys
import traceback


# Single instance of a game.  Maps, data, etc.
class Game(object):
	def __init__(self):
		pass

	def step(self):

		running = True
		x,y = 0,0

		while running:
			c = gfx.scr().getch()

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
				gfx.scr().clear()
				gfx.scr().addch(y,x,'@')


	# runs an interactive seesion of our game with the player.
	def play(self):

		#init
		gfx.start()

		try:
			self.step()
			
		except:
			gfx.stop()
			print(traceback.format_exc())
			sys.exit(-1)
		
		#cleanup
		gfx.stop()
			

	
