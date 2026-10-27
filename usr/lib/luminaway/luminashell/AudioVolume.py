from subprocess import Popen, PIPE

class AudioVolume:
    def __init__(self):
        self.volume = self.get_volume()
    
    def get_volume(self):
        process = Popen(['amixer', 'get', 'Master'], stdout=PIPE)
        output, _ = process.communicate()
        for line in output.decode().split('\n'):
            if '%' in line:
                start = line.find('[') + 1
                end = line.find('%')
                return int(line[start:end])
        return 0
    
    def set_volume(self, volume):
        Popen(['amixer', 'set', 'Master', f'{volume}%'])
        self.volume = volume