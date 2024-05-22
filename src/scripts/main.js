import { getApplicationState } from "./ApplicationState.js"
import { CustomCoffee } from "./CustomCoffee.js"

const mainContainer = document.querySelector("#container")

document.addEventListener("stateChanged", async () => {
    const currentState = getApplicationState()
    console.log(currentState)

    const newHTML = await CustomCoffee()
    mainContainer.innerHTML = newHTML

})

document.dispatchEvent(new CustomEvent("stateChanged"))