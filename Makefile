# Ruta donde se encuentra pdm instalado
PDM_PATH = $(HOME)/.local/bin/pdm

# Instalar pdm si no está disponible
install_pdm:
		if ! command -v $(PDM_PATH) &> /dev/null; then \
				echo "Instalando pdm..."; \
				pip install --user pdm; \
		fi

# Inicializar el proyecto si no tiene pyproject.toml
init_project:
		if [ ! -f pyproject.toml ]; then \
				echo "pyproject.toml no encontrado. Inicializando proyecto..."; \
				$(PDM_PATH) init; \
		fi

# Instalar dependencias, asegurando que el proyecto esté inicializado
install: install_pdm init_project
		$(PDM_PATH) install

# Ejecutar pruebas con pytest
test:
		$(PDM_PATH) run pytest

# Ejecutar flake8 para revisar el código
check:
		$(PDM_PATH) run flake8 src/

# Limpiar el entorno virtual
clean:
		$(PDM_PATH) venv remove in-project
