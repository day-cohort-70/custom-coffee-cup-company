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
        <div class="header">
        <img class="coffee-cup-image" src="images/coffee-cup.png" alt="oops that should be a coffee cup image">
        <h1 class="title" >Custom Coffee Cup Company Incorporated</h1>
        </div>
        <article class="choices">
            <section class="choices__sizes options">
                <h2 class="choice_title" >Sizes</h2>
                ${sizeChoices}
            </section>
            <section class="choices__flavors options">
                <h2 class="choice_title" >Flavors</h2>
                ${flavorBoxes}
            </section>
            <section class="choices__milks options">
                <h2 class="choice_title" >Milks</h2>
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
