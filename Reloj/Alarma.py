import time
import datetime 
import pygame

def set_alarm(alarm_time):
    print(f'alarm set for {alarm_time}')
    sound_file = 'Sonido_alarma.mp3'
    is_running = True
    while is_running: 
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'{current_time} = {alarm_time}')
        if current_time == alarm_time:
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)

if __name__ == '__main__':
        alarm_time = input('enter the alarm time (hh:mm:ss): ')
        set_alarm(alarm_time)

print('Alarm is ringing!')