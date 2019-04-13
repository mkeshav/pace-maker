[![CircleCI branch](https://img.shields.io/circleci/project/github/mkeshav/pace-maker/master.svg)](https://circleci.com/gh/mkeshav/pace-maker/tree/master)
[![PyPI version](https://badge.fury.io/py/pacemaker-mkeshav.svg)](https://badge.fury.io/py/pacemaker-mkeshav)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=mkeshav_pace-maker&metric=alert_status)](https://sonarcloud.io/dashboard?id=mkeshav_pace-maker)

# Pace Maker 
To keep the old heart ticking

# Install
python3 -m pip install pacemaker-mkeshav

# Usage
```
    from pacemaker import pace_me

    # Function that will yield data that the process function needs
    def data_gen(n=3):
        for i in range(n):
            yield [x for x in range(n)]

    # Will make 3 requests to that url/sec using 1 token everytime process method is called 
    @pace_me(data_gen, rate_per_second=3, number_of_tokens_per_call=1, n=6)
    def process(data):
        r = requests.post('https://httpbin.org/post', data = data)
```
# Run tests
- All tests (`docker-compose run --rm test`)