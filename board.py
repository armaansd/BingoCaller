import os
import random
import time
import select
import sys
from sayings import calls

class Board:
	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		self.table = []
		self.occur = set()

	def populate(self):
		count = 1
		for x in range(self.rows):
			inner = []
			for y in range(self.cols):
				inner.append(count)
				self.occur.add(count)
				count += 1
			self.table.append(inner)

	def print_all(self):
		for x in range(self.rows):
			for y in range(self.cols):
				if self.table[x][y] < 10: 
					print(self.table[x][y], end = '  ')
				else:
					print(self.table[x][y], end = ' ')
			print()

	def print(self):
		for x in range(self.rows):
			for y in range(self.cols):
				if self.table[x][y] not in self.occur:
					if self.table[x][y] < 10: 
						print(self.table[x][y], end = '  ')
					else:
						print(self.table[x][y], end = ' ')
				else:
					print('--', end = ' ')
			print()

if __name__ == '__main__':
	while True:
		try:
			size = int(input('Please enter the maximum number: '))
			if size <= 90:
				break
			else:
				print('Must be less than or equal to 90')
		except:
			print('Invalid input')
			continue
	r,c = size//10,10
	if size%10 > 0:
		r += 1
	game = Board(r,c)
	game.populate()
	game.print_all()
	wait, manual = 5, False
	while True:
		game_type = input('Please enter reading mechanism: Manual (M/m) or Automatic (A/a): ')
		if game_type.lower() == 'm' or game_type.lower() == 'manual':
			manual = True
			break
		elif game_type.lower() == 'a' or game_type.lower() == 'auto' or game_type.lower() == 'automatic':
			while True:
				try:
					wait = int(input('Please enter a wait time in seconds: '))
				except:
					print('Invalid input')
					continue
				if 30 >= wait >= 1:
					break

			break

	print('\nGame is ready!')
	if manual:
		print('Type: manual')
	else:
		print('Type: automatic ({} sec wait)'.format(wait))
	input('Return any key to begin... ')

	while game.occur:
		pick = random.sample(game.occur,1)
		game.occur.remove(pick[0])
		os.system('clear')
		print('number -> {}'.format(pick[0]))
		if not manual:
			print('\nReturn any key to pause...')
		os.system('say {} number {}, number {}'.format(calls[pick[0]], pick[0], pick[0]))

		if manual:
			looper = input('\nReturn any key to continue (q to quit)...')
			if looper.lower() == 'q':
				break
		else:
			inp = select.select([sys.stdin],[],[],wait)
			if inp[0]:
				input()
				extra = input('Return any key to reveal entire table of numbers (x to un-pause and q to quit)...')
				if extra == 'q':
					break
				elif extra != 'x':
					game.print()
					input('Return any key to continue...')

	print('Thank you for playing!')

		
