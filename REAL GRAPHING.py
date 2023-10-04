# Name:         Graph Generator
# Date:         1/13/2022
# Programmers:  Abhusha Ghimire
# Description:  Creates a graph.

import tkinter
import math

# Unused/Unfinished function
# Collects the name of all file would be used if still using selection option for files
def file_list_collector ( file_name ) :
    # List of all file names
    name_list = []

    #Create file in case it does not exist
    create_file = open(file_name, "a")
    create_file.close()

    # Reads file
    read_file = open(file_name, "r")

    # Appends first file
    name_list.append(read_file.readline().strip("\n"))

    # Appends all files
    while (name_list[-1] != ""):
        name_list.append(read_file.readline().strip("\n"))
    
    # Returns list
    return name_list

# Unused/Unfinished function
# Puts the name of all files into a file would still be used if above function was used
def master_file(name, old_name):
    # Name of file
    file_list = "apMaster"
    
    # Collects all current files
    current_files = file_list_collector("apMaster")

    # Checks to see if the file ever existed
    if (not (old_name in current_files)):
        # If not write all the files, but remove the empty lines
        list_of_files = open(file_list,"w")

        for i in current_files:
            if (i != ""):
                list_of_files.write(i + "\n")

        # Write the new name
        list_of_files.write(name + "\n")

        # Closes file
        list_of_files.close()

    # Checks to see if the file name changed
    elif (name != old_name):

        # Open file
        list_of_files = open(file_list,"w")

        # Write name of all the files
        for name_of_file in current_files:
            # Checks to see if the name isnt the old name or an empty name
            # before adding it
            if (name_of_file != old_name and name_of_file != ""):
                list_of_files.write(name_of_file + "\n")
        
        # Write the new name
        list_of_files.write(name)

        # Close file
        list_of_files.close()

#If name does not change, take old_name and make it name
def save_file_data(name, type_of_graph, coordinates):
    # File name data is stored
    file_name = "ap_" + name
    
    # Would be used if master file existed
    #master_file(name, old_name)

    #Opens file
    save_file = open(file_name, "w")

    #Writes type of graph
    save_file.write(type_of_graph + "\n")
    if (x_name.strip(" ") == "" or y_name.strip(" ") == ""):
        save_file.write("x y")
    else:
        save_file.write(f"{x_name} {y_name} \n")

    # Writes down multiple data sets, but program will only ever give one
    for l in range(0, len(coordinates)):

        # Stores x and y values as a string
        x_values = ""
        y_values = ""
        
        # Adds values to string
        for i in range(0, len(coordinates[l][0])):
            x_values += str(coordinates[l][0][i]) + " "
            y_values += str(coordinates[l][1][i]) + " "
        
        # Remove extra space at the end
        x_values = x_values[0:-1]
        y_values = y_values[0:-1]

        #Write strings into file
        save_file.write(x_values + "\n")
        save_file.write(y_values + "\n")
    
    # Close file
    save_file.close()

# Open files
def open_file(name):
    # Finds name of file
    file_name = "ap_" + name

    # Opens file
    open_file = open(file_name, "r")

    # Reads type of graph
    type_graph = open_file.readline().strip("\n")

    labels = open_file.readline().strip("\n").split()

    # Coordinates 
    coordinates = [[]]
   
    

    x_values = open_file.readline().strip("\n").split()
    coordinates[0].append(x_values)

    y_values = open_file.readline().strip("\n").split()
    coordinates[0].append(y_values)

    # Closes file
    open_file.close()

    # Return stuff from file
    return [type_graph, labels, coordinates]


# Find the lowest value of x
def find_lowest_x(coords):

    # Checks if list is empty
    if (len(coords[0][0]) != 0):

        # Sets lowest to a value
        lowest = coords[0][0][0]

        # Checks each value to see if their is a smaller one
        for l in range(len(coords)):
            for i in range(len(coords[l][0])):
                if (coords[l][0][i] < lowest):
                    lowest = coords[l][0][i]
    else:
        # If list empty just output 0
        lowest = 0
    
    # Return value
    return lowest

# Same as previous function except checks if higher
def find_highest_x(coords):
    if (len(coords[0][0]) != 0):
        highest = coords[0][0][0]
        for l in range(len(coords)):
            for i in range(len(coords[l][0])):
                if (coords[l][0][i] > highest):
                    highest = coords[l][0][i]
    else:
        highest = 1
    return highest

# Same as previous function except checks y values
def find_highest_y(coords):
    if (len(coords[0][1]) != 0):
        highest = coords[0][1][0]
        for l in range(len(coords)):
            for i in range(len(coords[l][1])):
                if (coords[l][1][i] > highest):
                    highest = coords[l][1][i]
    else:
        highest = 1
    
    print (highest)
    return highest

