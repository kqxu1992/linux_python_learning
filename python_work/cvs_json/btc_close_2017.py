import json

filename = "btc_close_2017.json"

with open(filename) as f:
	btc_data = json.load(f)

dates, months, weeks, weekdays, closes = [], [], [], [], []
for btc_dict in btc_data:
	date = btc_dict["date"]
	month = int(btc_dict["month"])
	week = int(btc_dict["week"])
	weekday = btc_dict["weekday"]
	close = int(float(btc_dict["close"]))
	
	dates.append(date)
	months.append(month)
	weeks.append(week)
	weekdays.append(weekday)
	closes.append(close)
	print("{} is month {} week {}, {}, the colse price is {} RMB".format(date, month, week, weekday, close))

import pygal
import math
line_chart = pygal.Line(x_label_ratation=20, show_minor_x_labels=False)
line_chart.title="last value"
line_chart.x_labels = dates
N = 20
line_chart.x_label_major = date[::20]
closes_log = [math.log10() for _ in closes]
line_chart.add("last value",closes_log)
line_chart.render_to_file("line_of_last_value.svg")
