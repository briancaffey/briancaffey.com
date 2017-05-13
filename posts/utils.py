import datetime 
import re
import math
from django.utils.html import strip_tags

def count_words(html_string):
	word_string = strip_tags(html_string)
	count = len(re.findall(r'\w+', word_string))
	return count

def get_read_time(html_string):
	count = count_words(html_string)
	read_time_min = math.ceil(count/200.0)
	# read_time_sec = read_time_min * 60
	# read_time = str(datetime.timedelta(seconds=read_time_sec))
	read_time = str(datetime.timedelta(minutes=read_time_min))
	return read_time