# Checks which data set has the lowest amount of elements
def lowest_x_amount (coords):
    lowest = 0

    for coord in coords:
        if ( len(coord[0]) > lowest ) :
            lowest = len(coord[0])
    
    return lowest

# Finds the average of a list
def average_nums(summed_list):
    if (len(summed_list) != 0):
        # Adds all the totals together then divides
        # by length of list
        total = 0

        for i in summed_list:
            total += i
        
        average = total/len(summed_list)
    else:
        # If len of list 0, average is 0
        average = 0
        
    return average

# Sorts the lists by averages and returns the indexes
def find_sorted_average(coords):
    # List where all indexes go
    index_locations = []

    # While list is not empty
    while len(index_locations) != len(coords):
        # Checks for the highest average to add to list
        if (len(coords[0][0]) != 0):
            highest = 0
            for i in range(0, len(coords)):
                if (average_nums(coords[highest][1]) < average_nums(coords[i][1])):
                    if ((not (i in index_locations))):
                        highest = i

            index_locations.append(highest)
    
    # Return indexes
    return index_locations

# Sort values of list
def sort_list(x_values, y_values):

    # Checks for length of list
    length_of_list = len(x_values)

    # Sorted list
    sorted_list_x = []
    sorted_list_y = []

    # Adds the smallest value to the list over and over again
    # Until list is empty
    while (length_of_list != 0):
        smallest_value = x_values[0]
        smallest_index = 0
        for i in range(1, length_of_list):
            if (smallest_value > x_values[i]):
                smallest_value = x_values[i]
                smallest_index = i
        sorted_list_x.append(smallest_value)
        sorted_list_y.append(y_values[smallest_index])
        del x_values[smallest_index]
        del y_values[smallest_index]
        length_of_list -= 1
    
    # Returns sorted list
    return [sorted_list_x, sorted_list_y]


# Create grey lines
def create_grey_lines(graph_canvas, extra_padding, 
horizontal_fifth_of_graph, vertical_fifth_of_graph):
    # Creates 7 lines
    for i in range(0, 7):

        # Horizontal lines
        grey_lines = graph_canvas.create_line(extra_padding, 
                                        500 - extra_padding - (vertical_fifth_of_graph * i), 
                                        500, 500 - extra_padding - (vertical_fifth_of_graph * i),
                                        fill="light grey", width=1)

        #Vertical lines                
        grey_lines = graph_canvas.create_line(extra_padding + (horizontal_fifth_of_graph * i), 
                                         500 - extra_padding, 
                                         extra_padding + (horizontal_fifth_of_graph * i), 
                                         extra_padding,
                                         fill = "light grey", width=1)

# Creates dot
def create_dot (x, y, graph_canvas, extra_padding, pixel_x_graph_ratio, 
pixel_y_graph_ratio, colour, lowest_value):
    x -= lowest_value
    dot = graph_canvas.create_oval((
        (x * pixel_x_graph_ratio) + extra_padding) - 3, 
        (500 - ((y * pixel_y_graph_ratio) + extra_padding)) - 3, 
        ((x * pixel_x_graph_ratio) + extra_padding) + 3, 
        (500 - ((y * pixel_y_graph_ratio) + extra_padding)) + 3, fill=colour)

# Creates line
def create_line (x_one, y_one, x_two, y_two, graph_canvas, extra_padding, 
pixel_x_graph_ratio, pixel_y_graph_ratio, colour, lowest_value):
    x_one -= lowest_value
    x_two -= lowest_value
    graph_line = graph_canvas.create_line( 
        (x_one * pixel_x_graph_ratio) + extra_padding, 
        500 - ((y_one * pixel_y_graph_ratio) + extra_padding),
        ((x_two * pixel_x_graph_ratio) + extra_padding),
        (500 - ((y_two * pixel_y_graph_ratio) + extra_padding)), 
        fill=colour, width=2)

# Creates polygon for area graph
def create_area (x_one, y_one, x_two, y_two, graph_canvas, extra_padding, 
pixel_x_graph_ratio, pixel_y_graph_ratio, colour, lowest_value):
    x_one -= lowest_value
    x_two -= lowest_value
    graph_line = graph_canvas.create_polygon( 
                (x_one * pixel_x_graph_ratio) + extra_padding, 
                500 - ((y_one * pixel_y_graph_ratio) + extra_padding),

                ((x_two * pixel_x_graph_ratio) + extra_padding),
                (500 - ((y_two * pixel_y_graph_ratio) + extra_padding)),

                ((x_two * pixel_x_graph_ratio) + extra_padding),
                500 - extra_padding,

                (x_one * pixel_x_graph_ratio) + extra_padding, 
                500 - extra_padding,

                (x_one * pixel_x_graph_ratio) + extra_padding, 
                500 - ((y_one * pixel_y_graph_ratio) + extra_padding),
                
                    fill=colour)

