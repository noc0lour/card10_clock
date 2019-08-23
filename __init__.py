from clock.main import Time
import ujson
import os


def main():
    if 'clockv2.json' in os.listdir('/'):
        with open('/clockv2.json', 'r') as clock_conf:
            config = ujson.loads(clock_conf.read())
        wf_name = config.get('watchface', 'digital_clock')
    else:
        wf_name = 'digital_clock'
    wf_module = {}
    exec('from clock.plugins import {} as wf'.format(wf_name), wf_module)
    c = wf_module['wf'].watch()
    t = Time(c)
    t.loop()


if __name__ == "__main__":
    exit(not main())
