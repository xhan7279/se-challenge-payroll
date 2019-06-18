from service import logger
from model.Files import FilesModel
import pandas as pd


class FileService:
    @staticmethod
    def upload(file, filename):
        try:
            if not FileService.check_fname(fname=filename):
                raise ValueError("File already uploaded.")

            df = pd.read_csv(file, parse_dates=['date'])
            if df.empty or len(df.index) == 0:
                # empty dataframe
                return True
            else:
                # upload per line
                pass

        except ValueError as e:
            logger.error(e)
            raise ValueError(e)

    @staticmethod
    def check_fname(fname):
        f = FilesModel.query.filter_by(name=fname).one_or_none()
        return f is None

