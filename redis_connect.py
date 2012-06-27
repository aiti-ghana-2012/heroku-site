import redis
import os
import re

def _get_redis_params():
		
	REDIS_URL = os.environ.get('REDISTOGO_URL','redis://redistogo:477481d93e425fef710484ac2eee5623@drum.redistogo.com:9696/')
	
	match_object = re.match(r"redis://redistogo:(?P<password>.+?)@(?P<host>.+?):(?P<port>\d+)",REDIS_URL)
	redis_params = match_object.groupdict()
	
	redis_params['port'] = int(redis_params['port'])
	return redis_params
	
	
	
def get_connection():

	return redis.Redis(**_get_redis_params())
	
	
	
