# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# 
# Example 1:
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:
# 
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def make_adj_list_dir(nodes, links):
            adj_lst = {}
            for i in range(nodes):
                adj_lst[i] = []
            for link in links:
                [left, right] = link
                adj_lst[left].append(right)
            return adj_lst
        
        adj_lst = make_adj_list_dir(numCourses, prerequisites)
        rev_adj_lst = make_adj_list_dir(numCourses, [[j, i] for [i, j] in prerequisites])
        roots = set(range(numCourses))
        for node, children in adj_lst.iteritems():
            if children:
                [roots.discard(c) for c in children]
        
        top_sort = []
        for root in roots:
            stack = [root]
            while stack:
                top = stack[0]
                stack = stack[1:]
                if rev_adj_lst[top] == [] and top not in top_sort:
                    top_sort.append(top)
                
                    for c in adj_lst[top]:
                        if top not in rev_adj_lst[c]:
                            print(top, c, top_sort)
                            return False
                        rev_adj_lst[c].remove(top)
                        stack.append(c)
                
                
        print(top_sort, rev_adj_lst)
        if len(top_sort) != numCourses:
            return False
        return True
        
            
        
