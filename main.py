import requests

from urllib.parse import parse_qs

VID = "Fmdb-KmlzD8"

def parse(qs):
    d = parse_qs(qs)
    m = d["url_encoded_fmt_stream_map"]
    print(m)

def main():
    resp = requests.get('https://www.youtube.com/get_video_info?video_id={}'.format(VID))
    parse(resp.content)

if name == "main" :
    main()
