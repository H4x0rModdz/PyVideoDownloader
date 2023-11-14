import yt_dlp

url = input("Put ur URL: ")
output_path = input("Enter the output path (press Enter for default): ")
custom_name = input("Enter a custom name for the video (press Enter to use the default name): ")

ydl_opts = {
    'outtmpl': f'{output_path}/%(title)s.%(ext)s' if output_path else None,
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
}

if custom_name:
    ydl_opts['outtmpl'] = f'{output_path}/{custom_name}.%(ext)s'

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Success!")
