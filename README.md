## Тестовый бот для погоды

Для установки и запуска бота переименуйте файл config.dist.toml в config.toml и заполните вашей информацией

Установите зависимости используй uv (рекомендуется) или pip

uv sync
pip install .

Запуск

uv run -m weather
python -m weather