install:  
		pdm install

test:
		pdm run pytest

# Ejecutar python -m py_compile para revisar solo la sintaxis del código
check:
		$(PDM_PATH) run python -m py_compile $(shell find src -name "*.py") || exit 1
		@echo "La comprobación de sintaxis ha finalizado sin errores."


# Limpiar el entorno virtual
clean:
		$(PDM_PATH) venv remove in-project
