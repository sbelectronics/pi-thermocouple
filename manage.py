#!/usr/bin/env python
import os
import sys
import grillmoncontroller

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grillmon.settings")

    from django.core.management import execute_from_command_line

    print "starting up grillmon"
    args = list(sys.argv)
    if ("--nohardware" in args):
        args.remove("--nohardware")
        grillmoncontroller.startup(noHardware=True)
    else:
        if ("runserver" in args) and ("--noreload" not in args):
            print >> sys.stderr, "please use --noreload after runserver"
            sys.exit(-1)
        grillmoncontroller.startup(noHardware=False)
    print "finished starting up grillmon"

    execute_from_command_line(args)