# Creates bar for bar graph
def create_bar (x, y, graph_canvas, extra_padding, pixel_x_graph_ratio,
 pixel_y_graph_ratio, colour):
    graph_line = graph_canvas.create_polygon( 
                (x * pixel_x_graph_ratio) + extra_padding + (pixel_x_graph_ratio * 0.8),  
                500 - ((y * pixel_y_graph_ratio) + extra_padding),

                ((x * pixel_x_graph_ratio) + extra_padding),
                (500 - ((y * pixel_y_graph_ratio) + extra_padding)),

                ((x * pixel_x_graph_ratio) + extra_padding),
                500 - extra_padding,

                (x * pixel_x_graph_ratio) + extra_padding + (pixel_x_graph_ratio * 0.8), 
                500 - extra_padding,

                (x * pixel_x_graph_ratio) + extra_padding + (pixel_x_graph_ratio * 0.8), 
                500 - ((y * pixel_y_graph_ratio) + extra_padding),
                
                    fill=colour)


# Scatter plot
def scatter_plot(graph_canvas, coords, colours):
    # Extra padding
    extra_padding = 35

    # Calculates pixels of graph horziontally
    pixels_of_graph = (500 - extra_padding)

    # Calculates ratio for grey lines
    horizontal_fifth_of_graph = pixels_of_graph//6
    # Calculates ratio for grey lines
    vertical_fifth_of_graph = (pixels_of_graph - extra_padding)//6
    create_grey_lines(graph_canvas, extra_padding, 
                        horizontal_fifth_of_graph, vertical_fifth_of_graph)

    # Creates graph lines
    line_x = graph_canvas.create_line(extra_padding, 500 - extra_padding, 
                                        500, 500 - extra_padding)
    line_y = graph_canvas.create_line(extra_padding, 500 - extra_padding, 
                                        extra_padding, extra_padding)
    # Calculates lowest and highest x values for scale
    lowest = find_lowest_x(coords)
    highest = find_highest_x(coords)

    # Calculates highest y value for scale
    highest_y = find_highest_y(coords)

    print(highest_y)
    print(lowest)
    print(highest)

    # Calculates pixel to graph ratio
    # Checks to see if denominator is 0 to avoid dividing by 0
    if (lowest != highest):
        pixel_x_graph_ratio = (pixels_of_graph-3)/(highest-lowest)
    else:
        pixel_x_graph_ratio = (pixels_of_graph-3)/2
    
    print(pixel_x_graph_ratio)
    
    # Calculate pixel to graph ratio
    pixel_y_graph_ratio = (pixels_of_graph - extra_padding)/highest_y
    
    # Create numbers scale for graph
    graph_canvas.create_text(extra_padding, 500 - (extra_padding/2), text=lowest, 
    fill="black", font=('Arial 10'))

    graph_canvas.create_text(500 - ((extra_padding/2) + (math.log(highest, 10) * 4)), 
                            500 - (extra_padding/2), 
                            text=highest, fill="black", font=('Arial 10'))

    graph_canvas.create_text(extra_padding/2, 500 - extra_padding, 
    text="0", fill="black", font=('Arial 10'))

    graph_canvas.create_text(extra_padding/2, extra_padding + 15, 
    text=highest_y, fill="black", font=(f'Arial 10'))

    graph_canvas.create_text(230, 500 - (extra_padding/2), 
    text=x_name, fill="black", font=(f'Arial 10'))

    graph_canvas.create_text(15, 250 + (extra_padding/2), 
    text=y_name, fill="black", font=(f'Arial 10'), angle=90)

    for l in range(len(coords)):
        for i in range(len(coords[l][0])):
            print("bing")
            print(coords[l][0][i])
            print(coords[l][1][i])
            create_dot (coords[l][0][i], coords[l][1][i], graph_canvas, 
            extra_padding, pixel_x_graph_ratio, pixel_y_graph_ratio, colours[l], lowest)

