from CreateClass.main import generate_file


def test() -> None:
	status: dict[str, int | str] = generate_file("Car", "name: str, block: int, land_id: int, orientation: int, surface: int, sell_price: int")
	print(status["message"])

if __name__ == "__main__":
	test()