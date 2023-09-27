from sqla_wrapper import SQLAlchemy
from datetime import datetime

db = SQLAlchemy("sqlite:///MachineData.sqlite")
date_time = datetime.now()
formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

parameter_type = {
    'NoneType': 0,
    'bool': 1,
    'int': 2,
    'float': 3,
    'str': 4,
}
