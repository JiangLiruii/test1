__Author__ = "Panda-J"

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [lambda x, y: (x + 1, y),
		lambda x, y: (x, y + 1),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y - 1),
        ]

def map_path(x1,y1,x2,y2):
	stack=[]
	stack.append((x1,y1))#添加起始点
	while len(stack)> 0:    #如果栈中有数据的话
		curNode=stack[-1]   #取最外面一个栈值
		if curNode[0]==x2 and curNode[1]==y2:   #如果到达终点
			print('found path')
			for p in stack:
				print(p)
			return True
		for dir in dirs:    #循环四个方向，注意优先级
			nextNode=dir(curNode[0],curNode[1]) #定义下一个点
			if maze[nextNode[0]][nextNode[1]]==0:   #如果下一个点可以走通
				stack.append(nextNode)  #添加进栈中
				maze[nextNode[0]][nextNode[1]] = -1 #改变值使不重复添加
				break
		else:
			stack.pop()
	print('found failed')
	return False

map_path(1,1,8,8)

