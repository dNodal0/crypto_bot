class MACDStrategy:
    def __init__(self, short_window=12, long_window=26, signal_window=9):
        self.short_window = short_window
        self.long_window = long_window
        self.signal_window = signal_window

    def generate_signals(self, market_data):
        """
        Génère des signaux d'achat ou de vente basés sur le MACD.
        :param market_data: Liste de prix (ex: [100, 102, 101, ...])
        :return: Liste de signaux (ex: ["buy", "sell", ...])
        """
        signals = []
        for i in range(len(market_data)):
            if i < self.long_window:
                signals.append(None)  # Pas assez de données pour le calcul
                continue

            short_ma = sum(market_data[i-self.short_window:i]) / self.short_window
            long_ma = sum(market_data[i-self.long_window:i]) / self.long_window
            macd = short_ma - long_ma

            signal_line = sum([macd for macd in market_data[i-self.signal_window:i]]) / self.signal_window

            if macd > signal_line:
                signals.append("buy")
            elif macd < signal_line:
                signals.append("sell")
            else:
                signals.append(None)

        return signals
