from service import logger
from model.Files import FilesModel
from model import transaction
from service.HistoryService import HistoryService
from service.JobGroupService import JobGroupService
import pandas as pd


class FileService:
    @staticmethod
    @transaction
    def upload(session, file):
        try:
            df, fname = FileService.parse_file(file)
            if not FileService.check_fname(fname=fname):
                raise ValueError("File already uploaded.")
            else:
                logger.info(f"Adding file={fname}")
                file = FilesModel(name=fname)
                session.add(file)
                fid = FilesModel.query.filter_by(name=fname).first().id
                JobGroupService.add(df=df)
                HistoryService.add(df=df, fid=fid)

        except Exception as e:
            logger.error(e)
            raise e

    @staticmethod
    def parse_file(file):
        try:
            columns = {'date': 'date',
                       'hours worked': 'hours',
                       'employee id': 'eid',
                       'job group': 'jg',
                       }
            df = pd.read_csv(file, parse_dates=['date'])
            if df.empty or len(df.index) == 0:
                raise ValueError("Empty file.")
            df.rename(columns=columns, inplace=True)
            # get filename from footer
            footer = df.tail(1)
            fname = footer.values.tolist()[0][1]
            return df[:-1], fname

        except Exception:
            raise

    @staticmethod
    def check_fname(fname):
        f = FilesModel.query.filter_by(name=fname).one_or_none()
        return f is None
