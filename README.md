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

    def data_gen(n=3):
        for i in range(n):
            yield [x for x in range(n)]

    @pace_me(data_gen)
    def process(data):
        print('Processing....{0}'.format(data))
```
# Run tests
- All tests (`docker-compose run --rm test`)
- Single test in a file(`docker-compose run --rm test bash -c "python setup.py develop &&  pytest tests/test_*.py -k 'test_float'"`)
- `docker inspect --format='{{.Id}} {{.Parent}}'     $(docker images --filter since=<image_id> --quiet)` to check dependent child images

# Sonar Scan
Gitignored .env file contains the SONAR_CLOUD_TOKEN variable (locally)

- `docker-compose run --rm test ./scan`