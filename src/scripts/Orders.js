import { settings } from "./Settings.js"

export const Orders = async () => {
    try {
        const orders = await fetch(`${settings.remoteURL}/orders?_expand=milk&_expand=size`)
            .then(res => res.json())
        if (response.status !== 200) {
            return "<h3>Could not load milks</h3>"
        }
    } catch (error) {
        return "<h3>Could not load Orders</h3>"
    }


    let html = orders.map((order) => {
        let totalCost = order.milk.price + order.size.price

        return `<div>Order #${order.id} costs ${totalCost.toLocaleString("en-US", {
            style: "currency",
            currency: "USD"
        })}</div>`
    })

    html = html.join("")

    return html
}
