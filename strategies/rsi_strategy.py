# Python file placeholder
class RSIStrategy:
    def __init__(self, period=14, overbought=70, oversold=30):
        self.period = period
        self.overbought = overbought
        self.oversold = oversold

    def calculate_rsi(self, prices):
        """
        Calcule l'indice RSI.
        :param prices: Liste de prix (ex: [100, 102, 101, ...])
        :return: Liste de RSI (ex: [50, 55, 60, ...])
        """
        deltas = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        gains = [delta if delta > 0 else 0 for delta in deltas]
        losses = [-delta if delta < 0 else 0 for delta in deltas]

        avg_gain = sum(gains[:self.period]) / self.period
        avg_loss = sum(losses[:self.period]) / self.period
        rsi_values = []

        for i in range(self.period, len(prices)):
            avg_gain = (avg_gain * (self.period - 1) + gains[i - 1]) / self.period
            avg_loss = (avg_loss * (self.period - 1) + losses[i - 1]) / self.period

            if avg_loss == 0:
                rsi = 100
            else:
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))
            rsi_values.append(rsi)

        return [None] * self.period + rsi_values

    def generate_signals(self, market_data):
        """
        Génère des signaux basés sur RSI.
        :param market_data: Liste de prix (ex: [100, 102, 101, ...])
        :return: Liste de signaux (ex: ["buy", "sell", ...])
        """
        rsi_values = self.calculate_rsi(market_data)
        signals = []

        for rsi in rsi_values:
            if rsi is None:
                signals.append(None)
            elif rsi < self.oversold:
                signals.append("buy")
            elif rsi > self.overbought:
                signals.append("sell")
            else:
                signals.append(None)

        return signals
