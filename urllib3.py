try:
    import wget
execept:
    import os
    result = os.system("pip install wget")
    try:
        import wget
    except ModuleNotFoundError:
        if result == 0:
            raise ImportError("Pip succeded, but wget was not found. Check PATH")
        raise ImportError("Pip failed, unable to install wget")
    except ImportError:
        print("Unknown error whilst trying to import wget, pip code is %s"%result)
    try:
        download=wget.download
    except Exception:
        print("wget can't download, pip code is %s"%result)
        raise ImportError("wget cannot download, perhaps you have another file wget.py?")
    if result != 0:
        print("Strange behaviour detected, pip failed but wget was imported correctly.")
 def get(link):
     wget.download(link)
