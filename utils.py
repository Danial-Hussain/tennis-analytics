"""
utils.py:
Collection of functions to help wrangle data, generate plots, and style tables.
"""

__author__ = "Ali Hussain"
__version__ = "1.0"

# Import libraries
from plotting import serve as serve_plot
from plotting import shot as shot_plot
import pandas as pd
import numpy as np

def tournament_data_serve(data, choice):
    """
    Gathers serve direction data for a player for each grandslam tournament
    """
    # Fetch Wimbledon
    p_data_chart_wimbledon = data[(data['Player Name'] == choice) &
        (data['level_1'].str.find("Total") == -1) & 
        (data['tournament'] == 'Wimbledon')]\
        .groupby('level_1').mean().iloc[:, 0:6]

    # Fetch US Open
    p_data_chart_us_open = data[(data['Player Name'] == choice) &
        (data['level_1'].str.find("Total") == -1) & 
        (data['tournament'] == 'US_Open')]\
        .groupby('level_1').mean().iloc[:, 0:6]

    # Fetch Roland Garros
    p_data_chart_roland = data[(data['Player Name'] == choice) &
        (data['level_1'].str.find("Total") == -1) & 
        (data['tournament'] == 'Roland_Garros')]\
        .groupby('level_1').mean().iloc[:, 0:6]

    # Fetch Australian Open
    p_data_chart_australian = data[(data['Player Name'] == choice) &
        (data['level_1'].str.find("Total") == -1) & 
        (data['tournament'] == 'Australian_Open')]\
        .groupby('level_1').mean().iloc[:, 0:6]

    # Fetch Combined Tournament
    total = data[(data['Player Name'] == choice) &
        (data['level_1'].str.find("Total") == -1)]\
        .groupby('level_1').mean().iloc[:, 0:6]

    return (p_data_chart_wimbledon, p_data_chart_us_open,
            p_data_chart_roland, p_data_chart_australian,
            total)

def tournament_data_shot(data, choice):
    """
    Gathers shot direction data for a player for each grandslam tournament
    """
    # Fetch Wimbledon
    p_data_chart_wimbledon = data[(data['player'] == choice) &
        (data['row'].str.find("Total") == -1) & 
        (data['row'].str.find("S") == -1) &
        (data['tournament'] == 'Wimbledon')]\
        .groupby(['player', 'row']).mean().iloc[:, 0:6]

    # Fetch US Open
    p_data_chart_us_open = data[(data['player'] == choice) &
        (data['row'].str.find("Total") == -1) & 
        (data['row'].str.find("S") == -1) &
        (data['tournament'] == 'US_Open')]\
        .groupby(['player', 'row']).mean().iloc[:, 0:6]

    # Fetch Roland Garros
    p_data_chart_roland = data[(data['player'] == choice) &
        (data['row'].str.find("Total") == -1) & 
        (data['row'].str.find("S") == -1) &
        (data['tournament'] == 'Roland_Garros')]\
        .groupby(['player', 'row']).mean().iloc[:, 0:6]

    # Fetch Australian Open
    p_data_chart_australian = data[(data['player'] == choice) &
        (data['row'].str.find("Total") == -1) & 
        (data['row'].str.find("S") == -1) &
        (data['tournament'] == 'Australian_Open')]\
        .groupby(['player', 'row']).mean().iloc[:, 0:6]

    # Fetch Combined Tournament
    total = data[(data['player'] == choice) &
        (data['row'].str.find("Total") == -1) & 
        (data['row'].str.find("S") == -1)]\
        .groupby(['player', 'row']).mean().iloc[:, 0:6]

    return (p_data_chart_wimbledon, p_data_chart_us_open,
        p_data_chart_roland, p_data_chart_australian, total)


