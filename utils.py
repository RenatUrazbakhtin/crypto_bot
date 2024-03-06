import asyncio
import ccxt.async_support as ccxt


async def get_crypt():
    poloniex = ccxt.poloniex()
    res = await poloniex.fetch_ticker('ETH/USDT')
    await poloniex.close()
    return res['close']





