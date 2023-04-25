from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
# def vars_for_all_templates(self):
#     # return dict(
#     #     p_hi = Constants.probability,
#     #     p_lo = 1 - Constants.probability,
#     #     hi = c(Constants.lottery_hi),
#     #     lo = c(Constants.lottery_lo)
#     # )
#     return {
#         'p_hi': "{0:.1f}".format(Constants.probability) + "%",
#         'p_lo': "{0:.1f}".format(100 - Constants.probability) + "%",
#         'hi':   c(Constants.lottery_hi),
#         'lo':   c(Constants.lottery_lo)
#
#     }

# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #
class Instructions(Page):

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return {
            'p_hi': "{0:.1f}".format(Constants.probability) + "%",
            'p_lo': "{0:.1f}".format(100 - Constants.probability) + "%",
            'hi':   c(Constants.lottery_hi),
            'lo':   c(Constants.lottery_lo),
            'n': Constants.num_choices
        }

# class Instructions_time(Page):
#
#     # only display instruction2 once AFTER results of risk task
#     # ----------------------------------------------------------------------------------------------------------------
#     def is_displayed(self):
#         return self.subsession.round_number == 1

# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class Decision(Page):

    # only display if previous choice was not "indifferent"
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        previous_choices = [p.choice for p in self.player.in_previous_rounds()]
        return 'I' not in previous_choices

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['choice']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------

    def vars_for_template(self):

        # specify info for progress bar
        total = Constants.num_choices
        page = self.subsession.round_number
        progress = page / total * 100

        # # specify info for progress bar TIME SURVEY
        # total2 = Constants.num_choices_time
        # page2 = self.subsession.round_number
        # progress2 = page2 / total * 100

        return {
            'p_hi': "{0:.1f}".format(Constants.probability) + "%",
            'p_lo': "{0:.1f}".format(100 - Constants.probability) + "%",
            'hi': c(Constants.lottery_hi),
            'lo': c(Constants.lottery_lo),
            'n': c(Constants.num_choices),
            'page':        page,
            'total':       total,
            'progress':    progress,
            'sure_payoff': self.participant.vars['icl_sure_payoffs'][page - 1],
            # 'page2':        page2,
            # 'total2':       total2,
            # 'progress2':    progress2,
            # 'time_payoff': self.participant.vars['time_payoffs'][page2 - 1],
            # 'fixed_payoff': c(Constants.time_fixed)
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.set_sure_payoffs()
        self.player.update_switching_row()
        self.player.set_payoffs()

        # self.player.set_sure_payoffs2()


# ******************************************************************************************************************** #
# *** PAGE RESULTS *** #
# ******************************************************************************************************************** #
class Results(Page):

    # skip results until last page
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # payoff information
        choice_to_pay = self.participant.vars['icl_choice_to_pay']
        option_to_pay = self.player.in_round(choice_to_pay).choice
        payoff_relevant = self.player.in_round(choice_to_pay).payoff_relevant
        sure_payoff = self.player.participant.vars['icl_sure_payoffs'][choice_to_pay - 1]

        return {
            'p_hi': "{0:.1f}".format(Constants.probability) + "%",
            'p_lo': "{0:.1f}".format(100 - Constants.probability) + "%",
            'hi': c(Constants.lottery_hi),
            'lo': c(Constants.lottery_lo),
            'n': c(Constants.num_choices),
            'sure_payoff':     sure_payoff,
            'option_to_pay':   option_to_pay,
            'payoff_relevant': payoff_relevant,
            'payoff':          self.player.in_round(choice_to_pay).payoff
        }


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [Decision]

if Constants.instructions:
    page_sequence.insert(0, Instructions)

if Constants.results:
    page_sequence.append(Results)
