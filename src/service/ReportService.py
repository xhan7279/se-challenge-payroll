from service import logger
from model import db
import pandas as pd


class RepportService:
    @staticmethod
    def generate_report():
        try:
            # left join job group for job group id
            history = pd.read_sql_table(table_name='history', con=db.engine, parse_dates=['date'])
            rate = pd.read_sql_table(table_name='rate', con=db.engine)
            df = pd.merge(history, rate, how='left', left_on='jid', right_on='jid', sort=True)
            df['amountpaid'] = df['hours'].astype(float) * df['rate'].astype(float)
            df['payperiod'] = df['date'].apply(lambda x: f"1/{x.month}/{x.year} - 15/{x.month}/{x.year}" if x.day <=15 else f"16/{x.month}/{x.year} - 30/{x.month}/{x.year}")
            df = df[['payperiod', 'eid', 'amountpaid']].groupby(['payperiod', 'eid']).sum().reset_index()
            return df

        except Exception as e:
            logger.error(e)
            raise e
