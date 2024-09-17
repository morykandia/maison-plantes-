import "../styles/Comptes.css"
import SignIn from "./SignIn"
import SignUp from "./SignUp"

function Compte(){

    return (
        <div>

            <div className="split left">
                <div className="centered">
                    <SignIn/>
                </div>
            </div>

            <div className="split right">
                <div className="centered">
                    <SignUp/>
                </div>
            </div>

            
        </div>
    )
}

export default Compte