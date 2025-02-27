"""Test charting extension."""

import pytest
from extensions.tests.conftest import parametrize
from openbb_charting.core.openbb_figure import OpenBBFigure
from openbb_core.app.model.obbject import OBBject


# pylint:disable=inconsistent-return-statements
@pytest.fixture(scope="session")
def obb(pytestconfig):
    """Fixture to setup obb."""
    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb  # pylint:disable=import-outside-toplevel

        return openbb.obb


# pylint:disable=redefined-outer-name

data: dict = {}


def get_equity_data():
    """Get equity data."""
    import openbb  # pylint:disable=import-outside-toplevel

    if "stocks_data" in data:
        return data["stocks_data"]

    symbol = "AAPL"
    provider = "fmp"

    data["stocks_data"] = openbb.obb.equity.price.historical(
        symbol=symbol, provider=provider
    ).results
    return data["stocks_data"]


@parametrize(
    "params",
    [
        (
            {
                "provider": "yfinance",
                "symbol": "AAPL",
                "chart": True,
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_equity_price_historical(params, obb):
    """Test chart equity price historical."""
    result = obb.equity.price.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "provider": "yfinance",
                "symbol": "JPYUSD",
                "chart": True,
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_currency_price_historical(params, obb):
    """Test chart currency price historical."""
    result = obb.currency.price.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "provider": "yfinance",
                "symbol": "BTCUSD",
                "chart": True,
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_crypto_price_historical(params, obb):
    """Test chart crypto price historical."""
    result = obb.crypto.price.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "provider": "yfinance",
                "symbol": "NDX",
                "chart": True,
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_index_price_historical(params, obb):
    """Test chart index price historical."""
    result = obb.index.price.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "provider": "yfinance",
                "symbol": "QQQ",
                "chart": True,
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_etf_historical(params, obb):
    """Test chart etf historical."""
    result = obb.etf.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "index": "date",
                "length": "60",
                "scalar": "90.0",
                "drift": "2",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_adx(params, obb):
    """Test chart ta adx."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.adx(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "index": "date",
                "length": "30",
                "scalar": "110",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_aroon(params, obb):
    """Test chart ta aroon."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.aroon(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "target": "high",
                "index": "",
                "length": "60",
                "offset": "10",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_ema(params, obb):
    """Test chart ta ema."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.ema(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "target": "high",
                "index": "date",
                "length": "55",
                "offset": "2",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_hma(params, obb):
    """Test chart ta hma."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.hma(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "target": "high",
                "index": "date",
                "fast": "10",
                "slow": "30",
                "signal": "10",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_macd(params, obb):
    """Test chart ta macd."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.macd(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "target": "high",
                "index": "date",
                "length": "16",
                "scalar": "90.0",
                "drift": "2",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_rsi(params, obb):
    """Test chart ta rsi."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.rsi(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "target": "high",
                "index": "date",
                "length": "55",
                "offset": "2",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_sma(params, obb):
    """Test chart ta sma."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.sma(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "target": "high",
                "index": "date",
                "length": "60",
                "offset": "10",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_wma(params, obb):
    """Test chart ta wma."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.wma(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "target": "high",
                "index": "date",
                "length": "55",
                "offset": "5",
                "chart": "True",
            }
        ),
    ],
)
@pytest.mark.integration
def test_charting_technical_zlma(params, obb):
    """Test chart ta zlma."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.zlma(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": "",
                "model": "yang_zhang",
                "chart": True,
            }
        )
    ],
)
@pytest.mark.integration
def test_charting_technical_cones(params, obb):
    """Test chart ta cones."""
    params = {p: v for p, v in params.items() if v}

    params["data"] = get_equity_data()

    result = obb.technical.cones(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": None,
                "symbol": "DGS10",
                "transform": "pc1",
                "chart": True,
                "provider": "fred",
            }
        )
    ],
)
@pytest.mark.integration
def test_charting_economy_fred_series(params, obb):
    """Test chart economy fred series."""
    result = obb.economy.fred_series(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": None,
                "symbol": "XRT,XLB,XLI,XLH,XLC,XLY,XLU,XLK",
                "chart": True,
                "provider": "finviz",
                "chart_params": {"limit": 4, "orientation": "h"},
            }
        )
    ],
)
@pytest.mark.integration
def test_charting_equity_price_performance(params, obb):
    """Test chart equity price performance."""
    result = obb.equity.price.performance(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": None,
                "symbol": "XRT,XLB,XLI,XLH,XLC,XLY,XLU,XLK",
                "chart": True,
                "provider": "intrinio",
                "chart_params": {"orientation": "v"},
            }
        )
    ],
)
@pytest.mark.integration
def test_charting_etf_price_performance(params, obb):
    """Test chart etf price performance."""
    result = obb.etf.price_performance(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)


@parametrize(
    "params",
    [
        (
            {
                "data": None,
                "symbol": "XRT",
                "chart": True,
                "provider": "fmp",
                "chart_params": {"orientation": "v", "limit": 10},
            }
        )
    ],
)
@pytest.mark.integration
def test_charting_etf_holdings(params, obb):
    """Test chart etf holdings."""
    result = obb.etf.holdings(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
    assert result.chart.content
    assert isinstance(result.chart.fig, OpenBBFigure)
