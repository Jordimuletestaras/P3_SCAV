

import subprocess as sp

if __name__ == '__main__':
    """line = 'ffmpeg -i bbb.mp4 -ss 00:00:00 -to 00:01:00 -c:v copy -c:a copy 1min_bbb.mp4'
    sp.run(line, shell=True)

    line = 'ffmpeg -i 1min_bbb.mp4 -vcodec copy -an 1min_onlyvideo_bbb.mp4'
    sp.run(line, shell=True)

    line = 'ffmpeg -i 1min_bbb.mp4 -q:a 0 -map a 1min_audio.mp3'
    sp.run(line, shell=True)

    line = 'ffmpeg -i 1min_audio.mp3 -ac 1 mono_1min_audio.mp3'
    sp.run(line, shell=True)

    line = 'ffmpeg -i 1min_audio.mp3 -codec:a libmp3lame -b:a 50k 1_min_lowbr_audio.mp3'
    sp.run(line, shell=True)"""

    line= 'ffmpeg -i 1min_onlyvideo_bbb.mp4 -i mono_1min_audio.mp3 -i 1_min_lowbr_audio.mp3 -map 0 -map 1 -map 2  container_1_min.mp4 '
    sp.run(line, shell=True)