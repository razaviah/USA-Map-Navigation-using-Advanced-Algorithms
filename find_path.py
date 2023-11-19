import networkx as nx
import matplotlib.pyplot as plt
import heapq
import queue
import sys





def readGraphData (file_name):
	with open(file_name) as f:
		G = nx.Graph()
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			if line=="END":
				break
			data = line.split(" ")

			if data[0] not in list(G):
				G.add_node(data[0])
			if data[1] not in list(G):
				G.add_node(data[1])
			G.add_edge(data[0], data[1], weight=data[2])
	return G


def readHeuristicData (file_name):
	with open(file_name) as f:
		h = {}
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			if line=="END":
				break
			data = line.split(" ")
			h[data[0]] = data[1]
	return h



def UCS (source_node, destination_node, G):
	frontier = []
	explored = set()
	paths = {source_node:source_node}
	heapq.heappush(frontier, (0, source_node))
	counter = 0
	while True:
		counter = counter + 1
		if frontier==[]:
			return (-1, "")
		if counter != 1:
			prevNode = node
		node = heapq.heappop(frontier)
		explored.add(node[1])
		if node[1] == destination_node:
			return(node[0], paths[node[1]])
		for child in G.neighbors(node[1]):
			childInFrontier = False
			pathCostChild = 0
			if (child not in explored):
				
				for e in frontier:
					if e[1] == child:
						childInFrontier = True
						pathCostChild = e[0]

				if childInFrontier == False:
					heapq.heappush(frontier, ((int(G[node[1]][child]["weight"]) + node[0]), child))
					paths[child] = paths[node[1]] + " " + child
			
			if (childInFrontier == True) and ((int(G[node[1]][child]["weight"]) + node[0]) < pathCostChild):
				frontierClone = []
				for i in range(len(frontier)):
					n = heapq.heappop(frontier)
					if n == (pathCostChild, child):
						heapq.heappush(frontierClone, (int(G[node[1]][child]["weight"]) + node[0], child))
						paths[child] = paths[node[1]] + " " + child
					else:
						heapq.heappush(frontierClone, n)
				frontier = frontierClone








def BFS (source_node, destination_node, G):
	node = source_node
	paths = {node:[0, node]}
	if node == destination_node:
		return (0, [paths[node]])
	frontier = queue.Queue()
	frontier.put(node)
	frontierLen = 1
	explored = set()
	while True:
		if frontier.empty():
			return (-1, "")
		node = frontier.get()
		frontierLen = frontierLen - 1
		explored.add(node)
		for child in G.neighbors(node):
			childInFrontier = False
			frontierClone = queue.Queue()
			for i in range(frontierLen):
				e = frontier.get()
				if  e == child:
					childInFrontier = True
				frontierClone.put(e)
				if i == (frontierLen-1):
					frontier = frontierClone
			if (child not in explored) and childInFrontier == False:
				if child == destination_node:
					return (paths[node][0] + int(G[node][child]["weight"]), paths[node][1] + " " + child)
				frontier.put(child)
				frontierLen = frontierLen + 1
				paths[child] = [int, str]
				paths[child][0] = paths[node][0] + int(G[node][child]["weight"])
				paths[child][1] = paths[node][1] + " " + child




def DFS (source_node, destination_node, G):
	stack = queue.LifoQueue()
	explored = set()
	stack.put(source_node)
	paths = {source_node:[0, source_node]}
	parentDict = {}
	while True:
		if stack.empty():
			return (-1, "")
		node = stack.get()
		if node in explored:
			continue
		if node == destination_node:
			parentNode = parentDict[node]
			return (paths[parentNode][0] + int(G[node][parentNode]["weight"]), paths[parentNode][1] + " " + node)
		explored.add(node)
		for child in G.neighbors(node):
			if not (child in explored):
				stack.put(child)
				paths[child] = [int, str]
				paths[child][0] = paths[node][0] + int(G[node][child]["weight"])
				paths[child][1] = paths[node][1] + " " + child
				parentDict[child] = node
	




def AStar (source_node, destination_node, h, G):
	frontier = []
	explored = set()
	paths = {source_node:source_node}
	heapq.heappush(frontier, (int(h[source_node]), source_node))
	counter = 0
	resultPath = ""
	while True:
		counter = counter + 1
		if frontier==[]:
			return (-1, "")
		if counter != 1:
			prevNode = node
		node = heapq.heappop(frontier)
		explored.add(node[1])
		if node[1] == destination_node:
			#resultPath = paths[node[1]]
			#break
			return(node[0], paths[node[1]])
		for child in G.neighbors(node[1]):
			childInFrontier = False
			pathAstarChild = 0
			if (child not in explored):
				
				for e in frontier:
					if e[1] == child:
						childInFrontier = True
						pathAstarChild = e[0]

				if childInFrontier == False:
					heapq.heappush(frontier, ((int(G[node[1]][child]["weight"]) + node[0] + int(h[child]) - int(h[node[1]])), child))
					paths[child] = paths[node[1]] + " " + child
			
			if (childInFrontier == True) and ((int(G[node[1]][child]["weight"]) + node[0] + int(h[child]) - int(h[node[1]])) < pathAstarChild):
				frontierClone = []
				for i in range(len(frontier)):
					n = heapq.heappop(frontier)
					if n == (pathAstarChild, child):
						heapq.heappush(frontierClone, (int(G[node[1]][child]["weight"]) + node[0] + int(h[child]) - int(h[node[1]]), child))
						paths[child] = paths[node[1]] + " " + child
					else:
						heapq.heappush(frontierClone, n)
				frontier = frontierClone


	

def main():
	# args = ["script.py", "ucs/bfs/dfs/astar", "input_file.txt","source_node", "destination_node", "heuristics.txt"]
	args = sys.argv
	G = readGraphData(args[2])
	if args[1] == "ucs":
		(cost, resultPath) = UCS(args[3], args[4], G)

	elif args[1] == "bfs":
		(cost, resultPath) = BFS(args[3], args[4], G)

	elif args[1] == "dfs":
		(cost, resultPath) = DFS(args[3], args[4], G)

	elif args[1] == "astar":
		h= readHeuristicData (args[5])
		(cost, resultPath) = AStar(args[3], args[4], h, G)

	else:
		print("argv[1] should be one of 'ucs', 'bfs', 'dfs' or 'astar'")
	if cost == -1:
		print("distance: infinity")
		print("path:")
		print("none")
	else:
		print("distance: %d mi" % cost)
		print("path:")
		cities = resultPath.split(" ")
		for i in range(len(cities)):
			if i != 0:
				print("%s to %s: %d mi" % (cities[i-1], cities[i], int(G[cities[i-1]][cities[i]]["weight"])))


main()