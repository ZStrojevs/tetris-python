#Disclamer wrote by myself very unompitimized code

import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((300, 600))
clock = pygame.time.Clock()
running = True

#Predefined pieces as matrix and predifined colors for them
piece_matrix = [[[1, 1], [1, 1]], [[1, 0], [1, 0], [1, 1]], [[0, 1], [1, 1], [1, 0]], [[0, 1], [0, 1], [1, 1]], [[1, 0], [1, 0], [1, 0], [1, 0]], [[1, 0], [1, 1], [0, 1]], [[1, 0], [1, 1], [1, 0]]]
piece_color = (pygame.Color(0, 0, 255, 255), pygame.Color(255, 0, 0, 255), pygame.Color(0, 255, 0, 255), pygame.Color(125, 125, 0, 255), pygame.Color(0, 125, 125, 255), pygame.Color(0, 80, 125, 255), pygame.Color(190, 0, 125, 255))


#Class Piece that makes randomized new piece
class Piece:

    def __init__(self):
        self.randpiece = random.randint(0, 6)
        self.type = piece_matrix[self.randpiece]
        self.color = piece_color[self.randpiece]
        self.state = False
    #function that does rotation 
    def rotation(self):
        size = len(self.type)

        width_of_matrix = len(self.type)
        height_of_matrix = len(self.type[0])
        temp_type = [[0 for _ in range(width_of_matrix)] for _ in range(height_of_matrix)]

        which_height = 0
        width_of_temp = width_of_matrix
        for line in self.type:
            for elem in line:
                temp_type[which_height][width_of_temp-1] = elem
                which_height += 1
            width_of_temp -= 1
            which_height = 0

        

        self.type = temp_type
        print(self.type)



#Before loop definied values
current_piece = Piece()
piece_starting_x = 5
piece_starting_y = 1
grid_info = [[0 for _ in range(10)] for _ in range(20)]


#Game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keystate = pygame.key.get_pressed()

    if keystate[pygame.K_UP]:
        if len(current_piece.type[0]) - 2 + current_saved_x > 10:
            pass
        else: current_piece.rotation()
    
    if keystate[pygame.K_LEFT]:
        if piece_starting_x == 0:
            pass
        else: piece_starting_x -= 1

    #Cheking the lenght of piece and then limiting right action button based on the length
    elif keystate[pygame.K_RIGHT]:

        how_long = 0

        for tuple in current_piece.type:
            temp_how_long = 0
            for in_tuple in tuple:
                if in_tuple == 1:
                    temp_how_long +=1
            if temp_how_long > how_long:
                how_long = temp_how_long  

        if piece_starting_x + how_long + 1 > 10:
                pass
        else: piece_starting_x += 1


    screen.fill("black")
    

    pygame.draw.line(screen, pygame.Color(255, 255, 255, 255), (50, 100), (250, 100))
    pygame.draw.line(screen, pygame.Color(255, 255, 255, 255), (50, 100), (50, 500))
    pygame.draw.line(screen, pygame.Color(255, 255, 255, 255), (250, 100), (250, 500))
    pygame.draw.line(screen, pygame.Color(255, 255, 255, 255), (50, 500), (250, 500))

    #Grid drawing
    starting_x = 70
    for i in range(10):
        starting_y = 100
        ending_y = 500
        pygame.draw.line(screen, pygame.Color(255, 255, 255, 255), (starting_x, starting_y), (starting_x, ending_y))
        starting_x += 20

    starting_y = 120
    for i in range(20):
        starting_x = 50
        ending_x = 250
        pygame.draw.line(screen, pygame.Color(255, 255, 255, 255), (starting_x, starting_y), (ending_x, starting_y))
        starting_y += 20

    row_num = 0

    #clearing out the line
    for row in grid_info:
        full_with_1 = set()
        for blocks in row:
            full_with_1.add(blocks)

        if full_with_1 == {1}:

            temp_grid_info = [[0 for _ in range(10)] for _ in range(20)]
            temp_grid_info = grid_info
            temp_grid_info[row_num] = [0 for _ in range(10)]

            reached_end = True


            while reached_end:
                if row_num > 0:
                    grid_info[row_num] = temp_grid_info[row_num-1]
                    row_num -= 1
                else:
                    reached_end = False
                    row_num = 0

            grid_info = temp_grid_info

        row_num += 1

                
    #Drawing the information about where grid is filled
    change_x = 55
    change_y = 105
    for rows in grid_info:
        for blocks in rows:
            if blocks == 1:
                pygame.draw.rect(screen, pygame.Color(100, 0, 100, 255), (change_x , change_y, 10, 10))

            else:
                pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (change_x , change_y, 10, 10))
            change_x += 20
        change_x = 55
        change_y += 20


    current_saved_y = piece_starting_y

    current_saved_x = piece_starting_x

    through_x = current_saved_x


    piece_height = len(current_piece.type)
    which_line = piece_height - 1
    block_pos = current_saved_y + piece_height - 2

    #Check if pieces matrix is empty bellow 
    full_with_0 = set()
    for blocks in current_piece.type[which_line]:
        full_with_0.add(blocks)
    if full_with_0 == {0}:
        del current_piece.type[which_line]
        which_line -= 1
        
    #Makes final position if there is already piece bellow it
    for block in current_piece.type[which_line]: 
        print(through_x)
        if through_x > 10:
            pass
        elif block == 1:
            if block_pos == 19:
                current_piece.state = True
            elif 1 in grid_info[block_pos+1]:
                if grid_info[block_pos+1][through_x] == 1:
                    current_piece.state = True
                    break
        elif block == 0:
            if current_piece.type[which_line-1][block] == 1:
                if grid_info[block_pos][through_x-1] == 1:
                    current_piece.state = True
                    break
        through_x += 1

    #Drawing function and position change
    if current_piece.state == False:

        for in_list in current_piece.type:

            for in_tuple in in_list:

                if in_tuple == 1:    
                    piece_x_transf = int((piece_starting_x*20) + 50)
                    piece_y_transf = int((piece_starting_y*20) + 100)
                    pygame.draw.rect(screen, current_piece.color, (piece_x_transf , piece_y_transf, 20, 20))

                piece_starting_x += 1


            piece_starting_x = current_saved_x
            piece_starting_y += 1
        piece_starting_y = current_saved_y + 1
        pygame.time.wait(50)


    #Saving the state
    elif current_piece.state == True:

        list_starting = block_pos - len(current_piece.type) + 1

        for in_list in current_piece.type:

            for in_tuple in in_list:
                if in_tuple == 1:    
                    piece_x_transf = (piece_starting_x*20) + 50
                    piece_y_transf = (piece_starting_y*20) + 100

                    block_index = int(piece_starting_x)
                    grid_info[list_starting][block_index] = 1
                piece_starting_x += 1
    
            piece_starting_x = current_saved_x
            piece_starting_y += 1
            list_starting += 1

        print(grid_info)
        current_piece = Piece()
        
        piece_starting_x = 5
        piece_starting_y = 1

    pygame.display.flip()



    if grid_info[0][4] or grid_info[0][5] == 1:
        running = False

    clock.tick(12)

pygame.quit()
