import '../styles/Cart.css'

function Cart(){

    const monsteraPrice = 8
    const ivyPrice = 10
    const flowerPrice = 15

    return (
        <div className="lmj-cart">
            <h2>Panier</h2>
            <ul>
                <li>Monstera : {monsteraPrice}</li>
                <li>Lierre: {ivyPrice}</li>
                <li>Fleurs: {flowerPrice}</li>
            </ul>
        </div>
    )

}

export default Cart