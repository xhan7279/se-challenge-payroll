from service import logger
from model.JobGroup import JobGroupModel
from service.HistoryService import HistoryService
import pandas as pd
from model import transaction


class JobGroupService:
    @staticmethod
    @transaction
    def add(session, df):
        # add job group if its new
        try:
            jgs = df['jg'].drop_duplicates()
            for name in jgs.values.tolist():
                jg = JobGroupModel.query.filter_by(name=name).first()
                if jg is None:
                    newjg = JobGroupModel(name=name)
                    session.add(newjg)

        except Exception as e:
            logger.error(e)
            raise e