# Create line graph
def line_graph(graph_canvas, coords, colours):
    # First part is similar to scatter plot
    extra_padding = 35
    pixels_of_graph = (500 - extra_padding)
    horizontal_fifth_of_graph = pixels_of_graph//6
    vertical_fifth_of_graph = (pixels_of_graph - extra_padding)//6
    
    create_grey_lines(graph_canvas, extra_padding, 
    horizontal_fifth_of_graph, vertical_fifth_of_graph)
    
    line_x = graph_canvas.create_line(extra_padding, 500 - extra_padding, 
    500, 500 - extra_padding)

    line_y = graph_canvas.create_line(extra_padding, 500 - extra_padding, 
    extra_padding, extra_padding)

    lowest = find_lowest_x(coords)
    highest = find_highest_x(coords)

    highest_y = find_highest_y(coords)


    if (lowest != highest):
        pixel_x_graph_ratio = (pixels_of_graph-3)/(highest-lowest)
    else:
        pixel_x_graph_ratio = (pixels_of_graph-3)/2

    pixel_y_graph_ratio = (pixels_of_graph - extra_padding)/highest_y

    
    graph_canvas.create_text(extra_padding, 500 - (extra_padding/2), text=lowest, 
    fill="black", font=('Arial 10'))

    graph_canvas.create_text(500 - ((extra_padding/2) + (math.log(highest, 10) * 4)), 
                            500 - (extra_padding/2), 
                            text=highest, fill="black", font=('Arial 10'))

    graph_canvas.create_text(extra_padding/2, 500 - extra_padding, 
    text="0", fill="black", font=('Arial 10'))

    graph_canvas.create_text(extra_padding/2, extra_padding + 15, 
    text=highest_y, fill="black", font=(f'Arial 10'))

    graph_canvas.create_text(230, 500 - (extra_padding/2), 
    text=x_name, fill="black", font=(f'Arial 10'))

    graph_canvas.create_text(15, 250 + (extra_padding/2), 
    text=y_name, fill="black", font=(f'Arial 10'), angle=90)
    
    # Creates a dot for every point
    for l in range(len(coords)):
        for i in range(len(coords[l][0])):
            create_dot (coords[l][0][i], coords[l][1][i], graph_canvas,
            extra_padding, pixel_x_graph_ratio, pixel_y_graph_ratio, colours[l], lowest)
    
    # Connects the sorted dots together
    for l in range(len(coords)):
        sorted_values = sort_list(coords[l][0], coords[l][1])
        coords[l][0] = sorted_values[0]
        coords[l][1] = sorted_values[1]
        for i in range(1, len(coords[l][0])):
            create_line(coords[l][0][i], coords[l][1][i], 
            coords[l][0][i-1], coords[l][1][i-1], graph_canvas, 
            extra_padding, pixel_x_graph_ratio,pixel_y_graph_ratio, colours[l], lowest)    

# Area graph
def area_graph(graph_canvas, coords, colours):
    # First part similar to line graph
    extra_padding = 35
    pixels_of_graph = (500 - extra_padding)
    horizontal_fifth_of_graph = pixels_of_graph//6
    vertical_fifth_of_graph = (pixels_of_graph - extra_padding)//6
    
    create_grey_lines(graph_canvas, extra_padding, 
    horizontal_fifth_of_graph, vertical_fifth_of_graph)
    
    line_x = graph_canvas.create_line(extra_padding, 500 - extra_padding,
                                     500, 500 - extra_padding)
    line_y = graph_canvas.create_line(extra_padding, 500 - extra_padding,
                                     extra_padding, extra_padding)
    
    lowest = find_lowest_x(coords)
    highest = find_highest_x(coords)

    highest_y = find_highest_y(coords)

    if (lowest != highest):
        pixel_x_graph_ratio = (pixels_of_graph-3)/(highest-lowest)
    else:
        pixel_x_graph_ratio = (pixels_of_graph-3)/2
    pixel_y_graph_ratio = (pixels_of_graph - extra_padding)/highest_y
    
    graph_canvas.create_text(extra_padding, 500 - (extra_padding/2), text=lowest, 
    fill="black", font=('Arial 10'))

    graph_canvas.create_text(500 - ((extra_padding/2) + (math.log(highest, 10) * 4)), 
                            500 - (extra_padding/2), 
                            text=highest, fill="black", font=('Arial 10'))

    graph_canvas.create_text(extra_padding/2, 500 - extra_padding, 
    text="0", fill="black", font=('Arial 10'))

    graph_canvas.create_text(extra_padding/2, extra_padding + 15, 
    text=highest_y, fill="black", font=(f'Arial 10'))

    graph_canvas.create_text(230, 500 - (extra_padding/2), 
    text=x_name, fill="black", font=(f'Arial 10'))

    graph_canvas.create_text(15, 250 + (extra_padding/2), 
    text=y_name, fill="black", font=(f'Arial 10'), angle=90)

    for l in range(len(coords)):
        for i in range(len(coords[l][0])):
            create_dot (coords[l][0][i], coords[l][1][i], graph_canvas, 
            extra_padding, pixel_x_graph_ratio, pixel_y_graph_ratio, colours[l], lowest)
    
    for l in range(0, len(coords)):
        sorted_values = sort_list(coords[l][0], coords[l][1])
        coords[l][0] = sorted_values[0]
        coords[l][1] = sorted_values[1]

        for i in range(1, len(coords[l][0])):
            create_area(coords[l][0][i], coords[l][1][i], 
            coords[l][0][i-1], coords[l][1][i-1], graph_canvas, 
            extra_padding, pixel_x_graph_ratio,pixel_y_graph_ratio, 
            colours[l], lowest)
    
    # Creates polygon for each line
    for l in range(0, len(coords)):
        sorted_values = sort_list(coords[l][0], coords[l][1])
        coords[l][0] = sorted_values[0]
        coords[l][1] = sorted_values[1]
        
        for i in range(1, len(coords[l][0])):
            create_line(coords[l][0][i], coords[l][1][i], 
            coords[l][0][i-1], coords[l][1][i-1], graph_canvas, 
            extra_padding, pixel_x_graph_ratio,pixel_y_graph_ratio, colours[l], lowest)


