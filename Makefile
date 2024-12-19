# Ruta donde se encuentra pdm instalado
PDM_PATH = $(HOME)/.local/bin/pdm

# Instalar pdm si no está disponible
install_pdm:
		if ! command -v $(PDM_PATH) &> /dev/null; then \
				echo "Instalando pdm..."; \
				pip install --user pdm; \
		fi


# Instalar dependencias, asegurando que el proyecto esté inicializado
install: install_pdm 
		$(PDM_PATH) install

# Ejecutar pruebas con pytest
test:
		$(PDM_PATH) run pytest

# Ejecutar pylint para revisar la sintaxis y estilo del código
check:
		$(PDM_PATH) run pylint src/ || exit 1
		@echo "La comprobación de sintaxis ha finalizado sin errores."

# Limpiar el entorno virtual
clean:
		$(PDM_PATH) venv remove in-project
