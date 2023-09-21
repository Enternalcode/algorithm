const arrs = [
    { id: 1, name: 'A', parentId: 0 },
    { id: 2, name: 'B', parentId: 1 },
    { id: 3, name: 'C', parentId: 1 },
    { id: 4, name: 'D', parentId: 2 },
    { id: 5, name: 'E', parentId: 2 },
    { id: 6, name: 'F', parentId: 3 }
];

function array2Tree(arrs) {
    let root = null
    const treeNode = new Map()
    arrs.forEach(item => {
        const { id, name, parentId } = item
        const node = { id, name }
        treeNode.set(id, node)

        // Search parent node by parentId
        const parentNode = treeNode.get(parentId)
        if (parentNode) {
            if (parentNode.children == null) {
                parentNode.children = []
            }
            parentNode.children.push(node)
        }
        if (parentId === 0) {
            root = node
        }
    })
    return root
}

const tree = array2Tree(arrs)
console.log(JSON.stringify(tree))