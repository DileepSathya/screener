from src.screener import logger
from src.screener.utils.common import format_symbol  # should handle both str and list if needed
from datetime import date, timedelta
from src.screener.configurations.config import config_manager
import yaml

from datetime import date, timedelta


class prev_day_data_pipeline:
    def get_data(self):
        choice = input("Do you want to retrieve custom data? (y/n): ").strip().lower()

        if choice == 'y':
            start_input = input("Enter start date (YYYY-MM-DD): ")

            start_date = date.fromisoformat(start_input)
            end_date = start_date
        else:
            start_date = date.today() - timedelta(days=1)
            end_date = start_date

        in_symbol_list = config_manager.data_loading_config()

        symbols_list = [format_symbol(symbol) for symbol in in_symbol_list]

        return symbols_list, start_date, end_date


