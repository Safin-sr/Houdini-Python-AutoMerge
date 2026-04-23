import hou

selected_nodes = hou.selectedNodes()

if len(selected_nodes) > 1:
    target_node = selected_nodes[-1]
    input_nodes = selected_nodes[:-1]

    try:
        start_index = len(target_node.inputs())
        for i, node in enumerate(input_nodes):
            target_node.setInput(start_index + i, node)
        hou.ui.setStatusMessage(f"Added to {target_node.name()}")
    except:
        parent = target_node.parent()
        new_merge = parent.createNode("merge", "merge_auto")
        
        for i, node in enumerate(input_nodes):
            new_merge.setInput(i, node)
            
        target_node.setInput(0, new_merge)
        
        new_merge.setPosition(target_node.position() + hou.Vector2(0, 1))
        new_merge.moveToGoodPosition()
        
        hou.ui.setStatusMessage("Created Merge for multiple inputs")
else:
    hou.ui.setStatusMessage("Select source node(s) and then the target!")
