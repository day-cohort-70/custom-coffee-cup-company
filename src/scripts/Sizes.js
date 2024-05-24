import { getApplicationState, setSizeChoice } from "./ApplicationState.js"
import { settings } from "./Settings.js"


document.addEventListener("change", (event) => {
    if (event.target.name === "size") {
        setSizeChoice(parseInt(event.target.value))
    }
})

export const CoffeeCupSizes = async () => {
    try {
        const response = await fetch(`${settings.remoteURL}/sizes`)

        if (response.status !== 200) {
            return "<h3>Could not load coffee cup sizes</h3>"
        }
        const sizes = await response.json()
        const currentUserChoices = getApplicationState()

        let html = `
            <ul>
            ${
                sizes.map(size => {
                    return `<li>
                        <input type="radio"
                            ${currentUserChoices.size === size.SizeId ? "checked" : ""}
                            name="size" value="${size.SizeId}" /> ${size.Description}
                    </li>`
                }).join("")
            }
            </ul>
        `

        return html

    } catch (error) {
        return "<h3>Could not load coffee cup sizes</h3>"
    }
}
