"""
dashboard.py:
Code to create streamlit dashboard.
"""

__author__ = "Ali Hussain"
__version__ = "1.0"

# Import libraries
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import json
from loading import (
    load_serve_mens,
    load_serve_womens,
    load_shot_mens,
    load_shot_womens,
    load_returns_mens,
    load_returns_womens)
from utils import (
    tournament_data_serve,
    tournament_data_shot,
    get_plots_serve,
    get_plots_shot,
    style_table,
    return_serve_table)

# --- Page Configuration/Layout --- 
st.set_page_config(
    page_title='Tennis Player Dashboard',
    layout="wide"
)

# --- Get Data ---
@st.cache
def get_data():
    mens_serve, womens_serve = load_serve_mens(), load_serve_womens()
    mens_shot, womens_shot = load_shot_mens(), load_shot_womens()
    mens_return, womens_return = load_returns_mens(), load_returns_womens()
    with open('data/headshots.json') as json_file:
        headshots = json.load(json_file)
    return (mens_serve, womens_serve,
            mens_shot, womens_shot, headshots,
            mens_return, womens_return)

(mens_serve, womens_serve,
 mens_shot, womens_shot,
 headshots, mens_return, womens_return) = get_data()

data = pd.concat([mens_serve, womens_serve]) # represents serve
shot = pd.concat([mens_shot, womens_shot])
returns = pd.concat([mens_return, womens_return])

# Create containers
introduction = st.beta_container()
compare = st.beta_container()

# --- Title ---
with introduction:
    title = st.beta_columns(1)[0]
    subtitle= st.beta_columns(1)[0]
    space = st.beta_columns(1)[0]
    space.header("\n")
    title.title("Tennis Player Analytics Dashboard")
    subtitle.header("Built by Ali Danial Hussain\n")
    details = st.beta_expander(
        "Learn More!"
    )

