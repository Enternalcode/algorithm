from typing import Dict, List, Optional
import json


class TreeNode:
    def __init__(self, id: int, name: str, children: Optional[List["TreeNode"]] = None):
        self.id = id
        self.name = name
        self.children = children or []


def list_to_tree(items: List[Dict[str, any]]) -> List[TreeNode]:
    item_map: Dict[int, TreeNode] = {}
    root_nodes: List[TreeNode] = []

    for item in items:
        node = TreeNode(item["id"], item["name"])
        item_map[node.id] = node

        parent_id = item.get("parentId")
        if parent_id == 0:
            root_nodes.append(node)
        else:
            parent_node = item_map.get(parent_id)
            if parent_node:
                if parent_node.children is None:
                    parent_node.children = []
                parent_node.children.append(node)

    return root_nodes


# Example usage:
items = [
    {"id": 1, "name": "A", "parentId": 0},
    {"id": 2, "name": "B", "parentId": 1},
    {"id": 3, "name": "C", "parentId": 1},
    {"id": 4, "name": "D", "parentId": 2},
    {"id": 5, "name": "E", "parentId": 2},
    {"id": 6, "name": "F", "parentId": 3},
]

tree = list_to_tree(items)


def print_tree(node: TreeNode, level: int = 0):
    indent = "  " * level
    print(f"{indent}- {node.name}")
    for child in node.children:
        print_tree(child, level + 1)


for root in tree:
    print(f"Root Node: {root.name}")
    print("Children:")
    for child in root.children:
        print_tree(child, 1)
    print()

