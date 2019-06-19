from service import logger
from model import db
from model.History import HistoryModel
from model.JobGroup import JobGroupModel
import pandas as pd
from model import transaction


class HistoryService:
    @staticmethod
    @transaction
    def add(session, df):
        try:
            # left join job group for job group id
            jg = pd.read_sql_table(table_name='jobgroup', con=db.engine)
            df = pd.merge(df, jg, how='left', left_on='jg', right_on='name', sort=True)
            for idx, row in df.iterrows():
                history = HistoryModel(date=row['date'],
                                       hours=row['hours'],
                                       eid=row['eid'],
                                       jid=row['id'])
                session.add(history)
        except Exception as e:
            raise e


