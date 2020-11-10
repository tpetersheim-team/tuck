
class Holding(object):
    def __init__(self, name: str, equity: float, price: float, percentage: float) -> None:
        super().__init__()
        self.name = name
        self.equity = equity
        self.price = price
        self.percentage = percentage

    name: str
    equity: float
    price: float


class Portfolio(object):
    def __init__(self, holdings: list[Holding]) -> None:
        super().__init__()
        self.holdings = holdings

class Profile(object):
    def __init__(self, equity: float, cash: float) -> None:
        super().__init__()
        self.equity = equity
        self.cash = cash

    equity: float
    cash: float