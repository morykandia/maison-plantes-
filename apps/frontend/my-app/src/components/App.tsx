//import Cart from './Cart'
import logo from '../assets/logo.png'
import ShoppingList from './ShoppingList'
import ShoppingListById from './ShoppingListById';
import ProductsList from './ProductsList';
import NavBar from './NavBar'


import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  const items = ["Produits", "Plantes", "Compte"];
  return (
    <BrowserRouter>
   
        <NavBar  navItems={items} imageSrcPath={logo} brandName={"la maison jungle"}/>
        <Routes>
            <Route  path="/Plantes"  element={<ShoppingList/>} />
            <Route path="/categories/:id" element={<ShoppingListById/>} />
            <Route  path="/Produits"  element={<ProductsList/>} />
        </Routes>
    
    </BrowserRouter>
          
    
  )
}

export default App
