from src.screener import logger
from src.screener.configurations.config import config_manager
import pandas as pd

class screener:
    def screening_phase(self):
        data_file_path=config_manager.json_file_path()

        df=pd.read_json(data_file_path)
        logger.info("data frmae load succesful")
        df['date'] = pd.to_datetime(df['date'])
        df['range'] = abs((df['high'] - df['low']) / df['low']) * 100
        df['body_range'] = abs((df['close'] - df['open']) / df['open']) * 100
        df['eligibility'] = (df['range'] < 1.75) & (df['body_range'] < 0.5)
        df=df[df['eligibility'] == True]

        df=df.drop(columns=['open','high','low','close','volume'])

        print(df)
