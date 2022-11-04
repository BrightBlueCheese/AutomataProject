import time
import pygame
import numpy as np

# conda create -n myvenv python=3.8.8 anaconda
# conda activate myvenv
# conda deactivate

# Code refered from https://www.youtube.com/watch?v=cRWg2SWuXtM&ab_channel=NeuralNine

color_bg = (10, 10, 10)
color_grid = (40, 40, 40)
color_alive_next_list = [(250, 250, 110), (156, 223, 124), (74, 189, 140), (0, 150, 142), (16, 110, 124)]



def update(displayer, grids, size, color_recorder, with_progress=False):
    updated_grids = np.zeros((grids.shape[0], grids.shape[1]))
    row_m, row_max, col_m, col_max = 0, (len(grids) - 1), 0, (len(grids[0]) - 1)
    for row, col in np.ndindex(grids.shape):
        
        # xmin ymin 
        if (row == row_m) and (col == col_m):
            alive = grids[row_m, col_m+1] + grids[row_m+1, col_m] + grids[row_m+1, col_m+1] + grids[row_max, col_m] + \
                grids[row_max, col_m+1] + grids[row_m, col_max] + grids[row_m+1, col_max] + grids[row_max, col_max]
        # xmax, ymax 
        elif (row == row_max) and (col == col_max):
            alive = grids[row_max, col_max-1] + grids[row_max-1, col_max] + grids[row_max-1, col_max-1] + grids[row_m, col_max] + \
                grids[row_m, col_max-1] + grids[row_max, col_m] + grids[row_max-1, col_m] + grids[row_m, col_m]
        # xmin ymax 
        elif (row == row_m) and (col == col_max):
            alive = grids[row_m, col_max-1] + grids[row_m+1, col_max] + grids[row_m+1, col_max-1] + grids[row_max, col_max] + \
                grids[row_max, col_max-1] + grids[row_m, col_m] + grids[row_m+1, col_m] + grids[row_max, col_m]
        # xmax ymin
        elif (row == row_max) and (col == col_m):
            alive = grids[row_max, col_m+1] + grids[row_max-1, col_m] + grids[row_max-1, col_m+1] + grids[row_m, col_m] + \
                grids[row_m, col_m+1] + grids[row_max, col_max] + grids[row_max-1, col_max] + grids[row_m, col_max]
        # xmin
        elif (row == row_m):
            alive = np.sum(grids[row:row+2, col-1:col+2]) - grids[row, col] + np.sum(grids[row-1, col-1:col+2])
        # xmax
        elif (row == row_max):
            alive = np.sum(grids[row-1:row+1, col-1:col+2]) - grids[row, col] + np.sum(grids[row-(len(grids)-1), col-1:col+2])
        # ymin
        elif (col == col_m):
            alive = np.sum(grids[row-1:row+2, col:col+2]) - grids[row, col] + np.sum(grids[row-1:row+2, col-1])
        # ymax
        elif (col == col_max):
            alive = np.sum(grids[row-1:row+2, col-1:col+2]) - grids[row, col] + np.sum(grids[row-1:row+2, col-(len(grids[0])-1)])
        else:
            alive = np.sum(grids[row-1:row+2, col-1:col+2]) - grids[row, col]


        color = color_bg if grids[row, col] == 0 else color_updator(row, col, color_recorder, update_color=False) # when stop and drawing

        
        
        if grids[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = color_updator(row, col, color_recorder)


            elif 2 <= alive <= 3:
                updated_grids[row, col] = 1
                if with_progress:
                    color = color_updator(row, col, color_recorder)


        else:
            if alive == 3:
                updated_grids[row, col] = 1
                if with_progress:
                    color = color_updator(row, col, color_recorder)


        
        
        pygame.draw.rect(displayer, color, (col*size, row*size, size-1, size-1))

    return updated_grids

def color_updator(row, col, color_recorder, update_color=True):
    if update_color == True:
        color_recorder[row][col] = (color_recorder[row][col] + 1) % 5
        target_color = int(color_recorder[row][col])
    elif update_color == False:
        target_color = int(color_recorder[row][col])
    return color_alive_next_list[target_color]

def main():
    size_whole = 50
    grid_row, grid_col = 12, 16
    pygame.init()
    displayer = pygame.display.set_mode((grid_col*size_whole, grid_row*size_whole))

    color_recorder = np.zeros((grid_row, grid_col))

    grids = np.zeros((grid_row, grid_col))
    displayer.fill(color_grid)
    update(displayer, grids, size_whole, color_recorder)
    
    pygame.display.flip()
    pygame.display.update()

    proceeding = False

    while True:
        for event in pygame.event.get():

            # when press quit, quit
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # when press space, pause
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    proceeding = not proceeding
                    update(displayer, grids, size_whole, color_recorder)
                    pygame.display.update()
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grids[pos[1]//size_whole, pos[0]//size_whole] = 1
                update(displayer, grids, size_whole, color_recorder)
                pygame.display.update()

        displayer.fill(color_grid)

        if proceeding:
            grids = update(displayer, grids, size_whole, color_recorder, with_progress=True)
            pygame.display.update()

        time.sleep(0.1)

if __name__ == '__main__':
    main()