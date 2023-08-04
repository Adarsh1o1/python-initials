import argparse
import requests


def download(url, fileName):
    if fileName is None:
        fileName = url.split("/")[-1]
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(fileName, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    return fileName


parser = argparse.ArgumentParser()
parser.add_argument("url", help="paste url here")
parser.add_argument("-o", "--output", type=str, help="save as", default=None)
args = parser.parse_args()
# print(args.url)
# print(args.output, type(args.output))
download(args.url,args.output)

