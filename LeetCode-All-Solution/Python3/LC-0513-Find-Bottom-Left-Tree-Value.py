#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""=================================================================
@Project : Algorithm_YuweiYin/LeetCode-All-Solution/Python3
@File    : LC-0513-Find-Bottom-Left-Tree-Value.py
@Author  : [YuweiYin](https://github.com/YuweiYin)
@Date    : 2022-06-22
=================================================================="""

import sys
import time
from typing import List, Optional
# import functools

"""
LeetCode - 0513 - (Medium) - Find Bottom Left Tree Value
https://leetcode.com/problems/find-bottom-left-tree-value/

Description & Requirement:
    Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
    Input: root = [2,1,3]
    Output: 1
Example 2:
    Input: root = [1,2,3,4,null,5,6,null,null,7]
    Output: 7

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -2^31 <= Node.val <= 2^31 - 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  # the left and right of leaf_node are both None

    @staticmethod
    def build_binary_tree_layer(val_list: List[int]):
        if not isinstance(val_list, list) or len(val_list) <= 0:
            return None

        node_list = []
        for v in val_list:
            if v is None:
                node_list.append(None)
            else:
                node_list.append(TreeNode(val=v))
        len_node_list = len(node_list)
        for idx, cur_node in enumerate(node_list):
            if cur_node is not None:
                cur_node_right_index = (idx + 1) << 1
                cur_node_left_index = cur_node_right_index - 1
                if cur_node_left_index < len_node_list:
                    cur_node.left = node_list[cur_node_left_index]
                if cur_node_right_index < len_node_list:
                    cur_node.right = node_list[cur_node_right_index]
        return node_list[0]  # return root_node

    @staticmethod
    def show_binary_tree_pre_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                val_list.append(cur_node.val)
                __dfs(cur_node.left)
                __dfs(cur_node.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_mid_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                val_list.append(cur_node.val)
                __dfs(cur_node.right)

        __dfs(root_node)
        return val_list

    @staticmethod
    def show_binary_tree_post_order(root_node) -> List[int]:
        val_list = []

        def __dfs(cur_node):
            if isinstance(cur_node, TreeNode):
                __dfs(cur_node.left)
                __dfs(cur_node.right)
                val_list.append(cur_node.val)

        __dfs(root_node)
        return val_list


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # exception case
        assert isinstance(root, TreeNode)
        # main method: (BFS layer traverse)
        return self._findBottomLeftValue(root)

    def _findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 83 ms, faster than 18.92% of Python3 online submissions for Find Bottom Left Tree Value.
        Memory Usage: 16.2 MB, less than 95.13% of Python3 online submissions for Find Bottom Left Tree Value.
        """
        assert isinstance(root, TreeNode)

        bfs_queue = [root]
        while len(bfs_queue) > 0:
            new_bfs_queue = []
            for node in bfs_queue:
                if isinstance(node.left, TreeNode):
                    new_bfs_queue.append(node.left)
                if isinstance(node.right, TreeNode):
                    new_bfs_queue.append(node.right)
            if len(new_bfs_queue) == 0:
                return bfs_queue[0].val
            bfs_queue = new_bfs_queue

        return root.val


def main():
    # Example 1: Output: 1
    # root = [2, 1, 3]

    # Example 2: Output: 7
    root = [1, 2, 3, 4, None, 5, 6, None, None, None, None, 7]

    root_node = TreeNode.build_binary_tree_layer(root)

    # init instance
    solution = Solution()

    # run & time
    start = time.process_time()
    ans = solution.findBottomLeftValue(root_node)
    end = time.process_time()

    # show answer
    print('\nAnswer:')
    print(ans)

    # show time consumption
    print('Running Time: %.5f ms' % ((end - start) * 1000))


if __name__ == "__main__":
    sys.exit(main())
