import { addCustomOrder, getApplicationState } from "./ApplicationState.js"
import { Flavors } from "./Flavors.js"
import { Milks } from "./Milks.js"
import { Orders } from "./Orders.js"
import { CoffeeCupSizes } from "./Sizes.js"

document.addEventListener("click", async (event)  => {
    if (event.target.id === "orderButton") {
        addCustomOrder()
    }
})


export const CustomCoffee = async () => {
    const flavorBoxes = await Flavors()
    const sizeChoices = await CoffeeCupSizes()
    const milkChoices = await Milks()
    const placedOrders = await Orders()


    return `
        <h1>Custom Coffee Cup Company Incorporated</h1>

        <article class="choices">
            <section class="choices__sizes options">
                <h2>Sizes</h2>
                ${sizeChoices}
            </section>
            <section class="choices__flavors options">
                <h2>Flavors</h2>
                ${flavorBoxes}
            </section>
            <section class="choices__milks options">
                <h2>Milks</h2>
                ${milkChoices}
            </section>
        </article>

        <article>
            <button id="orderButton">Order Your Custom Cup of Coffee</button>
        </article>

        <article class="customOrders">
            <h2>Custom Coffee Cup Orders</h2>
            ${placedOrders}
        </article>
    `
}
