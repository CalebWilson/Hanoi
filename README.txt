INTRODUCTION:
	This is an implementation of the classic Towers of Hanoi puzzle. It consists of
	three towers on which pieces of different sizes can be stacked. For the sake of
	this program, each piece is represented by a number denoting its size. 

RULES:
	- The puzzle starts out with all the pieces stacked on the left tower.
	- The puzzle is solved when all the pieces have been moved to the right tower.
	- Only one piece can be moved at a time.
	- No piece can be on top of a smaller piece.

RUNNING THE PROGRAM:
	To run the program with default settings, do:
		- python3 hanoi.py

	To run the program with a custom number of pieces, do:
		- python3 hanoi.py [number of pieces]

	To run the program with custom number of pieces and custom animation speed, do:
		- python3 hanoi.py [number of pieces] [number of seconds between frames]

	You can also replace the number of seconds between frames with the word
	"manual" to make the program wait for a carriage return from the user between
	each frame.
