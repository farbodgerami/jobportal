/* eslint-disable react-hooks/exhaustive-deps */
import React, { useContext, useEffect, useState } from "react";
import Image from "next/image";
import { useRouter } from "next/router";
import AuthContex from '../../context/AuthContext'
import { toast } from "react-toastify";
const Register = () => {
  const [firstname, setFirstName] = useState("");
  const [lastname, setLastname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const {loading,error,isAuthenticated,register,clearErrors}=useContext(AuthContex)

  const submitHandler =  (e) => {
    e.preventDefault()
register({firstname,lastname,email,password})
  };
  const router=useRouter()
  
  useEffect(()=>{
    if(error){
 
  toast.error(error)
  clearErrors()
    }
    if(isAuthenticated && !loading){
      router.push('/')
    }
  },[isAuthenticated,error,loading])
  
  return (
    <div className="modalMask">
      <div className="modalWrapper">
        <div className="left">
          <div style={{ width: "100%", height: "100%", position: "relative" }}>
            <Image src="/images/signup.svg" alt="register" layout="fill"/>
          </div>
        </div>
        <div className="right">
          <div className="rightContentWrapper">
            <div className="headerWrapper">
              <h2> SIGN UP</h2>
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
                    required
                  />
                </div>
              </div>
              <div className="registerButtonWrapper">
                <button type="submit" className="registerButton">
                              {loading ?'Authenticating...':'Register'}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Register;
