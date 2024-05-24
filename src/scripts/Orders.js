import { settings } from "./Settings.js"

export const Orders = async () => {
    let orders = []
    try {
        const response = await fetch(`${settings.remoteURL}/orders?_expand=milk&_expand=size&_expand=flavors`)
        if (response.status !== 200) {
            return "<h3>Could not load orders</h3>"
        }

        orders = await response.json()
    } catch (error) {
        return "<h3>Could not load Orders</h3>"
    }


    let html = orders.map(
        (order) => {
            let totalCost = 0
            try {
                totalCost = order.milk.price + order.size.price
                totalCost += order.flavors.reduce( (total, flavor) => total + flavor.price, totalCost )
                totalCost = totalCost.toLocaleString("en-US", { style: "currency", currency: "USD" })
            } catch (error) {
                totalCost = "check your receipt"
            }

            return `<div>Order #${order.id} costs ${totalCost}</div>`
        }
    ).join("")

    return html
}
