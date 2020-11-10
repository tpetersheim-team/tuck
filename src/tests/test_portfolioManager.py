from unittest.mock import MagicMock
from pytest import fixture
from pytest_mock.plugin import MockerFixture

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
    portfolioManager = PortfolioManager(MockStockAPI)

    targetDistributionDict: dict[str, TargetDistribution] = {
        "holding1": TargetDistribution(10),
        "holding2": TargetDistribution(20),
        "holding3": TargetDistribution(30),
        "holding4": TargetDistribution(40)
    }

    result = portfolioManager.RebalancePortfolio(targetDistributionDict)

    print(result)