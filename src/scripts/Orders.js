import { settings } from "./Settings.js"

export const Orders = async () => {
    const orders = await fetch(`${settings.remoteURL}/orders?_expand=milk&_expand=size`).then(res => res.json())

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
