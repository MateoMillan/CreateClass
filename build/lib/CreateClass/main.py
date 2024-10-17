def generate_constructor(parameters: str, /) -> str:
	params: list[str] = get_params_names(parameters)
	final_str: str = "\n\t\t".join([f"self.{param} = {param}" for param in params])
	return final_str


def get_params_names(parameters: str, /) -> list[str]:
	params: list[str] = parameters.split(",")
	params: map[str] = map(get_param_name, params)
	return params


def generate_str_method_return(parameters: str, /) -> str:
	params: list[str] = get_params_names(parameters)
	final_str: str = "f\"" + (" | ".join([f"{param.capitalize().replace("_", " ")}: {{self.{param}:^10}}" for param in params])) + "\""
	return final_str


def get_param_name(param: str) -> str:
	return param[:param.index(":")].strip()


def generate_class(name: str, parameters: str) -> str:
	return (
		f"class {name}:"
		f"\n\tdef __init__(self, {parameters}):"
		f"\n\t\t{generate_constructor(parameters)}\n"
		f"\n\tdef __str__(self):"
		f"\n\t\treturn {generate_str_method_return(parameters)}\n"
)


def generate_file(file_name: str, parameters: str) -> dict[str, int | str]:
	"""generates a {file_name}.py file containing the class


	:param file_name (str): the name of the file without the extention
	:param parameters (str): parameters/atributes of the class

	Returns:
		int: 1 for succes or -1 for failure
	"""
	try:
		with open(f"{file_name}.py", "wt") as file:
			file.write(generate_class(file_name, parameters))
			return {"status": 1, "message": "Success!"}
	except (FileExistsError, FileNotFoundError) as exc:
		return {"status": -1, "message": exc.strerror}
	