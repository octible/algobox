#!TODO <rounding>
import collections

from abc import ABC, abstractmethod

class BacktestAccount(ABAccount):
    """
    Tracks everything relevant to the trading account including cash balance,
    assets held, etc
    """
    def __init__(self, starting_balance):
        self.balance = starting_balance
        self.holdings = collections.defaultdict(int)
        self.balance_series = [starting_balance]

    def calculate_equity():
        pass

    def cash_asset_split(self):


    @property
    def equity(self):
        return sum()

    def purchase(self, asset, latest_price):
        """
        Backtest assumes max quantity of assets purchased
        """
        current_cash = self.balance
        quantity_to_purchase =  int(current_cash / latest_price)
        cost_to_purchase = quantity_to_purchase * latest_price

        self.holdings[asset] = quantity_to_purchase
        self.balance = self.balance - cost_to_purchase

    def sell(self, asset, quantity, latest_price):
        """
        Backtest assumes sale of all of specified asset
        """
        current_cash = self.balance
        quantity_to_sell = self.holdings[asset]
        proceeds_of_sale = quantity_to_sell * latest_price

        self.holdings[asset] = self.holdings[asset] - quantity_to_sell
        self.balance = self.balance + proceeds_of_sale
