import base
import querys
import tables
import strconv


def print_part_data(part_data):
    """

    :param part_data: Part data
    :return: Print part parameters
    """
    if part_data:
        date_time = part_data[0][0]
        serial_num = part_data[0][1]
        order_num = part_data[0][2]
        part_quality = part_data[0][3]

        if part_quality == 1:
            part_quality = 'OK'
        elif part_quality == 2:
            part_quality = 'NOK'
        else:
            part_quality = 'IN PROGRESS'

        print(f"""
            PART DATA
            Record created: {date_time}
            Serial number: {serial_num}
            Order number: {order_num}
            Status quality: {part_quality}
            """)

        for row_record in part_data:

            par_description = row_record[4]
            par_station = row_record[5]
            par_quality = row_record[6]
            par_value = row_record[7]
            par_type = row_record[8]
            par_unit = row_record[9]

            # Convert actual value data
            if par_type == base.parameter_type['bool']:
                par_value = strconv.convert_bool(par_value)
            elif par_type == base.parameter_type['int']:
                par_value = strconv.convert_int(par_value)
            elif par_type == base.parameter_type['float']:
                par_value = strconv.convert_float(par_value)
            elif par_type == base.parameter_type['str']:
                par_value = par_value
            else:
                par_value = ''

            # Convert status data parameter
            if par_quality == 1:
                par_quality = 'OK'
            elif par_quality == 2:
                par_quality = 'NOK'
            else:
                par_quality = 'NO STATUS'

            # Get actual value type
            par_type = list(base.parameter_type.keys())[list(base.parameter_type.values()).index(par_type)]

            # PRINT OUT DATA
            print(f"""
            PARAMETER
            Description: {par_description}
            Station: {par_station}
            Parameter Quality: {par_quality}
            Value: {par_value}{par_unit}
            Type: {par_type}
            """)
    else:
        print('No data')


if __name__ == '__main__':

    # Create tables if not exist
    tables.create_tables()

    # Simulated input data
    serial = '0008'
    Order = '0001'
    Plant = '1200'
    quality = 1

    actual_value = '97.2'
    val_type = base.parameter_type['float']
    unit = 'mm'
    description = 'Parameter 1'
    station = 'S6_Verification'

    # QUERYS - vprašanje:
    # Ali je vnos podatkov v dve povezani tabeli (one to many) na tak način pravilen
    # 1. INSERT vnesemo podatke v tabelo ONE
    # 2. S SELECT stavkom v tabeli ONE najdemo ID zapisa
    # 3. INSERT vnesemo podatke v tabelo MANY s podatkom ID od tabele ONE

    # Za brskanje zakomentiraj od tukaj dalje -->
    querys.insert_part(serial_num=serial,
                       order_num=Order,
                       quality=quality,
                       plant=Plant)
    data = querys.get_last_record_part_filter_serial_order_plant(serial, Order, Plant)
    querys.insert_parameter(id_pdh=data.id,
                            actual_value=actual_value,
                            unit=unit,
                            description=description,
                            quality=quality,
                            station=station,
                            val_type=val_type)

    actual_value = '21'
    val_type = base.parameter_type['int']
    unit = 'N'
    description = 'Parameter 2'
    station = 'S5_SprintTest'
    querys.insert_parameter(id_pdh=data.id,
                            actual_value=actual_value,
                            unit=unit,
                            description=description,
                            quality=quality,
                            station=station,
                            val_type=val_type)
    # <-- do tukaj

    data = querys.get_part_data(serial_num=serial, order_num=Order, plant=Plant)
    print_part_data(data)
