from unittest.mock import MagicMock
from pytest import fixture
from pytest_mock.plugin import MockerFixture
from models.services.stock import Holding, Portfolio, Profile

from services.portfolioManager import PortfolioManager, TargetDistribution


@fixture
def MockStockAPI(mocker: MockerFixture):
    return mocker.patch("src.services.stock.stockAPI.StockAPI")

def test_login_calls_stockAPI_login(MockStockAPI: MagicMock):
    portfolioManager = PortfolioManager(MockStockAPI)
    username = 'user'
    password = 'pass'
    stayLoggedIn = False
    mfa = 'mfa-code'

    result = portfolioManager.Login(username, password, stayLoggedIn, mfa)

    print(result)


    MockStockAPI.Login.assert_called_once_with(username, password, store_session=stayLoggedIn, mfa_code=mfa)
    # MockStockAPI.Login.assert_not_called()

def test_portfolio_balance(MockStockAPI: MagicMock):
    # Setup Mocks
    mockProfile = Profile(14, 6)
    MockStockAPI.RetrieveProfile = MagicMock(return_value = mockProfile)

    mockPortfolio = Portfolio([
        Holding("holding1", 1, 1),
        Holding("holding2", 2, 2),
        Holding("holding3", 3, 3),
        Holding("holding4", 8, 4)
    ])
    MockStockAPI.RetrievePortfolio = MagicMock(return_value = mockPortfolio)

    # Create our test portfolio manager
    portfolioManager = PortfolioManager(MockStockAPI)

    # Call test method
    targetDistributionDict: dict[str, TargetDistribution] = {
        "holding1": TargetDistribution(.1),
        "holding2": TargetDistribution(.2),
        "holding3": TargetDistribution(.3),
        "holding4": TargetDistribution(.4)
    }
    result = portfolioManager.RebalancePortfolio(targetDistributionDict)

    # TODO: Assert OrderByDollar was called multiple times correctly
    print(result)