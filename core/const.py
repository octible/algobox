class Event(object):
    PRICE_UPDATE = "PRICE_UPDATE"
    EQUITY_UPDATE = "EQUITY_UPDATE" # indicates a change in equity
    CASH_UPDATE = "CASH_UPDATE"

    TRANSACTION_BUY = "TRANSACTION_BUY" # rename !TODO
    TRANSACTION_SELL = "TRANSACTION_SELL" # rename !TODO

    SIGNAL_BUY = "SIGNAL_BUY"
    SIGNAL_SELL = "SIGNAL_SELL"
    SIGNAL_ACTIONABLE = [SIGNAL_BUY, SIGNAL_SELL]
    SIGNAL_NO_ACTION = "NO_ACTION"

    BANKRUPT_ACCOUNT = "BANKRUPT_ACCOUNT"
