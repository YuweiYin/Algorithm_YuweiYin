# Algorithm - Sort - Heap Sort

By [YuweiYin](https://yuweiyin.github.io/)

## 简介

堆排序算法 (Heap Sort)

(二叉)堆是一个数组，它可以被看成一个近似的完全二叉树：除了最后一层外，是完美二叉树（完全充满的二叉树），最后一层的结点全部靠左（但可能有奇数个）。树上的每一个结点对应数组中的一个元素。

表示堆的数组 A 包括两个属性：A.length 给出数组元素的个数，A.heap_size 表示有多少个堆元素存储在该数组中。取值范围 0 <= A.heap_size <= A.length。即：虽然数组 A[0..A.length-1] 可能都存有数据，但只有 A[0..A.heap_size-1] 中存放的是堆的有效元素。

![heap-sort-1](/img/info-technology/algorithm/sort/heap-sort-1.png)

树的根结点是数组首元素 A[0]，给定一个结点的下标 i，很容易计算得到它的父结点、左孩子和右孩子的下标：

- 计算父结点下标 `parent(i) = int(i / 2)`
- 计算左孩子下标 `left(i) = 2i`
- 计算右孩子下标`right(i) = 2i + 1`

当然，实际运算时要用移位操作代替乘除法。

二叉堆可以分为两种形式：最大堆和最小堆。

- **最大堆性质**：在最大堆中，除了根以外的所有结点 i 都要满足 `A[parent(i)] >= A[i]`。所以保证根结点最大
- **最小堆性质**：在最小堆中，除了根以外的所有结点 i 都要满足 `A[parent(i)] <= A[i]`。所以保证根结点最小

key 升序 heap-sort 使用最大堆，降序使用最小堆。

如果把堆看成一棵二叉树，定义一个堆中的结点的**高度**为该结点到叶结点最长简单路径的长度（边的数目）。故叶结点高度为 0。

由于堆是一棵近似的完全二叉树，那么包含 n 个元素的堆的高度是 O (log n)。堆上的基本操作的运行时间至多与树的高度成正比，即时间复杂度为 O(log n)。

- `build_max_heap`：构建最大堆。时间复杂度为 O(n)
- `max_heapify`：维护最大堆性质。时间复杂度为 O(log n)
- `heap_sort`：对一个数组进行原址排序。时间复杂度为 O(n log n)
- `max_heap_insert`、`max_extract_max`、`max_increase_key` 和 `max_maximum`：利用堆实现一个优先队列。各操作的时间复杂度均为 O(log n)

## 场景描述及分析

- 堆排序
	- 空间复杂度(辅助存储)：O(1)
	- 时间复杂度-平均/最好/最坏 O(n log n)
	- 算法稳定性：不稳定
	- 堆排序与(直接)插入排序的相同点在于空间原址性，只需要额外 O(1) 的辅助存储空间。
	- 堆排序与(二路)归并排序的相同点在于时间复杂度均为 O(n log n)。
	- 但堆排序是不稳定的，这跟(直接)插入排序和(二路)归并排序不同。

堆排序是个优秀的算法，但是在实际应用中，快速排序 Quick Sort 的性能一般会优于堆排序。

堆数据结构仍有许多应用，其中一个常见的应用就是**优先队列**的实现。可以用**最大堆**实现**最大优先队列**、用**最小堆**实现**最小优先队列**。

**优先队列** (Priority Queue) 是一种用来维护一组元素构成的集合 S 的数据结构，其中的每一个元素都有一个相关的值，称为**关键字** (key)。

一个最大优先队列支持以下操作：

- insert(S, x): 把元素 x 插入集合 S 中。这一操作等价于 S = S 并 {x}
- maximum(S): 返回 S 中具有最大关键字 key 的元素。
- extract_max(S): 去掉并返回 S 中的具有最大关键字 key 的元素。
- increase_key(S, x, k): 将元素 x 的关键字值增加到 k，这里假设 k 的值不小于 x 的原关键字值。

最大优先队列的应用有很多，其中一个就是在**共享计算机系统的作业调度**。最大优先队列记录将要执行的各个作业以及它们之间的**相对优先级**（或者他们的绝对优先级）。当一个作业完成或者被中断后，调度器调用 extract_max 从所有等待的作业中，**选出具有最高优先级的作业**来执行。在任何时候，调度器可以调用 insert 把一个新作业加入到队列中来。

相应地，最小优先队列支持的操作包括 insert、minimum、extract_min 和 decrease_key。最小优先队列可以被用于**基于事件驱动的模拟器**。队列中保存要模拟的时间，每个事件都有一个**发生时间**作为其关键字 key。事件必须**按照发生的时间顺序**进行模拟，因为某一事件的模拟结果可能会触发对其它事件的模拟。在每一步，模拟程序调用 extract_min 来选择下一个要模拟的事件。当一个新事件产生时，模拟器通过调用 insert 将其插入最小优先队列中。

每个元素除了有关键字 key，还应有一个**句柄** (handle) 作为资源标志符。本文实现中 Element 类中的 val 属性就可以存储句柄。

## 设计 & 细节

### 算法流程

### 实现细节

- `__init__`
- `do_sort`
- `_heap_sort`
- `build_max_heap`
- `build_min_heap`
- `_max_heapify`
- `_min_heapify`
- `get_maximum`
- `extract_max`
- `increase_key`
- `max_heap_insert`
- `get_minimum`
- `extract_min`
- `decrease_key`
- `min_heap_insert`
- `heap_insert`
- `_parent`
- `_left`
- `_right`
- `_max_exchange`
- `_min_exchange`
- `get_ele_list`
- `get_key_list`
- `get_val_list`
- `get_min_ele_list`
- `get_min_key_list`
- `get_min_val_list`
- `update_ele_list`

## 代码范例

### Python

Python 环境：Python 3.7

- **注**：
    - 排序算法的基类 Sort 和元素结构体类 Element 写法与 [此文章](./sort-base-class) 完全相同，故不在下方赘述。
    - 如果要运行此代码，则还需先将 Sort 类和 Element 类置于本代码中。
    - Element 类完全可以根据程序需求来自定义，但是需要给出该类中的 key 和 value 属性名。

[GitHub Code Link](https://github.com/YuweiYin/Code_Play/blob/master/Algorithm-Essence/sort/heap-sort.py)

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 6