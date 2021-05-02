"""
plotting.py:
Functions to generate plots in dashboard.
"""

__author__ = "Ali Hussain"
__version__ = "1.0"

# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib.collections import PatchCollection
from matplotlib.offsetbox import  OffsetImage
import urllib.request

""" Function to create serve plots """
def serve(
    title,
    serve_data,
    inner_court_color = "#A2C128",
    outer_court_color = "#A2C128",
    player_img_link = None,
    ax=None,
    color = 'white',
    lw = 4, 
    s = 2,
    x1 = -21,
    x2 = 21,
    y1 = -20,
    y2 = 45):
    
    fig = plt.figure()

    # Check if axis is provided
    if ax is None:
        ax = plt.gca()

    # Create outside of court
    fill_color = Rectangle(
        (-18, -39), 36, 78,
        linewidth = lw,
        color = inner_court_color,
        fill = True
    )
    outer_frame_line = Rectangle(
        (-18, -39), 36, 78,
        linewidth = lw,
        color = color,
        fill = False
    )
    # Create net
    net = Rectangle(
        (-19, 0), 38, 0,
        linewidth = lw * 1.5,
        color = '#e9f0f2',
        Fill = False
    )
    # Bottom of Court
    # Create Baseline 
    p1_baseline = Rectangle(
        (-13.5, -39), 27, 18,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create Left & Right Double's Ally
    p1_left_double = Rectangle(
        (-18, -39), 4.5, 39,
        linewidth = lw,
        color = color,
        Fill = False
    )
    p1_right_double = Rectangle(
        (13.5, -39), 4.5, 39,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create small line on baseline
    p1_baseline_line = Rectangle(
        (0, -39), 0, 2,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Top of Court
    p2_baseline = Rectangle(
        (-13.5, 21), 27, 18,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create Left & Right Service Box
    p2_left_service = Rectangle(
        (-13.5, 0), 13.5, 21,
        linewidth = lw,
        color = color,
        Fill = False
    )
    p2_right_service = Rectangle(
        (0, 0), 13.5, 21,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create Left & Right Double's Ally
    p2_left_double = Rectangle(
        (-18, 0), 4.5, 39,
        linewidth = lw,
        color = color,
        Fill = False
    )
    p2_right_double = Rectangle(
        (13.5, 0), 4.5, 39,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create small line on baseline
    p2_baseline_line = Rectangle(
        (0, 39), 0, -2,
        linewidth = lw,
        color = color,
        Fill = False
    )
  
    # Serve Stats
    p1_dc_wide = f"1st:\n{round(serve_data.iloc[0, 0],2)}\n\n 2nd:\n{round(serve_data.iloc[1, 0],2)}"
    p1_dc_body = f"1st:\n{round(serve_data.iloc[0, 1],2)}\n\n 2nd:\n{round(serve_data.iloc[1, 1],2)}"
    p1_dc_t = f"1st:\n{round(serve_data.iloc[0, 2],2)}\n\n 2nd:\n{round(serve_data.iloc[1, 2],2)}"
    p1_ad_wide = f"1st:\n{round(serve_data.iloc[0, 3],2)}\n\n 2nd:\n{round(serve_data.iloc[1, 3],2)}"
    p1_ad_body = f"1st:\n{round(serve_data.iloc[0, 4],2)}\n\n 2nd:\n{round(serve_data.iloc[1, 4],2)}"
    p1_ad_t = f"1st:\n{round(serve_data.iloc[0, 5],2)}\n\n 2nd:\n{round(serve_data.iloc[1, 5],2)}"
    
    # Create service boxes
    ind = [-13.5, -9, -4.5, 0, 4.5, 9]
    p1_serve_boxes = []
    for i in ind:
        p1_serve_box = Rectangle(
            (i, 0), 4.5, 21, linewidth = lw * .75, 
            color = "#F1F3F4", fill = True, alpha = 0.25, 
            linestyle = '-.')
        p1_serve_boxes.append(p1_serve_box)

    # Add Player 1 Stats
    ind = [-11.25, -6.75, -2.25, 2.25, 6.75, 11.25]
    p1_serve_stats = [p1_dc_wide, p1_dc_body, p1_dc_t,
                      p1_ad_wide, p1_ad_body, p1_ad_t]
    for i, val in enumerate(ind):
        ax.annotate(
            p1_serve_stats[i], (val, 10.5),
            color='white', weight='bold',
            fontsize=12, ha='center', va='center')

    # Plot the court
    court_color = PatchCollection([fill_color], zorder = 0)
    court_lines = PatchCollection(
        [p1_baseline, p1_left_double, p1_right_double,
         p2_baseline, p2_left_service, p2_right_service,
         p2_left_double, p2_right_double,
         net, p2_baseline_line], -1)
    p1_serve = PatchCollection(p1_serve_boxes, 1)

    ax.add_collection(court_lines)
    ax.add_collection(p1_serve)

    try:
        # Add Player Images
        player1 = urllib.request.urlretrieve(
            player_img_link)
        pic = plt.imread(player1[0])
        img = OffsetImage(pic, zoom=.18)
        img.set_offset((375,63))
        ax.add_artist(img)
    except:
        print("Couldn't find image")

    ax.set_xlim(x1,x2)
    ax.set_ylim(y1,y2)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(labelbottom='off', labelleft='off')
    ax.set_facecolor(outer_court_color)
    ax.axes.get_xaxis().set_ticks([])
    ax.axes.get_yaxis().set_ticks([])
    ax.set_title(title, fontsize = 15)
    plt.figure(figsize=(10,30))
    return fig


""" Function to create shot plots """
def shot(
    title,
    shot_data,
    inner_court_color = "#A2C128",
    outer_court_color = "#A2C128",
    player_img_link = None,
    ax=None,
    color = 'white',
    lw = 4, 
    s = 2,
    x1 = -21,
    x2 = 21,
    y1 = -20,
    y2 = 45):
    
    fig = plt.figure()

    # Check if axis is provided
    if ax is None:
        ax = plt.gca()

    # Create outside of court
    fill_color = Rectangle(
        (-18, -39), 36, 78,
        linewidth = lw,
        color = inner_court_color,
        fill = True
    )
    outer_frame_line = Rectangle(
        (-18, -39), 36, 78,
        linewidth = lw,
        color = color,
        fill = False
    )
    # Create net
    net = Rectangle(
        (-19, 0), 38, 0,
        linewidth = lw * 1.5,
        color = '#e9f0f2',
        Fill = False
    )
    # Bottom of Court
    # Create Baseline 
    p1_baseline = Rectangle(
        (-13.5, -39), 27, 18,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create Left & Right Double's Ally
    p1_left_double = Rectangle(
        (-18, -39), 4.5, 39,
        linewidth = lw,
        color = color,
        Fill = False
    )
    p1_right_double = Rectangle(
        (13.5, -39), 4.5, 39,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create small line on baseline
    p1_baseline_line = Rectangle(
        (0, -39), 0, 2,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Top of Court
    p2_baseline = Rectangle(
        (-13.5, 21), 27, 18,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create Left & Right Service Box
    p2_left_service = Rectangle(
        (-13.5, 0), 13.5, 21,
        linewidth = lw,
        color = color,
        Fill = False
    )
    p2_right_service = Rectangle(
        (0, 0), 13.5, 21,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create Left & Right Double's Ally
    p2_left_double = Rectangle(
        (-18, 0), 4.5, 39,
        linewidth = lw,
        color = color,
        Fill = False
    )
    p2_right_double = Rectangle(
        (13.5, 0), 4.5, 39,
        linewidth = lw,
        color = color,
        Fill = False
    )
    # Create small line on baseline
    p2_baseline_line = Rectangle(
        (0, 39), 0, -2,
        linewidth = lw,
        color = color,
        Fill = False
    )
  
    # Shot Stats
    b_cross_court = f"Backhand Crosscourt:\n{round(shot_data.iloc[0,0], 2)}"
    b_down_middle = f"Backhand Down Middle:\n{round(shot_data.iloc[0,1], 2)}"
    b_down_line = f"Backhand Down Line:\n{round(shot_data.iloc[0,2], 2)}"
    b_inside_out = f"Backhand Inside Out:\n{round(shot_data.iloc[0,3],2)}" # cross court
    b_inside_in = f"Backhand Inside In:\n{round(shot_data.iloc[0,4], 2)}" # down the line
    f_cross_court = f"Forehand Cross Court:\n{round(shot_data.iloc[1,0],2)}"
    f_down_middle = f"Forehand Down Middle:\n{round(shot_data.iloc[1,1],2)}"
    f_down_line = f"Forehand Down Line:\n{round(shot_data.iloc[1,2],2)}"
    f_inside_out = f"Forehand Inside Out:\n{round(shot_data.iloc[1,3],2)}" # cross court
    f_inside_in = f"Forehand Inside In:\n{round(shot_data.iloc[1,4], 2)}" # down the line

    # Create Shot Boxes
    ind = [-13.5, -4.5, 4.5]
    p1_shot_boxes = []
    for i in ind:
        p1_shot_box = Rectangle(
            (i, 21), 9, 18, linewidth = lw * .75, 
            color = "#F1F3F4", fill = True, alpha = 0.25, 
            linestyle = '-.')
        p1_shot_boxes.append(p1_shot_box)
        
    # Add Shot Stats
    ind = [-9, 0, 9]
    pos = [35, 31, 27, 23]
    pos2 = [35, 27]
    p1_shot_stats = [f_cross_court, f_inside_in,
                     b_down_line, b_inside_out,
                     f_down_middle, b_down_middle,
                     f_down_line, f_inside_out,
                     b_cross_court, b_inside_in]
    for i in range(4):
        ax.annotate(p1_shot_stats[i], (ind[0], pos[i] + 1),
         color = 'white', weight = 'bold',
         fontsize = 5.5, ha = 'center', va = 'center')
    for i in range(2):
        ax.annotate(p1_shot_stats[i+4], (ind[1], pos2[i]-1),
         color = 'white', weight = 'bold',
         fontsize = 5.5, ha = 'center', va = 'center')
    for i in range(4):
        ax.annotate(p1_shot_stats[i+6], (ind[2], pos[i] + 1),
         color = 'white', weight = 'bold',
         fontsize = 5.5, ha = 'center', va = 'center')

    # Plot the court
    court_color = PatchCollection([fill_color], zorder = 0)
    court_lines = PatchCollection(
        [p1_baseline, p1_left_double, p1_right_double,
         p2_baseline, p2_left_service, p2_right_service,
         p2_left_double, p2_right_double,
         net, p2_baseline_line], -1)
    p1_shot = PatchCollection(p1_shot_boxes, 1)

    ax.add_collection(court_lines)
    ax.add_collection(p1_shot)

    try:
        # Add Player Images
        player1 = urllib.request.urlretrieve(
            player_img_link)
        pic = plt.imread(player1[0])
        img = OffsetImage(pic, zoom=.18)
        img.set_offset((375,63))
        ax.add_artist(img)
    except:
        print("Couldn't find image")

    ax.set_xlim(x1,x2)
    ax.set_ylim(y1,y2)
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.tick_params(labelbottom='off', labelleft='off')
    ax.set_facecolor(outer_court_color)
    ax.axes.get_xaxis().set_ticks([])
    ax.axes.get_yaxis().set_ticks([])
    ax.set_title(title, fontsize = 15)
    plt.figure(figsize=(10,30))
    return fig