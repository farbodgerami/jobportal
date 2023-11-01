/* eslint-disable react-hooks/exhaustive-deps */
import React, { useContext, useEffect, useState } from "react";
import Image from "next/image";
import { useRouter } from "next/router";
import AuthContex from '../../context/AuthContext'
import { toast } from "react-toastify";
import Link from "next/link";
const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const {loading,error,isAuthenticated,login,clearErrors}=useContext(AuthContex)

  const submitHandler =  (e) => {
    e.preventDefault()
login({username:email,password})
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
            <Image src="/images/login.svg" alt="login" layout="fill" />
          </div>
        </div>
        <div className="right">
          <div className="rightContentWrapper">
            <div className="headerWrapper">
              <h2> LOGIN</h2>
            </div>
            <form className="form" onSubmit={submitHandler}>
              <div className="inputWrapper">
                <div className="inputBox">
                  <i aria-hidden className="fas fa-envelope"></i>
                  <input
                    // type="email"
                    type="text"
                    placeholder="Enter Your Email"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    // pattern="\S+@\S+\.\S+"
                    title='your Email is invalid'
                  />
                </div>
                <div className="inputBox">
                  <i aria-hidden className="fas fa-key"></i>
                  <input
                    type="password"
                    placeholder="Enter Your Password"
                    required
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                </div>
              </div>
              <div className="loginButtonWrapper">
                <button type="submit" className="loginButton">
                  {loading ?'Authenticating...':'Login'}
                </button>
              </div>
              <p style={{ textDecoration: "none" }} className="signup">
                New to Jobbee? <Link href="/register">Create an account</Link>
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
