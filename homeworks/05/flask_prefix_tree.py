from flask import Flask, request, render_template
import json

app = Flask(__name__)
#структура дерева такова, что в каждой конечной ячейке слова хранится слово целиком
#это сделано для того, чтобы упростить себе ЗЫЗНЬ. иначе не собирать его снизу вверх.
class Node:
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = dict()
    
    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key
    
    def __getitem__(self, key):
        return self.children[key]

class PrefixTree:
    def __init__(self):
        self.head = Node()
    
    def __getitem__(self, key):
        return self.head.children[key]
    
    def add(self, string):
        now = self.head
        finish = True
        for i in range(len(string)):
            if string[i] in now.children:
                now = now.children[string[i]]
            else:
                finished = False
                break
        if not finished:
            while i < len(string):
                now.addChild(string[i])
                now = now.children[string[i]]
                i += 1
        now.data = string
    
    def check(self, string):
        if string == '':
            return False
        if string == None:
            raise ValueError('Trie.check requires a not-Null string')
        now = self.head
        exists = True
        for letter in string:
            if letter in now.children:
                now = now.children[letter]
            else:
                exists = False
                break
        if exists:
            if now.data == None:
                exists = False
        return exists
    
    def check_part(self,string):
        if string == '':
            return False
        if string == None:
            raise ValueError('Trie.check_part requires a not-Null string')
        now= self.head
        exists = True
        for letter in string:
            if letter in now.children:
                now = now.children[letter]
            else:
                exists = False
                break
        return exists
    
    def getTop10(self, prefix):
        prefix = prefix.lower()
        ptr = list()
        if prefix == None:
            raise ValueError('Requires not-Null prefix')
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else: 
                return ptr
        if top_node == self.head:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]
        while queue:
            now = queue.pop()
            if now.data != None:
                ptr.append(now.data)
            queue = [node for key,node in now.children.items()] + queue
            
        nums = []
        for word in ptr:
            nums.append(int(word[len(word)-3:len(word)]))
        for i in range(0, len(nums)):
            flag = 0
            for j in range(0,len(nums)-1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    ptr[j], ptr[j + 1] = ptr[j + 1], ptr[j]
                    flag = 1
            if flag == 0:
                break
        result = []
        i = 0
        for word in ptr: 
            i += 1
            if i > 10:
                break
            result.append(ptr[i - 1][0:len(ptr[i - 1]) - 3])
        return result
    #TODO реализация класса prefix tree, методы как на лекции + метод дать топ 10 продолжений. Скажем на строку кросс выдаем кроссовки, кроссовочки итп. Как хранить топ? 
    #В терминальных (конечных) нодах может лежать json с топ актерами.
tree=PrefixTree()
def init_prefix_tree(filename, tr):
    file = open(filename, 'r')
    i = 1
    w = str()
    for line in file:
        w = '0'
        if i < 10:
            w += '0'
        w += str(i)
        if i > 99:
            w = str(i)
        aline = line.lower().replace('\xa0x', ' X').replace('ё', 'е')[:len(line)-1]
        aline += w
        tr.add(aline)
        i += 1

init_prefix_tree('movies.txt', tree)
tree.getTop10('п')

@app.route("/get_sudgest/<string>", methods=['GET', 'POST'])
def return_sudgest(string):
    #TODO по запросу string вернуть json, c топ-10 саджестами, и значениями из нод
    list_ = tree.getTop10(string)
    result = '<br><u>САМЫЕ ТОПОВЫЕ ФИЛЬМЫ ОВЕР ВСЕ ВРЕМЕНА по запросу </u> <b>' + string + '</b>:<br>'
    for item in list_:
        result += '<br>'
        result += item
    result += '<br>'
    return json.dumps(result, ensure_ascii = False)
@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
     return render_template("notes.html")

if __name__ == "__main__":
    app.run()
