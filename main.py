import BilibiliSP
import YoutubeSp
import CheckVideo
from libraries import *
from notification_screen import *
from download_bar import *
from undownload import del_file


if __name__ == '__main__':
    class Application(Frame, object):
        def __init__(self, master):
            super(Application, self). \
                __init__(master)

            master.title("The Universal Video Platform Downloader")
            master.wm_iconbitmap("./image/interface.ico")
            master.geometry("1000x600")
            master.configure(bg="#ffffff")

            self.create_widgets()

        def create_widgets(self):
            self.canvas = Canvas(
                self.master,
                bg="#ffffff",
                height=600,
                width=1000,
                bd=0,
                highlightthickness=0,
                relief="ridge")
            self.canvas.place(x=0, y=0)

            # Background for GUI
            self.background_img = PhotoImage(file=f"./image/main_page_bg.png")
            self.background = self.canvas.create_image(
                500.0, 300.0,
                image=self.background_img)

            # Creat a textbox
            self.textbox_img = PhotoImage(file=f"./image/main_page_textBox.png")
            self.textbox_bg = self.canvas.create_image(
                683.0, 210.5,
                image=self.textbox_img)

            self.textbox = Entry(
                bd=0,
                bg="#e4edf3",
                highlightthickness=0)

            self.textbox.place(
                x=460.0, y=190,
                width=446.0,
                height=39)

            # Download button
            self.download_img = PhotoImage(file=f"./image/main_page_download_btt.png")
            self.download_btt = Button(
                image=self.download_img,
                bg="#ffffff",
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_download_clicked,
                relief="flat")

            self.download_btt.place(
                x=484, y=256,
                width=115,
                height=50)

            # Open button button
            self.open_img = PhotoImage(file=f"./image/btt_open_folder.png")
            self.open_btt = Button(
                image=self.open_img,
                bg="#ffffff",
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_open_download_clicked,
                relief="flat")

            self.open_btt.place(
                x=758, y=255,
                width=137,
                height=50)

            # Bilibili button
            self.Bilibili_img = PhotoImage(file=f"./image/btt_bilibili.png")
            self.Bilibili_btt = Button(
                image=self.Bilibili_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_bilibili_clicked,
                relief="flat")

            self.Bilibili_btt.place(
                x=417, y=441,
                width=171,
                height=65)

            # Douyin platform button
            self.douyin_img = PhotoImage(file=f"./image/btt_douyin.png")
            self.douyin_btt = Button(
                image=self.douyin_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_douyin_clicked,
                relief="flat")

            self.douyin_btt.place(
                x=613, y=441,
                width=171,
                height=65)

            # Youtube platform button
            self.youtube_img = PhotoImage(file=f"./image/btt_youtube.png")
            self.youtube_btt = Button(
                image=self.youtube_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.btn_youtube_clicked,
                relief="flat")

            self.youtube_btt.place(
                x=809, y=441,
                width=171,
                height=65)

        def btn_download_clicked(self):

            bilibili_checkurl = "www.bilibili.com"
            youtube_checkurl = "www.youtube.com"
            douuyin_checkurl = "www.douyin.com"

            self.top = Toplevel()
            inp = self.textbox.get()
            if re.findall(bilibili_checkurl, inp):
                try:
                    CheckVideo.checkbilibili(inp)
                    windown_download = download(self.top, inp)
                except:
                    window_load = invalue_input_bilibili_exist(self.top)

            elif re.findall(youtube_checkurl, inp):
                try:
                    CheckVideo.checkyoutube(inp)
                    windown_download = download(self.top, inp)
                except:
                    window_load = invalue_input_youtube_exist(self.top)

            elif re.findall(douuyin_checkurl, inp):
                try:
                    CheckVideo.checkdouyin(inp)
                    windown_download = download(self.top, inp)
                except:
                    window_load = invalue_input_douyin_exist(self.top)

            else:
                windown_download = invalue_input(self.top)

        # Open youtube website when user clicked
        def btn_youtube_clicked(self):
            webbrowser.open('https://www.youtube.com/')

        # Open bilibili website when user clicked
        def btn_bilibili_clicked(self):
            webbrowser.open('https://www.bilibili.com/')

        # Open douyin website when user clicked
        def btn_douyin_clicked(self):
            webbrowser.open('https://www.douyin.com/discover')

        # Open Download document when user clicked
        def btn_open_download_clicked(self):
            os.system('explorer .\\Download')

    del_file()
    test_ff()
    root = Tk()
    root.resizable(False, False)
    app = Application(root)
    app.mainloop()
