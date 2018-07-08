import requests
from urllib.parse import parse_qs
import shutil

VID = "Fmdb-KmlzD8"


def parse(qs):
    d = parse_qs(qs)
    steam_lst = d["url_encoded_fmt_stream_map"]
    d2 = parse_qs(steam_lst[0])
    url = d2["url"]
    print(url)
    return url


def main():
    resp = requests.get('https://www.youtube.com/get_video_info?video_id={}'.format(VID))
    url = parse(resp.text)[0]
    res = requests.get(url)
    with open("{}.mp4".format(VID), "wb") as file:
        shutil.copyfileobj(res.raw, file)

if __name__ == "__main__":
    main()
