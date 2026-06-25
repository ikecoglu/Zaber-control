from zaber_motion import Units
from zaber_motion.ascii import Connection

# Set the correct serial port for your system.
with Connection.open_serial_port("COM3") as connection:
    connection.enable_alerts()

    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    device_x = device_list[0]
    device_y = device_list[1]
    device_z = device_list[2]

    axis_x = device_x.get_axis(1)
    axis_y = device_y.get_axis(1)
    axis_z = device_z.get_axis(1)

    # Home all axes, y axis first
    if not axis_y.is_homed():
        axis_y.home()
    if not axis_z.is_homed():
        axis_z.home()
    if not axis_x.is_homed():
        axis_x.home()

    # Move to the start position
    axis_x.move_absolute(0, Units.LENGTH_MILLIMETRES)
    axis_y.move_absolute(0, Units.LENGTH_MILLIMETRES)
    axis_z.move_absolute(0, Units.LENGTH_MILLIMETRES)

    # Move to the end position
    axis_x.move_absolute(50, Units.LENGTH_MILLIMETRES)
    axis_y.move_absolute(50, Units.LENGTH_MILLIMETRES)
    axis_z.move_absolute(25, Units.LENGTH_MILLIMETRES)

    # Move to middle of the travel range
    axis_x.move_absolute(25, Units.LENGTH_MILLIMETRES)
    axis_y.move_absolute(25, Units.LENGTH_MILLIMETRES)
    axis_z.move_absolute(12.5, Units.LENGTH_MILLIMETRES)