# Inserts a value into a list so that it is sorted x
def add_value_sorted_list_x(nums, value):
    index = 0
    #print(nums)
    for i in nums:
        if (i > value):
            index += 1

    return index

# Inserts a value into a list so that is is sorted y
def add_value_sorted_list_y(nums, value):
    index = 0
    for i in nums:
        if (i[0] > value):
            index += 1

    return index

# Sorts the bar info into something that even with multiple data points
# Can be read
# Makes a list with an x value and every y value sorted for it
# Example [[[1], [5, 3, 2]], [[2], [10, 2, 1]]]
def sort_bar_info(coords, colours):
    new_coords_x = []
    new_coords_y = []
    for l in range(0, len(coords)):
        for i in range(0, len(coords[l][0])):
            # Checks if x values exists
            if ( not (coords[l][0][i] in new_coords_x) ):
                index = add_value_sorted_list_x(new_coords_x, coords[l][0][i])
                new_coords_x.insert(index, coords[l][0][i])
                new_coords_y.insert(index, [ [coords[l][1][i], colours[l]] ])
            # Insert y value into x value list
            else:
                for index in range(0, len(new_coords_x)):
                    if (new_coords_x[index] == coords[l][0][i]):
                        new_coords_y[index].insert(
                            add_value_sorted_list_y(new_coords_y[index], coords[l][1][i]), 
                            [coords[l][1][i], colours[l]])
    
    # Combines the x and y coordinates into one list
    combined_coords = []

    for i in range(len(new_coords_x) - 1, -1, -1):
        combined_coords.append([new_coords_x[i], new_coords_y[i]])

    return combined_coords

# Bar graph
def bar_graph(graph_canvas, coords, colours):
    # First part similar to scatter plot
    extra_padding = 35
    pixels_of_graph = (500 - extra_padding)
    
    line_x = graph_canvas.create_line(extra_padding, 500 - extra_padding,
                                     500, 500 - extra_padding)
    line_y = graph_canvas.create_line(extra_padding, 500 - extra_padding,
                                     extra_padding, extra_padding)
    

    highest_y = find_highest_y(coords)

    pixel_y_graph_ratio = (pixels_of_graph - extra_padding)/highest_y
    lowest = lowest_x_amount(coords)
    if (lowest != 0):
        pixel_x_graph_ratio = (pixels_of_graph)/(lowest)
    else:
        pixel_x_graph_ratio = 0
    pixel_y_graph_ratio = (pixels_of_graph - extra_padding)/highest_y
    
    # Gets coords sorted into bar graph form for overlapping bars
    # Would be unnessary if only one set of data, like the program
    # Is giving
    combined_coords = sort_bar_info(coords, colours)

    graph_canvas.create_text(extra_padding, 500 - (extra_padding/2), text=lowest, 
    fill="black", font=('Arial 10'))




    graph_canvas.create_text(extra_padding/2, extra_padding + 15, 
    text=highest_y, fill="black", font=(f'Arial 10'))


    graph_canvas.create_text(230, 500 - (extra_padding/2), 
    text=x_name, fill="black", font=(f'Arial 10'))

    graph_canvas.create_text(15, 250 + (extra_padding/2), 
    text=y_name, fill="black", font=(f'Arial 10'), angle=90)

    # For every value in combined coords plot bar
    for i in range(0, len(combined_coords)):
        l = 0
        current_value = combined_coords[i][1][l][1]
        current_streak = 0
        while (l < len(combined_coords[i][1])):
            create_bar(i, combined_coords[i][1][l][0], 
                    graph_canvas, extra_padding, 
                    pixel_x_graph_ratio,pixel_y_graph_ratio, 
                    combined_coords[i][1][l][1])
            l += 1
        
    

