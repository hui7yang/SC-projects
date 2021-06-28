"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
-------------------------------
Author: Hui-Chi Yang
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """

    plus_per_year = (width - 2*GRAPH_MARGIN_SIZE)/len(YEARS)  # 80 (20, 100, 180, 260,...)
    x_coordinate = GRAPH_MARGIN_SIZE + (plus_per_year * year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # vertical line
    for year_index in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        # add on specific year
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[year_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    '''
    for year_index in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        if name_data[lookup_names][year_index] > MAX_RANK:
            name_data[lookup_names][year_index] = '*'
            canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=lookup_names, anchor=tkinter.NW)
        else:
            canvas.create_text(x + TEXT_DX, name_data[lookup_names][year_index], text=lookup_names)
    '''
    color_count = 0
    for name in lookup_names:  # (e.g. lookup_names = [kylie, nick, andy])
        all_its_rank = []
        all_its_text = []

        # (kylie's rank)
        # get the "rank" of the name
        # loop over the years(key) & rank(value) in name_data[name](dict)
        # for year, rank in sorted(name_data[name].items()):

        if name in name_data:
            for year in YEARS:
                year = str(year)
                if year not in name_data[name]:
                    name_data[name][year] = MAX_RANK
                    all_its_rank.append(name_data[name][year])
                    all_its_text.append('*')

                else:
                    all_its_rank.append(name_data[name][year])  # rank(str)
                    all_its_text.append(name_data[name][year])
        color_count += 1
        color = COLORS[color_count % len(COLORS)]

        # (got the rank already)
        # (create line)
        # (x = year(get_x_coor) y = margin + rank)
        for year_index in range(len(YEARS)):  # 12 runs
            if year_index != len(YEARS)-1:  # !

                x1 = get_x_coordinate(CANVAS_WIDTH, year_index)
                y1 = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000 * int(all_its_rank[year_index]) + GRAPH_MARGIN_SIZE

                x2 = get_x_coordinate(CANVAS_WIDTH, year_index+1)
                y2 = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000 * int(all_its_rank[year_index+1]) + GRAPH_MARGIN_SIZE

                canvas.create_line(x1, y1, x2, y2, width = LINE_WIDTH, fill = color)
                canvas.create_text(x1+TEXT_DX, y1, text = name +','+ str(all_its_text[year_index]), anchor=tkinter.SW)
            else:
                x1 = get_x_coordinate(CANVAS_WIDTH, year_index)
                y1 = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(all_its_rank[year_index]) + GRAPH_MARGIN_SIZE
                canvas.create_text(x1 + TEXT_DX, y1, text=name +','+ str(all_its_text[year_index]), anchor=tkinter.SW)


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
