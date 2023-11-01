/* eslint-disable react-hooks/exhaustive-deps */
import React, { useContext, useEffect, useState } from "react";
import Image from "next/image";
import { useRouter } from "next/router";
import AuthContex from '../../context/AuthContext'
import { toast } from "react-toastify";
const UpdateProfile = ({access_token}) => {
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const {loading,error,user,clearErrors,update,updated,setUpdated}=useContext(AuthContex)

  const submitHandler =  (e) => {
    e.preventDefault()
update({updated,firstname,lastname,email,password,update,setUpdated},access_token)

  };
  const router=useRouter()
  
  useEffect(()=>{
    if(user){
        setFirstName(user.first_name)
        setLastname(user.last_name)
        setEmail(user.email)

    }
    if(error){
 
  toast.error(error)
  clearErrors()
    }
    if(updated){
setUpdated(false)
router.push('/me')
    }
   
  },[error,updated,user])
  
  return (
    <div className="modalMask">
      <div className="modalWrapper">
        <div className="left">
          <div style={{ width: "100%", height: "100%", position: "relative" }}>
            <Image src="/images/profile.svg" alt="register" layout="fill"/>
          </div>
        </div>
        <div className="right">
          <div className="rightContentWrapper">
            <div className="headerWrapper">
              <h2>Profile</h2>
            </div>
            <form className="form" onSubmit={submitHandler}>
              <div className="inputWrapper">
                <div className="inputBox">
                  <i aria-hidden className="fas fa-user"></i>
                  <input type="text" placeholder="Enter First Name" value={firstname} onChange={e=>setFirstName(e.target.value)} required />
                </div>

                <div className="inputBox">
                  <i aria-hidden className="fas fa-user-tie"></i>
                  <input type="text" placeholder="Enter Last name" value={lastname} onChange={e=>setLastname(e.target.value)}  required />
                </div>

                <div className="inputBox">
                  <i aria-hidden className="fas fa-envelope"></i>
                  <input type="email" placeholder="Enter Your Email" value={email} onChange={e=>setEmail(e.target.value)}  required />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-key"></i>
                  <input
                    type="password"
                    placeholder="Enter Your Password"
                    value={password}
                    // minLength={6}
                    onChange={e=>setPassword(e.target.value)} 
                  
                  />
                </div>
              </div>
              <div className="registerButtonWrapper">
                <button type="submit" className="registerButton">
                              {loading ?'updating...':'Update'}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UpdateProfile;
