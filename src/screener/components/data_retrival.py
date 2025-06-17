from src.screener import logger
from src.screener.utils.common import read_yaml
from src.screener.configurations.config import config_manager
from fyers_apiv3 import fyersModel
from src.screener.pipeline.prev_day_data_pipeline import prev_day_data_pipeline
from datetime import datetime
from src.screener.utils.common import extract_candles_with_symbol,save_to_hist_data_json,clear_hist_data_json

class data_retrival:
    def __init__(self):
        logger.info("Accessing client_id and acesstoken")
        client_id, access_token = config_manager.authentication()
        logger.info("Accessing client_id and acesstoken successful")
        self.fyers = fyersModel.FyersModel(
            client_id=client_id,
            is_async=False,
            token=access_token,
            log_path=""
        )
    def prev_day_data(self):
        pipeline=prev_day_data_pipeline()
        symbol_list,start_date,end_date=pipeline.get_data()
        file_path=config_manager.json_file_path()
        clear_hist_data_json(file_path)

        for symbol in symbol_list:
            data = {
                    "symbol": symbol,
                    "resolution": "D",
                    "date_format": "1",
                    "range_from": start_date,
                    "range_to": end_date,
                    "cont_flag": "1"
            }
            
            print(f"\n Fetching data for {symbol} from {start_date} to {end_date}...")
            response = self.fyers.history(data=data)
            data_with_symbols=extract_candles_with_symbol(response_json=response,symbol=symbol)
                
            
            save_to_hist_data_json(data_with_symbols,file_path)
    
    def bactest_data(self):
        symbol_list,start_date,end_date=prev_day_data_pipeline.backtest()
       

        for symbol in symbol_list:
            data = {
                    "symbol": symbol,
                    "resolution": "D",
                    "date_format": "1",
                    "range_from": start_date,
                    "range_to": end_date,
                    "cont_flag": "1"
            }
            print(f"\n Fetching data for {symbol} from {start_date} to {end_date}...")
            response = self.fyers.history(data=data)
            data_with_symbols=extract_candles_with_symbol(response_json=response,symbol=symbol)
                
            file_path=config_manager.backtest_data_path()
            logger.info("Entering clearing phase")
            
            save_to_hist_data_json(data_with_symbols,file_path)