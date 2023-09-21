const originArrs = [
    { id: 1, name: 'A', parentId: 0 },
    { id: 2, name: 'B', parentId: 1 },
    { id: 3, name: 'C', parentId: 1 },
    { id: 4, name: 'D', parentId: 2 },
    { id: 5, name: 'E', parentId: 2 },
    { id: 6, name: 'F', parentId: 3 }
]
// Define the data type of the array item, including the id, name, parentId basic attributes
interface ArrayItem {
    id: number,
    name: string,
    parentId: number
}

// Define the data type of the tree node with id, name, passible child  nodes
interface TreeNode {
    id: number,
    name: string,
    children?: TreeNode[]
}

function list2Tree(arr: ArrayItem[]): TreeNode | null {
    // Used for mapping between id and TreeNode, map<key, value>, can quickly find to tree node by id, time complexity is O(1)
    const treeNode: Map<number, TreeNode> = new Map();
    let root: TreeNode | null = null;
    arr.forEach(item => {
        const { id, name, parentId } = item;
        // Define the tree node and use Map to maintain the relationship between ids and nodes
        const node: TreeNode = { id, name }
        treeNode.set(id, node);

        // Use parentId to find the parentNode
        const parentNode = treeNode.get(parentId);
        if (parentNode) {
            if (parentNode.children == null) {
                parentNode.children = [];
            }
            // Once the parent node is found, add the node converted from the current array item to the
            // list of child nodes.
            parentNode.children.push(node)
        }

        // Find the root node in the first loop, we assume that id=0 denotes the root note
        if (parentId === 0) {
            root = node;
        }
    })
    return root;
}
const resultTree = list2Tree(originArrs);
console.log(JSON.stringify(resultTree));