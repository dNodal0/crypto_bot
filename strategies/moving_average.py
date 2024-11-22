class MovingAverageStrategy:
    def __init__(self, short_window=10, long_window=30):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, market_data):
        """
        Génère des signaux d'achat ou de vente basés sur les moyennes mobiles.
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

            if short_ma > long_ma:
                signals.append("buy")
            elif short_ma < long_ma:
                signals.append("sell")
            else:
                signals.append(None)

        return signals
