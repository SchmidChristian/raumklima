from os.path import dirname

from rs5002redis.saver import save_data_to_redis
from rs500reader.reader import Rs500Reader


def fetch_and_save():
    reader = Rs500Reader()
    data = reader.get_data()
    if data is not None:
        to_save = {}
        for channel, values in data.items():
            if values is not None:
                to_save['c{}_temp'.format(channel)] = values.temperature
                to_save['c{}_humi'.format(channel)] = values.humidity
        save_data_to_redis(to_save, dirname(__file__) + '/' + 'rs5002redis.ini')


if __name__ == '__main__':
    fetch_and_save()
