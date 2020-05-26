import pygame
import random
surface = pygame.display.set_mode((500,600))
pygame.init()
pygame.display.set_caption('The Greatest Snake Game of all Time')
#snake class
class Snake(object):
	def __init__(self):
		self.len = 1
		self.color = (100,200,111)
		pygame.draw.rect(surface, self.color, (p_x*25,p_y*25,25,25))

	def update_pos(self,direction):
		global prev_pos

		prev_pos[0][0] += direction[0]
		prev_pos[0][1] += direction[1]

	def draw(self):
		global prev_pos
		bod_num = 0
		for i in range(self.len):
			x = prev_pos[bod_num][0]
			y = prev_pos[bod_num][1]
			pygame.draw.rect(surface, self.color, (x*25, y*25,25,25))
			bod_num += 1

	def grow(self):
		self.len += 1
		
#checks if player are food		
def food_check():
	global fpos
	global prev_pos
	global player

	if prev_pos[0] == fpos:
		player.len += 1

		while True:
			f_x = random.randint(0,19)
			f_y = random.randint(0,19)
			fpos = [f_x, f_y]
			if not(fpos == prev_pos[0]):
				break

def draw_score():
	global player
	pygame.draw.rect(surface, (255,255,255), (180, 510, 160, 83), 4)
	pygame.draw.line(surface, (255,255,255), (180, 556), (339, 556), 4)
	title = font.render("SCORE", True, (255,255,255))
	surface.blit(title , (200,520))
	score = font.render(str(player.len), True, (255,255,255))
	surface.blit(score , (250,560))

def death_check():
	global prev_pos

	#players head
	p_head = prev_pos[0]

	#checks if player ran into wall
	if p_head[0] > 19 or p_head[0] < 0 or p_head[1] > 19 or p_head[1] < 0:
		restart_game()


	if player.len > 1:
		bod_num = 1
		h_pos = prev_pos[0]
		for i in range(player.len):
			bod_pos = prev_pos[bod_num]
			if h_pos == bod_pos:
				restart_game()
				break
			bod_num += 1



def draw_food():
	global fpos
	x = fpos[0]
	y = fpos[1]
	pygame.draw.rect(surface, (255,0,0), (x*25,y*25,25,25))
	
def draw_grid():
	#Draws the grid
	grid_size = 25
	grid_num = 0
	for line in range(int(500/grid_size)):
		pygame.draw.line(surface, (255,255,255), (grid_num*grid_size, 0 ),(grid_num*grid_size, 500))
		grid_num += 1

	grid_num = 0
	for line in range(int(500/grid_size)):
		pygame.draw.line(surface, (255,255,255), (0 , grid_num*grid_size),(500 ,grid_num*grid_size))
		grid_num += 1

	pygame.draw.line(surface, (255,255,255), (0 , 500),(500 ,grid_num*grid_size))	

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)


#initiates the game
draw_grid()


def restart_game():
	#player head position
	global p_x
	global p_y
	global time
	global prev_pos
	global direction
	global clock
	global player
	global fpos

	#spawns player
	p_x = random.randint(0,19)
	p_y = random.randint(0,19)
	pos = [p_x, p_y]

	#list of previous positions
	prev_pos = []
	prev_pos.append(pos)
	direction = RIGHT
	player = Snake()
	clock = pygame.time.Clock()
	time = 0




p_x = random.randint(0,19)
p_y = random.randint(0,19)
pos = [p_x, p_y]

#food position
while True:
	f_x = random.randint(0,19)
	f_y = random.randint(0,19)
	fpos = [f_x, f_y]
	if not(fpos == pos):
		break

#list of previous positions
prev_pos = []
prev_pos.append(pos)
direction = RIGHT
player = Snake()
clock = pygame.time.Clock()
time = 0
font = pygame.font.SysFont('freesansbold.ttf', 50)


while True:
	pygame.time.delay(100)

	#event loop
	for event in pygame.event.get():

		#exit button
		if event.type == pygame.QUIT:
			pygame.quit()
			break

		#handles button press
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if not(prev_dir == RIGHT):
					direction = LEFT
			if event.key == pygame.K_RIGHT:
				if not(prev_dir == LEFT):
					direction = RIGHT
			if event.key == pygame.K_UP:
				if not(prev_dir == DOWN):
					direction = UP
			if event.key == pygame.K_DOWN:
				if not(prev_dir == UP):
					direction = DOWN
			if event.key == pygame.K_z:
				player.grow()

	#Game clock
	speed = 5
	time += clock.tick()
	if time > speed:
		prev_dir = direction

		#adds previous position to list
		x = int(prev_pos[0][0])
		y = int(prev_pos[0][1])
		prev_pos.insert(1, [x, y])

		#moves player
		player.update_pos(direction)
		surface.fill((0,0,0))
		draw_grid()
		draw_food()
		draw_score()
		player.draw()
		time = 0

		#checks if food was eatin and grows accordingly
		food_check()
		death_check()




	pygame.display.update()
