// Script to delete and click on items based on XPaths and clues given
function manipulateElements(itemsToRemove, indicesToRemove, itemsToClick, indicesToClick) {
    try {
        if (!Array.isArray(itemsToRemove) || itemsToRemove.length < 1 ||
            !Array.isArray(indicesToRemove) || indicesToRemove.length < 1 ||
            !Array.isArray(itemsToClick) || itemsToClick.length < 1 ||
            !Array.isArray(indicesToClick) || indicesToClick.length < 1) {
            return { success: false, message: 'Insufficient or invalid XPaths provided!' };
        }
        
        // Function to handle removing elements
        function removeElements(results, indices) {
            for (let i = 0; i < indices.length; i++) {
                let element = results.snapshotItem(indices[i]);
                if (element) {
                    element.remove();
                }
            }
        }

        // Function to handle clicking elements
        function clickElements(results, indices) {
            for (let i = 0; i < indices.length; i++) {
                let element = results.snapshotItem(indices[i]);
                if (element) {
                    element.remove();
                }
            }
        }

        for (let i = 0; i < itemsToRemove.length; i++) {
            let resultsToRemove = document.evaluate(itemsToRemove[i], document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
            removeElements(resultsToRemove, indicesToRemove[i]);
        }

        for (let i = 0; i < itemsToClick.length; i++) {
            let resultsToClick = document.evaluate(itemsToClick[i], document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
            clickElements(resultsToClick, indicesToClick[i]);
        }
        
    } catch (error) {
        console.error('Error in manipulateElements function:', error);
        return { success: false, message: 'Error in manipulateElements function!' };
    }
    
    return { success: true, message: 'Elements removed/clicked successfully!' };
}
