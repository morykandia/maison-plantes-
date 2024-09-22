//import Cart from './Cart'
import logo from '../assets/logo.png'
import ShoppingList from './ShoppingList'
import ShoppingListById from './ShoppingListById';
import ProductsList from './ProductsList';
import NavBar from './NavBar'
import Compte from './Comptes';
import { Routes, Route } from "react-router-dom";
//import DefaultLayout from '../layouts/defaultLayout';
import ProtectedLayout from '../layouts/protectedLayout';
import Home from './Home';
//<Route element={<DefaultLayout />}></Route>
function App() {
  const items = ["Produits", "Plantes", "Compte"];
  return (
    <>
        <NavBar  navItems={items} imageSrcPath={logo} brandName={"la maison jungle"}/>
        <Routes>
            <Route >
                  <Route  path="/Plantes"  element={<ShoppingList/>} />
                  <Route  path="/categories/:id" element={<ShoppingListById/>} />
                  <Route  path="/Produits"  element={<ProductsList/>} />
                  <Route path='/Compte' element={<Compte/>}/>
            </Route>
            <Route element={<ProtectedLayout />}>
                <Route path="/homeUser" element={<Home/>} />
            </Route>
        </Routes>
    
    </>
  )
}

export default App
