from service import logger
from model import db
from model.History import HistoryModel
import pandas as pd
from model import transaction
import datetime

class HistoryService:
    @staticmethod
    @transaction
    def add(session, df, fid):
        try:
            # left join job group for job group id
            jg = pd.read_sql_table(table_name='jobgroup', con=db.engine)
            df = pd.merge(df, jg, how='left', left_on='jg', right_on='name', sort=True)

            for idx, row in df.iterrows():
                history = HistoryModel(date=datetime.datetime.strptime(row['date'], '%d/%m/%Y'),
                                       hours=row['hours'],
                                       eid=row['eid'],
                                       jid=row['id'],
                                       fid=fid)
                session.add(history)
        except Exception as e:
            logger.error(e)
            raise e


