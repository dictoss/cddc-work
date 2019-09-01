#!/bin/bash
#
#
#

## this file is ~/.config/ibus/bus directory.
IBUS_PATH="unix:abstract=/tmp/dbus-qbChHyUN,guid=0fcf53c759a8558c883fc0d25d6b2a9e"

echo "== DBus root path in org.freedesktop.DBus"
echo "==== /org/freedesktop/DBus, org.freedesktop.DBus.ListNames"
dbus-send --bus=${IBUS_PATH} --dest=org.freedesktop.DBus --type=method_call --print-reply /org/freedesktop/DBus org.freedesktop.DBus.ListNames

echo

#
# scan /org/freedesktop/Ibus functions and properties.
#
echo "== /org/freedesktop/Ibus path, call function."
DBUS_PATH_IBUS__FUNC="org.freedesktop.DBus.Introspectable.Introspect"

for f in ${DBUS_PATH_IBUS__FUNC}; do
    echo "/org/freedesktop/IBus, $f"
    dbus-send --bus=${IBUS_PATH} --dest=org.freedesktop.IBus --type=method_call --print-reply /org/freedesktop/IBus $f
done

#
# 
#
echo "== /org/freedesktop/Ibus path, call function."
DBUS_PATH_IBUS__FUNC="org.freedesktop.DBus.Introspectable.Introspect"

for f in ${DBUS_PATH_IBUS__FUNC}; do
    echo "/org/freedesktop/IBus, $f"
    dbus-send --bus=${IBUS_PATH} --dest=org.freedesktop.IBus --type=method_call --print-reply /org/freedesktop/IBus $f
done

