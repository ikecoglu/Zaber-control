from zaber_motion import Units
from zaber_motion.ascii import Connection

# Set the correct serial port for your system.
with Connection.open_serial_port("/dev/tty.usbserial-A10PQWLG") as connection:
    connection.enable_alerts()

    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    device_x = device_list[0]
    device_y = device_list[1]
    device_z = device_list[2]

    axis_x = device_x.get_axis(1)
    axis_y = device_y.get_axis(1)
    axis_z = device_z.get_axis(1)

    if not axis_x.is_homed():
        axis_x.home()
    if not axis_y.is_homed():
        axis_y.home()
    if not axis_z.is_homed():
        axis_z.home()

    # Move to middle of the travel range
    axis_x.move_absolute(25, Units.LENGTH_MILLIMETRES)
    # axis_y.move_absolute(25, Units.LENGTH_MILLIMETRES)
    # axis_z.move_absolute(12.5, Units.LENGTH_MILLIMETRES)

    # Move by an additional 5mm
    # axis_x.move_relative(5, Units.LENGTH_MILLIMETRES)
    # axis_y.move_relative(5, Units.LENGTH_MILLIMETRES)
    # axis_z.move_relative(5, Units.LENGTH_MILLIMETRES)

    # Sine wave motion on the X axis
    axis_x.move_sin(10, Units.LENGTH_MILLIMETRES, 10, Units.TIME_SECONDS, count=2)