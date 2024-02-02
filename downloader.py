from pytube import YouTube


def main():

    yt = YouTube("http://youtube.com/watch?v=DquoH-H-sWo&")

    stream = yt.streams.get_by_itag(22)
    stream.download()


main()
