# A simple, Noughts and Crosses game for two human players implemented using
# the PyGame framework. Created by Liam Fraser for a Linux User and Developer
# tutorial.

# Provides the PyGame framework
import pygame 

# Provides the sys.exit function we use to exit our game loop
import sys 
from pygame import *

# Import constants used by PyGame
from pygame.locals import * 



######################
#4. Background Class
#the Background class
class Background:
	def __init__(self, displaySize):
		self.image = Surface(displaySize)
		#Draw a title
		#Create the font to be used
		self.font = font.Font(None, (displaySize[0] / 12))
		#Create the text surface
		self.text = self.font.render("Noughts and Crosses", True, (Color("white")))
		# Work out where to place the text
		self.textRect = self.text.get_rect()
		self.textRect.centerx = displaySize[0] / 2
		# Add a little margin
		self.textRect.top = displaySize[1] * 0.02
		# Blit the text to the background image
		self.image.blit(self.text, self.textRect)

	def draw(self, display):
		display.blit(self.image, (0, 0))
######################

######################
#5. Grid squares
# a class for an individual grid square 
class GridSquare(sprite.Sprite):
	def __init__(self, position, gridSize):
		#Initialize the sprite base class
		super(GridSquare, self).__init__()
		# to know which row and column we are in
		self.position = position

		# State can be "X", "O" or " "
		self.state = ""
		self.permanentState = False
		self.newState = ""
		# Work out the position and size of the square
		width = gridSize[0] / 3
		height = gridSize[1] / 3
		#Get the x and y coordinate of the top left corner
		x = (position[0] * width) - width
		y = (position[1] * height) - height
######################

######################
# 6. Grid square surfaces
# coordinate(0,0) is the top-left corner
# Create the image, the rect and then position the rect
		self.image = Surface((width, height))
		self.image.fill(Color("white"))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		# The rect we have is white, which is the parent rect
		# We draw another rect in the middle so that we have
		# a white border but a blue center
		self.childImage = Surface(((self.rect.w* 0.9), (self.rect.h * 0.9)))
		self.childImage.fill(Color("blue"))
		self.childRect = self.childImage.get_rect()
		self.childRect.center = ((width / 2), (height / 2))
		self.image.blit(self.childImage, self.childRect)
		# Create the font we'll use to display O and X
		self.font = font.Font(None, (self.childRect.w))   
######################

######################
# 9. Finish the GridSquare
	def update(self):
		#Need to update if we need to set a new state
		if (self.state != self.newState):
			#Refill the childImage blue
			self.childImage.fill(Color("blue"))
			text = self.font.render(self.newState, True, (Color("white")))
			testRect = text.get_rect()
			textRect.center = ((self.childRect.w / 2), (self.childRect.h /2))
			#to blit twice because the new child image needs to be blitted to the parent image
			self.childImage.blit(text, textRect)
			self.image.blit(self.childImage, self.childRect)
			#Reset the newState variable
			self.state = self.newState
			self.newState = ""

	def setState(self, newState, permanent = False):
		if not self.permanentState:
			self.newState = newState
			if permanent:
				self.permanentState = True
######################

######################
# 7. Constructing a grid
# A class for the 3X3 grid
class Grid:
	def __init__(self, displaySize):
		self.image = Surface(displaySize)
		# Make a number of grid squares
		gridSize = (displaySize[0] * 0.75, displaySize[1] * 0.75)
		# Work out the coordinate of the top left corner of the grid
		# so that it can be centered on the screen
		self.position = ((displaySize[0] / 2) - (gridSize[0] / 2), (displaySize[1] /2) - (gridSize[1] /2))
		# An empty array to hold our grid squares in 
		self.sqaures = []
		for row in range(1,4):
			# Loop to make 3 rows
			for column in range(1, 4):
				#Loop to make 3 columns
				squarePosition = (column, row)
				self.squares.append(GridSquare(squarePosition, gridSize))
		#Get the square in a sprite group
		self.sprites = sprite.Group()
		for square in self.squares:
			self.sprites.add(square)
######################

######################
# 8. the grid draw function
# update each square sprite, draws them to the grid's surface
	def draw(self, display):
		self.sprites.update()
		self.sprites.draw(self.image)
		display.blit(self.image, self.position)
######################

######################
#11. Finishing off the grid class
# for who has won the game
	def getSquareState(self, column, row):
		#get the square with the requested position
		for square in self.squares:
			if square.position == (column, row):
				return square.state

	def full(self):
		#Finds out if the grid is full
		count = 0
		for square in self.squares:
			if square.permanentState == True:
				count += 1
		if count == 9:
			return True
		else:
			return False
###################### 

