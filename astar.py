import pygame
import utils
import math
from queue import PriorityQueue
from scipy.spatial import distance



RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def h(p1, p2):
	x1 = p1[0]
	y1 = p1[1]
	x2 = p2[0]
	y2 = p2[1]
	return distance.euclidean([x1, y1], [x2, y2])
	#return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.color = PURPLE
		draw()


def algorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	#f_score[start] = h(start.get_pos(), end.get_pos())
	p1 = (start.row, start.col)
	p2 = (end.row, end.col)
	f_score[start] = h(p1, p2)

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.color = GREEN
			start.color = RED
			return True

		for neighborCor in current.neighbors:
			neighbor = grid[neighborCor[0]][neighborCor[1]]
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				p1 = (neighbor.row, neighbor.col)
				f_score[neighbor] = temp_g_score + h(p1, p2) #p2 = end spot
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.color = TURQUOISE

		draw()
		#pygame.display.update() #update screen

		if current != start:
			current.color = WHITE

	return False


def get_clicked_pos(pos, width):
	y, x = pos

	row = y // width
	col = x // width

	return row, col


def start(grid, width):
	WIDTH = 700
	win = pygame.display.set_mode((WIDTH, 500))
	pygame.display.set_caption("A* Path Finding Algorithm")


	start = None
	end = None

	run = True
	while run:
		#draw(win, grid, ROWS, width)
		utils.showGrid(win, grid)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					#start.make_start()
					start.color = RED

				elif not end and spot != start:
					end = spot
					end.color = GREEN
					#end.make_end()


			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, width)
				spot = grid[row][col]
				spot.color = WHITE
				#spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					#algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
					algorithm(lambda: utils.showGrid(win, grid), grid, start, end)

		#pygame.display.update() #update screen

	pygame.quit()

#main(WIN, WIDTH)