# Figures out what graph to call
def create_graph(graph_frame, coords, colours, type_of_graph):
    global canvas
    # Canvas defined
    canvas = tkinter.Canvas (graph_frame, bg="white", height=500, width=500)
    
    # Checks for each type of graph
    if (type_of_graph == "scatter plot"):
        scatter_plot(canvas, coords, colours)

    elif (type_of_graph == "bar graph"):
        bar_graph(canvas, coords, colours)
    
    elif (type_of_graph == "area graph"):
        area_graph(canvas, coords, colours)
    
    elif (type_of_graph == "line graph"):
        line_graph(canvas, coords, colours)

    # Updates canvas
    canvas.pack()
    canvas.update()

#Exits out of the window
def exit_program ():
    exit()

#Validates integers
def int_valid(x):
    if (x[:].isdigit() and x[0] != ""):
        valid = True
    else:
        valid = False
    return valid

#Creates empty label for design purposes
def empty_label(x, y, z, a, b):
    empty = tkinter.Label(x, bg=bkg, width=a, height=b)
    empty.grid(row=y, column=z)

#What happenes when create new is clicked
def create_click():
   
    global exit_frame_1, logo_frame_1, open_frame

    exit_frame_1.destroy()
    logo_frame_1.destroy()
    open_frame.destroy()
   
    second_page()

#Yeo Umair add the file thingies here
def opening_file():
    global x_list, y_list, info
    global type_graph, x_name, y_name, name
    global exit_frame_1, logo_frame_1, open_frame

    name = open_files_entry.get()

    exit_frame_1.destroy()
    logo_frame_1.destroy()
    open_frame.destroy()

    info = open_file(name)
    print(info)
    type_graph = info[0]
    x_list = info[2][0][0]
    y_list = info[2][0][1]
    x_name = info[1][0]
    y_name = info[1][1]

    for i in range(len(x_list)):
        x_list[i] = int(x_list[i])
        y_list[i] = int(y_list[i])
    print(x_list)
    print(y_list)
    third_page()

#What happens when open file button is pressed
def open_click():
    global open_frame, create_button, open_button
    global create_button, open_button, open_files_entry

    create_button.destroy()
    open_button.destroy()

    open_files_text = tkinter.Label(open_frame, text="Type the name of your file:",
                                    font=("Times New", 19), anchor="center", bg=bkg)
    open_files_text.grid(row=1, column=1)

    empty_label(open_frame, 1, 2, 3, 1)
    empty_label(open_frame, 1, 4, 3, 1)

    open_files_entry = tkinter.Entry(open_frame, width=50, font=(16), bg=bkg)
    open_files_entry.grid(row=1, column=3)

    open_files_button = tkinter.Button(open_frame, width=10, text="Enter", font=(16),
                                       anchor="center", command=opening_file)
    open_files_button.grid(row=1, column=5)

#Brings you from second page to first page
def back_click():

    global exit_frame_2, logo_frame_2, dn_frame, input_frame, graph_frame, canvas
   

    exit_frame_2.destroy()
    logo_frame_2.destroy()
    dn_frame.destroy()
    input_frame.destroy()
    graph_frame.destroy()
    canvas.destroy()
    first_page()

#What happenes when user wants to change the title
#       and then click the change tiltle button

def dn_1_click():
   
    global dn_1, dn_1_e, dn_frame, dn_1_c
   
    dn_1_c = True
    dn_1.destroy()

    dn_1_e = tkinter.Entry(dn_frame, bg="White", width=30, font=("Times new", 18))
    dn_1_e.grid(row=1, column=0)

#What happens when Enter or Return is clicked
def r_click(event=" "):

    global title_1_e, title_1, dn_frame, dn_g1, dn_1_c, f_tf, s_tf, ds1_tf, input_frame

    if (dn_1_c == True):
       
        if (dn_1_e.get() != " " and dn_1_e.get() != ""):
            dn_g1 = dn_1_e.get()
           
#Destroys entry creates button with new text for title
        dn_1_e.destroy()
        dn_1 = tkinter.Button(dn_frame, text=dn_g1, anchor="center", bg=bkg, font=("Times new", 18),
                               command = dn_1_click, width=30, relief="flat")
        dn_1.grid(row=1, column=0)
        dn_1_c = False

#Data set 1, all the x and y entries        
def ds1():
   
    global input_frame, ds1_tf, ex1, ey1
   
    ds1_tf = True
    ex1 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
   
    ey1 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    for i in range(20):
        num = i + 2
        ex1[i] = tkinter.Entry(input_frame, bg="White", width=15, font=(14))
        ex1[i].grid(row=num, column=0)

        ey1[i] = tkinter.Entry(input_frame, bg="White", width=15, font=(14))
        ey1[i].grid(row=num, column=2)

