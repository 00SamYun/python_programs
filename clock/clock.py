import re
import requests
import time
from playsound import playsound
from multiprocessing import Process


class Clock():
    
    def __init__(self):
        self.timezones = requests.get('http://worldtimeapi.org/api/timezone/').json()
        self.timer_sound = 'timer_sound_effect.mp3'
        self.alarm_sound = 'alarm_sound_effect.mp3'
        
    
    def local_time(self):
        h_m_s = [str(x) for x in time.localtime()[3:6]]
        return ':'.join([x if len(x)==2 else '0' + x for x in h_m_s])
    
    
    def world_time(self):

        time_obj = re.compile(r'\d\d:\d\d:\d\d')

        location = input('Location: ').replace(' ', '_')
        candidates = [x for x in self.timezones if x.endswith(location)]

        if len(candidates) == 1:
            candidate = candidates[0]
#         elif len(candidates) > 1:
#             area = input(f'There are more than one location with the name: {location}.'
#                         '\nWhich location are you referring to?'
#                         f'\n{candidates}'
#                         '\n: ')
#             candidate = [x for x in candidates if x.startswith(area)][0]
        else:
            return 'Location not found. Make sure to capitalize the location name.'

        response = requests.get('http://worldtimeapi.org/api/timezone/' + candidate)
        datetime = response.json()['datetime']

        return re.search(time_obj, datetime).group(0)
    
    
    def alarm(self):
        time_str = input('Enter Time Of Alarm hh:mm \n')
        stop_time = tuple(int(x) for x in time_str.split(':'))
        cur_time = ()

        while cur_time != stop_time:
            cur_time = time.localtime()[3:5]

        alarm = Process(target=playsound, args=(self.alarm_sound,))
        alarm.start()
        input('Click Enter')
        alarm.terminate()
        
        
    def timer(self):
        hrs = int(input('HOUR: '))
        mins = int(input('MINUTE: '))
        secs = int(input('SECOND: '))
        total_secs = hrs*3600 + mins*60 + secs

        timer = Process(target=playsound, args=(self.timer_sound,))

        time.sleep(total_secs)
        print('Times Up!')
        timer.start()
        input('Click Enter')
        timer.terminate()
        
        
    def stopwatch(self):
        input('Click enter to start')
        start = time.time()
        input('Click enter to stop')
        stop = time.time()

        secs = stop-start

        m_s = round((secs % 1) * 100)
        s = int(secs % 60)
        m = int((secs//60) % 60)
        h = int((secs//3600))

        string = [str(x) for x in [h, m, s, m_s]]
        string = [x if len(x)==2 else '0' + x if len(x)==1 else '00' for x in string]

        return ':'.join(string)
    

# clock = Clock()

# clock.local_time()

# clock.timezones
# clock.world_time()

# clock.alarm()
# clock.timer()
# clock.stopwatch()
