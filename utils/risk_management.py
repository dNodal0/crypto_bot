# risk_management.py
class RiskManagement:
    def __init__(self, capital, stop_loss_pct):
        self.capital = capital
        self.stop_loss_pct = stop_loss_pct

    def calculate_position_size(self, entry_price, stop_loss_price):
        """
        Calcule la taille de la position en fonction du risque.
        :param entry_price: Prix d'entrée de la position
        :param stop_loss_price: Prix du stop-loss
        :return: Quantité d'actifs à acheter/vendre
        """
        risk_amount = self.capital * self.stop_loss_pct
        risk_per_unit = entry_price - stop_loss_price
        position_size = risk_amount / risk_per_unit
        return position_size
