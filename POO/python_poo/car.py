
from veiculo import Veiculo
class Car(Veiculo):
    def __init__(self, model, year, color, for_sale, vei_type):
        super().__init__(model, year, color, for_sale)
        self.vei_type = vei_type