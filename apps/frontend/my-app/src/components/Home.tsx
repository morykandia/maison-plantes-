import  { useEffect } from "react";
import { useAppDispatch, useAppSelector } from "../hooks/redux-hooks";
import { getUser, logout } from "../slices/authSlice";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  const basicUserInfo = useAppSelector((state) => state.auth.basicUserInfo);
  const userProfileInfo = useAppSelector((state) => state.auth.userProfileData);

  useEffect(() => {
    if (basicUserInfo) {
      dispatch(getUser());
    }
  }, [basicUserInfo]);

  const handleLogout = async () => {
    try {
      await dispatch(logout()).unwrap();
      navigate("/Compte");
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <>
      <h1>Home</h1>
      <h4>First Name: {userProfileInfo?.first_name}</h4>
      <h4>Last Name: {userProfileInfo?.last_name}</h4>
      <h4>Email: {userProfileInfo?.email}</h4>
      <button   onClick={handleLogout}>Logout</button>
      
    </>
  );
};

export default Home;


