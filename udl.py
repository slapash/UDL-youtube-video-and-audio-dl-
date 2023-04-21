import PySimpleGUI as sg
from pytube import YouTube

sg.theme('DarkBlue')

layout = [
    [sg.Text('URL de video youtube:')],
    [sg.InputText('', key='video_url')],
    [sg.Text('Choisissez la qualité de la vidéo:')],
    [sg.Combo(['Haute', 'Basse'], key='video_quality')],
    [sg.Radio('Video', 'media_type', default=True, key='video_option'), sg.Radio('Audio', 'media_type', key='audio_option')],
    [sg.Button('Télécharger'), sg.Button('Quitter')]
]

window = sg.Window('YouTube Video Downloader', layout)

def download_video(url, quality, video_option):
    try:
        yt = YouTube(url)
        if video_option:
            if quality == 'Haute':
                video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
            else:
                video = yt.streams.filter(progressive=True, file_extension='mp4').get_lowest_resolution()
            video.download()
        else:
            audio = yt.streams.filter(only_audio=True).first()
            audio.download()
        return True
    except Exception as e:
        print(e)
        return False

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break
    elif event == 'Télécharger':
        url = values['video_url']
        quality = values['video_quality']
        video_option = values['video_option']
        
        if not url:
            sg.popup('Entrez une URL valide')
        else:
            success = download_video(url, quality, video_option)
            if success:
                sg.popup('Téléchargement términé')
            else:
                sg.popup("Erreur. Vérifiez l'URL avant de réessayer")

window.close()