######################
#3. Starting the Game class
#Our game class
class OAndX:
	def __init__(self):
		#initialize PyGame
		pygame.init()
		#Create a clock to manage the game loop
		self.clock = time.Clock()
		#set the window title
		display.set_caption("Noughts and Crosses")
		#Create the window with a resolution of 640x480
		self.displaySize = (640, 480)
		self.screen = display.set_mode(self.displaySize)
		#either be O or X
		self.player = "O"
#####################

######################
# 12. Working out the winner
# either return nothing, the winning player (O or X), or 'draw'
# start defining players
	def getWinner(self):
		players = ["X", "O"]

		for player in players:
			#check horizontal spaces
			for column in range (1, 4):
				for row in range (1, 4):
					square1 = self.grid.getSquareState(column, row)
					square2 = self.grid.getSquareState((column + 1), row)
					sqaure3 = self.grid.getSquareState((column + 2), row)
					# Get the player of the square (either O or X)
					if (square1 == player) and (square2 == player) and (square3 == player):
						return player
			#check vertical spaces
			for column in range (1, 4):
				for row in range (1, 4):
					square1 = self.grid.getSquareState(column, row)
					sqaure2 = self.grid.getSquareState(column, (row + 1))
					square3 = self.grid.getSquareState(column, (row + 2))
					#Get the player of the square (either O or X)
					if(square1 == player) and (square2 == player) and (square3 == player):
						return player

			#check forwards diagonal spaces
			for column in range (1, 4):
				for  row in range(1, 4):
					square1 = self.grid.getSquareState(column, row)
					square2 = self.grid.getSquareState((column + 1), (row -1))
					square3 = self.grid.getSquareState((column + 2), (row -2))
					#Get the player of the square (either O or X)
					if(square1 == player) and (square2 == player) and (square3 == player):
						return player

			#check backwards diagonal spaces
			for column in range(1, 4):
				for row in range (1, 4):
					square1 = self.grid.getSquareState(column, row)
					square2 = self.grid.getSquareState((column + 1), (row + 1))
					square3 = self.grid.getSquareState((column + 2), (row + 2))
					#Get the player of the square (either O or X)
					if (square1 == player) and (square2 == player) and (square3 == player):
						return player

			# Check if grid is full if someone hasn't won already
			if self.grid.full():
				return "draw"
######################

######################
# 13. Displaying a message when a winner is found
	def winMessage(self, winner):
		#Display message then reset the game to its initial state
		#Blank out the screen 
		self.screen.fill(Color("Black"))
		#Create the font we'll use
		textFont = font.Font(None, (self.displaySize[0] / 6))
		testString = ""
		if winner == "draw":
			testString = "It was a draw!"
		else: 
			textString = winner + " Wins!"
		# Create the text surface
		text = textFont.render(textString, True, (Color("white")))
		testRect = text.get_rect()
		textRect.centerx = self.displaySize[0] /2
		textRect.centery = self.displaySize[1] /2
		# Blit changes and update the display before we sleep
		self.screen.blit(text, textRect)
		display.update()
		#time.wait comes from pygame libs
		time.wait(2000)
		# Set game to its initial state
		self.reset()
######################

######################
# 15. Handling events
# two important events: click / mouse button up
# find out position of mouse: rect.collidepoint function
	def handleEvents(self):
		# We need to know if the mouse has been clicked later on
		mouseClicked = False
		# Handle events, starting with quit
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONUP:
				mouseclicked = True
		# Get the coordinate of the mouse
		mousex, mousey = mouse.get_pos()
		# These are relative to the top left of the screen, 
		# we need to make them relative to the top left of the grid
		mousex -= self.grid.position[0]
		mousey -= self.grid.position[1]
		# Find which rect the mouse is in
		for square in self.grid.squares:
			if square.rect.collidepoint((mousex, mousey)):
				if mouseClicked:
					square.setState(self.player, True)
					#Change to next player
					if self.player == "O":
						self.player = "X"
					else:
						self.player = "O"
					# Check for a winner
					winner = self.getWinner()
					if winner:
						self.winMessage(winner)
				else:
					square.setState(self.player)
			else:
				# Set it to blank, only if permanentState == False
				square.setState("")
######################

######################
# 14. The game loop
	def run(self):
		while True:
			# Our Game Loop
			# handle events
			self.handleEvents()
			# Draw our background and grid
			self.background.draw(self.screen)
			self.grid.draw(self.screen)
			# Update our display
			display.update()
			# Limit the game to 10fps
			self.clock.tick(10)
######################

######################
# 10. Extending the game class
# add the Background and Grid into the initializer of main OAndX class
def reset(self):
		#create an instance of our background and grid class
	self.background = Background(self.displaySize)
	self.grid = Grid(self.displaySize)
######################

######################
# 16. Final
if __name__ == '__main__':
	game = OAndX()
	game.run()
######################
