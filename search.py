# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class Node:
    def __init__(self, state, path = [], priority = 0):
        self.state = state
        self.path = path 
        self.priority = priority # This is for the priority_queue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        # util.raiseNotDefined()
        return

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        # util.raiseNotDefined()
        return

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        # util.raiseNotDefined()
        return 

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        # util.raiseNotDefined()
        return 


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    stack.push(Node(problem.getStartState()))
    visited = []
    while not stack.isEmpty():
        # get the first node in the stack. LIFO
        cur_node = stack.pop()
        # check whether this node is visited, if visited, jump to next node
        if cur_node.state in visited:
            continue
        # if not visited, label this node as visited
        visited.append(cur_node.state)
        # print([x.state for x in visited])
        # print()
        if problem.isGoalState(cur_node.state):
            return cur_node.path
        # for all available children in the search graph, set their path as current node + it and push it into stack
        children = problem.getSuccessors(cur_node.state) # For a given state, children is a list of triples, (successor, action, stepCost)
        for child in children:
            if child[0] not in visited:
                stack.push(Node(child[0], cur_node.path+[child[1]]))
            
    

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    """return a path to the goal state"""
    "*** YOUR CODE HERE ***"
    
    queue = util.Queue()
    queue.push(Node(problem.getStartState()))
    visited = []
    while not queue.isEmpty():
        # get the first node in the stack. LIFO
        cur_node = queue.pop()
        # check whether visited
        # if cur_node in visited: 
        #     continue
        if cur_node.state in visited:
            continue
        visited.append(cur_node.state)
        if problem.isGoalState(cur_node.state):
            # print(cur_node.path)
            return cur_node.path
        # get all available children
        # print(problem.getSuccessors(cur_node.state))
        children = problem.getSuccessors(cur_node.state) # For a given state, children is a list of triples, (successor, action, stepCost)
        for child in children:
            if child[0] not in visited:
                queue.push(Node(child[0],cur_node.path+[child[1]]))
        

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    heap = util.PriorityQueue()
    heap.push(Node(problem.getStartState(), path = [], priority = 0), priority = 0)
    visited = []
    while not heap.isEmpty():
        cur_node = heap.pop()
        if cur_node.state in visited:
            continue
        visited.append(cur_node.state)
        if problem.isGoalState(cur_node.state):
            return cur_node.path
        children = problem.getSuccessors(cur_node.state)
        # children is a list of triples, (successor, action, stepCost)
        for child in children:
            heap.update(Node(child[0],cur_node.path+[child[1]], cur_node.priority+child[2]), cur_node.priority+child[2])
    
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # A* algo uses the heap structure too, but it is conducted with a heristic
    # Actually A* is quite like UnifromSearch
    result = []
    heap = util.PriorityQueue()
    heap.push(Node(problem.getStartState(), path = [], priority = 0), priority = 0)
    visited = [] # A list to store state. Think: can the elements of this list be the nodes rather than states?
    while not heap.isEmpty():
        cur_node = heap.pop()
        if cur_node.state in visited:
            continue
        visited.append(cur_node.state)
        if problem.isGoalState(cur_node.state):
            result = cur_node.path
            break
        children = problem.getSuccessors(cur_node.state)
        for child in children:
            heap.update(Node(child[0], cur_node.path+[child[1]], cur_node.priority+child[2]), priority=(heuristic(child[0], problem) + cur_node.priority +child[2] ))
    return result
        
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
