import {useState} from "react";
//import { Link } from  "react-router-dom" ; <Link to="/register">Don't have an account? Register</Link>
//autoComplete="on"
import { useAppDispatch } from  "../hooks/redux-hooks" ; 
import { login } from  "../slices/authSlice" ; 

function SignIn(){

    const dispatch = useAppDispatch (); 
    const [email, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const handleLogin = async () => {
        if (email && password) { 
            try { 
                await dispatch ( login ({email, password}) 
              ). unwrap (); 
            } catch (e) { 
              console.error(e); 
            } 
          } else { 
            // Afficher un message d'erreur.
           } 
    };

    return (
        <div className="main">
            <form>
                <input type="text"  value={email} placeholder="Email" onChange={(e) => setUsername(e.target.value)} />
                <input type="password" value={password} placeholder="Password" autoComplete="on"  onChange={(e) => setPassword(e.target.value)} />
                <button type="submit" onClick={handleLogin}> Submit</button>
            </form>
        </div>
    )
}

export default SignIn