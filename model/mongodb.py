from pymongo import MongoClient
import datetime


#dbname = "howard-good31"


class site_record:
    ##########連接並建立資料庫############
    def __init__(self):
        client = MongoClient("mongodb://kiwi:410531118morris@ac-hclae5s-shard-00-00.kfjeisg.mongodb.net:27017,ac-hclae5s-shard-00-01.kfjeisg.mongodb.net:27017,ac-hclae5s-shard-00-02.kfjeisg.mongodb.net:27017/?ssl=true&replicaSet=atlas-6bpxdc-shard-0&authSource=admin&retryWrites=true&w=majority")
        kiwiDB = "MRT_line_bot"
        kiwiDF = "MRT_dataframe"
        self.db = client[kiwiDB]  #db就是一個資料庫
        self.collect = self.db[kiwiDF]  #collect就是一個資料表
        
        
    ###########新增儲存點############
    def add_todo(self, user_name, user_id, site, abstract):
        now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
        pattern = re.compile(r'(?P<city>[^縣市]+[縣市])(?P<zone>[^縣市區鄉鎮]+[縣市區鄉鎮])')
        city = match.group('city')
        zone = match.group('zone')
        i = 1
        is_exis = True
        return "進到mongo"
        # if self.collect.find_one({"user_id" : user_id, "site" : site}):
        #     content = "這個點被存過囉，請確認後重新嘗試！"
        #     return content
        # while is_exis:
        #     is_exis = self.collect.find_one({"user_id" : user_id, "site_number" : i})
        #     i += 1
        # i -= 1
        # self.collect.insert_one(
        #     {"user_id" : user_id,
        #     "user_name" : user_name,
        #     "site_number" : i,
        #     "site" : site,
        #     "city" : city,
        #     "zone" : zone,
        #     "abstract" : abstract,
        #     "create_time" : now.strftime('%Y/%m/%d %H:%M:%S')
        # }
        # )
        # content = "地點儲存成功"
        # return content


#########################################檢視資料########################################################

    ##########檢視儲存點(全部)###########
    def display_all(self, user_id):
        all_lst = [self.collect.find({"user_id" : user_id})]
        for i in len(all_lst):
            content += f'儲存點{all_lst[i]["site_number"]}\n地址:{all_lst[i]["site"]}\n摘要:{all_lst[i]["abstract"]}\n建立時間:{all_lst[i]["create_time"]}\n\n'
            content = content.rstrip('\n\n')
        return content
    ##########檢視儲存點(按城市)###########
    def display_city(self, user_id, city):
        all_lst = [self.collect.find({"user_id" : user_id, "city" : city})]
        for i in len(all_lst):
            content += f'儲存點{all_lst[i]["site_number"]}\n地址:{all_lst[i]["site"]}\n摘要:{all_lst[i]["abstract"]}\n建立時間:{all_lst[i]["create_time"]}\n\n'
            content = content.rstrip('\n\n')
        return content
    ##########檢視儲存點(按區)###########
    def display_zone(self, user_id, zone):
        all_lst = [self.collect.find({"user_id" : user_id, "zone" : zone})]
        for i in len(all_lst):
            content += f'儲存點{all_lst[i]["site_number"]}\n地址:{all_lst[i]["site"]}\n摘要:{all_lst[i]["abstract"]}\n建立時間:{all_lst[i]["create_time"]}\n\n'
            content = content.rstrip('\n\n')
        return content


#########################################刪除資料########################################################

    ##########刪除儲存點(指定號碼)###########
    def delete_number(self, user_id, site_number):
        if self.collect.find_one({"user_id" : user_id, "site_number": site_number}):
            self.collect.delete_one({"user_id" : user_id, "site_number" : site_number})
            content = f"儲存點{site_number}刪除成功"
            return content
        else:
            content = f"找不到儲存點{site_number}，請重新嘗試！"
            return content
    ##########刪除儲存點(指定城市)###########
    def delete_city(self, user_id, city):
        if self.collect.find_one({"user_id" : user_id, "city": city}):
            delete_count = self.collect.delete_many({"user_id" : user_id, "city" : city})
            content = f"{delete_count.delete_count}個{city}的儲存點已刪除成功"
            return content
        else:
            content = f"找不到{city}的儲存點，請重新嘗試！"
            return content
    ##########刪除儲存點(指定區)###########
    def delete_zone(self, user_id, zone):
        if self.collect.find_one({"user_id" : user_id, "zone": zone}):
            delete_count = self.collect.delete_many({"user_id" : user_id, "zone" : zone})
            content = f"{delete_count.delete_count}個{zone}的儲存點已刪除成功"
            return content
        else:
            content = f"找不到{zone}的儲存點，請重新嘗試！"
            return content
    ##########清空儲存點###########
    def delete_all(self, user_id):
        if self.collect.find_one({"user_id" : user_id}):
            delete_count = self.collect.delete_many({"user_id" : user_id})
            content = f"您的的儲存點已刪除成功"
            return content
        else:
            content = f"找不到您的儲存點，請重新嘗試！"
            return content