#!/usr/bin/env python
import sys
import datetime

SHORT_BREAK_LENGTH = 5
LONG_BREAK_LENGTH = 20
POMODORO_LENGTH = 25

if __name__ == '__main__':
    number_of_pomodoros = int(sys.argv[1])
    number_of_long_breaks = (number_of_pomodoros - 1) / 4
    number_of_short_breaks = number_of_pomodoros - 1 - number_of_long_breaks
    time = (number_of_pomodoros * POMODORO_LENGTH +
            number_of_long_breaks * LONG_BREAK_LENGTH +
            number_of_short_breaks * SHORT_BREAK_LENGTH)

    print "expected time: %s" % str(datetime.timedelta(minutes=time))
 
