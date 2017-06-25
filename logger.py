import os
import datetime
from play import PlayAPI
from multiprocessing import Pool

def to_ts(dt):
    timestamp = (dt - datetime.datetime(1970, 1, 1)).total_seconds()
    return int(timestamp)

def update(package):
    try:
        playAPI = PlayAPI()
        now = to_ts(datetime.datetime.now())
        ratings, last_updated = playAPI.get_stats(package)
        print ratings, last_updated, now
        log_entry = "%d,%s,%d\n" % (now, ','.join([str(x) for x in ratings]), to_ts(last_updated))
        open('data/' + package, 'a').write(log_entry)
    except Exception,e:
        print "Error", package
        print str(e)

if __name__ == "__main__":
    packages = open('packages.txt').readlines()
    packages = [p.rstrip() for p in packages]
    os.system('mkdir -p data')

    pool = Pool(processes=4)
    pool.map(update, packages)