# --- Create Plots ---
def get_plots_serve(court_w, court_u, court_r, court_a, image, choice):
    """
    Creates serve plots
    """
    if not court_w.empty:
        plot_court_w = serve_plot(
            title = f"Average Serve Percentage: Wimbledon",
            serve_data = court_w,
            player_img_link = image,
            outer_court_color = "#A2C128")
    else:
        plot_court_w = f"No Wimbledon data available for {choice}"

    if not court_u.empty:
        plot_court_u = serve_plot(
            title = f"Average Serve Percentage: US Open",
            serve_data = court_u,
            player_img_link = image,
            outer_court_color = "#3C638E")
    else:
        plot_court_u = f"No US Open data available for {choice}"

    if not court_r.empty:
        plot_court_r = serve_plot(
            title = f"Average Serve Percentage: Roland Garros",
            serve_data = court_r,
            player_img_link = image,
            outer_court_color = "#b06835")
    else:
        plot_court_r = f"No Roland Garros data available for {choice}"

    if not court_a.empty:
        plot_court_a = serve_plot(
            title = f"Average Serve Percentage: Australian Open",
            serve_data = court_a,
            player_img_link = image,
            outer_court_color = "#377DB8")
    else:
        plot_court_a = f"No Australian Open data available for {choice}"

    return (plot_court_w, plot_court_u, plot_court_r, plot_court_a)


def get_plots_shot(court_w, court_u, court_r, court_a, image, choice):
    """
    Creates shot plots
    """
    if not court_w.empty:
        plot_court_w = shot_plot(
            title = f"Average Shot Percentage: Wimbledon",
            shot_data = court_w,
            player_img_link = image,
            outer_court_color = "#A2C128")
    else:
        plot_court_w = f"No Wimbledon data available for {choice}"

    if not court_u.empty:
        plot_court_u = shot_plot(
            title = f"Average Shot Percentage: US Open",
            shot_data = court_u,
            player_img_link = image,
            outer_court_color = "#3C638E")
    else:
        plot_court_u = f"No US Open data available for {choice}"

    if not court_r.empty:
        plot_court_r = shot_plot(
            title = f"Average Shot Percentage: Roland Garros",
            shot_data = court_r,
            player_img_link = image,
            outer_court_color = "#b06835")
    else:
        plot_court_r = f"No Roland Garros data available for {choice}"

    if not court_a.empty:
        plot_court_a = shot_plot(
            title = f"Average Shot Percentage: Australian Open",
            shot_data = court_a,
            player_img_link = image,
            outer_court_color = "#377DB8")
    else:
        plot_court_a = f"No Australian Open data available for {choice}"

    return (plot_court_w, plot_court_u, plot_court_r, plot_court_a)


# --- Style Table ---
def style_table(dataset):
    """
    Color styling for data table
    """
    color1 = '#d6eaff'
    color2 = '#eaf4ff'
    mask1 = dataset.iloc[:, 0] > dataset.iloc[:, 2]
    mask2 = dataset.iloc[:, 2] > dataset.iloc[:, 0]
    mask3 = dataset.iloc[:, 1] > dataset.iloc[:, 3]
    mask4 = dataset.iloc[:, 3] > dataset.iloc[:, 1]
    df = pd.DataFrame('background-color',
        index = dataset.index,
        columns = dataset.columns)
    df.iloc[:,0] = np.where(
        mask1, f'background-color: {color1}',
        dataset.iloc[:, 0])
    df.iloc[:,2] = np.where(
        mask2, f'background-color: {color1}',
        dataset.iloc[:, 2])
    df.iloc[:,1] = np.where(
        mask3, f'background-color: {color2}',
        dataset.iloc[:, 1])
    df.iloc[:,3] = np.where(
        mask4, f'background-color: {color2}',
        dataset.iloc[:, 3])
    df.columns = dataset.columns
    return df

# --- Comparison Table ---
def return_serve_table(returns, serves, return_player, serve_player):
    """
    Creates table comparing serve and return 
    """
    try:
        r = returns[returns['Player Name'] == return_player]\
         .groupby("row").mean()[['return_percentage']]
        s = serves[(serves['Player Name'] == serve_player)\
         & (serves['level_1'].str.find("Total") == -1)]\
         .groupby("Player Name").mean().T
        t = r.join(s)
        t = np.round(t, 2)
        t.columns = [f"{return_player} return %",
                     f"{serve_player} serve %"]
        t = t[t.columns[::-1]]
        mask1 = np.max(t.iloc[0:3, 0])
        mask2 = np.max(t.iloc[3:, 0])
        mask3 = np.min(t.iloc[0:3, 1])
        mask4 = np.min(t.iloc[3:, 1])
        masks = [mask1, mask2, mask3, mask4]
        color = '#d6eaff'
        return t.style.apply(
            lambda x: [f"background: {color}" if v in\
             masks else "" for v in x], axis = 1)
    except:
        return "Couldn't generate comparison table"