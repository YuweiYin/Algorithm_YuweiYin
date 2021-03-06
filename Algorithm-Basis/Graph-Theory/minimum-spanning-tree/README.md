# Algorithm - Graph Theory

Algorithm - [YuweiYin](https://github.com/YuweiYin)

**Minimum Spanning Tree**

## 目录

- 最小生成树 MST
	- [Prim 算法](./mst-prim)
	- [Kruskal 算法](./mst-kruskal)
	- Sollin 算法
	- 次优最小生成树
	- 第 k 小生成树
	- 瓶颈生成树
	- 最优比例生成树
	- 最小树形图
	- 最小度限制生成树
	- 平面点的欧几里德最小生成树
	- 平面点的曼哈顿最小生成树
	- 最小平衡生成树

## 最小生成树 MST

最小生成树 (Minimum Spanning Tree, MST)

### MST 问题引入

在电子电路设计中，常常需要将多个组件的针脚连接在一起。要连接 n 个针脚，可以使用 n-1 根连线。每根连线连接两个针脚。目标是让所使用的连线长度最短。

可以将上述布线问题用一个带边权的连通无向图 G = (V, E) 来表示，这里 V 是针脚的集合，E 是针脚之间的可能连接。并且对于每条边 (u, v) \in E，为其赋予权重 w(u, v) 作为连接针脚 u 和针脚 v 的代价（也就是连线的长度）。目标是找到一个无环子集 $ T \subseteq E $，既能够将所有的结点(针脚)连接起来，又具有最小的权重，即求和 $ w(T) = \sum_{(u, v) \in T} w(u, v) $ 的值最小。

由于 T 是无环的，并且连通所有的结点，因此 T 必然是一棵树，被称为(图 G 的)**生成树**。如果 w(T) 是最小(极小)的，那么这棵树是一棵**最小生成树**，可能不唯一。

![mst-1](/img/info-technology/algorithm/graph-theory/minimum-spanning-tree/mst-1.png)

解决最小生成树问题的两种常用算法为：Kruskal 算法和 Prim 算法。如果使用普通的[二叉堆](../../data-structure/heap-priority-queue)，那么可以将这两个算法的时间复杂度限制在 `O(|E| log |V|)` 的数量级内。如果使用[斐波那契堆](../../data-structure/fibonacci-heap)，Prim 算法的运行时间将改善为 `O(|E| + |V| log |V|)`，此运行时间在结点数 `|V|` 远远小于边数 `|E|` 的情况下较好（即稠密图）。

这两种算法都是[贪心算法](../../greedy-algorithm/)。贪心算法的每一步都要在多个可能的选择中选择当前最优的一个，这种策略并不一定保证在所有问题中都能获得最优解，但是对于 MST 问题来说，可以证明：某些贪心策略确实能够找到一棵总权重 w(T) 最小的生成树。

### 最小生成树的形成

假定一个连通无向图 G(V, E) 和权重函数 `w: E->R`，希望找出图 G 的一棵最小生成树。贪心策略在每个时刻生长 MST 的一条边，并在整个策略的实施过程中，管理一个遵守下述循环不变式的边集合 A：

在每遍循环之前，A 是某棵最小生成树的一个子集。

在每一步，需要做的是选择一条边 (u, v)，将其加入到集合 A 中，使得 A 不违反循环不变式，即 $ A \cup {(u, v)} $ 也是某棵最小生成树的子集。由于可以安全地将这种边加入到集合 A 而不会破坏 A 的循环不变式，因此称这样的边为集合 A 的**安全边**。如下伪代码给出了一个通用的模式：

```
GENERIC_MST(G, w)
1  A = \emptyset
2  while A does not form a spanning tree
3      find an edge(u, v) that is safe for A
4      A = A \cup {(u, v)}
5  return A
```

此算法的关键之处（贪心选择性质）是第 3 行能够“安全”地选择一条边加入。因此需要有辨认安全边的规则，引出此规则前，给出一些定义。无向图 G = (V, E) 的一个**切割** (S, V-S) 是集合 V 的一个划分，如果一条边 (u, v) \in E 的一个端点位于集合 S，而另一个端点位于集合 V-S，则称该条边**横跨**切割 (S, V-S)。如果集合 A 中不存在横跨该切割的边，则称该切割**尊重**集合 A。

在横跨一个切割的所有边中，权重最小的边称为**轻量级边**。轻量级边可能不是唯一的，一般而言，如果一条边是满足某个性质的所有边中权重最小的，则称该条边是满足给定性质的一条轻量级边。

![mst-2](/img/info-technology/algorithm/graph-theory/minimum-spanning-tree/mst-2.png)

用来辨认安全边的规则由下面的定理给出：

《CLRS》**定理 23.1**：设 G = (V, E) 是一个在边集 E 上定义了实数值权重函数 w 的连通无向图。设集合 A 为 E 的一个子集，且 A 包括在图 G 的某棵最小生成树中，设 (S, V-S) 是图 G 中尊重集合 A 的任意一个切割，又设 (u, v) 是横跨切割 (S, V-S) 的一条轻量级边。那么边 (u, v) 对于集合 A 是安全的。

![mst-3](/img/info-technology/algorithm/graph-theory/minimum-spanning-tree/mst-3.png)

定理 23.1 表明，随着算法 `GENERIC_MST` 的推进，集合 A 总是保持在无环状态。在算法执行的任意时刻，图 GA = (V, A) 是一个森林，GA 中的每个连通分量则是一棵树。而且由于 $ A \cup {(u, v)} $ 必须是无环的，所有对于集合 A 为安全的边 (u, v) 所连接的是 GA 中不同的连通分量。

算法 `GENERIC_MST` 的第 2～4 行的 while 循环总共执行 `|V| - 1` 次，因为每遍循环的都要找出 `|V| - 1` 条边中的一条。在初始时，当 A 为空集时，GA 中有 `|V|` 棵树，每遍循环将树的数量减少 1 棵。当整个森林仅包含一棵树时，该算法就终止。

《CLRS》**推论 23.2**：设 G = (V, E) 是一个连通无向图，并有定义在边集合 E 上的实数值权重函数 w。设集合 A 为 E 的一个子集，且该子集包括在 G 的某棵最小生成树里，并设 C = (VC, EC) 为森林 GA = (V, A) 中的一个连通分量(树)。如果边 (u, v) 是连接 C 和 GA 中某个其它连通分量的一条轻量级边，则边 (u, v) 对于集合 A 是安全的。

- 在 Kruskal 算法中，集合 A 是一个森林，其结点就是给定图的结点。每个加入到集合 A 中的安全边 永远是**权重最小**的**连接两个不同分量的边**。
- 在 Prim 算法中，集合 A 则是一棵树。每次加入到 A 中的安全边永远是**连接 A 和 A 之外某个结点**的边中 **权重最小的边**。

## 参考资料

- Introduction to Algorithm (aka CLRS) Third Edition - Chapter 23