#What happens when create graph is clicked, all variables make the graph
def create_graph_click():
    global x_name, y_name
    global x_name_entry, y_name_entry, x_axis_entry, y_axis_entry, dn_g1
    global x_scale_entry, y_scale_entry, ex1, ey1, x_list, y_list, title

    title = dn_g1
   
    x_list = []
    y_list = []

    x_name = x_name_entry.get()
    y_name = y_name_entry.get()


    for i in range(20):
        if (int_valid(ex1[i].get()) == True and int_valid(ey1[i].get()) == True):
            x_list.append(int(ex1[i].get()))
            y_list.append(int(ey1[i].get()))

    print(x_list)
    print(y_list)
    canvas.destroy()
    create_graph(graph_frame, [[x_list, y_list]],
                 ["black"], graph_type)

def create_graph_click_2():
    print(1)

#Creates the page after open file is clicked
def third_page():
   
    global window, graph_frame_2

    graph_frame_2 = tkinter.Frame(window, width=500)
    graph_frame_2.grid(row=0, column =0, sticky="E")

    info = open_file(name)
    print(info)
    type_graph = info[0]
    x_list = info[2][0][0]
    y_list = info[2][0][1]
    for i in range(len(x_list)):
        x_list[i] = int(x_list[i])
        y_list[i] = int(y_list[i])
    x_name = info[1][0]
    y_name = info[1][1]
    create_graph(graph_frame_2, [[x_list, y_list]],
                 ["black"], type_graph)
   
#What happens when create graph is clicked, all variables make the graph
def create_graph_click():
    global x_name, y_name
    global x_name_entry, y_name_entry, x_axis_entry, y_axis_entry, dn_g1
    global x_scale_entry, y_scale_entry, ex1, ey1, x_list, y_list, title

    title = dn_g1
   
    x_list = []
    y_list = []

    x_name = x_name_entry.get()
    y_name = y_name_entry.get()


    for i in range(20):
        if (int_valid(ex1[i].get()) == True and int_valid(ey1[i].get()) == True):
            x_list.append(int(ex1[i].get()))
            y_list.append(int(ey1[i].get()))

    print(x_list)
    print(y_list)
    canvas.destroy()
    create_graph(graph_frame, [[x_list, y_list]],
                 ["black"], graph_type)

#Function called so file can be saved
def gui_save_file():
    global title
    print("BERRRRRSDF")
    print (title)
    if (title != "Click to name graph."):
        print("Br")
        save_file_data(title, graph_type, [[x_list, y_list]])
    else:
        save_file_data(name, graph_type, [[x_list, y_list]])

 #First page/home page      
def first_page():

    global exit_frame_1, logo_frame_1, open_frame, f_tf, s_tf, dn_1_c
    global create_button, open_button, name

    name = "Unnamed"
   
    f_tf = True
    s_tf = False
    dn_1_c = False
   
    exit_frame_1 = tkinter.Frame(window, bg=bkg)
    exit_frame_1.grid(row=0, column=0)

    logo_frame_1 = tkinter.Frame(window, bg=bkg)
    logo_frame_1.grid(row=1, column=0)

    open_frame = tkinter.Frame(window, bg=bkg)
    open_frame.grid(row=2, column=0)

    empty_label(exit_frame_1, 0, 0, 195, 1)

    exit_button = tkinter.Button(exit_frame_1, text="X", command=exit_program, width=3, height=1,
                                 bg="#ED6A6A", fg="White")
    exit_button.grid(row=0, column=1)

    empty_label(logo_frame_1, 0, 0, 1, 38)

    logo = tkinter.Label(logo_frame_1, bg="White", text="A Priori",
                         font=("Century 40 bold"), anchor="center")
    logo.grid(row=0, column=1)

    create_button = tkinter.Button(open_frame, text="Create New", font=("Times new", 15, "bold"),
                                   anchor="center", bg="#6B2012", command = create_click, width=30,
                                   fg="White")
    create_button.grid(row = 0, column = 0)

    empty_label(open_frame, 0, 1, 15, 1)

    open_button = tkinter.Button(open_frame, text="Open File", font=("Times new", 15, "bold"),
                                 anchor="center", bg="#093535", command = open_click, width=30,
                                 fg="White")
    open_button.grid(row = 0, column = 2)

