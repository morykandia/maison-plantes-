import {useState} from "react";
function SignIn(){

    const [email, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const handleLogin = () => {};

    return (
        <div className="main">
            <form>
                <input type="text"  value={email} placeholder="Email" onChange={(e) => setUsername(e.target.value)} />
                <input type="password" value={password} placeholder="Password"  onChange={(e) => setPassword(e.target.value)} />
                <button type="submit" onClick={handleLogin}> Submit</button>
            </form>
        </div>
    )
}

export default SignIn