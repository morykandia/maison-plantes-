import { Link } from 'react-router-dom';
import '../styles/ShoppingList.css'
import {useState,  useEffect } from "react";

interface category  {
    id: number;
    name: string;
    description: string 
  };

function ShoppingList() {

    const [data, setData] = useState<category[]>([]);
    useEffect(() => {
        fetch("http://0.0.0.0:8000/monsite-api-category/categoriesAll/")
        .then(response => response.json())
        .then(json => setData(json))
      }, []);

    const CategoryById = (id:number) => {
        fetch(`http://0.0.0.0:8000/monsite-api-category/categoriesById/${id}`) 
        .then(response => response.json())
        .then(json => setData(json))
    }
  return (
		<div>
            <ul className='menu'>
                {data && data.map(({id,name} ) => ( 
                <li key={id}>
                    <h3><Link to ={`/categories/${id}`} onClick={()=>CategoryById(id)} >{name}</Link></h3>
                </li>
                 ))}
            </ul>
       
        
		</div>
  )
}

export default ShoppingList
