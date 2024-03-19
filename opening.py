import webbrowser


def open(type="google") -> None:
    if "google" in type:
        webbrowser.open("https://www.google.com/")
    elif "facebook" in type:
        webbrowser.open("https://www.facebook.com/")
    elif "youtube" in type:
        webbrowser.open("https://www.youtube.com/")
    else:
        webbrowser.open("https://www.google.com/")
