#!/usr/bin/python3
#
#
# auther: dictoss@live.jp (Norimitsu Sugimoto)
import sys
import subprocess
import xml.etree.ElementTree as ET 

import dbus

_IS_VERBOSE = False


def _debug_print(s):
    if _IS_VERBOSE:
        print(s)


def main():
    #scan_dbus_interface()
    scan_dbus_interface_for_ibus()


def scan_dbus_interface():
    _bus = dbus.SessionBus()
    _proxy = _bus.get_object(        
        "org.freedesktop.DBus",
        "/org/freedesktop/DBus")

    _res_xml = _proxy.Introspect()
    _debug_print(_res_xml)

    _tree = ET.fromstring(_res_xml)
    _debug_print(_tree)
    _ifs = _tree.findall("interface")
    _debug_print(_ifs)
    
    for o in _ifs:
        print("interface: %s" % (o.get("name")))

        _props = o.findall("property")
        for p in _props:
            print("  property: %s" % (p.get("name")))

        _methods = o.findall("method")
        for m in _methods:
            print("  method: %s" % (m.get("name")))


def scan_dbus_interface_for_ibus():
    # get ibus unix domain socket path.
    _stdout = subprocess.check_output(["ibus", "address"])
    _ibus_unix_addr = _stdout.decode("utf8").rstrip("\n")
    
    _bus = dbus.connection.Connection(_ibus_unix_addr)

    _proxy = _bus.get_object(
        "org.freedesktop.IBus",
        "/org/freedesktop/IBus")

    _proxy_if = dbus.Interface(
        _proxy,
        "org.freedesktop.DBus.Introspectable")

    _res_xml = _proxy_if.Introspect()    
    _debug_print(_res_xml)

    _tree = ET.fromstring(_res_xml)
    _debug_print(_tree)
    _ifs = _tree.findall("interface")
    _debug_print(_ifs)
    
    for o in _ifs:
        print("interface: %s" % (o.get("name")))

        _props = o.findall("property")
        for p in _props:
            print("  property: %s" % (p.get("name")))

        _methods = o.findall("method")
        for m in _methods:
            print("  method: %s" % (m.get("name")))


if '__main__' == __name__:
    main()
