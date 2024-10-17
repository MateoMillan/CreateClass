class Car:
	def __init__(self, name: str, block: int, land_id: int, orientation: int, surface: int, sell_price: int):
		self.name = name
		self.block = block
		self.land_id = land_id
		self.orientation = orientation
		self.surface = surface
		self.sell_price = sell_price

	def __str__(self):
		return f"Name: {self.name:^10} | Block: {self.block:^10} | Land id: {self.land_id:^10} | Orientation: {self.orientation:^10} | Surface: {self.surface:^10} | Sell price: {self.sell_price:^10}"
