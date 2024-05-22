import { getApplicationState, setMilkChoice } from "./ApplicationState.js"
import { settings } from "./Settings.js"


document.addEventListener("change", (event) => {
    if (event.target.name === "size") {
        setMilkChoice(parseInt(event.target.value))
    }
})

export const Milks = async () => {
    try {
        const response = await fetch(`${settings.remoteURL}/milks`)
        if (response.status !== 200) {
            return "<h3>Could not load milks</h3>"
        }
        const milks = await response.json()
        const currentUserChoices = getApplicationState()

        let html = `
            <ul>
            ${
                milks.map(milk => {
                    return `<li>
                        <input type="radio"
                            ${currentUserChoices.milk === milk.id ? "checked" : ""}
                            name="milk" value="${milk.id}" /> ${milk.type}
                    </li>`
                }).join("")
            }
            </ul>
        `

        return html

    } catch (error) {
        return "<h3>Could not load milks</h3>"
    }
}
