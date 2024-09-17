import {useState} from "react";

function SignUp()
{
    const [username, setUsername] = useState<string>("");
    const [first_name, setFirst_name] = useState<string>("");
    const [last_name, setLast_name] = useState<string>("");
    const [email, setEmail] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const handleRegister = async () => {};

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