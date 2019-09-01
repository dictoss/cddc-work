#!/usr/bin/python3
#
# scan dbus interface for ibus
#
# auther: dictoss@live.jp (Norimitsu Sugimoto)
#
import sys
import subprocess
import xml.etree.ElementTree as ET 

import dbus

_IS_VERBOSE = False

class DbusProperty(object):
    def __init__(self, name, vertype, access):
        self.name = name
        self.vertype = vertype
        self.access = access


class DbusMethodArg(object):
    def __init__(self, name, vertype, direction):
        self.name = name
        self.vertype = vertype
        self.direction = direction


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
        _proplist = []
        for p in _props:
            _tmp_prop = DbusProperty(p.get("name"), p.get("type"), p.get("access"))
            _proplist.append(_tmp_prop)

        # print property
        if 0 < len(_proplist):
            print("  PROPERTY:")
            for a in _proplist:
                print("  %02s | %s | %s" % (a.vertype, a.name, a.access))


        _methods = o.findall("method")
        for m in _methods:
            print("  method: %s" % (m.get("name")))

            _args = m.findall("arg")
            _in_args = []
            _out_args = []
            for a in _args:
                # direction: in/out
                # name:
                # type: parameter type(string, object, value, binary)
                _tmp_arg = DbusMethodArg(a.get("name"), a.get("type"), a.get("direction"))

                if a.get("direction") == "in":
                    _in_args.append(_tmp_arg)
                elif a.get("direction") == "out":
                    _out_args.append(_tmp_arg)
                else:
                    raise Exception("ERROR: unknown direction")

            # print in-parameter
            if 0 < len(_in_args):
                print("    IN  ARGS")
                for a in _in_args:
                    print("      %02s | %s" % (a.vertype, a.name))
            else:
                print("    IN  NO-ARGS")

            if 0 < len(_out_args):
                print("    OUT ARGS")
                for a in _out_args:
                    print("      %02s | %s" % (a.vertype, a.name))
            else:
                print("    OUT  NO-ARGS")


if '__main__' == __name__:
    main()
