import {useState,  useEffect } from "react";

interface Products{
    id:number 
    categorie : string ,
    name: string, 
    price : number,
    digital: boolean,
    image: string,
    date_ajout : Date

}


function ProductsList(){
const [data, setData] = useState<Products[]>([]);

useEffect(() => {
    fetch("http://0.0.0.0:8000/monsite-api-product/productsAll")
    .then(response => response.json())
    .then(json => setData(json))
  }, []);
  console.log(data)
    return (
        <div>
            <ul>
            { data.map(({id,name, price, image} ) => ( 
                <li key={id}>
                    <h3>{name}</h3>
                    <h3>{price}</h3>
                    <img src={image} />
                </li>
            ))}
            </ul>
        </div>
    )
}

export default ProductsList



