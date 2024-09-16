import { useState } from "react";
import { Link } from 'react-router-dom';
import '../styles/NavBar.css'

interface NavBarProps {
  navItems: string[];
  imageSrcPath: string;
  brandName: string;
}

function NavBar({navItems,imageSrcPath, brandName}: NavBarProps) {
  const [selectedIndex, setSelectedIndex] = useState(-1);
  return (
  <nav>
        <div className="navBase">
                    <a className="navbar-brand" href="/">
                      <img src={imageSrcPath} width="60" height="60" className="d-inline-block align-center"alt=""/>
                      <span className="fw-bolder fs-4">{brandName}</span>
                    </a>
                    <ul className="navbar-nav">
                        {navItems.map((items, index) => (
                        <li key={items} className="nav-item"onClick={() => setSelectedIndex(index)}>
                            <h3 > <Link className={selectedIndex == index? "nav-link active fw-bold": "nav-link"} to={items}>{items}</Link></h3>
                        </li>
                        
                        ))}
                    </ul>
                    <form className="search">
                            <input className="form-control" type="search" placeholder="Search" aria-label="Search"/>
                            <button className="btn" type="submit">Search</button>
                    </form>  
          </div>
    
    </nav>
  );
}

export default NavBar;