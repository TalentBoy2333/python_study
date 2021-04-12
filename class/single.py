class MusicPlayer:
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self): # 初始化程序只执行一次
        if MusicPlayer.init_flag:  # 已经执行过
            return
        print("初始化播放器")
        MusicPlayer.init_flag = True

mp1 = MusicPlayer()
mp2 = MusicPlayer()
print(mp1)
print(mp2)