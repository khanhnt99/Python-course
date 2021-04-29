import tkinter as tk
import urllib.request


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(text="PyMi.vn checker")
        self.label.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind("<Key-Return>", self.check_site)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = (
            "Check web site up/down." " Enter URL with http(s):"
        )
        self.hi_there["command"] = self.check_site
        self.hi_there.pack()

        self.quit = tk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

    def check_site(self, event=None):
        url = self.contents.get().strip() or "https://pymi.vn"
        if not url.startswith("http"):
            url = "http://{}".format(url)

        # fake useragent as cloudflare block python agent
        r = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "python-requests/2.23.0"},
        )
        resp = urllib.request.urlopen(r, timeout=2)
        print("response: {} {}".format(resp.status, resp.url))


root = tk.Tk()
app = Application(master=root)
app.master.title("My checker app")
app.master.minsize(300, 200)
app.mainloop()
