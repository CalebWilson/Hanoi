"""
	Solve the famous Towers of Hanoi problem using recursion.
"""

from time import sleep  # rendering delay for watchability
import sys              # command line arguments

# get parameters from command line
try:
	DELAY = 1                                               # animation speed
	SIZE  = int(sys.argv[1]) if len(sys.argv) > 1 else 5    # number of pieces

	if len(sys.argv) > 2:
		DELAY = None if sys.argv[2] == "manual" else float(sys.argv[2])

except ValueError:
	print (
		"",
		"ERROR:",
		"",
		"First parameter must be an integer number of pieces; second parameter",
		"must be a decimal number of seconds between each animation frame, or the",
		"word \"manual\" to wait for a carriage return between frames.",
		sep = "\n"
	)
	print()

	exit()

# initialize towers
towers = ([i for i in range (SIZE, 0, -1)], [], [])

""" move tower of height `depth` from `origin` via `via` to destination `dest` """
def move_tower (depth, origin, via, dest):

	# if no more pieces, stop
	if depth == 0:
		return

	# if trying to move more than one piece, first move all but the bottom to `via`
	if depth > 1:
		move_tower (depth - 1, origin, dest, via)

	# move the bottom
	dest.append (origin.pop())

	#show move
	render()

	# move the rest of the pieces to destination
	move_tower (depth - 1, via, origin, dest)

# end move_tower

""" display the current state of the puzzle """
def render():
	spaces = 3  # spacing between towers

	print()
	print()

	# for each layer
	for i in range (SIZE, 0, -1):

		# for each tower in the layer
		for tower in towers:

			# get piece number or background
			piece = str(tower[i - 1]) if len(tower) >= i else "|"

			# display piece
			print (
				" " * (spaces),  # padding
				piece,           # piece or background

				# padding to account for differing number lengths
				" " * (len(str(SIZE)) - len(piece)),

				# don't put \n between towers
				end=""
			)

		# put \n between layers
		print()

	# print base. it's complicated, okay?
	print ("-" * (
		spaces + (  # leading spaces
			len(towers) * (  # for each tower
				len(str(SIZE)) +  # piece length
				spaces +          # space between towers
				(len(towers) - 1) # concatenation spaces from print()
			)
		)

	))  # end base

	# buffer between frames
	print ()
	if DELAY is None:
		input()
	else:
		sleep (DELAY)

# end render

""" solve the puzzle """
def main():
	render()
	move_tower (SIZE, towers[0], towers[1], towers[2])

	print ("SOLVED!")
	print ()

# run the script
if __name__ == "__main__":
	main()
