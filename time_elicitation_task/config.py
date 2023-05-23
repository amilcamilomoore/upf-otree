# <imports>
from otree.api import Currency as c
from otree.constants import BaseConstants
# </imports>


# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    # ---------------------------------------------------------------------------------------------------------------- #
    # --- Task-specific Settings --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    # number of steps in the staircase procedure (see graph in the docs)
    # note that <num_choices = x> implies a choice list with <2^x> choices, i.e. <2^x> possible switching points
    # thus, for instance, <num_choice = 5> yields 32 different classifications for preferences towards risks
    # num_choices = 5

    # # lottery payoffs (in currency units set in settings.py)  and probability (in %) for the high lottery outcome
    # # <lottery_hi> and <lottery_lo> define the "high" and "low" outcomes of the lottery ("Option A")
    # # <probability> determines the likelihood that the lottery pays the "high" outcome as percentage number
    # # thus, <probability = x> implies that the lottery pays <lottery_hi> in <x>% and <lottery_lo> in <100-x>%
    # lottery_hi = 300.00
    # lottery_lo = 0.00
    # probability = 50.00
    #
    # # (initial) sure payoff, i.e. the certain payment in the first choice
    # # <sure_payoff> defines the certain amount offered as "Option B" in the first of <num_choices> choices
    # # the sure payoffs for subsequent choices are determined by <delta> (see below)
    # sure_payoff = 160.00
    #
    # # (initial) increase/decrease in sure payoff
    # # while the first choice offers a fix payment of <sure_payoff>, "Option B" in subsequent choices depend on <delta>
    # # generally, for choice <i = 1, 2, ... num_choices>, <sure_payoff_i = sure_payoff + delta / 2 ^ (i-1)> if choice
    # # <i-1> = "A" and <sure_payoff_i = sure_payoff - delta / 2 ^ (i-1)> if choice <i-1> = "B"
    # # thus, if a subject chooses "A" ("B"), <sure_payoff_i> increases (decreases) by half of the previous rounds <delta>
    # # for example: if <sure_payoff = x> and <delta = y>, "Option B" offers <x +/- y/2> in choice 2, <x +/- y/2 +/- y/4>
    # # in choice 3, etc.
    # delta = 80.00

    ###### SAME FOR TIME DECISIONS ######
    num_choices = 5
    time_fixed = 100.00
    delta = 80.00 # I will need a matrix for this
    first_number = 154
    time_matrix = {
        154: [185, 125],
        185: [202, 169],
        202: [210, 193],
        210: [215, 206],
        193: [197, 189],
        169: [177, 161],
        177: [181, 173],
        161: [165, 158],
        125: [139, 112],
        139: [146, 132],
        146: [150, 143],
        132: [136, 122],
        112: [119, 106],
        119: [129, 116],
        106: [109, 103], #tree ends here, patience num starts below
        215: [1, 2],
        206: [3, 4],
        197: [5, 6],
        189: [7, 8],
        181: [9, 10],
        173: [11, 12],
        165: [13, 14],
        158: [15, 16],
        150: [17, 18],
        143: [19, 20],
        136: [21, 22],
        122: [23, 24],
        129: [25, 26],
        116: [27, 28],
        109: [29, 30],
        103: [31, 32]
    }

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- Overall Settings and Appearance --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    # add "indifference" option
    # if <indifference = False>, subjects can only reveal their preference for either "Option A" or "Option B"
    # if <indifference = True>, an additional option is available to indicate indifference between Option "A" and "B"
    # whenever a subject chooses "Indifferent", the iteration procedure stops as indifference is already reached
    # thus, if a subject chooses "Indifferent" in some choice <x>, all subsequent choices are automatically skipped
    # if an "Indifferent" choice is drawn for payoff, it's randomly determined whether "A" or "B" constitute the payment
    indifference = False

    # render buttons instead of radio buttons
    # if <buttons = True>, a button will be displayed for each choice ("A", "B", "Indifferent") instead of radio buttons
    # that is, subjects only click a single button than rather choosing a radio button and clicking on "Next"
    # <buttons = True> accelerates input of choices but implies that decisions can not be modified
    buttons = True

    # show progress bar
    # if <progress_bar = True> and <one_choice_per_page = True>, a progress bar is rendered
    # if <progress_bar = False>, no information with respect to the advance within the task is displayed
    # the progress bar graphically depicts the advance within the task in terms of how many decision have been made
    # further, information in terms of "page x out of <num_choices>" (with x denoting the current choice) is provided
    progress_bar = True

    # show instructions page
    # if <instructions = True>, a separate template "Instructions.html" is rendered prior to the task
    # if <instructions = False>, the task starts immediately (e.g. in case of printed instructions)
    instructions = True

    # show results page summarizing the task's outcome including payoff information
    # if <results = True>, a separate page containing all relevant information is displayed after finishing the task
    # if <results = False>, the template "Decision.html" will not be rendered
    results = False

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- oTree Settings (Don't Modify) --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    name_in_url = 'time_elicitation_task'
    players_per_group = None
    num_rounds = num_choices
