class Item:
    def __init__(self,obj,count):
        self.bid = obj.id
        self.book_name = obj.book_name
        self.pic = obj.isbn
        self.ddprice = obj.dd_price
        self.price = obj.price
        self.allprice = self.ddprice
        self.count = count
        self.state = True
class Buycar:
    def __init__(self):
        self.items =[]
        self.allprice = 0
        self.save = 0
        self.count = 0
    def add(self,item):
        if not self.items:
            self.allprice = item.ddprice
            self.count = 1
            self.save = item.price - item.ddprice
            self.items.append(item)
        else:
            self.allprice += item.allprice
            self.count += item.count
            self.save +=item.price-item.ddprice
            for i in self.items:
                if i.bid == item.bid:
                    i.count +=1
                    i.allprice = item.ddprice * i.count
                    break
            else:
                self.items.append(item)

    def find(self,item_id):
        item_id = (item_id if isinstance(item_id, int) else int(item_id))
        for i in self.items:
            if item_id == i.bid:
                return i
        return False
    def remove(self,info_id):
        '移入回收站'
        for i in self.items:
            if i.bid == int(info_id):
                i.state = False
        self.change()

    def recover(self,info_id):
        '从回收站恢复'
        self.find(info_id).state = True
        self.change()
    def change(self):
        '内容变更，同步更新其相关信息'
        # ddprice = 0
        allprice = 0
        count = 0
        save = 0
        for i in self.items:
            if i.state:
                # dangdang_price += item.dangdang_price * item.amount  # 购物车当当价总计
                i.allprice = i.ddprice * i.count
                allprice += i.ddprice * i.count  # 原价总计
                count += i.count  # 数量总计
                save += (i.price - i.ddprice)*count
            else:
                # dangdang_price += item.dangdang_price * item.amount  # 购物车当当价总计
                i.allprice -= i.ddprice * i.count  # 原价总计
                i.count -= i.count  # 数量总计
                save -= (i.price - i.ddprice)*count
        # self.dangdang_price = dangdang_price
        self.allprice = allprice
        self.count = count
        self.save = save
    def upc(self,item_id,new_count):
        item = self.find(item_id)
        item.count = new_count
        self.change()
        return item.allprice
        # for i in self.items:
        #     if i.bid == item_id:
        #         self.allprice += item.allprice
        #         self.save += item.price - item.ddprice
        #         i.count += 1

    # def query(self):
    #     return