#Second page/ main page
def second_page():

    global window, exit_frame_2, logo_frame_2, input_frame, dn_1, dn_frame
    global f_tf, s_tf, dn_g1, x_name_entry, y_name_entry, graph_frame, graph_type, x_name, y_name

    f_tf = False
    s_tf = True

    x_name = "X"
    y_name = "Y"

    dn_g1 = "Click to name graph."

    exit_frame_2 = tkinter.Frame(window, bg=bkg)
    exit_frame_2.grid(row=0, column=0)
   
    logo_frame_2 = tkinter.Frame(window, bg=bkg)
    logo_frame_2.grid(row=1, column=0)
   
    dn_frame = tkinter.Frame(window, bg=bkg)
    dn_frame.grid(row=2, column=0)

    input_frame = tkinter.Frame(window, bg=bkg)
    input_frame.grid(row=3, column=0)

    back_button = tkinter.Button(exit_frame_2, text="< Back", anchor="center", bg=bkg,  width=10,
                                 font=("Times new", 13), command = back_click, relief="flat")
    back_button.grid(row = 0, column = 0)

    empty_label(exit_frame_2, 0, 1, 166, 1)

    exit_button = tkinter.Button(exit_frame_2, text="X", command=exit_program, width=3, height=1,
                                 bg="#ED6A6A", fg="White", anchor="n")
    exit_button.grid(row=0, column=2)
   
    logo = tkinter.Label(exit_frame_2, bg="White", text="A Priori",
                         font=("Times new", 20, "bold"), anchor="center")
    logo.grid(row=0, column=1)

    empty_label(dn_frame, 1, 0, 1, 3)

    dn_1 = tkinter.Button(dn_frame, text=dn_g1, anchor="center", bg=bkg, font=("Times new", 18),
                               command = dn_1_click, width=30, relief="flat")
    dn_1.grid(row=1, column=0)

    empty_label(dn_frame, 0, 2, 98, 1)

    empty_label(input_frame, 0, 1, 3, 1)
    empty_label(input_frame, 1, 6, 98, 1)
    empty_label(input_frame, 1, 3, 7, 1)

    for i in range(20):
        num = i + 2
        empty_label(input_frame, num, 0, 20, 2)
        empty_label(input_frame, num, 2, 20, 2)

    x_label = tkinter.Label(input_frame, bg="#106A6A", text="X", fg=bkg,
                         font=(12), anchor="center", width=15)
    x_label.grid(row=1, column=0)
   
    y_label = tkinter.Label(input_frame, bg="#9A3C83", text="Y", fg=bkg,
                         font=(12), anchor="center", width=15)
    y_label.grid(row=1, column=2)

    ds1()

    #Creates labels and entry points so users can customize their graphs
    x_name_label = tkinter.Label(input_frame, bg=bkg, text="Enter X-axis name:",
                                 font=(12), anchor="center", width=20)
    x_name_label.grid(row=3, column=4)

    y_name_label = tkinter.Label(input_frame, bg=bkg, text="Enter Y-axis name:",
                                 font=(12), anchor="center", width=20)
    y_name_label.grid(row=5, column=4)
   
    x_name_entry = tkinter.Entry(input_frame, bg="White", width=20, font=(14))
    x_name_entry.grid(row=4, column=4)

    y_name_entry = tkinter.Entry(input_frame, bg="White", width=20, font=(14))
    y_name_entry.grid(row=6, column=4)

    type_label = tkinter.Label(input_frame, bg=bkg, text="Select graph type:",
                                 font=(12), anchor="center", width=20)
    type_label.grid(row=9, column=4)

    graph_type = "scatter plot"
   
    scatter = tkinter.Button(input_frame, text="Scatter Plot", anchor="center", font=(15),
                               command=scatter_func, width=20)
    scatter.grid(row=10, column=4)
   
    line = tkinter.Button(input_frame, text="Line Graph", anchor="center", font=(15),
                               command=line_func, width=20)
    line.grid(row=11, column=4)
   
    bar = tkinter.Button(input_frame, text="Bar Graph", anchor="center", font=(15),
                               command=bar_func, width=20)
    bar.grid(row=12, column=4)
   
    area = tkinter.Button(input_frame, text="Area Graph", anchor="center", font=(15),
                               command=area_func, width=20)
    area.grid(row=13, column=4)

    create = tkinter.Button(input_frame, text="Create Graph", anchor="center", font=(15),
                               command=create_graph_click, width=20)
    create.grid(row=17, column=4)

    save = tkinter.Button(input_frame, text="Save File", anchor="center", font=(15),
                          command=gui_save_file, width=20)
    save.grid(row=19, column=4)

    graph_frame = tkinter.Frame(window, width=500)
    graph_frame.grid(row=3, column =0, sticky="E")

    create_graph(graph_frame, [[[], []]],
                 ["black"], "line graph")


def scatter_func():
    global graph_type
    graph_type = "scatter plot"


def line_func():
    global graph_type
    graph_type = "line graph"


def bar_func():
    global graph_type
    graph_type = "bar graph"


def area_func():
    global graph_type
    graph_type = "area graph"

def main():

    global window, bkg

    bkg = "White"
    
    window = tkinter.Tk()
    window.title("Graphing")
    window.geometry("1400x900")
    window.configure(bg=bkg)
    window.bind("<Return>", r_click)

    first_page()

    window.mainloop()
    
main()
