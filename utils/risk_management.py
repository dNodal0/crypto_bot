class RiskManagement:
    def __init__(self, trade_settings):
        self.risk_per_trade = trade_settings["risk_per_trade"]
        self.max_open_trades = trade_settings["max_open_trades"]
        self.account_balance = trade_settings["account_balance"]
        self.stop_loss_distance = trade_settings["stop_loss_distance"]

    def calculate_position_size(self):
        # Calcul de la taille de la position
        risk_amount = self.account_balance * self.risk_per_trade
        position_size = risk_amount / self.stop_loss_distance
        return position_size

    def check_max_open_trades(self, current_open_trades):
        return current_open_trades < self.max_open_trades
