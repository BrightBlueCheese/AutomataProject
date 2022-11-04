import time
import pygame
import numpy as np


# conda create -n myvenv python=3.8.8 anaconda
# conda activate myvenv
# conda deactivate


# donut, toroidal, periodic boundary condition

color_bg = (10, 10, 10)
color_grid = (40, 40, 40)
# color_die_next = (170, 170, 170)
color_alive_next = (42, 72, 88) # when stop and drawing
# color_alive_next_list=[(250, 250, 110), (196, 236, 116), (146, 220, 126), (100, 201, 135), (57, 180, 142)]
color_alive_next_list = [(250, 250, 110), (156, 223, 124), (74, 189, 140), (0, 150, 142), (16, 110, 124)]

# # new
# grid_row, grid_col = 12, 16
# size_whole = 50

# # new
# color_recorder = np.zeros((grid_row, grid_col))

def update(screen, cells, size, color_recorder, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    row_m, row_max, col_m, col_max = 0, (len(cells) - 1), 0, (len(cells[0]) - 1)
    for row, col in np.ndindex(cells.shape):
        # print(mat_mat2[row, col])

        # color = color_bg if cells[row, col] == 0 else color_alive_next
        
        # xmin ymin (0, 0)
        
        if (row == row_m) and (col == col_m):
            # print(f'xmin, ymin : {cells[row, col]}')
            # xmin_ymin_list.append((row, col))
            alive = cells[row_m, col_m+1] + cells[row_m+1, col_m] + cells[row_m+1, col_m+1] + cells[row_max, col_m] + \
                cells[row_max, col_m+1] + cells[row_m, col_max] + cells[row_m+1, col_max] + cells[row_max, col_max]

        # xmax, ymax (2, 2)
        elif (row == row_max) and (col == col_max):
            # print(f'xmax, ymax : {cells[row, col]}')
            # xmax_ymax_list.append((row, col))
            alive = cells[row_max, col_max-1] + cells[row_max-1, col_max] + cells[row_max-1, col_max-1] + cells[row_m, col_max] + \
                cells[row_m, col_max-1] + cells[row_max, col_m] + cells[row_max-1, col_m] + cells[row_m, col_m]
        # xmin ymax (0, 2)
        elif (row == row_m) and (col == col_max):
            # print(f'xmin, ymax : {cells[row, col]}')
            # xmin_ymax_list.append((row, col))
            alive = cells[row_m, col_max-1] + cells[row_m+1, col_max] + cells[row_m+1, col_max-1] + cells[row_max, col_max] + \
                cells[row_max, col_max-1] + cells[row_m, col_m] + cells[row_m+1, col_m] + cells[row_max, col_m]
        # xmax ymin (2, 0)
        elif (row == row_max) and (col == col_m):
            # print(f'xmax, ymin : {cells[row, col]}')
            # xmax_ymin_list.append((row, col))
            alive = cells[row_max, col_m+1] + cells[row_max-1, col_m] + cells[row_max-1, col_m+1] + cells[row_m, col_m] + \
                cells[row_m, col_m+1] + cells[row_max, col_max] + cells[row_max-1, col_max] + cells[row_m, col_max]
        # xmin
        elif (row == row_m):
        # print(f'xmin : {cells[row, col]}')
        # xmin_list.append((row, col))
            alive = np.sum(cells[row:row+2, col-1:col+2]) - cells[row, col] + np.sum(cells[row-1, col-1:col+2])
        # xmax
        elif (row == row_max):
            # print(f'xmax : {cells[row, col]}')
            # xmax_list.append((row, col))
            alive = np.sum(cells[row-1:row+1, col-1:col+2]) - cells[row, col] + np.sum(cells[row-(len(cells)-1), col-1:col+2])
        # ymin
        elif (col == col_m):
            # print(f'ymin : {cells[row, col]}')
            # ymin_list.append((row, col))
            alive = np.sum(cells[row-1:row+2, col:col+2]) - cells[row, col] + np.sum(cells[row-1:row+2, col-1])
        # ymax
        elif (col == col_max):
            # print(f'ymin : {cells[row, col]}')
            # ymax_list.append((row, col))
            alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col] + np.sum(cells[row-1:row+2, col-(len(cells[0])-1)])
        else:
            # print(f'else : {cells[row, col]}')
            # the_rest_list.append((row, col))
            alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]


        # color_recorder[row][col] = (color_recorder[row][col] + 1) % 5
        #             # color = color_alive_next_list[color_recorder[row][col]]
        # yes = int(color_recorder[row][col])
        # color_1 = color_alive_next_list[yes]
        color = color_bg if cells[row, col] == 0 else color_updator(row, col, color_recorder, update_color=False) # when stop and drawing
        # color = color_bg if cells[row, col] == 0 else (255, 0, 0)
        
        
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    # color_recorder[row][col] = (color_recorder[row][col] + 1) % 5
                    # # color = color_alive_next_list[color_recorder[row][col]]
                    # yes = int(color_recorder[row][col])
                    color = color_updator(row, col, color_recorder)
                    # print(f'{yes}')

            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    # # color = color_alive_next
                    # color_recorder[row][col] = (color_recorder[row][col] + 1) % 5
                    # # color = color_alive_next_list[color_recorder[row][col]]
                    # yes = int(color_recorder[row][col])
                    color = color_updator(row, col, color_recorder)
                    # print(f'{yes}')

        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    # # color = color_alive_next
                    # color_recorder[row][col] = (color_recorder[row][col] + 1) % 5
                    # yes = int(color_recorder[row][col])
                    color = color_updator(row, col, color_recorder)
                    # print(f'{yes}')

        
        
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return updated_cells

def color_updator(row, col, color_recorder, update_color=True):
    if update_color == True:
        color_recorder[row][col] = (color_recorder[row][col] + 1) % 5
        # color = color_alive_next_list[color_recorder[row][col]]
        target_color = int(color_recorder[row][col])
    elif update_color == False:
        target_color = int(color_recorder[row][col])
    return color_alive_next_list[target_color]

def main():
    size_whole = 50
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # new
    grid_row, grid_col = 12, 16

    # new
    color_recorder = np.zeros((grid_row, grid_col))

    cells = np.zeros((grid_row, grid_col))
    screen.fill(color_grid)
    update(screen, cells, size_whole, color_recorder)
    
    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():

            # when press quit, quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # when press space, pause
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, size_whole, color_recorder)
                    pygame.display.update()
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//size_whole, pos[0]//size_whole] = 1
                update(screen, cells, size_whole, color_recorder)
                pygame.display.update()

        screen.fill(color_grid)

        if running:
            cells = update(screen, cells, size_whole, color_recorder, with_progress=True)
            pygame.display.update()

        time.sleep(0.1)

if __name__ == '__main__':
    main()
                
