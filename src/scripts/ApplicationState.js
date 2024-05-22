import { settings } from "./Settings.js"

let applicationState = {
    flavors: new Set(),
    size: 0,
    milk: 0,
}

export const getApplicationState = () => {
    return {...applicationState}
}

export const setSizeChoice = (chosenSizeId) => {
    applicationState.size = chosenSizeId
    document.dispatchEvent(new CustomEvent("stateChanged"))
}

export const setMilkChoice = (chosenMilkId) => {
    applicationState.milk = chosenMilkId
    document.dispatchEvent(new CustomEvent("stateChanged"))
}

export const updateFlavors = (flavorId) => {
    applicationState.flavors.has(flavorId)
        ? applicationState.flavors.delete(flavorId)
        : applicationState.flavors.add(flavorId)

    document.dispatchEvent(new CustomEvent("stateChanged"))
}

export const addCustomOrder = async () => {
    const response = await fetch(`${settings.remoteURL}/orders`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            sizeId: applicationState.size,
            milkId: applicationState.milk
        })
    })
    if (response.status === 201) {
        window.alert("You wild dawg, you. Chillax while we build that tasty custom coffee cup.")
    }
    else {
        window.alert("Sorry, fam. We can't craft that custom coffee cup right now.")
    }

    applicationState = {
        size: 0,
        flavors: new Set(),
        milk: 0
    }

    document.dispatchEvent(new CustomEvent("stateChanged"))
}
