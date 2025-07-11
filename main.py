from src.screener import logger
from src.screener.components.fyers_login import fyers_login
from src.screener.components.data_retrival import data_retrival
from src.screener.components.screener import screener



def login():
    STAGE="login Stage"
    try:
        logger.info(f"-----{STAGE}-----")
        login=fyers_login.login()
        logger.info(f"{STAGE} sucessful")
    except Exception as e:
        logger.exception(e)
        raise e
    
def hist_data():
    STAGE="Data retrival Stage"
    try:
        logger.info(f"-----{STAGE}-----")
        retriever = data_retrival()
        retriever.prev_day_data()
        logger.info(f"{STAGE} sucessful")
    except Exception as e:
        logger.exception(e)
        raise e
    

    
def screener_phase():
    STAGE="Screening stage"
    try:
        logger.info(f"-----{STAGE}-----")
        sc=screener()
        sc.screening_phase()
        logger.info(f"{STAGE} sucessful")

    except Exception as e:
        logger.exception(e)
        raise e
    
if __name__=="__main__":


    hist_data()
    screener_phase()