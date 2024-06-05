// Script to add people by clicking button until number reaches 4
function addPersons(xpathForButton) {
    try {
        function extractDigits(str) {
            let matches = str.match(/\d+/g);
            return matches ? matches.map(Number) : [];
        }

        let button = document.evaluate(xpathForButton, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
        while (extractDigits(button.singleNodeValue.parentNode.textContent)[0] < 4) {
            button.singleNodeValue.click();
        }
        return { success: true, message: 'Persons added successfully!' };
    } catch (error) {
        console.error('Error in ' + addPersons.name + ' function:', error);
        return { success: false, message: 'Error in addPersons function!' };
    }
}