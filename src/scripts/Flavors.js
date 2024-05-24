import { getApplicationState, updateFlavors } from "./ApplicationState.js"
import { settings } from "./Settings.js"

document.addEventListener("change", (event) => {
    if (event.target.name === "flavor") {
        updateFlavors(parseInt(event.target.value))
    }
})

export const Flavors = async () => {
    try {
        const response = await fetch(`${settings.remoteURL}/flavors`)
        if (response.status !== 200) {
            return "<h3>Could not load flavors</h3>"
        }
        const flavors = await response.json()
        const currentUserChoices = getApplicationState()

        let html = "<ul>"

        const listItems = flavors.map(flavor => {
            return `<li>
                <input type="checkbox"
                    ${currentUserChoices.flavors.has(flavor.FlavorId) ? "checked" : ""}
                    name="flavor" value="${flavor.FlavorId}" /> ${flavor.Description}
            </li>`
        })

        html += listItems.join("")
        html += "</ul>"
        return html

    } catch (error) {
        return "<h3>Could not load flavors</h3>"
    }

}

