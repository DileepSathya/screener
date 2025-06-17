from src.screener import logger
from src.screener.utils.common import format_symbol  # should handle both str and list if needed
from datetime import date, timedelta
from src.screener.configurations.config import config_manager
import yaml

class prev_day_data_pipeline:
    def prev_day_data():

        in_symbol_list=config_manager.data_loading_config()
        symbols_list = [format_symbol(symbol) for symbol in in_symbol_list]

        
        start_date = date.today() - timedelta(days=1)
        end_date=start_date


        return symbols_list,start_date,end_date