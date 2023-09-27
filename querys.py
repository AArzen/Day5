from tables import *
import base


def insert_part(serial_num: str, order_num: str, quality: int, date=base.formatted_date_time, plant=''):
    """

    :param serial_num: Part serial number
    :param order_num: Work order number
    :param quality: Part quality number [0 - in progress, 1 - good, 2 - bad]
    :param date: Date and time [FORMAT - %Y-%m-%d %H:%M:%S] DEFAULT=Current date & time
    :param plant: Plant number
    :return: None
    """

    data = Parts(serial_num=serial_num, order_num=order_num, quality=quality, date=date, plant=plant)
    db.add(data)
    db.commit()


def insert_parameter(id_pdh, actual_value='', unit='', description='', quality=1, station='', val_type=0):
    """

    :param id_pdh:
    :param actual_value: Parameter STRING value
    :param unit: Parameter unit
    :param description: Parameter description
    :param quality: Parameter quality number [0 - no status, 1 - good, 2 - bad]
    :param station: Station number
    :param val_type: Actual value type
    :return: None
    """

    data = ParameterList(id_parts=id_pdh,
                         actual_value=actual_value,
                         unit=unit,
                         description=description,
                         quality=quality,
                         station=station,
                         type=val_type)
    db.add(data)
    db.commit()


def get_last_record_part_filter_serial_order_plant(serial_num: str, order_num: str, plant: str):
    """

    :param serial_num: Part serial number
    :param order_num: Part work order number
    :param plant: Part Plant
    :return: record part
    """

    data = db.query(Parts).filter(Parts.serial_num == serial_num, Parts.order_num == order_num,
                                  Parts.plant == plant).first()
    return data


def get_part_data(serial_num: str, order_num: str, plant: str):
    """

    :param serial_num: Part serial number
    :param order_num: Part Order number
    :param plant: Part Plant
    :return: Part data
    """

    data = db.query(Parts.date, Parts.serial_num, Parts.order_num, Parts.quality,
                    ParameterList.description, ParameterList.station, ParameterList.quality,
                    ParameterList.actual_value, ParameterList.type, ParameterList.unit)\
        .filter(Parts.id == ParameterList.id_parts,
                Parts.serial_num == serial_num,
                Parts.order_num == order_num,
                Parts.plant == plant).all()
    return data
