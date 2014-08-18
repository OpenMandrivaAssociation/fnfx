# We can't run without acpi:
[ -e /proc/acpi ] || exit

# If toshiba_acpi doesn't exist, try loading the module...
[ -e /proc/acpi/toshiba ] || /sbin/modprobe toshiba_acpi &>/dev/null

# Don't bother if /proc/acpi/toshiba still doesn't exist
[ -e /proc/acpi/toshiba ]|| exit
