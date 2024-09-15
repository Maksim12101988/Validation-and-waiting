.PHONY: all test clean

# Переменные
PYTHON := python
PYTEST := $(PYTHON) -m pytest
APP_DIR := app
TEST_DIR := tests

# Цель по умолчанию
all: test

# Запуск тестов
test:
	$(PYTEST) $(TEST_DIR)

# Очистка файлов, созданных в процессе сборки и тестирования
clean:
	find . -name "__pycache__" -exec rm -r {} +
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.pyo" -exec rm -f {} +
	find . -name ".pytest_cache" -exec rm -rf {} +