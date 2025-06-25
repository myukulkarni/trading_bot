from binance.client import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        logging.basicConfig(filename='bot.log', level=logging.INFO)

    def place_order(self, symbol, quantity, side, order_type='MARKET'):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type=order_type.upper(),
                quantity=quantity
            )
            logging.info(f"Order placed: {order}")
            print(f"Order placed successfully: {order}")
        except Exception as e:
            logging.error(f"Error placing order: {e}")
            print(f"Error: {e}")
