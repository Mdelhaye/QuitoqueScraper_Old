// Script to check if recipe or help category is not available
function checkRecipeAvailability(xpath) {
    try {
        if (document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue !== null) {
            return { success: false, message: 'Recipe unavailable!' };
        }
        return { success: true, message: 'Recipe available' };
    } catch (error) {
        console.error('Error in ' + checkRecipeAvailability.name + ' function:', error);
        return { success: false, message: 'Error in checkRecipeAvailability function: ' + error};
    }
}

function checkHelpCategoryAvailability(xpath) {
    try {
        if (document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue !== null) {
            return { success: false, message: 'Help category available!' };
        }
        return { success: true, message: 'Help category unavailable' };
    } catch (error) {
        console.error('Error in ' + checkHelpCategoryAvailability.name + ' function:', error);
        return { success: false, message: 'Error in checkHelpCategoryAvailability function: ' + error};
    }
}

function checkAvailability(xpaths) {
    try {
        if (!Array.isArray(xpaths) || xpaths.length < 2) {
            return { success: false, message: 'Insufficient or invalid XPaths provided!' };
        }

        let recipeCheck = checkRecipeAvailability(xpaths[0]);
        if (!recipeCheck.success) {
            return recipeCheck; 
        }

        let helpCategoryCheck = checkHelpCategoryAvailability(xpaths[1]);
        if (!helpCategoryCheck.success) {
            return helpCategoryCheck; 
        }
    } catch (error) {
        console.error('Error in ' + checkAvailability.name + ' function:', error);
        return { success: false, message: 'Error in checkAvailability function: ' + error};
    }

    return { success: true, message: 'Elements checked successfully!' };
}
