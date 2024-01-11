import requests
from bs4 import BeautifulSoup
import datetime

class MRT:

    def __init__(self, start, direction):
        self.enter_station = start
        self.direction = direction

    #enter_station = '技擊館'

    ##################建立現在時間(now是時:分:秒)##############
    def time_generate(self):
        today = datetime.date.today()
        self.now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).time()

        week = today.isoweekday()


        if week>=1 and week <=4:
            self.week_str = 'n'
        elif week == 5:
           self.week_str = 'b'
        else:
            self.week_str = 'h'


    ###############字典建立######################
    def url_dict(self):    
        normal = "https://www.krtc.com.tw/Guide/train_times?n="
        before = "https://www.krtc.com.tw/Guide/train_times_before_holiday?n="
        holiday = "https://www.krtc.com.tw/Guide/train_times_holiday?n="

        self.fixed_url = {
            "n":normal,
            "b":before,
            "h":holiday
        }

        self.station_orange = {
            "西子灣":"O1",
            "鹽埕埔":"O2",
            "市議會(舊址)":"O4",
            "美麗島":"O5",
            "信義國小":"O6",
            "文化中心":"O7",
            "五塊厝":"O8",
            "技擊館":"O9",
            "衛武營":"O10",
            "鳳山西站(高雄市議會)":"O11",
            "鳳山":"O12",
            "大東":"O13",
            "鳳山國中":"O14",
            "大寮":"OT1"
        }

        self.station_red = {
            "小港":"R3",
            "高雄國際機場":"R4",
            "草衙":"R4A",
            "前鎮高中":"R5",
            "凱旋":"R6",
            "獅甲":"R7",
            "三多商圈":"R8",
            "中央公園":"R9",
            "美麗島":"R10",
            "高雄車站":"R11",
            "後驛":"R12",
            "凹子底":"R13",
            "巨蛋":"R14",
            "生態園區":"R15",
            "左營":"R16",
            "世運":"R17",
            "油廠國小":"R18",
            "楠梓加工區":"R19",
            "後勁":"R20",
            "都會公園":"R21",
            "青埔":"R21",
            "橋頭糖廠":"R22A",
            "橋頭火車站":"R23",
            "南岡山":"R24"
        }

        #######分每個站每個日子的時刻表網址#######
        self.url_dict_orange = {
            std_key:{
                f_key : f_value + std_value + "#articleBox" for f_key,f_value in self.fixed_url.items()
            }
            for std_key, std_value in self.station_orange.items()
        }

        self.url_dict_red = {
            std_key:{
                f_key : f_value + std_value + "#articleBox" for f_key,f_value in self.fixed_url.items()
            }
            for std_key, std_value in self.station_red.items()
        }





###########從起訖站跟周幾決定好爬蟲的網址##########
    def url_generate(self):
        self.url_dict()
        if self.direction == '東' or self.direction == '西':
            r = requests.get(self.url_dict_orange[self.enter_station][self.week_str])
        elif self.direction == '南' or self.direction == '北':
            r = requests.get(self.url_dict_red[self.enter_station][self.week_str])
        soup = BeautifulSoup(r.text,"html.parser")
        self.table = soup.select('.tableTimeTableData')


###########往東或往北的時刻表#########
    def table_up(self):
        toki_up = self.table[0].select('tr th')
        bun_up = self.table[0].select('td')
        toki_up_lst = [t.get_text()[:-1] for t in toki_up]
        time_up = {}
        i = 0
        for t in toki_up_lst:
            time_up[int(t) % 24] = [int(b.get_text()) for b in bun_up[i].select('span')]
            i+=1
        time_up = [datetime.time(t,m) for t,m_l in time_up.items() for m in m_l]


        return time_up
    
###########往西或往南的時刻表#########
    def table_down(self):
        toki_down = self.table[1].select('tr th')
        bun_down = self.table[1].select('td')
        toki_down_lst = [t.get_text()[:-1] for t in toki_down]
        time_down = {}
        j = 0
        for t in toki_down_lst:
            time_down[int(t) % 24] = [int(b.get_text()) for b in bun_down[j].select('span')]
            j+=1
        time_down = [datetime.time(t,m) for t,m_l in time_down.items() for m in m_l]
        return time_down

###############決定要產生往哪裡的時刻表字典##########
    def table_generate(self):
        self.url_generate()

        #再從方向決定時刻表字典
        if self.direction == '東' or self.direction == '北':
            if self.table[0].select('tr th') != []:
                time_up = self.table_up()
            else:
                time_up = {}
            return time_up
        
        elif self.direction == "西" or self.direction == '南':        
            if self.table[1].select('tr th') != []:
                time_down = self.table_down()
            else:
                time_down = {}
            return time_down

    ###############以上是爬蟲####################


    ###############產出結果的文字####################
    def return_time_result(self):
        self.time_generate()
        table = self.table_generate()
        result_lst = []
        result_str = "現在最近的班次有:\n"

        if self.table == {}:
            return "該站沒有該方向，請確認後重新查詢"
        else:
            for i in table:
                if self.now < i:
                    result_lst.append(i)

            for i in range(5):
                try:
                    result_str += str(result_lst[i].strftime('%H:%M')) + " "
                except IndexError:
                    break
        
            return result_str
