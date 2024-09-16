import { useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';

interface categoryById {
    id: number,
    name: string,
    description: string
    image: string,

}
 
function ShoppingListById(){
    const [data, setData] = useState<categoryById>();
    let { id } = useParams();
    useEffect(() => {
        fetch(`http://0.0.0.0:8000/monsite-api-category/categoriesById/${id}`)
        .then(response => response.json())
        .then(json => setData(json))
      });
      
    return(
        <div>
            <h2> {data?.name}</h2>
            <div>{data?.description}</div>
            <img src={data?.image} />
        </div>
        )
    }


export default ShoppingListById