# -- Comparison ---
with compare:
    choice= st.beta_columns(3)
    player1, player2 = st.beta_columns(2)

    # Choose what to compare
    user_choice = choice[0].radio(
        label = "What would you like to compare?",
        options = ("Serve Direction", "Shot Direction"),
        index = 0
    )

    # When comparing service direction data
    if user_choice == "Serve Direction":

        _, table, _ = st.beta_columns([1,6,1])
        rs_table1, _, rs_table2 = st.beta_columns([4, 2, 4])
        p1chart1, p1chart2, p2chart1, p2chart2 = st.beta_columns(4)
        p1chart3, p1chart4, p2chart3, p2chart4 = st.beta_columns(4)
        p1_line, _, p2_line = st.beta_columns([4, 2, 4])
        names = sorted(list(data['Player Name'].unique()))

        p1_choice = player1.selectbox(
            label = 'Select Player 1',
            options = names,
            index = names.index("Roger Federer")
        )
        p2_choice = player2.selectbox(
            label = 'Select Player 2',
            options = names,
            index = names.index("Rafael Nadal")
        )

        # Get the data for each tournament for the specified player
        p1_w, p1_u, p1_r, p1_a, p1_total = tournament_data_serve(data, p1_choice)
        p2_w, p2_u, p2_r, p2_a, p2_total = tournament_data_serve(data, p2_choice)

        # Create combined dataset
        combined = pd.concat([p1_total.T, p2_total.T], axis = 1)
        try:
            combined = combined.style.apply(style_table, axis = None)
        except:
            combined = "Please select two distinct players."

        # Try to get the player's headshot
        try:
            p1_image = headshots[p1_choice]
        except:
            p1_image = None
        try:
            p2_image = headshots[p2_choice]
        except:
            p2_image = None

        # Create return and serve comparison table
        rs_table1.write(return_serve_table(returns, data, p2_choice, p1_choice))
        rs_table2.write(return_serve_table(returns, data, p1_choice, p2_choice))

        # Create the court plots
        p1_court_w, p1_court_u, p1_court_r, p1_court_a = get_plots_serve(
            p1_w, p1_u, p1_r, p1_a, p1_image, p1_choice
        )
        p2_court_w, p2_court_u, p2_court_r, p2_court_a = get_plots_serve(
            p2_w, p2_u, p2_r, p2_a, p2_image, p2_choice
        )

        # Plot the courts
        p1chart1.write(p1_court_w)
        p1chart2.write(p1_court_u)
        p1chart3.write(p1_court_r)
        p1chart4.write(p1_court_a)
        p2chart1.write(p2_court_w)
        p2chart2.write(p2_court_u)
        p2chart3.write(p2_court_r)
        p2chart4.write(p2_court_a)

        # Show data table
        table.write(combined)

    # When comparing shot direction data
    if user_choice == "Shot Direction":

        _, table, _ = st.beta_columns([2,4,2])
        p1chart1, p1chart2, p2chart1, p2chart2 = st.beta_columns(4)
        p1chart3, p1chart4, p2chart3, p2chart4 = st.beta_columns(4)
        names = sorted(list(shot['player'].unique()))

        p1_choice = player1.selectbox(
            label = 'Select Player 1',
            options = names,
            index = names.index("Roger Federer")
        )
        p2_choice = player2.selectbox(
            label = 'Select Player 2',
            options = names,
            index = names.index("Rafael Nadal")
        )

        # Get the data for each tournament for the specified player
        p1_w, p1_u, p1_r, p1_a, p1_total = tournament_data_shot(shot, p1_choice)
        p2_w, p2_u, p2_r, p2_a, p2_total = tournament_data_shot(shot, p2_choice)

        # Create combined dataset
        combined = pd.concat([p1_total.T, p2_total.T], axis = 1)
        try:
            combined = combined.style.apply(style_table, axis = None)
        except:
            combined = "Please select two distinct players."

        # Try to get the player's headshot
        try:
            p1_image = headshots[p1_choice]
        except:
            p1_image = None
        try:
            p2_image = headshots[p2_choice]
        except:
            p2_image = None

        # Create the court plots
        p1_court_w, p1_court_u, p1_court_r, p1_court_a = get_plots_shot(
            p1_w, p1_u, p1_r, p1_a, p1_image, p1_choice
        )
        p2_court_w, p2_court_u, p2_court_r, p2_court_a = get_plots_shot(
            p2_w, p2_u, p2_r, p2_a, p2_image, p2_choice
        )

        # Plot the courts
        p1chart1.write(p1_court_w)
        p1chart2.write(p1_court_u)
        p1chart3.write(p1_court_r)
        p1chart4.write(p1_court_a)
        p2chart1.write(p2_court_w)
        p2chart2.write(p2_court_u)
        p2chart3.write(p2_court_r)
        p2chart4.write(p2_court_a)

        # Show data table
        table.write(combined)

with details:
    st.markdown(
        """
        ### Serve Direction:
        The serve direction option displays the average direction in\
        which different players serve. The average is calculated for\
        the different positions on the deuce side of the court\
        (right side for the server) and for the different positions\
        on the ad side of the court(left side for the server). This data\
        is further segmented into the 4 grandslam tournaments. Below the\
        top table, is two sub tables comparing each player's\
        serve tendencies, with the opponent's success rate on returning a\
        serve in that direction.

        ### Shot Direction:
        The shot direction option displays the average direction in\
        which different players hit their groundstrokes. The average is\
        calculated for forehands and the average is calculated for\
        backhands. This data is further segmented into the 4 grandslam\
        tournaments.

        ### Grandslams:
        In tennis, there are 4 grandslam tournaments:

        1. Wimbledon: played on grass court
        2. US Open: played on hard court
        3. Roland Garros (French Open): played on clay court
        4. Australian Open: played on hard court

        Each grandslam is played on a different surface which effects the\
        way in which the ball bounces. This also effects the tactics and\
        strategies used by the players.
        """
    )