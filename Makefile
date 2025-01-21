install_uv:
	@echo "Se esta instalando UV..."
	@wget -qO- https://astral.sh/uv/install.sh | sh

# Instalar dependencias, asegurando que el proyecto esté inicializado
install-dependencies: 
	uv build

install: install_uv install-dependencies

# Ejecutar pruebas con pytest
test:
		uv run pytest

# Ejecutar python -m py_compile para revisar solo la sintaxis del código
check:
		run python -m py_compile $(shell find src -name "*.py") || exit 1
		@echo "La comprobación de sintaxis ha finalizado sin errores."
