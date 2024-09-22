
import { useState } from "react";
//import { Link } from "react-router-dom";<Link to="/login">Already have an account? Login</Link>
import { useAppDispatch } from  "../hooks/redux-hooks" ; 
import { register } from "../slices/authSlice";

function SignUp()
{
    const dispatch = useAppDispatch();
    
    const [username, setUsername] = useState<string>("");
    const [first_name, setFirst_name] = useState<string>("");
    const [last_name, setLast_name] = useState<string>("");
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const handleRegister = async () => {

        if (username && first_name && last_name && email && password) {
            try {
              await dispatch(register({username,first_name,last_name,email,password,})
              ).unwrap();
            } catch (e) {
              console.error(e);
            }
          } else {
            // Afficher un message d'erreur.
          }
    };

    return (
        <div>
            <input type="text" value={first_name} placeholder="First Name" onChange={(e) => setFirst_name(e.target.value)} />
             <input type="text" value={last_name} placeholder="Last Name" onChange={(e) => setLast_name(e.target.value)} />
             <input type="text" value={username} placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
            <input type="email" value={email} placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
            <input type="password" value={password} placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
            <button type="submit" onClick={handleRegister}> Submit </button>
        </div>
    )
}

export default SignUp